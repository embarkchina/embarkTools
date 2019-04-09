import os
from base64 import b64decode, b64encode

from sqlalchemy import create_engine
from pgcontents.api_utils import split_api_filepath, to_b64
from pgcontents.query import get_file, save_file
from pgcontents import crypto


def get_engine():
    return create_engine(os.environ.get("PGCONTENTS_DB_URL"), echo=False)


def read(path):
    """读取路径下的文件"""
    user_id = os.environ.get("JUPYTERHUB_USER") or ""
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
