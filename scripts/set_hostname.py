#!/usr/bin/env python
import subprocess
from utils import file_templates
from utils.validation import is_valid_hostname


def main():
	user_input = raw_input("Want to change the hostname?: Y/N")
	if user_input == 'Y':
		new_hostname = ''
		while new_hostname == '':
			user_input = raw_input("Enter a new hostname: ")
			if is_valid_hostname(user_input):
				new_hostname = user_input
			else:
				print("'{0}' is not a valid hostname!".format(user_input))
		update_file('/etc/hosts', new_hostname)
		update_file('/etc/hostname', new_hostname)
		subprocess.call(['/etc/init.d/hostname.sh'])
	else:
		print("Skipping hostname...")


def update_file(path, new_hostname):
	template_name = path.split('/')[-1]
	new_file_data = file_templates.build(template_name, [new_hostname])
	with open(path, 'w') as f:
		f.write(new_file_data)


if __name__ == '__main__':
	main()
