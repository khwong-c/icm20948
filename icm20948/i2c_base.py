from smbus2 import SMBus


class I2CDevice:
    def __init__(self, i2c_addr, i2c_bus=None):
        self._addr = i2c_addr

        if i2c_bus is None:
            self._bus = SMBus(1)
        else:
            self._bus = i2c_bus

    def _write(self, reg, value):
        """Write byte to i2c device."""
        self._bus.write_byte_data(self._addr, reg, value)

    def _read(self, reg):
        """Read byte from i2c device."""
        return self._bus.read_byte_data(self._addr, reg)

    def _read_bytes(self, reg, length=1):
        """Read byte(s) from device."""
        return self._bus.read_i2c_block_data(self._addr, reg, length)

    def _write_bytes(self, reg, length=1):
        """Write byte(s) to device."""
        return self._bus.read_i2c_block_data(self._addr, reg, length)
