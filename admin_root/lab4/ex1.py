import os
import sys

def find_largest_file(dirName):
    largest_file = ''
    max_size = 0

    for item_name in os.listdir(dirName):
        full_path = os.path.join(dirName, item_name)

        if os.path.isdir(full_path):
            sub_largest_file, sub_max_size = find_largest_file(full_path)
            if sub_max_size > max_size:
                max_size = sub_max_size
                largest_file = sub_largest_file

        elif os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            if size > max_size:
                max_size = size
                largest_file = full_path

    return largest_file, max_size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex1.py <directory_path>")
        sys.exit(1)

    dir_path = sys.argv[1]
    largest_file, size = find_largest_file(dir_path)
    print(f"Largest file: {largest_file} with size: {size} bytes")