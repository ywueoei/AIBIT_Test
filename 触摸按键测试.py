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


def  touch_key():#触摸按键
     fm.register(9, fm.fpioa.GPIO2)
     fm.register(10, fm.fpioa.GPIO3)
     fm.register(11, fm.fpioa.GPIO4)
     fm.register(15, fm.fpioa.GPIO5)
     fm.register(17, fm.fpioa.GPIO6)
     fm.register(18, fm.fpioa.GPIO7)
     key_a = GPIO(GPIO.GPIO2,GPIO.IN,GPIO.PULL_UP)
     key_i = GPIO(GPIO.GPIO3,GPIO.IN,GPIO.PULL_UP)
     key_s = GPIO(GPIO.GPIO4,GPIO.IN,GPIO.PULL_UP)
     key_t = GPIO(GPIO.GPIO5,GPIO.IN,GPIO.PULL_UP)
     key_e = GPIO(GPIO.GPIO6,GPIO.IN,GPIO.PULL_UP)
     key_m = GPIO(GPIO.GPIO7,GPIO.IN,GPIO.PULL_UP)
     img = image.Image()
     print("开始触摸按键测试...")
     print("按下key1开始...")
     lcd.draw_string(90, 30, 'Start test Touch_key ', lcd.RED, lcd.BLACK)
     lcd.draw_string(90, 50, 'Press key 1 to start ', lcd.RED, lcd.BLACK)
     lcd.draw_string(20, 10,' ||  Direction', lcd.RED, lcd.BLACK)
     lcd.draw_string(20, 20,' || ', lcd.RED, lcd.BLACK)
     lcd.draw_string(20, 30,'\||/ ', lcd.RED, lcd.BLACK)
     lcd.draw_string(20, 40,' \/ ', lcd.RED, lcd.BLACK)
     time.sleep(1)

     while True:
        if key_a.value()==0:
            print("key_a" ,key_a.value())
            while (key_i.value()):
                print("key_i =" ,key_i.value())
                lcd.draw_string(90, 100, ' key 1 ok! ', lcd.RED, lcd.BLACK)
                time.sleep(0.05)
            while (key_s.value()):
                print("key_s =" ,key_s.value())
                lcd.draw_string(90, 120, ' key 2 ok! ', lcd.RED, lcd.BLACK)
                time.sleep(0.05)
            while (key_t.value()):
                print("key_t =" ,key_t.value())
                lcd.draw_string(90, 140, ' key 3 ok! ', lcd.RED, lcd.BLACK)
                time.sleep(0.05)
            while (key_e.value()):
                print("key_e =" ,key_e.value())
                lcd.draw_string(90, 160, ' key 4 ok! ', lcd.RED, lcd.BLACK)
                time.sleep(0.05)
            while (key_m.value()):
                print("key_m =" ,key_m.value())
                lcd.draw_string(90, 180, ' key 5 ok! ', lcd.RED, lcd.BLACK)
                time.sleep(0.05)
            lcd.draw_string(90, 200, ' key 6 ok! ', lcd.RED, lcd.BLACK)
            print("触摸按键测试完成")
            lcd.draw_string(30, 220, 'End Touch_key test ! ', lcd.RED, lcd.BLACK)
            time.sleep(1)
            lcd.clear()
            break


######################开始测试#######################
touch_key()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

