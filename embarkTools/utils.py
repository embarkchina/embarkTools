import os


def rela2abs(path):
    # when it is not absolute path
    basepath = os.path.dirname(os.environ.get("virtual_path"))
    path = os.path.join(basepath, path)
    return path
