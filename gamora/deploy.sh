#!/bin/bash

ampy --port /dev/tty.SLAB_USBtoUART rmdir /domain
ampy --port /dev/tty.SLAB_USBtoUART put ./domain/
ampy --port /dev/tty.SLAB_USBtoUART ls domain
ampy --port /dev/tty.SLAB_USBtoUART run gamora.py