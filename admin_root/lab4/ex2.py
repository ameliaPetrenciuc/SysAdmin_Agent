import os
import subprocess
import sys

def listdir_method(directory_path):
    return sorted(os.listdir(directory_path))

def subprocess_method(directory_path):
    result = subprocess.run(['/bin/ls', '-1', directory_path], capture_output=True, text=True)
    return sorted(result.stdout.splitlines())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ex2.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    result1 = listdir_method(directory_path)
    result2 = subprocess_method(directory_path)
    print("Directory contents using os.listdir():", result1)
    print("Directory contents using /bin/ls:", result2)
