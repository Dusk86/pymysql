import yaml

class YamlUtil:
    def connect_sql(self, yaml_path):
        with open(yaml_path, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value