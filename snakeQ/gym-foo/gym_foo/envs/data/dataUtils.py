import json
from pathlib import Path

# config.json

def getConfig(config):
    mapFile = Path("snakeQ/gym-foo/gym_foo/envs/data/config.json")
    with open(mapFile) as f:
        d = json.load(f)
        return d[config]
