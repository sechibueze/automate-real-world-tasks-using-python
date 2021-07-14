import multiprocessing
import subprocess
import os

src = "."  # replace <source-path> with the source directory
dest = "./data"  # replace <destination-path> with the destination directory
# subprocess.call(["rsync", "-arq", src, dest])

# Basic test
WORKING_DIR = os.getcwd()
source = os.path.join(WORKING_DIR, "prod")
destination = os.path.join(WORKING_DIR, "dest")

def get_path_list(src_directory):
    path_list = []
    for directory, folderslist, fileslist in os.walk(src_directory):
        # print("path", path)
        print("-------------row start-------------------")
        # print("diretory is : ", directory)
        # print("folders : ", folderslist)
        # print("files", fileslist)
        # print("------------------------row end ------------------")

        for f in fileslist:
            # Get the sub folder
            subfolder = directory[len(source):]
            file_item = f
            # Add subfolder and file to list
            # so we can get them via src/subfolder/file_iten
            path_list.append((subfolder, file_item))
        for d in folderslist:
            subfolder = directory[len(source):]
            path_list.append((subfolder, d))
    return path_list

def backup(path):
    _from = os.path.join(source, path[0], path[1])
    to = os.path.join(destination, path[0])
    flags = "-arq"
    subprocess.call(["rsync", flags, _from, to])


if __name__ == "__main__":
    backup_source = get_path_list(source)
    with multiprocessing.Pool(len(backup_source), maxtasksperchild=1) as pool:
        pool.map(backup, backup_source)

print("backup list", get_path_list(source))
# subprocess.call(["rsync", "-arq", src, dest])