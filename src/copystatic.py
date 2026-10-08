import os
import shutil


def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    else:
        raise ValueError("destination path does not exist")

    if os.path.exists(source):
        shutil.copy(source, dest)
