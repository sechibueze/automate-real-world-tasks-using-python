#!/usr/bin/env python
import subprocess
import os
from multiprocessing inport Pool

src = "/data/prod/"
dest = "/data/prod_backup/"
WORKING_DIR = os.getcwd()

src = os.path.abspath(src)
dest = os.path.abspath(dest)

# Basic test

#source = os.path.join(WORKING_DIR, "prod")
#destination = os.path.join(WORKING_DIR, "dest")
print("working dir", WORKING_DIR)
print("src dir", src)
print("dest", dest)

def get_path_list(src_directory):
    src_directory = os.path.abspath(src_directory)
    print("src backup dir : ", src_directory)
    path_list = []
    for directory, folderslist, fileslist in os.walk(src_directory):
        directory = os.path.abspath(directory)
        subfolder = directory[len(src_directory):]
        print("processing root dir ", directory)
        for f in fileslist:
            # Get the sub folder

            file_item = f
            # Add subfolder and file to list
            # so we can get them via src/subfolder/file_iten
            # print("subfolder : root/", subfolder)
            print("file root/subfolder/", (subfolder, file_item))
            path_list.append((subfolder, file_item))
        if folderslist != []:
            for d in folderslist:
                # subfolder = directory[len(src_directory):]
                # print("subfolder : root/", subfolder)
                print("file root/subfolder/", (subfolder, d))
                path_list.append((subfolder, d))
    return path_list

def backup(path):
    print("backing up", path)
    _from = os.path.join(os.path.abspath(src), path[0], path[1])
    to = os.path.join(os.path.abspath(dest), path[0])
    flags = "-arq"
    print("processing...", _from, " => ", to)
    subprocess.call(["rsync", flags, _from, to])


if __name__ == "__main__":
    backup_source = get_path_list(src)
    print("backup src size", len(backup_source))
    # with multiprocessing.Pool(len(backup_source), maxtasksperchild=1) as pool:
    pool = Pool(len(backup_source))
    pool.map(backup, backup_source)

print("backup list", get_path_list(source))
# subprocess.call(["rsync", "-arq", src, dest])
