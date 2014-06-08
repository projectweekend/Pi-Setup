#!/usr/bin/env python
import subprocess


def main():
	subprocess.call(['apt-get','install','ssh'])
	subprocess.call(['update-rc.d', 'ssh', 'defaults'])


if __name__ == '__main__':
	main()
