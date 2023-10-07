from enum import Enum


class Registers(Enum):
    # In the form of (Bank, Address)
    BANK_SEL = (-1, 0x7F)
    ...

    # Bank 0
    WHO_AM_I            = (0, 0x00)
    LPF                 = (0, 0x01)
    USER_CTRL           = (0, 0x03)

    LP_CONFIG           = (0, 0x05)
    PWR_MGMT_1          = (0, 0x06)
    PWR_MGMT_2          = (0, 0x07)

    INT_PIN_CFG         = (0, 0x0F)
    INT_ENABLE          = (0, 0x10)
    INT_ENABLE_1        = (0, 0x11)
    INT_ENABLE_2        = (0, 0x12)
    INT_ENABLE_3        = (0, 0x13)

    DMP_INT_STATUS      = (0, 0x18)
    INT_STATUS          = (0, 0x19)
    INT_STATUS_1        = (0, 0x1A)
    INT_STATUS_2        = (0, 0x1B)

    SINGLE_FIFO_PRIORITY_SEL = (0, 0x26)

    GYRO_XOUT_H_SH       = (0, 0x33)

    TEMPERATURE          = (0, 0x39)
    TEMP_CONFIG          = (0, 0x53)

    EXT_SLV_SENS_DATA_00 = (0, 0x3B)
    EXT_SLV_SENS_DATA_08 = (0, 0x43)
    EXT_SLV_SENS_DATA_09 = (0, 0x44)
    EXT_SLV_SENS_DATA_10 = (0, 0x45)

    FIFO_EN              = (0, 0x66)
    FIFO_EN_2            = (0, 0x67)
    FIFO_RST             = (0, 0x68)
    FIFO_COUNT_H         = (0, 0x70)
    FIFO_COUNT_L         = (0, 0x71)
    FIFO_R_W             = (0, 0x72)
    FIFO_CFG             = (0, 0x76)

    HW_FIX_DISABLE       = (0, 0x75)

    ACCEL_XOUT_H_SH      = (0, 0x2D)
    ACCEL_XOUT_L_SH      = (0, 0x2E)
    ACCEL_YOUT_H_SH      = (0, 0x2F)
    ACCEL_YOUT_L_SH      = (0, 0x30)
    ACCEL_ZOUT_H_SH      = (0, 0x31)
    ACCEL_ZOUT_L_SH      = (0, 0x32)

    MEM_START_ADDR       = (0, 0x7C)
    MEM_R_W              = (0, 0x7D)
    MEM_BANK_SEL         = (0, 0x7E)

    # Bank 1
    TIMEBASE_CORRECTION_PLL   = (1, 0x28)
    TIMEBASE_CORRECTION_RCOSC = (1, 0x29)
    SELF_TEST1                = (1, 0x02)
    SELF_TEST2                = (1, 0x03)
    SELF_TEST3                = (1, 0x04)
    SELF_TEST4                = (1, 0x0E)
    SELF_TEST5                = (1, 0x0F)
    SELF_TEST6                = (1, 0x10)

    XA_OFFS_H                 = (1, 0x14)
    XA_OFFS_L                 = (1, 0x15)
    YA_OFFS_H                 = (1, 0x17)
    YA_OFFS_L                 = (1, 0x18)
    ZA_OFFS_H                 = (1, 0x1A)
    ZA_OFFS_L                 = (1, 0x1B)

    # Bank 2
    GYRO_SMPLRT_DIV     = (2, 0x00)
    GYRO_CONFIG_1       = (2, 0x01)
    GYRO_CONFIG_2       = (2, 0x02)

    XG_OFFS_USRH        = (2, 0x03)
    XG_OFFS_USRL        = (2, 0x04)
    YG_OFFS_USRH        = (2, 0x05)
    YG_OFFS_USRL        = (2, 0x06)
    ZG_OFFS_USRH        = (2, 0x07)
    ZG_OFFS_USRL        = (2, 0x08)

    ACCEL_SMPLRT_DIV_1  = (2, 0x10)
    ACCEL_SMPLRT_DIV_2  = (2, 0x11)

    ACCEL_CONFIG        = (2, 0x14)
    ACCEL_CONFIG_2      = (2, 0x15)

    PRS_ODR_CONFIG      = (2, 0x20)
    PRGM_START_ADDRH    = (2, 0x50)

    MOD_CTRL_USR        = (2, 0x54)

    # Bank 3
    I2C_MST_ODR_CONFIG  = (3, 0x00)
    I2C_MST_CTRL        = (3, 0x01)
    I2C_MST_DELAY_CTRL  = (3, 0x02)

    I2C_SLV0_ADDR       = (3, 0x03)
    I2C_SLV0_REG        = (3, 0x04)
    I2C_SLV0_CTRL       = (3, 0x05)
    I2C_SLV0_DO         = (3, 0x06)

    I2C_SLV1_ADDR       = (3, 0x07)
    I2C_SLV1_REG        = (3, 0x08)
    I2C_SLV1_CTRL       = (3, 0x09)
    I2C_SLV1_DO         = (3, 0x0A)

    I2C_SLV2_ADDR       = (3, 0x0B)
    I2C_SLV2_REG        = (3, 0x0C)
    I2C_SLV2_CTRL       = (3, 0x0D)
    I2C_SLV2_DO         = (3, 0x0E)

    I2C_SLV3_ADDR       = (3, 0x0F)
    I2C_SLV3_REG        = (3, 0x10)
    I2C_SLV3_CTRL       = (3, 0x11)
    I2C_SLV3_DO         = (3, 0x12)

    I2C_SLV4_ADDR       = (3, 0x13)
    I2C_SLV4_REG        = (3, 0x14)
    I2C_SLV4_CTRL       = (3, 0x15)
    I2C_SLV4_DO         = (3, 0x16)
