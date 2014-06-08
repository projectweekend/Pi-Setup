TEMPLATES_FOLDER = './file_templates'


def build(template_name, data):
    file = TEMPLATES_FOLDER + "/" + template_name
    with open(file, 'r') as f:
        template = f.read()
    return template.format(data)
