#!/usr/bin/env python
import subprocess


def main():
    user_input = raw_input("Want to install ipython-notebook? (Y/N): ")
    if user_input == 'Y':
        subprocess.call(["apt-get", "-y", "install", "ipython-notebook"])
    else:
        print("Skipping ipython-notebook...")


if __name__ == '__main__':
    main()
