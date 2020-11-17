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

ADC_ADDR                    = 0x48
i2c = I2C(I2C.I2C0, freq=100000, scl=21, sda=22)
devices = i2c.scan()
lcd.init()


def gpio():#IO测试，需检测io输出电平
#########K210_IO测试############
    '''
    fm.register(9, fm.fpioa.GPIO0)
    fm.register(10, fm.fpioa.GPIO1)
    fm.register(23, fm.fpioa.GPIO2)
    fm.register(27, fm.fpioa.GPIO3)
    fm.register(26, fm.fpioa.GPIO4)
    fm.register(28, fm.fpioa.GPIO5)
    fm.register(25, fm.fpioa.GPIO6)
    fm.register(21, fm.fpioa.GPIO7)
    fm.register(22, fm.fpioa.GPIOHS0)
    #IO9 =  GPIO(GPIO.GPIO0,GPIO.OUT)
    IO10 = GPIO(GPIO.GPIO1,GPIO.OUT)
    IO23 = GPIO(GPIO.GPIO2,GPIO.OUT)
    IO27 = GPIO(GPIO.GPIO3,GPIO.OUT)
    IO26 = GPIO(GPIO.GPIO4,GPIO.OUT)
    IO28 = GPIO(GPIO.GPIO5,GPIO.OUT)
    IO25 = GPIO(GPIO.GPIO6,GPIO.OUT)
    IO21 = GPIO(GPIO.GPIO7,GPIO.OUT)
    IO22 = GPIO(GPIO.GPIOHS0,GPIO.OUT)

    #IO9. value(1)
    IO10.value(0)
    IO23.value(1)
    IO27.value(0)
    IO26.value(1)
    IO28.value(0)
    IO25.value(1)
    IO21.value(0)
    IO22.value(1)


    #IO9. value(0)
    IO10.value(1)
    IO23.value(0)
    IO27.value(1)
    IO26.value(0)
    IO28.value(1)
    IO25.value(0)
    IO21.value(1)
    IO22.value(0)
    '''

    ylw = i2c.readfrom(ADC_ADDR,7)
    print ("Stm32版本: V_" ,ylw[4],".",ylw[5],sep='')
    print("IO输出状态已就绪...")
    lcd.draw_string(40, 20, 'Stm32_Ver: ' + str(ylw[4]) + '.' +str(ylw[5]), lcd.RED, lcd.BLACK)
    lcd.draw_string(90, 50, 'Start test GPIO... ', lcd.RED, lcd.BLACK)


####STM32_IO测试(不能同时和k210_IO测试一起使用)#######
####配合跳线帽分别将P0和P1,P2和P3,.....P8和3.3v短接测试

    from aibit import *
    pin_1 = Pin(1,inout_mode = 0) #输入
    pin_6 = Pin(6,inout_mode = 1) #输出
    pin_12 = Pin(12,inout_mode = 0)
    pin_0 = Pin(0,inout_mode = 1)
    pin_2 = Pin(2,inout_mode = 0)
    pin_3 = Pin(3,inout_mode = 1)
    pin_4 = Pin(4,inout_mode = 0)
    pin_5 = Pin(5,inout_mode = 1)
    pin_7 = Pin(7,inout_mode = 0)


    #pin_1.set_digtial(0) #P0
    pin_6.set_digtial(1) #P1
    #pin_12.set_digtial(0)#P2
    pin_0.set_digtial(0) #P3
    #pin_2.set_digtial(0) #P4
    pin_3.set_digtial(1) #P5 (K210->IO9)
    #pin_4.set_digtial(0) #P6
    pin_5.set_digtial(0) #P7
    #pin_7.set_digtial(0) #P8

    P0=pin_1.digtial()
    #P1=pin_6.digtial()
    P2=pin_12.digtial()
    #P3=pin_0.digtial()
    P4=pin_2.digtial()
    #P5=pin_3.digtial()
    P6=pin_4.digtial()
    #P7=pin_5.digtial()
    P8=pin_7.digtial()
    print("P0 P2 P4 P6 P8 IO状态：")
    print(P0,P2,P4,P6,P8)
    lcd.draw_string(90, 70, "IO :"+str(P0)+str(P2)+str(P4)+str(P6)+str(P8) , lcd.RED, lcd.BLACK)
    if (P0==1 and P2==0 and P4==1 and P6==0 and P8==1) ==1 :
        print("GPIO第一次测试通过！！")
        time.sleep(1)

        #lcd.draw_string(90, 100, ' GPIO ok!! ', lcd.RED, lcd.BLACK)
    else:
        print("GPIO第一次测试失败！！")
        lcd.draw_string(70, 140, ' GPIO test failed! ', lcd.GREEN, lcd.BLACK)
        time.sleep(5)

    ##输入输出交换
    pin_1 = Pin(1,inout_mode = 1) #输出
    pin_6 = Pin(6,inout_mode = 0) #输入
    pin_12 = Pin(12,inout_mode = 1)
    pin_0 = Pin(0,inout_mode = 0)
    pin_2 = Pin(2,inout_mode = 1)
    pin_3 = Pin(3,inout_mode = 0)
    pin_4 = Pin(4,inout_mode = 1)
    pin_5 = Pin(5,inout_mode = 0)
    pin_7 = Pin(7,inout_mode = 1)

    pin_1.set_digtial(1) #P0
    pin_12.set_digtial(0)#P2
    pin_2.set_digtial(1) #P4
    pin_4.set_digtial(0) #P6
    pin_7.set_digtial(1) #P8

    P1=pin_6.digtial()
    P3=pin_0.digtial()
    P5=pin_3.digtial()
    P7=pin_5.digtial()
    print("P1 P3 P5 P7 IO状态：")
    print(P1,P3,P5,P7)
    lcd.draw_string(90, 70, "IO :"+str(P1)+str(P3)+str(P5)+str(P7)+"  " , lcd.RED, lcd.BLACK)
    if (P1==1 and P3==0 and P5==1 and P7==0 ) ==1 :
        print("GPIO测试通过！！")
        lcd.draw_string(90, 100, ' GPIO ok!! ', lcd.RED, lcd.BLACK)
    else:
        print("GPIO测试失败！！")
        lcd.draw_string(70, 140, ' GPIO test failed! ', lcd.GREEN, lcd.BLACK)
        time.sleep(5)

    time.sleep(2)
    lcd.clear()

######################开始测试#######################
gpio()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

