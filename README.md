-------------------------------------------------------------------------------
### Usage
-------------------------------------------------------------------------------

#### Step 1: Clone this repository

```
git clone https://github.com/projectweekend/Pi-Setup.git
```

#### Step 2: Run the script

From the project directory `/Pi-Setup`, run the following command:

```
./pi_setup.sh
```

#### Step 3: Reboot

```
sudo reboot
```


-------------------------------------------------------------------------------
### Features
-------------------------------------------------------------------------------

This setup script will help you perform the following tasks. Launching the script with no parameters (`./pi_setup`) will run through all of its steps prompting you to confirm each **optional** item before it begins. This is handy when setting up a brand new Raspberry Pi, however each **optional** item can be executed individually by passing the appropriate **parameter** to the script. Example: `./pi_setup vnc`

#### Automatic Items

* apt-get update & upgrade
* install [avahi-daemon](http://en.wikipedia.org/wiki/Avahi_(software))
* install [python-dev](https://packages.debian.org/wheezy/python-dev)
* install [python-pip](https://packages.debian.org/wheezy/python-pip)
* install [virtualenv](http://virtualenv.readthedocs.org/en/latest/)
* install [rpi-update](https://github.com/Hexxeh/rpi-update)

#### Optional Items

* wifi setup (**parameter**: `wireless`)
* GPU memory split (**parameter**: `boot`)
* change hostname (**parameter**: `hostname`)
* change `pi` user password (**parameter**: `password`)
* enable [I2C](http://en.wikipedia.org/wiki/I²C) & [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) pins (**parameter**: `i2c`)
* enable GPIO for serial data (**parameter**: `serial`)
* install a [VNC server](http://www.tightvnc.com) (**parameter**: `vnc`)
* browse and install various optional software (**parameter**: `software`)
