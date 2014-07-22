#!/usr/bin/env python
import subprocess
from utils.installation import OptionalInstall


def main():
    prompt_txt = "Want to install ipython-notebook? (Y/N): "
    skip_txt = "Skipping ipython-notebook..."

    def action():
        subprocess.call(["apt-get", "-y", "install", "ipython-notebook"])

    OptionalInstall(prompt_txt, skip_txt, action).run()


if __name__ == '__main__':
    main()
