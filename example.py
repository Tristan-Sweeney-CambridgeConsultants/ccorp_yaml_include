import pprint

from ccorp.ruamel.yaml.include import YAML
yaml = YAML(typ='safe', pure=True)

with open('data/root.yaml', 'r') as f:
    data = yaml.load(f)

pprint.pprint(data)
