import re

def is_valid_hostname(new_hostname):
    return re.match('^[\w-]+$', new_hostname)
