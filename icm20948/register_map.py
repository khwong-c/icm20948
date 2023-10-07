from enum import Enum


class Registers(Enum):
    # In the form of (Bank, Address)
    BANK_SEL = (-1, 0x7F)

    # Bank 0
    WHO_AM_I = (0, 0x00)
    USER_CTRL = (0, 0x03)

    LP_CONFIG = (0, 0x05)
    PWR_MGMT_1 = (0, 0x06)
    PWR_MGMT_2 = (0, 0x07)

    INT_PIN_CFG = (0, 0x0F)
    INT_ENABLE = (0, 0x10)
    INT_ENABLE_1 = (0, 0x11)
    INT_ENABLE_2 = (0, 0x12)
    INT_ENABLE_3 = (0, 0x13)

    I2C_MST_STATUS = (0, 0x17)
    DMP_INT_STATUS = (0, 0x18)
    INT_STATUS = (0, 0x19)
    INT_STATUS_1 = (0, 0x1A)
    INT_STATUS_2 = (0, 0x1B)
    INT_STATUS_3 = (0, 0x1C)

    SINGLE_FIFO_PRIORITY_SEL = (0, 0x26)

    DELAY_TIME_H = (0, 0x28)
    DELAY_TIME_L = (0, 0x29)

    ACCEL_XOUT_H = (0, 0x2D)
    ACCEL_XOUT_L = (0, 0x2E)
    ACCEL_YOUT_H = (0, 0x2F)
    ACCEL_YOUT_L = (0, 0x30)
    ACCEL_ZOUT_H = (0, 0x31)
    ACCEL_ZOUT_L = (0, 0x32)
    GYRO_XOUT_H = (0, 0x33)
    GYRO_XOUT_L = (0, 0x34)
    GYRO_YOUT_H = (0, 0x35)
    GYRO_YOUT_L = (0, 0x36)
    GYRO_ZOUT_H = (0, 0x37)
    GYRO_ZOUT_L = (0, 0x38)

    TEMP_OUT_H = (0, 0x39)
    TEMP_OUT_L = (0, 0x3A)

    EXT_SLV_SENS_DATA_00 = (0, 0x3B)
    EXT_SLV_SENS_DATA_01 = (0, 0x3C)
    EXT_SLV_SENS_DATA_02 = (0, 0x3D)
    EXT_SLV_SENS_DATA_03 = (0, 0x3E)
    EXT_SLV_SENS_DATA_04 = (0, 0x3F)
    EXT_SLV_SENS_DATA_05 = (0, 0x40)
    EXT_SLV_SENS_DATA_06 = (0, 0x41)
    EXT_SLV_SENS_DATA_07 = (0, 0x42)
    EXT_SLV_SENS_DATA_08 = (0, 0x43)
    EXT_SLV_SENS_DATA_09 = (0, 0x44)
    EXT_SLV_SENS_DATA_10 = (0, 0x45)
    EXT_SLV_SENS_DATA_11 = (0, 0x46)
    EXT_SLV_SENS_DATA_12 = (0, 0x47)
    EXT_SLV_SENS_DATA_13 = (0, 0x48)
    EXT_SLV_SENS_DATA_14 = (0, 0x49)
    EXT_SLV_SENS_DATA_15 = (0, 0x4A)
    EXT_SLV_SENS_DATA_16 = (0, 0x4B)
    EXT_SLV_SENS_DATA_17 = (0, 0x4C)
    EXT_SLV_SENS_DATA_18 = (0, 0x4D)
    EXT_SLV_SENS_DATA_19 = (0, 0x4E)
    EXT_SLV_SENS_DATA_20 = (0, 0x4F)
    EXT_SLV_SENS_DATA_21 = (0, 0x50)
    EXT_SLV_SENS_DATA_22 = (0, 0x51)
    EXT_SLV_SENS_DATA_23 = (0, 0x52)

    FIFO_EN_1 = (0, 0x66)
    FIFO_EN_2 = (0, 0x67)
    FIFO_RST = (0, 0x68)
    FIFO_MODE = (0, 0x69)
    FIFO_COUNT_H = (0, 0x70)
    FIFO_COUNT_L = (0, 0x71)
    FIFO_R_W = (0, 0x72)
    FIFO_CFG = (0, 0x76)
    DATA_RDY_STATUS = (0, 0x74)

    HW_FIX_DISABLE = (0, 0x75)

    MEM_START_ADDR = (0, 0x7C)
    MEM_R_W = (0, 0x7D)
    MEM_BANK_SEL = (0, 0x7E)

    # Bank 1
    TIMEBASE_CORRECTION_PLL = (1, 0x28)
    TIMEBASE_CORRECTION_RCOSC = (1, 0x29)
    SELF_TEST1 = (1, 0x02)
    SELF_TEST2 = (1, 0x03)
    SELF_TEST3 = (1, 0x04)
    SELF_TEST4 = (1, 0x0E)
    SELF_TEST5 = (1, 0x0F)
    SELF_TEST6 = (1, 0x10)

    XA_OFFS_H = (1, 0x14)
    XA_OFFS_L = (1, 0x15)
    YA_OFFS_H = (1, 0x17)
    YA_OFFS_L = (1, 0x18)
    ZA_OFFS_H = (1, 0x1A)
    ZA_OFFS_L = (1, 0x1B)

    # Bank 2
    GYRO_SMPLRT_DIV = (2, 0x00)
    GYRO_CONFIG_1 = (2, 0x01)
    GYRO_CONFIG_2 = (2, 0x02)

    XG_OFFS_USRH = (2, 0x03)
    XG_OFFS_USRL = (2, 0x04)
    YG_OFFS_USRH = (2, 0x05)
    YG_OFFS_USRL = (2, 0x06)
    ZG_OFFS_USRH = (2, 0x07)
    ZG_OFFS_USRL = (2, 0x08)

    ODR_ALIGN_EN = (2, 0x09)

    ACCEL_SMPLRT_DIV_1 = (2, 0x10)
    ACCEL_SMPLRT_DIV_2 = (2, 0x11)
    ACCEL_INTEL_CTRL = (2, 0x12)
    ACCEL_WOM_THR = (2, 0x13)

    ACCEL_CONFIG = (2, 0x14)
    ACCEL_CONFIG_2 = (2, 0x15)

    FSYNC_CONFIG = (2, 0x52)
    TEMP_CONFIG = (2, 0x53)

    PRS_ODR_CONFIG = (2, 0x20)
    PRGM_START_ADDRH = (2, 0x50)

    MOD_CTRL_USR = (2, 0x54)

    # Bank 3
    I2C_MST_ODR_CONFIG = (3, 0x00)
    I2C_MST_CTRL = (3, 0x01)
    I2C_MST_DELAY_CTRL = (3, 0x02)

    I2C_SLV0_ADDR = (3, 0x03)
    I2C_SLV0_REG = (3, 0x04)
    I2C_SLV0_CTRL = (3, 0x05)
    I2C_SLV0_DO = (3, 0x06)

    I2C_SLV1_ADDR = (3, 0x07)
    I2C_SLV1_REG = (3, 0x08)
    I2C_SLV1_CTRL = (3, 0x09)
    I2C_SLV1_DO = (3, 0x0A)

    I2C_SLV2_ADDR = (3, 0x0B)
    I2C_SLV2_REG = (3, 0x0C)
    I2C_SLV2_CTRL = (3, 0x0D)
    I2C_SLV2_DO = (3, 0x0E)

    I2C_SLV3_ADDR = (3, 0x0F)
    I2C_SLV3_REG = (3, 0x10)
    I2C_SLV3_CTRL = (3, 0x11)
    I2C_SLV3_DO = (3, 0x12)

    I2C_SLV4_ADDR = (3, 0x13)
    I2C_SLV4_REG = (3, 0x14)
    I2C_SLV4_CTRL = (3, 0x15)
    I2C_SLV4_DO = (3, 0x16)
    I2C_SLV4_DI = (3, 0x17)

    @property
    def bank(self):
        return self.value[0]

    @property
    def addr(self):
        return self.value[1]


class Values:
    class WHO_AM_I:
        ICM20948 = 0xEA

    class USER_CTRL:
        DMP_EN = 0x80
        FIFO_EN = 0x40
        I2C_MST_EN = 0x20
        I2C_IF_DIS = 0x10
        DMP_RST = 0x08
        SRAM_RST = 0x04
        I2C_MST_RST = 0x02

    class LP_CONFIG:
        I2C_MST_CYCLE = 0x40
        ACCEL_CYCLE = 0x20
        GYRO_CYCLE = 0x10

    class PWR_MGMT_1:
        DEVICE_RESET = 0x80
        SLEEP = 0x40
        LP_EN = 0x20
        TEMP_DIS = 0x08
        CLK_PLL = 0x01
        CLK_STOP = 0x07

    class PWR_MGMT_2:
        DISABLE_ACCEL = 0x38
        DISABLE_GYRO = 0x07
        DISABLE_ALL = 0x7f

    class INT_PIN_CFG:
        INT1_ACTL = 0x80
        INT1_OPEN = 0x40
        INT1_LATCH_EN = 0x20
        INT_ANYRD_2CLEAR = 0x10
        ACTL_FSYNC = 0x08
        FSYNC_INT_MODE_EN = 0x04
        BYPASS_EN = 0x02

    class INT_ENABLE:
        REG_WOF_EN = 0x80
        WOM_INT_EN = 0x08
        PLL_RDY_EN = 0x04
        DMP_INT1_EN = 0x02
        I2C_MST_INT_EN = 0x01

    class INT_ENABLE_1:
        RAW_DATA_0_RDY_EN = 0x01

    class INT_ENABLE_2:
        FIFO_OVERFLOW_EN = 0x01

    class INT_ENABLE_3:
        FIFO_WM_EN = 0x01

    class I2C_MST_STATUS:
        PASS_THROUGH = 0x80
        I2C_SLV4_DONE = 0x40
        I2C_LOST_ARB = 0x20
        I2C_SLV4_NACK = 0x10
        I2C_SLV3_NACK = 0x08
        I2C_SLV2_NACK = 0x04
        I2C_SLV1_NACK = 0x02
        I2C_SLV4_NACK = 0x01

    class INT_STATUS:
        WOM_INT = 0x08
        PLL_RDY_INT = 0x04
        DMP_INT1 = 0x02
        I2C_MST_INT = 0x01

    class INT_STATUS_1:
        RAW_DATA_0_RDY_INT = 0x01

    class INT_STATUS_2:
        FIFO_OVERFLOW_INT = 0x01

    class INT_STATUS_3:
        FIFO_WM_INT = 0x01

    class FIFO_EN_1:
        SLV_3_FIFO_EN = 0x08
        SLV_2_FIFO_EN = 0x04
        SLV_1_FIFO_EN = 0x02
        SLV_0_FIFO_EN = 0x01

    class FIFO_EN_2:
        ACCEL_FIFO_EN = 0x10
        GYRO_Z_FIFO_EN = 0x08
        GYRO_Y_FIFO_EN = 0x04
        GYRO_X_FIFO_EN = 0x02
        TEMP_FIFO_EN = 0x01

    class FIFO_RST:
        FIFO_RESET = 0x0F

    class FIFO_MODE:
        FIFO_MODE = 0x01

    class FIFO_CFG:
        MULTI_FIFO_CFG = 0x01
        SINGLE_FIFO_CFG = 0x00

    class GYRO_CONFIG_1:
        GYRO_FCHOICE = 0x01

        GYRO_DLPFCFG_360HZ = 7 << 3
        GYRO_DLPFCFG_200HZ = 0 << 3
        GYRO_DLPFCFG_150HZ = 1 << 3
        GYRO_DLPFCFG_120HZ = 2 << 3
        GYRO_DLPFCFG_50HZ = 3 << 3
        GYRO_DLPFCFG_25HZ = 4 << 3
        GYRO_DLPFCFG_12HZ = 5 << 3
        GYRO_DLPFCFG_5HZ = 6 << 3

        GYRO_FS_SEL_250DPS = 0 << 1
        GYRO_FS_SEL_500DPS = 1 << 1
        GYRO_FS_SEL_1000DPS = 2 << 1
        GYRO_FS_SEL_2000DPS = 3 << 1

    class GYRO_CONFIG_2:
        XGYRO_CTEN = 0x20
        YGYRO_CTEN = 0x10
        ZGYRO_CTEN = 0x08

        GYRO_AVGCFG_1X = 0
        GYRO_AVGCFG_2X = 1
        GYRO_AVGCFG_4X = 2
        GYRO_AVGCFG_8X = 3
        GYRO_AVGCFG_16X = 4
        GYRO_AVGCFG_32X = 5
        GYRO_AVGCFG_64X = 6
        GYRO_AVGCFG_128X = 7

    class ODR_ALIGN_EN:
        ODR_ALIGN_EN = 0x01

    class ACCEL_INTEL_CTRL:
        ACCEL_INTEL_EN = 0x02
        ACCEL_INTEL_MODE_INT = 0x01

    class ACCEL_CONFIG:
        ACCEL_DLPFCFG_475HZ = 7 << 3
        ACCEL_DLPFCFG_250HZ = 1 << 3
        ACCEL_DLPFCFG_115HZ = 2 << 3
        ACCEL_DLPFCFG_50HZ = 3 << 3
        ACCEL_DLPFCFG_25HZ = 4 << 3
        ACCEL_DLPFCFG_12HZ = 5 << 3
        ACCEL_DLPFCFG_6HZ = 6 << 3

        ACCEL_FS_SEL_2G = 0 << 1
        ACCEL_FS_SEL_4G = 1 << 1
        ACCEL_FS_SEL_8G = 2 << 1
        ACCEL_FS_SEL_16G = 3 << 1

        ACCEL_FCHOICE = 0x01

    class ACCEL_CONFIG_2:
        AX_ST_EN_REG = 0x10
        AY_ST_EN_REG = 0x08
        AZ_ST_EN_REG = 0x04

        DEC3_CFG_AVG_1X = 0
        DEC3_CFG_AVG_4X = 0
        DEC3_CFG_AVG_8X = 1
        DEC3_CFG_AVG_16X = 2
        DEC3_CFG_AVG_32X = 3

    class FSYNC_CONFIG:
        DELAY_TIME_EN = 0x80
        WOF_DEGLITCH_EN = 0x02
        WOF_EDGE_INT = 0x01

        EXT_SYNC_SET_DISABLE = 0
        EXT_SYNC_SET_TEMP_OUT = 1
        EXT_SYNC_SET_GYRO_XOUT = 2
        EXT_SYNC_SET_GYRO_YOUT = 3
        EXT_SYNC_SET_GYRO_ZOUT = 4
        EXT_SYNC_SET_ACCEL_XOUT = 5
        EXT_SYNC_SET_ACCEL_YOUT = 6
        EXT_SYNC_SET_ACCEL_ZOUT = 7

    class TEMP_CONFIG:
        TEMP_DLPFCFG_8000HZ = 0
        TEMP_DLPFCFG_220HZ = 1
        TEMP_DLPFCFG_123HZ = 2
        TEMP_DLPFCFG_66HZ = 3
        TEMP_DLPFCFG_34HZ = 4
        TEMP_DLPFCFG_17HZ = 5
        TEMP_DLPFCFG_9HZ = 6

    class MOD_CTRL_USR:
        REG_LP_DMP_EN = 0x01

    class I2C_MST_CTRL:
        MULT_MST_EN = 0x80
        I2C_MST_P_NSR = 0x10
        I2C_MST_CLK_RECOMMEND = 0x07

    class I2C_MST_DELAY_CTRL:
        DELAY_ES_SHADOW = 0x80
        I2C_SLV4_DELAY_EN = 0x10
        I2C_SLV3_DELAY_EN = 0x08
        I2C_SLV2_DELAY_EN = 0x04
        I2C_SLV1_DELAY_EN = 0x02
        I2C_SLV0_DELAY_EN = 0x01

    class I2C_SLV_ADDR:
        I2C_SLV0_RNW = 0x80

    class I2C_SLV_CTRL:
        I2C_SLV_EN = 0x80
        I2C_SLV_BYTE_SW = 0x40
        I2C_SLV_REG_DIS = 0x20
        I2C_SLV_GRP = 0x10

    class I2C_SLV4_CTRL:
        I2C_SLV4_EN = 0x80
        I2C_SLV4_BYTE_SW = 0x40
        I2C_SLV4_REG_DIS = 0x20


class MagRegisters:
    WIA2 = 0x01
    ST1 = 0x10
    DATA_X_L = 0x11
    DATA_X_H = 0x12
    DATA_Y_L = 0x13
    DATA_Y_H = 0x14
    DATA_Z_L = 0x15
    DATA_Z_H = 0x16
    ST2 = 0x18
    CNTL2 = 0x31
    CNTL3 = 0x31


class MagValues:
    class WIA2:
        WIA = 0x08

    class ST1:
        DOR = 0x02
        DRDY = 0x01

    class ST2:
        HOFL = 0x08

    class CNTL2:
        PWR_DOWN = 0x00
        SINGLE = 0x01
        CONTINUOUS_10HZ = 0x02
        CONTINUOUS_20HZ = 0x04
        CONTINUOUS_50HZ = 0x06
        CONTINUOUS_100HZ = 0x80
        SELFTEST = 0x10

    class CNTL3:
        SRST = 0x01
