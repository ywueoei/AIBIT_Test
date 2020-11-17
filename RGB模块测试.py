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



def rgb():#RGB三色灯
    print("开始RGB模块测试...")
    lcd.draw_string(30, 50, 'Start test RGB_LDE ', lcd.RED, lcd.BLACK)
    tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
    tim2 = Timer(Timer.TIMER1, Timer.CHANNEL0, mode=Timer.MODE_PWM)
    tim3 = Timer(Timer.TIMER2, Timer.CHANNEL0, mode=Timer.MODE_PWM)
    led_r = PWM(tim1, freq=3000, duty=100, pin=13)
    led_g = PWM(tim2, freq=3000, duty=100, pin=12)
    led_b = PWM(tim3, freq=3000, duty=100, pin=14)
    led_g.duty(100)
    led_b.duty(100)
    led_r.duty(0)
    time.sleep(0.5)
    led_g.duty(0)
    led_b.duty(100)
    led_r.duty(100)
    time.sleep(0.5)
    led_g.duty(100)
    led_b.duty(0)
    led_r.duty(100)
    time.sleep(0.5)
    led_g.duty(100)
    led_b.duty(100)
    led_r.duty(0)
    time.sleep(0.5)
    led_g.duty(0)
    led_b.duty(100)
    led_r.duty(100)
    time.sleep(0.5)
    led_g.duty(100)
    led_b.duty(0)
    led_r.duty(100)
    lcd.draw_string(30, 90, 'End RGB_LDE test ', lcd.RED, lcd.BLACK)
    time.sleep(1)
    lcd.clear()
    print("RGB模块测试完成")




######################开始测试#######################

rgb()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)


