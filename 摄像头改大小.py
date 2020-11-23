# Untitled - By: YW - 周一 11月 23 2020

from machine import Timer,PWM
from fpioa_manager import *
from Maix import GPIO
import image
import lcd
import time
import sensor
import os
from machine import I2C
import network
from machine import UART
from fpioa_manager import fm, board_info


i2c = I2C(I2C.I2C0, freq=100000, scl=21, sda=22)
devices = i2c.scan()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_windowing((200, 200)) #取中间的 240*240 区域
sensor.run(1)
sensor.skip_frames()
while True:
    img =sensor.snapshot()
    lcd.display(img,roi=(0,0,240,240))
    #lcd.display(img)
