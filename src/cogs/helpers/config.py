import yaml

def load():
    parsed_config_data = yaml.load(open('src/config.yml'), Loader=yaml.SafeLoader)
    return parsed_config_data