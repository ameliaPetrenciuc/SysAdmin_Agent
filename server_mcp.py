import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os
from typing import List
from mcp.server.fastmcp import FastMCP
import os
from typing import List, Dict

ADMIN_ROOT="admin_root"

if not os.path.isdir(ADMIN_ROOT):
    os.makedirs(ADMIN_ROOT, exist_ok=True)
    print(f"Created directory: {ADMIN_ROOT}")

mcp = FastMCP(name="System File Manager MCP", port=8002)

  

@mcp.tool()
def list_directory(dir_path: str) -> Dict[str, List[str]]:

    full_path=os.path.join(ADMIN_ROOT, dir_path)
    abs_path=os.path.normpath(full_path)

    if not abs_path.startswith(ADMIN_ROOT):
        return {"directories": [], "files": ["Access denied."]}
    if not os.path.isdir(abs_path):
        return {"directories": [], "files": ["Directory does not exist."]}
    
    directories = []
    files = []

    for entry in os.listdir(abs_path):
        entry_path = os.path.join(abs_path, entry)
        if os.path.isdir(entry_path):
            directories.append(entry)
        elif os.path.isfile(entry_path):
            files.append(entry)

    return {"directories": directories, "files": files}


@mcp.tool()
def get_file_content(file_path: str) -> str:
    
    full_path = os.path.join(ADMIN_ROOT, file_path)
    abs_path = os.path.normpath(full_path)

    if not abs_path.startswith(ADMIN_ROOT):
        return "Access denied."
    
    safe_path=abs_path
    if not os.path.exists(safe_path):
        return f"Eroare: Fișierul '{file_path}' nu există."
    
    if not os.path.isfile(safe_path):
        return f"Eroare: '{file_path}' nu este un fișier valid."
    
    with open(safe_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content

@mcp.tool()
def list_files_recursive(dir_path: str) -> Dict[str, List[str]]:
    full_path = os.path.join(ADMIN_ROOT, dir_path)
    abs_path = os.path.normpath(full_path)

    if not abs_path.startswith(ADMIN_ROOT):
        return {"files": ["Access denied."]}
    if not os.path.isdir(abs_path):
        return {"files": ["Directory does not exist."]}

    all_files = []

    for root, dirs, files in os.walk(abs_path):
        for file in files:
            file_full_path=os.path.join(root, file)
            file_relative_path=os.path.relpath(file_full_path, ADMIN_ROOT)
            all_files.append(file_relative_path.replace("\\","/"))

    return {"files": all_files}

@mcp.tool()
def get_file_size(file_path: str) -> str:
    
    full_path = os.path.join(ADMIN_ROOT, file_path)
    abs_path = os.path.normpath(full_path)

    if not abs_path.startswith(ADMIN_ROOT):
        return "Access denied."

    if not os.path.exists(abs_path):
        return f"Error: File '{file_path}' does not exist."

    if not os.path.isfile(abs_path):
        return f"Error: '{file_path}' is not a valid file."

    size_bytes = os.path.getsize(abs_path)

    return f"File size: {size_bytes} bytes"

@mcp.tool()
def find_largest_file(dir_path:str):

    full_path = os.path.join(ADMIN_ROOT, dir_path)
    abs_path = os.path.normpath(full_path)
    
    if not abs_path.startswith(ADMIN_ROOT):
        return "Access denied."

    if not os.path.isdir(abs_path):
        return f"Error: Directory '{dir_path}' does not exist."

    def recurse(folder):
        largest_file = ''
        max_size = 0

        items = os.listdir(folder)

        for item_name in items:
            full_path = os.path.join(folder, item_name)

            if os.path.isdir(full_path):
                sub_largest_file, sub_max_size = recurse(full_path)
                if sub_max_size > max_size:
                    max_size = sub_max_size
                    largest_file = sub_largest_file

            elif os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                if size > max_size:
                    max_size = size
                    largest_file = full_path

        return largest_file, max_size
    
    largest_file, size = recurse(abs_path)

    if largest_file=="":
        return "No files found in the directory."
    
    relative_path=os.path.relpath(largest_file, ADMIN_ROOT)
    return f"Largest file: {relative_path} with size: {size} bytes"



if __name__ == "__main__":
    mcp.run(transport="streamable-http", mount_path="/mcp")