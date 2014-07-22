#!/usr/bin/env python
import subprocess
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Want to set a new password? (Y/N): "
    skip_txt = "Skipping password..."

    def action():
        subprocess.call(["passwd"])

    OptionalInstall(prompt_txt, skip_txt, action).run()


if __name__ == '__main__':
	main()
