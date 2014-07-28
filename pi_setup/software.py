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
		user_input = ""
		while user_input != "done":

			for i in OPTIONAL_SOFTWARE:
				print(i)
			print("When you are finished type: done")

			user_input = raw_input("Item to install: ")
			try:
				OPTIONAL_SOFTWARE[user_input]()
			except KeyError:
				print("'{0}' is not a valid selection".format(user_input))
		else:
			print("Optional software complete...")

	OptionalInstall(prompt_txt, skip_txt, action)
