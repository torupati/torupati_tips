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

(1) /boot/config.txt

```
dtoverlay=pps-gpio, gpsiopin=18
```

Is PPS signal comes as high (as is usueal case), this is OK. If positie case, add like this.

```
dtoverlay=pps-gpio, gpsiopin=18,assert_falling_edge=true
```

Someone reported that bluetooth should be disabled.

```
dtoverlay=disable-bt
```

(2) /etc/modules

Newly registered input must be registered at /etc/modules.


```
pps-gpio
```

### PPS test

Now you can find /dev/pps0.

```
$ sudo apt-get install pps-tools
$ sudo ppstest /dev/pps0
```

### GPSd

Install and configure. Configuration may be different in gpsd version.

```
$ sudo apt install gpsd gpsd-clients
```

/etc/bpsd

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

You can run ```$ gpsmon``` or ```$cgps -s``` for monitoring on terminals.

### Chronyc

```
$ sudo apt-get install chrony
```

/etc/chrony/corony.conf

> log tracking measurements statistics<br>
> logdir /var/log/chrony<br>
> refclock SHM 0 refid SHM0 offset 0.053 noselect<br>
> refclock SHM 1 refid SHM1 pps prefer trust<br>
> refclock SHM 2 refid SHM2

You can see ```$ chronyc sources -v```

