#!/usr/bin/env bash
sudo python pi_setup/system.py
python pi_setup/password.py
sudo python pi_setup/hostname.py
sudo python pi_setup/wireless.py
sudo python pi_setup/boot_config.py
sudo python pi_setup/i2c.py
sudo python pi_setup/serial.py
sudo python pi_setup/firmware.py
