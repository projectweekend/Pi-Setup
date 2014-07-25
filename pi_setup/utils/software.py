import subprocess


def install_nodejs():
    subprocess.call(["add-apt-repository", "ppa:chris-lea/node.js"])
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "install", "nodejs"])
    subprocess.call(["apt-get", "-y", "install", "npm"])
