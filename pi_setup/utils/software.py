import os
import subprocess


def install_nodejs():
	subprocess.call('curl -sL https://deb.nodesource.com/setup | bash -', shell=True)
	subprocess.call('apt-get -y install nodejs', shell=True)


def install_ipython():
	subprocess.call(["apt-get", "-y", "install", "ipython-notebook"])


def install_upstart():
	subprocess.call("echo Yes, do as I say! | sudo apt-get -y --force-yes install upstart", shell=True)


def install_bluez():
	subprocess.call(["apt-get", "-y", "install", "libusb-dev"])
	subprocess.call(["apt-get", "-y", "install", "libdbus-1-dev"])
	subprocess.call(["apt-get", "-y", "install", "libglib2.0-dev"])
	subprocess.call(["apt-get", "-y", "install", "libudev-dev"])
	subprocess.call(["apt-get", "-y", "install", "libical-dev"])
	subprocess.call(["apt-get", "-y", "install", "libreadline-dev"])

    # Install BlueZ
	os.chdir("/home/pi")
	subprocess.call(["mkdir", "bluez"])
	os.chdir("bluez")
	subprocess.call(["wget", "https://www.kernel.org/pub/linux/bluetooth/bluez-5.22.tar.xz"])
	subprocess.call(["unxz", "bluez-5.22.tar.xz"])
	subprocess.call(["tar", "xvf", "bluez-5.22.tar"])
	os.chdir("bluez-5.22")
	subprocess.call(["./configure", "--disable-systemd"])
	subprocess.call(["make"])
	subprocess.call(["make", "install"])

    # Clean up BlueZ build directory
	os.chdir("/home/pi")
	subprocess.call(["rm", "-r", "bluez"])

    # Install BluePy
	subprocess.call(["git", "clone", "https://github.com/IanHarvey/bluepy.git"])
	os.chdir("bluepy/bluepy")
	subprocess.call(["make"])

	subprocess.call(["cp", "bluepy-helper", "/usr/local/lib/python2.7/dist-packages/"])
	subprocess.call(["cp", "btle.py", "/usr/local/lib/python2.7/dist-packages/"])
	subprocess.call(["cp", "sensortag.py", "/usr/local/lib/python2.7/dist-packages/"])

    # Clean up BluePy build directory
	os.chdir("/home/pi")
	subprocess.call(["rm", "-r", "bluepy"])
