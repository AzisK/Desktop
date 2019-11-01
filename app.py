import os
import fnmatch


PATH = f"{os.environ['HOME']}/Desktop"

# DOCUMENTS_FOLDER = f"{PATH}/Documents"
# SCREENSHOTS_FOLDER = f"{PATH}/Screenshots"
# PICTURES_FOLDER = f"{PATH}/Pictures"

DOCUMENT = {
    "name": f"{PATH}/Documents",
    "description": "document",
}

SCREENSHOT = {
    "name": f"{PATH}/Screenshots",
    "description": "screen shot",
}

PICTURE = {
    "name": f"{PATH}/Pictures",
    "description": "picture",
}

def main():
    # Have everything in main first for the tutorial
    for file in os.listdir(PATH):
        if os.path.isfile(f"{PATH}/{file}"):
            print(f"Desktop has {file}")
            # if fnmatch.fnmatch(file, '*.docx') or fnmatch.fnmatch(file, '*.pdf') or fnmatch.fnmatch(file, '*.txt'):
            if fnmatch_any(file, "*.docx", "*.pdf", "*.txt"):
                move_to_documents(file)
            if fnmatch_any(file, "Screen Shot*.png"):
                move_to_screen_shots(file)

def fnmatch_any(file, *args):
    for arg in args:
        if fnmatch.fnmatch(file, arg):
            return True
    return False

def move_to_screen_shots(file: str):
    move_to_folder(SCREENSHOT, file)

def move_to_documents(file: str):
    move_to_folder(DOCUMENT, file)

def move_to_folder(folder, file: str):
    print(f"{file} is a {folder['description']}!")
    is_directory(folder['name'])
    move(file, folder['name'])

def move(file: str, folder: str):
    current_path = f"{PATH}/{file}"
    new_path = f"{folder}/{file}"

    os.rename(current_path, new_path)
    print(f"File '{file}' has been moved from '{current_path}' to '{new_path}'")

def is_directory(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__== "__main__":
    main()
