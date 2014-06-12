#!/usr/bin/env python
import subprocess


def main():
	user_input = raw_input("Want to set a new password? (Y/N): ")
	if user_input == 'Y':
		subprocess.call(["passwd"])
	else:
		print("Skipping password...")


if __name__ == '__main__':
	main()
