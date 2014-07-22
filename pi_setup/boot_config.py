#!/usr/bin/env python
from utils import file_templates
from utils.validation import is_valid_gpu_mem
from utils.installation import OptionalInstall


def main():
	prompt_txt = "Want to change the GPU memory split? (Y/N): "
	skip_txt = "Skipping GPU memory split..."

	def action():
		gpu_mem = 0
		while gpu_mem == 0:
			mem_split = raw_input("Enter GPU memory in MB (16/32/64/128/256): ")
			if is_valid_gpu_mem(mem_split):
				gpu_mem = mem_split
			else:
				print("Acceptable memory values are: 16/32/64/128/256")
		update_file('/boot/config.txt', gpu_mem)

	OptionalInstall(prompt_txt, skip_txt, action).run()


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
