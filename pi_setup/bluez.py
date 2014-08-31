#!/usr/bin/env python
import subprocess
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Want to install BlueZ & BluePy for Bluetooth...this will take a while (Y/N): "
    skip_txt = "Skipping BlueZ & BluePy..."

    def action():
    	subprocess.call(["apt-get", "-y", "install", "libusb-dev"])
    	subprocess.call(["apt-get", "-y", "install", "libdbus-1-dev"])
    	subprocess.call(["apt-get", "-y", "install", "libglib2.0-dev"])
    	subprocess.call(["apt-get", "-y", "install", "libudev-dev"])
    	subprocess.call(["apt-get", "-y", "install", "libical-dev"])
    	subprocess.call(["apt-get", "-y", "install", "libreadline-dev"])

    	subprocess.call(["cd", "/home/pi"])
    	subprocess.call(["mkdir", "bluez"])
    	subprocess.call(["cd", "bluez"])
    	subprocess.call(["wget", "https://www.kernel.org/pub/linux/bluetooth/bluez-5.22.tar.xz"])
    	subprocess.call(["unxz", "bluez-5.22.tar.xz"])
    	subprocess.call(["tar", "xvf", "bluez-5.22.tar"])
    	subprocess.call(["cd", "bluez-5.22"])
    	subprocess.call(["./configure", "--disable-systemd"])
    	subprocess.call(["make"])
    	subprocess.call(["make", "install"])
    	subprocess.call(["cd", "/home/pi"])
    	subprocess.call(["rm", "-r", "bluez"])

    	subprocess.call(["git", "clone", "https://github.com/IanHarvey/bluepy.git"])
    	subprocess.call(["cd", "bluepy/bluepy"])
    	subprocess.call(["make"])

    OptionalInstall(prompt_txt, skip_txt, action).run()


if __name__ == '__main__':
	main()