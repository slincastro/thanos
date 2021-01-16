#!/bin/bash
echo "----------------------------------------------"
echo "-------- Preparing to deploy gamora ----------"
echo "----------------------------------------------"
echo "Cleaning older artifacts"
echo "----------------------------------------------"
#sh ./clean.sh
echo "----------------------------------------------"
echo "Deploying Artifacts"
echo "----------------------------------------------"
ampy --port /dev/tty.SLAB_USBtoUART put ./domain/
ampy --port /dev/tty.SLAB_USBtoUART put ./configuration/
ampy --port /dev/tty.SLAB_USBtoUART put ./util/
ampy --port /dev/tty.SLAB_USBtoUART put gamora.py main.py
ampy --port /dev/tty.SLAB_USBtoUART put config.json
echo "---------------Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls 
echo "---------------Domain Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls domain
echo "---------------Util Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls util
echo "---------------Configuration Folder------------------"
ampy --port /dev/tty.SLAB_USBtoUART ls configuration
echo "Run Application ......"
#ampy --port /dev/tty.SLAB_USBtoUART run gamora.py