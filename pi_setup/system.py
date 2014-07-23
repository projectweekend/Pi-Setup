#!/usr/bin/env python
import subprocess
from utils.installation import OptionalInstall


def main():
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])
    subprocess.call(["apt-get", "-y", "install", "avahi-daemon"])
    subprocess.call(["apt-get", "-y", "install", "rpi-update"])
    subprocess.call(["pip", "install", "virtualenv"])
    optional_install_upstart()


def optional_install_upstart():
    prompt_txt = "Want to install Upstart (Y/N): "
    skip_txt = "Skipping Upstart server..."

    def action():
        subprocess.call(["apt-get", "-y", "install", "upstart"])

    OptionalInstall(prompt_txt, skip_txt, action).run()


if __name__ == '__main__':
	main()
