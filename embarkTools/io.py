import os
from io import StringIO
from base64 import b64decode, b64encode

from pgcontents.api_utils import split_api_filepath, to_b64
from pgcontents.query import get_file, save_file
from pgcontents import crypto

import pandas as pd
from pandas.core.frame import DataFrame

from .utils import rela2abs, get_engine


def read(path):
    """读取路径下的文件"""
    user_id = os.environ.get("JUPYTERHUB_USER") or ""
    if not path.startswith("/"):
        path = rela2abs(path)

    with get_engine().begin() as db:
        src_file = get_file(
            db,
            user_id,
            path,
            True,
            crypto.NoEncryption().decrypt
        )
    return b64decode(src_file['content'].decode("utf-8"))


def save(data, path, format='text'):
    """将文件存储在指定目录下"""
    if format not in ['text', 'base64', 'bytes']:
        print("Unexcept format type: %s." % (format))
        return
    if not path.startswith("/"):
        path = rela2abs(path)
    directory, name = split_api_filepath(path)
    user_id = os.environ.get("JUPYTERHUB_USER") or ""

    content = b64encode(data) if format == 'bytes' else to_b64(data, format)

    with get_engine().begin() as db:
        save_file(
            db,
            user_id,
            path,
            content,
            crypto.NoEncryption().encrypt,
            0
        )


def read_csv(path, **kwargs):
    """读取csv, 返回 `pandas.core.frame.DataFrame`"""
    if not path.startswith("/"):
        path = rela2abs(path)
    data = read(path)
    return pd.read_csv(
        StringIO(data.decode("utf-8")),
        **kwargs
    )


def save_csv(df, path, **kwargs):
    """存储csv文件, 可以是`DataFrame` 或者 `str` 类型"""
    if not path.startswith("/"):
        path = rela2abs(path)
    data = None
    if isinstance(df, DataFrame):
        data = df.to_csv(**kwargs)
    elif isinstance(df, str):
        data = df
    else:
        return "data type must be `DataFrame` or `str`"
    save(data, path)
