#!/usr/bin/env python
from utils import file_templates


def main():
	user_input = raw_input("Setup GPIO serial for data? (Y/N): ")
	if user_input == 'Y':
		update_file('/etc/inittab')
	else:
		print("Skipping GPIO serial...")


def update_file(path):
    template_name = path.split('/')[-1]
    new_file_data = file_templates.load(template_name)
    with open(path, 'w') as f:
        f.write(new_file_data)


if __name__ == '__main__':
	main()
