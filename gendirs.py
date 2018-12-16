import os
import argparse
import concurrent.futures as cf

#
# change type of executor
#
DIRECTORY_EXECUTOR = cf.ThreadPoolExecutor
# DIRECTORY_EXECUTOR = cf.ProcessPoolExecutor

MAX_WORKERS=1
# MAX_WORKERS=10
# MAX_WORKERS=100
# MAX_WORKERS=1000

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--dir', required=True,
                    help='the directory to start creating a tree in')
parser.add_argument('--fpd', type=int, default=20,
                    help='files per directory')
parser.add_argument('--dpd', type=int, default=10,
                    help='directories per directory')
parser.add_argument('--fs', type=int, default=1024,
                    help='file size (mb)')
parser.add_argument('--depth', type=int, default=2,
                    help='file size (mb)')
# parser.add_argument('--strategy', type=int, default=2,
#                     help='file size (mb)')


args = parser.parse_args()
print(args.dir)
print(args.fpd)
print(args.dpd)
print(args.fs)
print(args.depth)

def create_file(absolute_path, file_size):
    with open(absolute_path, 'w+') as f:
        f.write("x"*file_size)

#
# Basic Solution
#
def create_directory(aboslute_directory_path, files_per_directory, directory_per_directory, file_size, depth):
    if depth == 0:
        return
    try:
        os.mkdir(aboslute_directory_path)
    except FileExistsError:
        pass
        # print("Directory Exists")
    for file_number in range(files_per_directory):
        create_file(os.path.join(aboslute_directory_path, "{}.txt".format(file_number)), file_size)
    for directory_number in range(directory_per_directory):
        create_directory(os.path.join(aboslute_directory_path, "dir-{}".format(directory_number)), files_per_directory, directory_per_directory, file_size, depth - 1)

#
# Executor (either thread or process)
#
def create_directory_executor(aboslute_directory_path, files_per_directory, directory_per_directory, file_size, depth):
    if depth == 0:
        return
    try:
        os.mkdir(aboslute_directory_path)
    except FileExistsError:
        pass
        # print("Directory Exists")
    for file_number in range(files_per_directory):
        create_file(os.path.join(aboslute_directory_path, "{}.txt".format(file_number)), file_size)
    with DIRECTORY_EXECUTOR(max_workers=MAX_WORKERS) as executor:
        for directory_number in range(directory_per_directory):
            executor.submit(create_directory, os.path.join(aboslute_directory_path, "dir-{}".format(directory_number)), files_per_directory, directory_per_directory, file_size, depth - 1)

# create_directory(args.dir, args.fpd, args.dpd, args.fs, args.depth)
create_directory_executor(args.dir, args.fpd, args.dpd, args.fs, args.depth)