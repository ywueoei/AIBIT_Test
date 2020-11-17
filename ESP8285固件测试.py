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



def wifi_enable(en):

    fm.register(8, fm.fpioa.GPIOHS0)
    wifi_en=GPIO(GPIO.GPIOHS0,GPIO.OUT)
    fm.register(board_info.WIFI_RX,fm.fpioa.UART2_TX)
    fm.register(board_info.WIFI_TX,fm.fpioa.UART2_RX)
    wifi_en.value(en)

def wifi(): #wifi
    from aibit import *
    print("开始WIFI模块测试...")
    lcd.draw_string(30, 50, 'Start test WIFI (End by touch) ', lcd.RED, lcd.BLACK)
    uart = UART(UART.UART2,115200,timeout=1000, read_buf_len=4096)
    wifi_enable(1)
    time.sleep_ms(200)
    wifi_enable(1)
    time.sleep_ms(200)
    fm.register(9, fm.fpioa.GPIO1)
    key_4 = GPIO(GPIO.GPIO1,GPIO.IN,GPIO.PULL_UP)
    read = uart.read()
    print(read)
    i=1
    while (key_4.value() == 1):

        #print(read[11:26])
        uart.write("AT+GMR\r\n")
        time.sleep_ms(200)
        read = uart.read()
        print(read)
        #read = read.decode(“utf-8”)
        try:
            lcd.draw_string(20, 90, 'Ver:' + str(read[11:38]+')'), lcd.RED, lcd.BLACK)
            lcd.draw_string(50, 90, '  ', lcd.RED, lcd.BLACK)
        except TypeError:
            print ("Error: 没有找到有效版本号")
            lcd.draw_string(50, 160, 'WIFI test failed!!!  ', lcd.GREEN, lcd.BLACK)
            time.sleep(0.05)
        if i > 10:
            break
        i +=1

    print("WIFI模块测试完成")
    time.sleep(3)
    lcd.clear()



######################开始测试#######################
wifi()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

