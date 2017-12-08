#probably gonna scrap this whole folder

def presets_path():
    try:
        import appdirs
        config_path = appdirs.user_config_dir('inkscape-embroidery')
    except ImportError:
        config_path = os.path.expanduser('~/.inkscape-embroidery')

    if not os.path.exists(config_path):
        os.makedirs(config_path)
    return os.path.join(config_path, 'presets.json')
