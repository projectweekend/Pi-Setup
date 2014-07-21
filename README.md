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
* enable I2C for GPIO
* enable GPIO for serial data
* install a VNC server
* install `ipython-notebook`

#### Automatic Items

* apt-get update & upgrade
* install `avahi-daemon`
* install `python-dev`
* install `python-pip`
* install `virtualenv`
* install `rpi-update`
