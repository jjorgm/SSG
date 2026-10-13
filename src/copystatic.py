import os
import shutil


def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    os.mkdir(dest)

    if os.path.exists(source):
        paths = os.listdir(source)
        for path in paths:
            source_path = os.path.join(source, path)
            if os.path.isfile(source_path):
                shutil.copy(source_path, dest)
                print(f"File: {source_path}, Destination: {dest}")
            else:
                dest_path = os.path.join(dest, path)
                copy_static(source_path, dest_path)
