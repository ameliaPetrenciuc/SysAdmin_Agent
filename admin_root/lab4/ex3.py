import os
import shutil
import sys

def remove_empty_dir(dir_path):
    is_empty=True

    for item_name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item_name)

        if os.path.isdir(full_path):
            if not remove_empty_dir(full_path):
                is_empty=False
        elif os.path.isfile(full_path):
            is_empty=False

    if is_empty:
        print(f"\nDirectorul este gol: {dir_path}")
        while True:
            user_input = input(f"Doriti sa stergeti directorul gol '{dir_path}'? (y/n): ").strip().lower()
            if user_input == 'y':
                os.rmdir(dir_path)
                print(f"Am sters directorul gol: {dir_path}")
                return True
            elif user_input == 'n':
                print(f"Nu am sters directorul: {dir_path}")
                return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ex3.py <directory_path>")
        sys.exit(1)

    source_dir=sys.argv[1]
    directory_path = sys.argv[2]

    shutil.copytree(source_dir, directory_path)
    print(f"Am copiat cu succes {source_dir} in {directory_path}")

    remove_empty_dir(directory_path)
    print(f"Curățarea directorului '{directory_path}' s-a terminat.")



