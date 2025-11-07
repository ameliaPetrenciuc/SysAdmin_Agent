import sys
import os

def which_python(arg):
    path_var=os.getenv('PATH')
    paths=path_var.split(os.pathsep)

    for p in paths:
        python_executable=os.path.join(p, arg)
        if os.path.isfile(python_executable) and os.access(python_executable, os.X_OK):
            return python_executable
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex4.py <executable_name>")
        sys.exit(1)

    python_path=which_python(sys.argv[1])
    if python_path:
        print(f"Python executable found at: {python_path}")
    else:
        print("Python executable not found in PATH.")