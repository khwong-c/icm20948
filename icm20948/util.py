def imu_byte_to_int(x: bytes) -> int:
    return int.from_bytes(x, byteorder="big", signed=True)


def imu_int_to_byte(x: int) -> bytes:
    return x.to_bytes(length=2, byteorder="big", signed=True)


def mag_byte_to_int(x: bytes) -> int:
    return int.from_bytes(x, byteorder="little", signed=True)
