#!/usr/bin/env python
import subprocess


def main():
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "install", "software-properties-common"])
    subprocess.call(["apt-get", "-y", "install", "python-software-properties"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])
    subprocess.call(["apt-get", "-y", "install", "avahi-daemon"])
    subprocess.call(["apt-get", "-y", "install", "rpi-update"])
    subprocess.call(["pip", "install", "virtualenv"])


if __name__ == '__main__':
	main()
