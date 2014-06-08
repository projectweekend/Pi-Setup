import re

def is_valid_hostname(new_hostname):
    return re.match('^[\w-]+$', new_hostname)


def is_valid_gpu_mem(gpu_mem):
    accepted_values = [16, 32, 64, 128, 256]
    return gpu_mem in accepted_values
