import os

__version__ = '0.1.0'
__port__ = 0


def get_base_path():
    """
    get package base dir
    """
    return os.path.dirname(__file__)