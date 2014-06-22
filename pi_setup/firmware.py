#!/usr/bin/env python
import subprocess


def main():
	user_input = raw_input("Want to update firmware? (Y/N): ")
	if  user_input == 'Y':
		subprocess.call(['rpi-update'])


if __name__ == '__main__':
	main()
