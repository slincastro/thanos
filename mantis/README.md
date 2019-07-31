#M4ntis

M4ntis is an IOT node of Thanos project, its writed on micropython and designed to run in an esp32mod.

#### the first step is Load a micropython firmware on esp8266mod.

* Install Python 3
   
### load micropython firmware on Mac

1. list ports.

`ls /dev/tty.*`

[Reference](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)

Ej. (Port Name): 
`/dev/tty.SLAB_USBtoUART`

2. Install esptool with pip command. 
   
    `pip install esptool`

------------------------------------

3. Prerequisites

    * Excecute upload_firmware.sh outside of the project folder

        `sh upload_firmware.sh`

#### OR

    * Install Drivers Mac [Drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers),

    `curl -o Mac_OSX_VCP_Driver.zip https://www.silabs.com/documents/public/software/Mac_OSX_VCP_Driver.zip`

    * Download Firmare [Latest Framework Now] (https://micropython.org/resources/firmware/esp32-20190731-v1.11-183-ga8e3201b3.bin)

1. Clear flash with esptool.
   
    `esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`

2. Load firmware on esp32.

    `esptool.py --chip esp32 --port <port> --baud 460800 write_flash -z 0x1000 <<Firmware>>`
    
