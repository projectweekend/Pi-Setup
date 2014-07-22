#!/usr/bin/env python
import subprocess
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Want to install VNC server? (Y/N): "
    skip_txt = "Skipping VNC server..."

    def action():
        subprocess.call(["apt-get", "-y", "install", "tightvncserver"])

    OptionalInstall(prompt_txt, skip_txt, action).run()

if __name__ == '__main__':
	main()
