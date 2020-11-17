# Untitled - By: YW - 周五 11月 13 2020

# Untitled - By: yewoei - 周四 11月 5 2020

# Untitled - By: yewoei - 周二 11月 3 2020


i2c = I2C(I2C.I2C0, freq=100000, scl=21, sda=22)
devices = i2c.scan()
lcd.init()


def buzzer():#蜂鸣器
     print("开始测试蜂鸣器...")
     lcd.draw_string(30, 50, 'Start test Buzzer ', lcd.RED, lcd.BLACK)
     tim4 = Timer(Timer.TIMER2, Timer.CHANNEL1, mode=Timer.MODE_PWM)
     ch = PWM(tim4, freq=30, duty=50, pin=34)
     ch.freq(523)
     time.sleep(0.3)
     ch.freq(587)
     time.sleep(0.3)
     ch.freq(659)
     time.sleep(0.3)
     ch.freq(689)
     time.sleep(0.3)
     ch.freq(784)
     time.sleep(0.3)
     ch.freq(880)
     time.sleep(0.3)
     ch.freq(988)
     time.sleep(0.3)
     tim4.stop()
     lcd.draw_string(30, 90, 'End Buzzer test ', lcd.RED, lcd.BLACK)
     time.sleep(1)
     lcd.clear()
     print("蜂鸣器测试完成")



######################开始测试#######################
buzzer()

print("全部测试已完成！！")
lcd.draw_string(90, 100, 'End of  test !! ', lcd.RED, lcd.BLACK)
lcd.draw_string(90, 120, 'End of all test !!! ', lcd.RED, lcd.BLACK)

