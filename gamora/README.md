#Gam0ra

Gamora is an IOT node of Thanos project, its writed on micropython and designed to run in an esp8266mod.

the first step is Load a micropython firmware on esp8266mod.

### load micropython firmware on Mac

1. list ports.

`ls /dev/tty.usb*`

[Reference](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)

`/dev/tty.SLAB_USBtoUART`

2. Install esptool with pip command. 
   
    `pip install esptool`

3. Clear flash with esptool.
   
    `esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`

1. Load firmware on esp8266.
    
    `esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin`

### install ampy

You need ampy in order to connect in realtime on esp by serial port
pip install adafruit-ampy

### install miniconda

download miniconda
[link](https://docs.conda.io/en/latest/miniconda.html)

export PATH="$HOME/miniconda3/bin:$PATH"
source $HOME/miniconda3/bin/activate

* create environment
  
    `conda create --name`

* activate environmen
  
    `conda activate thanos`

https://pythonforundergradengineers.com/upload-py-files-to-esp8266-running-micropython.html

### install ampy

Run local script on esp8266

`pip install adafruit-ampy`

* List files in esp

    `ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 ls`

* Connect by serial to esp8266
    
    `python -m serial.tools.miniterm --raw /dev/tty.SLAB_USBtoUART 115200`

* Run local script on esp8266
  
    `ampy --port /dev/tty.SLAB_USBtoUART run --no-output gamora.py`

* Put reference on esp memory
    
    `ampyampy --port /dev/tty.SLAB_USBtoUART put LedManager.py`

* Remove directory

    `ampy --port /dev/tty.SLAB_USBtoUART rmdir /domain`

* Put directory

    `ampy --port /dev/tty.SLAB_USBtoUART put ./domain/`

