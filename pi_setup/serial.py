#!/usr/bin/env python
from utils import file_templates
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Setup GPIO serial for data? (Y/N): "
    skip_txt = "Skipping GPIO serial..."

    def action():
        update_file('/etc/inittab')
        update_file('/boot/cmdline.txt')

    OptionalInstall(prompt_txt, skip_txt, action).run()


def update_file(path):
    template_name = path.split('/')[-1]
    new_file_data = file_templates.load(template_name)
    with open(path, 'w') as f:
        f.write(new_file_data)


if __name__ == '__main__':
	main()
