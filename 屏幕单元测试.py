# Untitled - By: YW - 周四 11月 12 2020

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


# Untitled - By: yewoei - 周二 11月 3 2020

def screen():
    print("开始屏幕显示测试...")
    img = image.Image()
    img.draw_rectangle(0,0,320,240,color=(255,0,0),fill=True)
    lcd.display(img)
    time.sleep(1)
    img.draw_rectangle(0,0,320,240,color=(0,255,0),fill=True)
    lcd.display(img)
    time.sleep(1)
    img.draw_rectangle(0,0,320,240,color=(0,0,255),fill=True)
    lcd.display(img)
    time.sleep(1)
    lcd.clear()
    print("屏幕显示测试完成")


def deaw_picture():
    screen = Screen()
    screen.set_txt_size(2)
    screen.set_txt_color(255,0,0)
    screen.text(80,90,str('Hello'))
    screen.show_screen()

    screen.clear((255,204,204))
    screen.set_line_width(3)
    screen.set_line_color(51,204,255)
    screen.ellipse(160,70,50,50,True)
    screen.set_line_width(3)
    screen.set_line_color(255,255,255)
    screen.ellipse(160,80,45,40,True)
    screen.set_line_width(2)
    screen.set_line_color(0,0,0)
    screen.ellipse(140,50,10,13,False)
    screen.ellipse(180,50,10,13,False)
    screen.set_line_width(2)
    screen.set_line_color(0,0,0)
    screen.ellipse(145,55,4,4,True)
    screen.ellipse(175,55,4,4,True)
    screen.set_line_width(1)
    screen.set_line_color(0,0,0)
    screen.line(110,65,148,70)
    screen.line(110,80,148,80)
    screen.line(110,95,148,90)
    screen.set_line_width(1)
    screen.set_line_color(0,0,0)
    screen.line(170,70,208,65)
    screen.line(170,80,208,80)
    screen.line(170,90,208,95)
    screen.set_line_width(2)
    screen.set_line_color(255,0,0)
    screen.ellipse(160,105,20,15,True)
    screen.set_line_width(2)
    screen.set_line_color(255,255,255)
    screen.ellipse(160,95,15,15,True)
    screen.set_line_width(2)
    screen.set_line_color(51,204,255)
    screen.ellipse(160,173,58,53,True)
    screen.set_line_width(2)
    screen.set_line_color(255,255,255)
    screen.ellipse(160,180,30,35,True)
    screen.set_line_width(2)
    screen.set_line_color(0,0,0)
    screen.ellipse(160,185,13,10,False)
    screen.set_line_width(2)
    screen.set_line_color(255,204,102)
    screen.ellipse(160,130,12,12,True)
    screen.set_line_width(2)
    screen.set_line_color(0,0,0)
    screen.line(150,125,170,125)
    screen.line(148,130,172,130)
    screen.ellipse(160,135,3,3,True)
    screen.set_line_width(2)
    screen.set_line_color(51,204,255)
    screen.ellipse(95,140,45,12,True)
    screen.ellipse(225,140,45,12,True)
    screen.set_line_width(2)
    screen.set_line_color(255,255,255)
    screen.ellipse(50,140,13,13,True)
    screen.ellipse(270,140,13,13,True)
    screen.set_line_width(2)
    screen.set_line_color(255,255,255)
    screen.ellipse(130,230,27,10,True)
    screen.ellipse(190,230,27,10,True)
    time.sleep(3)
    screen.show_screen()


######################开始测试#######################

screen()
deaw_picture()

print("全部测试已完成！！")
lcd.draw_string(90, 120, '  End of  test ! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 150, 'End of all test !! ', lcd.RED, lcd.BLACK)

