from contextlib import contextmanager
from .i2c_base import I2CDevice
from .register_map import Registers

ICM20948_ADDR = 0x68


class ICM20948Transport(I2CDevice):
    def __init__(self, i2c_addr=ICM20948_ADDR, i2c_bus=None):
        super().__init__(i2c_addr=i2c_addr, i2c_bus=i2c_bus)
        self._bank = self.get_bank()

    def set_bank(self, bank: int):
        if self._bank != bank:
            self._write(Registers.BANK_SEL.addr, bank << 4)
            self._bank = bank

    def get_bank(self) -> int:
        cur_bank = self._read(Registers.BANK_SEL.addr)
        cur_bank >>= 4
        self._bank = cur_bank
        return cur_bank

    @contextmanager
    def bank(self, bank: int):
        prev_bank = self._bank
        self.set_bank(bank)
        yield
        self.set_bank(prev_bank)

    def set_register(self, register: Registers, value: bytes):
        with self.bank(register.bank):
            self.write(register.addr, value)

    def get_register(self, register: Registers):
        with self.bank(register.bank):
            return self.read(register.addr)
