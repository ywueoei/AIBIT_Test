# Untitled - By: YW - 周五 11月 13 2020


from machine import Timer,PWM
from fpioa_manager import *
from Maix import GPIO
import image
import lcd
import time
import sensor
import os
from machine import I2C

import network, time
from machine import UART
from Maix import GPIO
from fpioa_manager import fm, board_info

GRAVITY  = 9.80665
MSA300_ADDRESS = 0x26
MSA_300_REG_SOFT_RESET        =  0x00 #///< Soft reset (R)
MSA300_REG_PARTID             =  0x01 #///< Part ID (R)
MSA300_REG_ACC_X_LSB          =  0x02 #///< X-acceleration LSB (R)
MSA300_REG_ACC_X_MSB          =  0x03 #///< X-acceleration MSB (R)
MSA300_REG_ACC_Y_LSB          =  0x04 #///< Y-acceleration LSB (R)
MSA300_REG_ACC_Y_MSB          =  0x05 #///< Y-acceleration MSB (R)
MSA300_REG_ACC_Z_LSB          =  0x06 #///< Z-acceleration LSB (R)
MSA300_REG_ACC_Z_MSB          =  0x07 #///< Z-acceleration MSB (R)
MSA300_REG_MOTION_INT         =  0x09 #///< Motion interrupt (R)
MSA300_REG_DATA_INT           =  0x0A #///< Data interrupt (R)
MSA300_REG_TAP_ACTIVE_STATUS  =  0x0B #///< Tap status (R)
MSA300_REG_ORIENT_STATUS      =  0x0C #///< Orientation status (R)
MSA300_REG_RES_RANGE          =  0x0F #///< Resolution/Range (R/W)
MSA300_REG_ODR                =  0x10 #///< Output Data Rate (R/W)
MSA300_REG_PWR_MODE_BW        =  0x11 #///< Power Mode/Bandwidth (R/W)
MSA300_REG_SWAP_POLARITY      =  0x12 #///< Swap Axis Polarity (R/W)
MSA300_REG_INT_SET_0          =    0x16 #///< Interrupt Set 0 (R/W)
MSA300_REG_INT_SET_1          =    0x17 #///< Interrupt Set 1 (R/W)
MSA300_REG_INT_MAP_0          =    0x19 #///< Interrupt Map 0 (R/W)
MSA300_REG_INT_MAP_1          =    0x1A #///< Interrupt Map 1 (R/W)
MSA300_REG_INT_MAP_2_1        =    0x1B #///< Interrupt Map 2_1 (R/W)
MSA300_REG_INT_MAP_2_2        =    0x20 #///< Interrupt Map 2_2 (R/W)
MSA300_REG_INT_LATCH          =    0x21 #///< Interrupt Latch (R/W)
MSA300_REG_FREEFALL_DUR       =    0x22 #///< Freefall Duration (R/W)
MSA300_REG_FREEFALL_TH        =    0x23 #///< Freefall Threshold (R/W)
MSA300_REG_FREEFALL_HY        =    0x24 #///< Freefall Hysteresis (R/W)
MSA300_REG_ACTIVE_DUR         =    0x27 #///< Active Duration (R/W)
MSA300_REG_ACTIVE_TH          =    0x28 #///< Active Threshold (R/W)
MSA300_REG_TAP_DUR            =    0x2A #///< Tap Duration (R/W)
MSA300_REG_TAP_TH             =    0x2B #///< Tap Threshold (R/W)
MSA300_REG_ORIENT_HY          =   0x2C #///< Orientation Hysteresis (R/W)
MSA300_REG_Z_BLOCK            =    0x2D #///< Z Blocking (R/W)
MSA300_REG_OFFSET_COMP_X      =    0x38 #///< X Offset Compensation (R/W)
MSA300_REG_OFFSET_COMP_Y      =   0x39 #///< Y Offset Compensation (R/W)
MSA300_REG_OFFSET_COMP_Z      =   0x3A #///< Z Offset Compensation (R/W)
MSA300_MG2G_MULTIPLIER_16_G = 0.00195  # ///< 1.95mg per lsb
MSA300_MG2G_MULTIPLIER_8_G  = 0.000976 #///< 0.976mg per lsb
MSA300_MG2G_MULTIPLIER_4_G  = 0.000488 #///< 0.488mg per lsb
MSA300_MG2G_MULTIPLIER_2_G  = 0.000244 #///< 0.244mg per lsb
MSA300_MG2G_TAP_TH_16_G  =   0.5     # ///< 500mg per lsb
MSA300_MG2G_TAP_TH_8_G   =   0.25     #///< 250mg per lsb
MSA300_MG2G_TAP_TH_4_G   =   0.125    #///< 125mg per lsb
MSA300_MG2G_TAP_TH_2_G   =   0.0625   #///< 62.5mg per lsb
MSA300_MG2G_ACTIVE_TH_16_G  =   0.03125    #///< 31.25mg per lsb
MSA300_MG2G_ACTIVE_TH_8_G   =   0.015625   #///< 15.625mg per lsb
MSA300_MG2G_ACTIVE_TH_4_G   =   0.00781    #///< 7.81mg per lsb
MSA300_MG2G_ACTIVE_TH_2_G   =   0.00391    #///< 3.91mg per lsb
MSA300_DATARATE_1000_HZ     = 0b1111   #///<  500Hz Bandwidth, not available in low power mode
MSA300_DATARATE_500_HZ      = 0b1001   #///<  250Hz Bandwidth, not available in low power mode
MSA300_DATARATE_250_HZ      = 0b1000   # ///<  125Hz Bandwidth
MSA300_DATARATE_125_HZ      = 0b0111   # ///<   62.5Hz Bandwidth
MSA300_DATARATE_62_5_HZ     = 0b0110   #///<   31.25Hz Bandwidth
MSA300_DATARATE_31_25_HZ    = 0b0101   #///< 15.63Hz Bandwidth
MSA300_DATARATE_15_63_HZ    = 0b0100   #///< 7.81Hz Bandwidth
MSA300_DATARATE_7_81_HZ     = 0b0011   #///< 3.9Hz Bandwidth
MSA300_DATARATE_3_9_HZ      = 0b0010   #  ///< 1.95Hz Bandwidth
MSA300_DATARATE_1_95_HZ     = 0b0001   #  ///< 0.975Hz Bandwidth, not available in normal mode
MSA300_DATARATE_1_HZ        = 0b0000   # ///< 0.5Hz Bandwidth, not available in normal mode
ORIENT_UPWARD_LOOKING       = 0b0  #   ///< Upward looking orientation
ORIENT_DOWNWARD_LOOKING     = 0b1  #   ///< Downward looking orientation
ORIENT_PORTRAIT_UPRIGHT     = 0b00  #   ///< Portait upright orientation
ORIENT_PORTRAIT_UPSIDEDOWN  = 0b01  #   ///< Portait upsidedown orientation
ORIENT_LANDSCAPE_LEFT       = 0b10  #   ///< Landscape left orientation
ORIENT_LANDSCAPE_RIGHT      = 0b11  #   ///< Landscape right orientation
X_POLARITY                  = 3   #///< X polarity
Y_POLARITY                  = 2   #///< Y polarity
Z_POLARITY                  = 1   #///< Z polarity
X_Y_SWAP                    = 0   #///< XY polarity swap
MODE_SYMMETRICAL            = 0b00   #///< Symmetrical mode
MODE_HIGH_ASYMMETRICAL      = 0b01   #///< High asymmetrical mode
MODE_LOW_ASYMMETRICAL       = 0b10   #///< Low asymmetrical mode
ORIENT_NO_BLOCKING          = 0b00   #///< No blocking
ORIENT_Z_BLOCKING           = 0b01   #///< Z blocking
ORIENT_Z_BLOCKING_0_2_G     = 0b10   #///< Z blocking or slope in any axis > 0.2g
ADC_ADDR                    = 0x48

def getPartID(i2c):
    return  i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_PARTID,1)
def mpu_init(i2c):
  _multiplier = MSA300_MG2G_MULTIPLIER_4_G;

  time.sleep(0.200)
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_PWR_MODE_BW, 0X10)
  time.sleep(0.200)
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_ODR, MSA300_DATARATE_1000_HZ)
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_RES_RANGE, 0X01)
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_INT_SET_0,0x00);         #设置低通滤波器
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_INT_SET_1,0x00);    #陀螺仪量程2000deg/s
  i2c.writeto_mem(MSA300_ADDRESS, MSA300_REG_INT_LATCH,0x81);   #加速度量程4g
  return 0;
def get_accel_data(i2c):
  acc_x_h = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_X_MSB,1);
  acc_x_l = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_X_LSB,1);
  acc_y_h = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_Y_MSB,1);
  acc_y_l = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_Y_LSB,1);
  acc_z_h = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_Z_MSB,1);
  acc_z_l = i2c.readfrom_mem(MSA300_ADDRESS,MSA300_REG_ACC_Z_LSB,1);
  acc_x = acc_x_h[0] * 256 + acc_x_l[0]
  acc_y = acc_y_h[0] * 256 + acc_y_l[0]
  acc_z = acc_z_h[0] * 256 + acc_z_l[0]
  if(acc_x >= 0x8000):
    actual_acc_x = -((65535 - acc_x) + 1)
  else:
    actual_acc_x = acc_x
  if(acc_y >= 0x8000):
    actual_acc_y = -((65535 - acc_y) + 1)
  else:
    actual_acc_y = acc_y
  if(acc_z >= 0x8000):
    actual_acc_z = -((65535 - acc_z) + 1)
  else:
    actual_acc_z = acc_z
  return {'x': actual_acc_x, 'y': actual_acc_y, 'z': actual_acc_z}


i2c = I2C(I2C.I2C0, freq=100000, scl=21, sda=22)
devices = i2c.scan()
lcd.init()



def mpu6050():#三轴加速度
     mpu_init(i2c)
     lcd.draw_string(30, 0, 'Start test MPU6050 (End by touch)', lcd.RED, lcd.BLACK)
     print("开始测试三轴加速度...")
     #fm.register(9, fm.fpioa.GPIO1)
     #key_4 = GPIO(GPIO.GPIO1,GPIO.IN,GPIO.PULL_UP)
     #print(key_4.value())
     ax_last=ay_last=az_last=0
     flag_x =flag_y =flag_z =0
     #while (key_4.value() == 1):
     while ((flag_x*flag_y*flag_z) ==0):
         accel_data = get_accel_data(i2c)
         print(accel_data)
         lcd.draw_string(30, 20, 'ax : ' + str(accel_data['x']) +'   ', lcd.RED, lcd.BLACK)
         lcd.draw_string(30, 40, 'ay : ' + str(accel_data['y']) +'   ', lcd.RED, lcd.BLACK)
         lcd.draw_string(30, 60, 'az : ' + str(accel_data['z']) +'   ', lcd.RED, lcd.BLACK)
         ax =accel_data['x']
         ay =accel_data['y']
         az =accel_data['z']
         #if ((ax*ax_last <0 and ay*ay_last<0 and az*az_last) <0):
         if ( ax*ax_last<0):
            flag_x =1
         if ( ay*ay_last<0):
            flag_y =1
         if ( az*az_last<0):
            flag_z =1
         ax_last =ax
         ay_last =ay
         az_last =az
         time.sleep(0.1)
     lcd.draw_string(90, 120, ' MPU6050 ok!! ', lcd.RED, lcd.BLACK)
     time.sleep(1)
     lcd.clear()
     print ("mpu6050测试通过")
     print("三轴加速度测试完成")





######################开始测试#######################

mpu6050()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

