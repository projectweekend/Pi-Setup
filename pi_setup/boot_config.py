#!/usr/bin/env python
from utils import file_templates
from utils.validation import is_valid_gpu_mem


def main():
	gpu_mem = 0
	while gpu_mem == 0:
		user_input = raw_input("Enter GPU memory in MB (16/32/64/128/256): ")
		if is_valid_gpu_mem(user_input):
			gpu_mem = user_input
		else:
			print("Acceptable memory values are: 16/32/64/128/256")
	update_file('/boot/config.txt', gpu_mem)


def update_file(path, gpu_mem):
	data = {
		'gpu_mem': gpu_mem
	}
	template_name = path.split('/')[-1]
	new_file_data = file_templates.build(template_name, data)
	with open(path, 'w') as f:
		f.write(new_file_data)


if __name__ == '__main__':
	main()
