import imp

def get_custom_module_dir(module_name):
    # assume this module contains __init__.py and is globally available
    # find the absolute directory of this module
    # return the absolute directory
    _, path, _ = imp.find_module(module_name)
    return path
