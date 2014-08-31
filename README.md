-------------------------------------------------------------------------------
### Setup
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

This setup script will help you perform the following tasks. You will be prompted to confirm each optional item before it begins.

#### Optional Items

* wifi setup
* GPU memory split
* change hostname
* change `pi` user password
* enable [I2C](http://en.wikipedia.org/wiki/I²C) & [SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus) pins
* enable GPIO for serial data
* install a [VNC server](http://www.tightvnc.com)
* install [ipython-notebook](http://ipython.org/notebook.html)
* install [upstart](http://upstart.ubuntu.com/)
* install [BlueZ](http://en.wikipedia.org/wiki/Bluetooth_stack#BlueZ) Bluetooth stack & [BluePy](https://github.com/IanHarvey/bluepy) a Python interface for Bluetooth Low Energy.

#### Automatic Items

* apt-get update & upgrade
* install [avahi-daemon](http://en.wikipedia.org/wiki/Avahi_(software))
* install [python-dev](https://packages.debian.org/wheezy/python-dev)
* install [python-pip](https://packages.debian.org/wheezy/python-pip)
* install [virtualenv](http://virtualenv.readthedocs.org/en/latest/)
* install [rpi-update](https://github.com/Hexxeh/rpi-update)
