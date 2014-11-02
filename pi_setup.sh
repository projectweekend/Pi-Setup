#!/usr/bin/env bash

sudo python pi_setup/system.py

if [ -z "$1" ];
    then
        sudo python pi_setup/vnc.py
        sudo python pi_setup/ipython.py
        python pi_setup/password.py
        sudo python pi_setup/hostname.py
        sudo python pi_setup/wireless.py
        sudo python pi_setup/boot_config.py
        sudo python pi_setup/i2c.py
        sudo python pi_setup/serial.py
        sudo python pi_setup/bluez.py
        sudo python pi_setup/firmware.py

elif [ -n "$1" ] && [ $1 == 'vnc' ];
    then
    sudo python pi_setup/vnc.py

elif [ -n "$1" ] && [ $1 == 'ipython' ];
    then
    sudo python pi_setup/ipython.py

elif [ -n "$1" ] && [ $1 == 'password' ];
    then
    python pi_setup/password.py

elif [ -n "$1" ] && [ $1 == 'hostname' ];
    then
    sudo python pi_setup/hostname.py

elif [ -n "$1" ] && [ $1 == 'wireless' ];
    then
    sudo python pi_setup/wireless.py

elif [ -n "$1" ] && [ $1 == 'boot' ];
    then
    sudo python pi_setup/boot_config.py

elif [ -n "$1" ] && [ $1 == 'i2c' ];
    then
    sudo python pi_setup/i2c.py

elif [ -n "$1" ] && [ $1 == 'serial' ];
    then
    sudo python pi_setup/serial.py

elif [ -n "$1" ] && [ $1 == 'firmware' ];
    then
    sudo python pi_setup/firmware.py

elif [ -n "$1" ] && [ $1 == 'bluez' ];
    then
    sudo python pi_setup/bluez.py
fi
