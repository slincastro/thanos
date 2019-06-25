#list ports

[Reference](http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware)

`ls /dev/tty.usb*`
`/dev/tty.SLAB_USBtoUART`
`esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`
`esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin`
`screen name port`

pip install adafruit-ampy

download miniconda
https://docs.conda.io/en/latest/miniconda.html

export PATH="$HOME/miniconda3/bin:$PATH"
source $HOME/miniconda3/bin/activate
conda create --name

conda activate thanos

https://pythonforundergradengineers.com/upload-py-files-to-esp8266-running-micropython.html

pip install adafruit-ampy

ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 ls

python -m serial.tools.miniterm --raw /dev/tty.SLAB_USBtoUART 115200

run local script on esp8266
´ampy --port /dev/tty.SLAB_USBtoUART run --no-output gamora.py´

