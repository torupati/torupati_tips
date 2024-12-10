# Procedure

1. Raspberry PiのGPIOの設定
2. PPS信号のテスト
3. GPSd の導入
4. chrony の導入

### GPIOピンの設定

- PPSを受ける信号の設定
- UARTを受けるため

raspi-config でI2Cを有効にする。
他の方法でもよいのかもしれないが。/etc/modules にi2c が書かれているはず。

(1) /boot/firmware/config.txt or /boot/config.txt

Legacy raspbian seems using /boot/config.txt. 
To activate I2C and UART, raspi-config is enough.

```
dtoverlay=pps-gpio, gpsiopin=18
```

Is PPS signal comes as high (as is usueal case), this is OK. If positie case, add like this.

```
dtoverlay=pps-gpio, gpsiopin=18,assert_falling_edge=true
```

Someone reported that bluetooth should be disabled. This is related enable_uart1 in config.txt

```
dtoverlay=disable-bt
```

```
[all]
...
enable_uart=1
```

(2) /etc/modules

Newly registered input must be registered at /etc/modules.

```
i2c-dev
pps-gpio
```

(3) /boot/cmdline

Deactivate serial login by UART.

```
sudo sed -i 's/console=serial0,115200 //g' /boot/cmdline.txt 
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
```


### PPS test

Now you can find /dev/pps0.

```
$ sudo apt install pps-tools
$ sudo ppstest /dev/pps0
```

### GPSd

Install and configure. Configuration may be different in gpsd version.

```
$ sudo apt install gpsd gpsd-clients
```

/etc/gpsd

```
> DEVICES="/dev/ttyAMA0 /dev/pps0"
> GPSD_OPTIONS="-b -n"
> USBAUTO="false"
```

Add system controle of Linux.

```
$ sudo sytemctl enable gpsd.service
$ sudo sytemctl restart gpsd.service
$ sudo sytemctl enable gpsd.socket
$ sudo sytemctl restart gpsd.socket
```

You can run ```$ gpsmon -n``` or ```$cgps -s``` for monitoring on terminals.


### Chronyc

```
$ sudo apt install chrony
```

chronyd, chronyc are installed.

/etc/chrony/corony.conf

> log tracking measurements statistics<br>
> logdir /var/log/chrony<br>
> refclock PPS lock NMEA refid GPS<br>
> refclock SHM 0 offset 0.5 delay 0.1 refid NMEA noselect<br>

Register to OS service.

```
$ sudo systemctl enable chrony
$ sudo systemctl start chrony
$ sudo systemctl disable systemd-timesyncd.service
```

Check status.

```
$ systemctl is-enabled chronyd.service
$ systemctl status chronyd.service
$ timedatectl
```

You can see ```$ chronyc sources -v``` or ```$ chronyc tracking```

Version of gpsd is also important. Here, using SOCK is documented for gpsd 3.25 etc.

[2.13. How should chronyd be configured with gpsd?](https://chrony-project.org/faq.html)



# References

- [chrony.conf(5) Manual Page](https://chrony-project.org/doc/4.3/chrony.conf.html)
- [How to serve the Network Time Protocol with chrony](https://discourse.ubuntu.com/t/how-to-serve-the-network-time-protocol-with-chrony/36311
)
- [How to serve the Network Time Protocol with chrony](https://ubuntu.com/server/docs/how-to-serve-the-network-time-protocol-with-chrony)

- [RPi4, Ubuntu22.04, GPS, 1PPS, chrony](https://blog.bitmeister.jp/?p=5238)
- [RaspberryPi に GPSレシーバー と RTC をつけてGPS 1PPS対応NTPサーバにする](https://qiita.com/yamakenjp/items/e69eeabdefd9cc960610)

- [GPSD Time Service HOWTO](https://gpsd.gitlab.io/gpsd/gpsd-time-service-howto.html)

- [Configuration examples and accuracy](https://chrony-project.org/examples.html) Many example analysis.