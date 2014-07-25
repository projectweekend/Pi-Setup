#!/usr/bin/env python
from utils.installation import OptionalInstall
from utils.software import install_nodejs


OPTIONAL_SOFTWARE = {
	"nodejs": install_nodejs
}


def main():
	prompt_txt = "Want to see a list of optional software to install? (Y/N): "
	skip_txt = "Skipping optional software..."

	def action():
		start_optional_software()

	OptionalInstall(prompt_txt, skip_txt, action)


def start_optional_software():
	print_software_list()

	user_input = ""
	while user_input != "done":
		pass


def print_software_list():
	for i in OPTIONAL_SOFTWARE:
		print(i)
	print("When you are finished type: done")
