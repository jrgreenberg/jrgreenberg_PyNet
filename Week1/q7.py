import yaml
import json
from pprint import pprint
with open ("q6yaml.yml") as f:
    yaml_data = yaml.load(f)
with open ("q6json.json") as ff:
    json_data = json.load(ff)

seperator = "-" * 20
print seperator
pprint("YAML output")
print seperator
pprint(yaml_data)
print seperator
pprint("JSON output")
print seperator
pprint(json_data)
print seperator
