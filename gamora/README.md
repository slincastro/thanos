# Gam0ra

Gamora is an IOT node of Thanos project, its writed on micropython and designed to run in an esp8266mod.

The first step is Load a micropython firmware on esp8266mod.

### Prerequisites

0. Install Board Drivers for Mac [Drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)

0. Install [Python3](https://docs.python-guide.org/starting/install3/osx/)

### Load micropython firmware on Mac

1. List ports to find the name of the board.

    `ls /dev/tty.*`

    `/dev/tty.SLAB_USBtoUART`

1.  Donwload bin file [Reference](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)

1. Install esptool with pip command. 
   
    `pip install esptool`

1. Clear flash with esptool.
   
    `esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`

1. Load firmware on esp8266.
    
    `esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin`

### Install ampy

You need ampy in order to connect in realtime on esp by serial port

### Install ampy

- depending of the python version :
    > `pip install adafruit-ampy`

    > `pip3.8 install adafruit-ampy`

* Include ampy in path (this works for 3.8 version)
    `PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/; export PATH`

* List files in esp

    `ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 ls`

* Connect by serial to esp8266
    
    `python -m serial.tools.miniterm --raw /dev/tty.SLAB_USBtoUART 115200`

* Run local script on esp8266
  
    `ampy --port /dev/tty.SLAB_USBtoUART run --no-output gamora.py`

* Put reference on esp memory
    
    `ampy --port /dev/tty.SLAB_USBtoUART put LedManager.py`

* Remove directory

    `ampy --port /dev/tty.SLAB_USBtoUART rmdir /domain`

* Put directory

    `ampy --port /dev/tty.SLAB_USBtoUART put ./domain/`

* Get file 
    
    `ampy --port /serial/port get boot.py`

### Set an Alias :

`alias gamora='ampy --port /dev/tty.SLAB_USBtoUART' `

now you can use gamora instead of apmpy .....
