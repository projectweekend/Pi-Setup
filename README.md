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

This setup script will perform the following tasks:

* wifi setup
* GPU memory split
* change hostname
* apt-get update & upgrade
* install `avahi-daemon`
* install `python-dev`
* install `python-pip`
* install `virtualenv`
