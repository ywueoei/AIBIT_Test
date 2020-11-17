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


i2c = I2C(I2C.I2C0, freq=100000, scl=21, sda=22)
devices = i2c.scan()
lcd.init()

def bit_sensor():#摄像头
     print("开始测试摄像头...")
     try:
        lcd.draw_string(30, 50, 'Start test Camera (End by touch) ', lcd.RED, lcd.BLACK)
        sensor.reset()
        sensor.set_pixformat(sensor.RGB565)
        sensor.set_framesize(sensor.QVGA)
        sensor.run(1)
        sensor.skip_frames()
     except:
        #break
        lcd.draw_string(90, 120, 'Camera test failed! ', lcd.GREEN, lcd.BLACK)
        print("摄像头初始化失败！")

     i=0
     fm.register(9, fm.fpioa.GPIO1)
     key_4 = GPIO(GPIO.GPIO1,GPIO.IN,GPIO.PULL_UP)
     while (key_4.value() == 1):
          lcd.display(sensor.snapshot())
          i=i+1
          if i >150:
            break
     lcd.draw_string(90, 90, 'End Camera test ', lcd.RED, lcd.BLACK)
     time.sleep(1)
     lcd.clear()
     print("摄像头实时显示测试完成")



######################开始测试#######################

bit_sensor()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

