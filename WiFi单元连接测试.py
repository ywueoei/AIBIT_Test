# Untitled - By: YW - 周五 11月 13 2020

import network, time
from machine import UART
from Maix import GPIO
from fpioa_manager import fm, board_info

import socket, network, time
import lcd, image
from Maix import GPIO
from machine import UART
from fpioa_manager import fm, board_info
WIFI_SSID = "cool"
WIFI_PASSWD = "12369874"
#WIFI_SSID = "12345678"        # 改变wifi并多次连接测试
#WIFI_PASSWD = "123456788"

# En SEP8285
fm.register(8, fm.fpioa.GPIOHS0, force=True)
wifi_en=GPIO(GPIO.GPIOHS0, GPIO.OUT)

'''
# for new MaixGO board, if not, remove it
fm.register(0, fm.fpioa.GPIOHS1, force=True)
wifi_io0_en=GPIO(GPIO.GPIOHS1, GPIO.OUT)
wifi_io0_en.value(0)
'''
fm.register(board_info.WIFI_RX, fm.fpioa.UART2_TX, force=True)
fm.register(board_info.WIFI_TX, fm.fpioa.UART2_RX, force=True)

uart = UART(UART.UART2,115200,timeout=1000, read_buf_len=4096)

def wifi_enable(en):
    global wifi_en
    wifi_en.value(en)

def wifi_deal_ap_info(info):
    res = []
    for ap_str in info:
        ap_str = ap_str.split(",")
        info_one = []
        for node in ap_str:
            if node.startswith('"'):
                info_one.append(node[1:-1])
            else:
                info_one.append(int(node))
        res.append(info_one)
    return res


wifi_enable(1)
time.sleep(2)
nic = network.ESP8285(uart)

ap_info = nic.scan()
ap_info = wifi_deal_ap_info(ap_info)

ap_info.sort(key=lambda x:x[2], reverse=True) # sort by rssi
for ap in ap_info:
    print("SSID:{:^20}, RSSI:{:>5} , MAC:{:^20}".format(ap[1], ap[2], ap[3]) )

nic.connect(WIFI_SSID, WIFI_PASSWD)


#print("ping baidu.com:", nic.ping("www.baidu.com"), "ms")
'''
#nic.
nic.ifconfig()

err = 0
sock = socket.socket()
while 1:
    try:
        addr = socket.getaddrinfo("dl.sipeed.com", 80)[0][-1]
        break
    except Exception:
        err += 1
    if err > 5:
        raise Exception("get ip failed!")
'''
