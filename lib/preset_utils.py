import os
import sys
import json
import traceback
from cStringIO import StringIO


def presets_path():
    try:
        import appdirs
        config_path = appdirs.user_config_dir('inkscape-embroidery')
    except ImportError:
        config_path = os.path.expanduser('~/.inkscape-embroidery')

    if not os.path.exists(config_path):
        os.makedirs(config_path)
    return os.path.join(config_path, 'presets.json')


def load_presets():
    try:
        with open(presets_path(), 'r') as presets:
            presets = json.load(presets)
            return presets
    except:
        return {}


def save_presets(presets):
    with open(presets_path(), 'w') as presets_file:
        json.dump(presets, presets_file)


def load_preset(name):
    return load_presets().get(name)


def save_preset(name, data):
    presets = load_presets()
    presets[name] = data
    save_presets(presets)


def delete_preset(name):
    presets = load_presets()
    presets.pop(name, None)
    save_presets(presets)
