#!/usr/bin/env python
import os
import subprocess
from utils import file_templates
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Want to enable the I2C pins? (Y/N): "
    skip_txt = "Skipping I2C..."

    def action():
        update_file('/etc/modules')
        subprocess.call(["apt-get", "-y", "install", "python-smbus"])
        subprocess.call(["apt-get", "-y", "install", "i2c-tools"])
        if os.path.isfile('/etc/modprobe.d/raspi-blacklist.conf'):
            update_file('/etc/modprobe.d/raspi-blacklist.conf')

    OptionalInstall(prompt_txt, skip_txt, action).run()


def update_file(path):
    template_name = path.split('/')[-1]
    new_file_data = file_templates.load(template_name)
    with open(path, 'w') as f:
        f.write(new_file_data)


if __name__ == '__main__':
    main()
