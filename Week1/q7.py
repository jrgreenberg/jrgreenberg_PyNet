import yaml
from pprint import pprint
with open ("q6yaml.yml") as f:
    yaml_data = yaml.load(f)
pprint(yaml_data)
