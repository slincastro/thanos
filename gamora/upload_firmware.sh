#!/bin/sh

USER=$(id -un)
BASE_PATH=$(pwd)'/esp8266-dependencies/'
FIRMWARE_PATH=$BASE_PATH'esp8266-Frirmware.bin'
FIRMWARE_URL='https://micropython.org/resources/firmware/esp8266-20200911-v1.13.bin'
ESP8266_PORT=$(ls /dev/tty.* | grep "USB")

echo "---------------------------------------------------------------------------"
echo "Base Path :" $BASE_PATH
echo "Firmware Path :" $FIRMWARE_PATH
echo "Firmware URL :" $FIRMWARE_URL
echo "USER :" $USER
echo "ESP PORT :"$ESP8266_PORT
echo "---------------------------------------------------------------------------"

rm -rf $BASE_PATH
mkdir $BASE_PATH

curl -o $FIRMWARE_PATH $FIRMWARE_URL

esptool.py --port $ESP8266_PORT erase_flash

esptool.py --port $ESP8266_PORT --baud 460800 write_flash --flash_size=detect 0 $FIRMWARE_PATH

rm -rf $BASE_PATH
