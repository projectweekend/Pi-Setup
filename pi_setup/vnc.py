#!/usr/bin/env python
import subprocess


def main():
	user_input = raw_input("Want to install VNC server? (Y/N): ")
	if user_input == 'Y':
		subprocess.call(["apt-get", "-y", "install", "tightvncserver"])
	else:
		print("Skipping VNC server...")


if __name__ == '__main__':
	main()
