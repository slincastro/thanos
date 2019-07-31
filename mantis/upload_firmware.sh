#!/bin/sh
rm /Users/scastro/Projects/esp32-dependencies/esp32-Frirmware.bin

FIRMWARE_PATH= '/Users/scastro/Projects/esp32-dependencies/esp32-Frirmware.bin'


curl -o /Users/scastro/Projects/esp32-dependencies/esp32-Frirmware.bin 'https://micropython.org/resources/firmware/esp32-20190529-v1.11.bin' 

#SERIAL_PORT= ls /dev/tty.* | grep 'USB'
#ESP32_PORT= "/dev/tty.SLAB_USBtoUART"
#echo "Port :"
#echo $ESP32_PORT
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART erase_flash

esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 /Users/scastro/Projects/esp32-dependencies/esp32-Frirmware.bin

#esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin


