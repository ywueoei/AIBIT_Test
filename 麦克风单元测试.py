# Untitled - By: YW - 周五 11月 13 2020

# Untitled - By: yewoei - 周四 11月 5 2020

# Untitled - By: yewoei - 周二 11月 3 2020

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




def mic():#麦克风
    from aibit import *
    print("开始测试麦克风...")
    lcd.draw_string(30, 50, 'Start test MIC (End by touch) ', lcd.RED, lcd.BLACK)
    #fm.register(9, fm.fpioa.GPIO1)
    #key_4 = GPIO(GPIO.GPIO1,GPIO.IN,GPIO.PULL_UP)
    mic=Mic()
    while ((mic.get_intensity()<50)):
        value=mic.get_intensity()
        lcd.draw_string(30, 70, 'MIC : ' + str(value), lcd.RED, lcd.BLACK)
        time.sleep(0.1)
        print(value)
    lcd.draw_string(30, 90, ' MIC test ok! ', lcd.RED, lcd.BLACK)
    time.sleep(1)
    lcd.clear()
    print("麦克风测试完成")




######################开始测试#######################

mic()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

