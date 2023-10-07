from smbus2 import SMBus


class I2CDevice:
    def __init__(self, i2c_addr, i2c_bus=None):
        self._addr = i2c_addr

        if i2c_bus is None:
            self._bus = SMBus(1)
        else:
            self._bus = i2c_bus

    def write(self, reg, value):
        """Write byte(s) to device."""
        if isinstance(reg, int):
            reg = reg.to_bytes(1, byteorder='little', signed=False)
        if len(value) == 1:
            self._bus.write_byte_data(self._addr, reg, value)
        self._bus.write_i2c_block_data(self._addr, reg, value)

    def read(self, reg, length=1) -> bytes:
        """Read byte(s) from device."""
        if length == 1:
            return self._bus.read_byte_data(self._addr, reg)
        return bytes(self._bus.read_i2c_block_data(self._addr, reg, length))
