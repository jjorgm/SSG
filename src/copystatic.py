import os
import shutil


def copy_static(source, dest):
    if os.path.exists(source):
        shutil.rmtree(source)
