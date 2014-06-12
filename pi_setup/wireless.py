#!/usr/bin/env python
from utils import file_templates


def main():
	user_input = raw_input("Want to setup wifi? (Y/N): ")
	if user_input == 'Y':
		ssid = ''
		password = ''
		while ssid == '' and password == '':
			ssid = raw_input("Wifi network name (ssid): ")
			password = raw_input("Wifi password: ")
		update_file('/etc/network/interfaces', ssid, password)
	else:
		print("Skipping wifi...")


def update_file(path, ssid, password):
	data = {
		'ssid': ssid,
		'password': password
	}
	template_name = path.split('/')[-1]
	new_file_data = file_templates.build(template_name, data)
	with open(path, 'w') as f:
		f.write(new_file_data)


if __name__ == '__main__':
	main()
