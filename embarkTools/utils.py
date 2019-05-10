import os

from jupyter_core.paths import (
    jupyter_config_dir,
    jupyter_config_path
)
from ipython_genutils import py3compat
from traitlets.config.application import Application
from traitlets.config.loader import Config
from sqlalchemy import create_engine


__all__ = [
    'rela2abs',
    'get_engine',
    'config_file_paths'
]


def rela2abs(path):
    # when it is not absolute path
    basepath = os.path.dirname(os.environ.get("virtual_path"))
    path = os.path.join(basepath, path)
    return path


def config_file_paths():
    path = jupyter_config_path()
    if jupyter_config_dir() not in path:
        path.insert(0, jupyter_config_dir())
    path.insert(0, py3compat.getcwd())
    return path


def load_config():
    filename, ext = os.path.splitext("jupyter_notebook_config.py")
    new_config = Config()
    for config in Application._load_config_files(filename, path=config_file_paths()):
        new_config.merge(config)
    return new_config


def get_engine():
    pg_db_url = load_config().PostgresContentsManager.db_url
    return create_engine(pg_db_url, echo=False)
