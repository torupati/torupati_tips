

If you ware said "fatal error: bcm_host.h:No such file or directory, run this.

```
sudo apt-get install libraspberrypi-dev raspberrypi-kernel-headers
```

[fatal error: bcm_host.h: No such file or directory](https://raspberrypi.stackexchange.com/questions/36121/fatal-error-bcm-host-h-no-such-file-or-directory-compilation-terminated)
[link](https://geek.tacoskingdom.com/blog/135#:~:text=%E6%89%8B%E9%A0%86%E3%81%A8%E3%81%97%E3%81%A6%E3%81%AF%E3%83%A1%E3%83%BC%E3%82%AB%E3%83%BC%E3%81%AE,%E3%81%8B%E3%82%89%E3%82%84%E3%81%A3%E3%81%A6%E3%81%84%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82&text=%E3%81%BE%E3%81%9A%E3%81%AF%E3%83%89%E3%83%A9%E3%82%A4%E3%83%90%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%8B%E3%82%89,show%20Reading%20package%20lists...)


interface/mmal/mmal.h: No such file

Here are some steps to install from build mmal on Raspberry Pi:
Install pre-required packages
sudo apt-get install cmake
libopencv-dev
Place Raspberry Pi userland project in /home/pi/src/raspberrypi/userland
`mkdir -p /home/pi/src/raspberrypi
`cd /home/pi/src/raspberrypi
git clone --depth 1
Build pre-required libraries
sudo mkdir motion
sudo cd motion
sudo apt-get install autoconf automake build-essential pkgconf libtool libzip-dev libjpeg-dev git libavformat-dev libavcodec-dev libavutil-dev﻿