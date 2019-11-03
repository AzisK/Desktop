import os
import fnmatch
import PySimpleGUI as sg


PATH = f"{os.environ['HOME']}/Desktop"

# DOCUMENTS_FOLDER = f"{PATH}/Documents"
# SCREENSHOTS_FOLDER = f"{PATH}/Screenshots"
# PICTURES_FOLDER = f"{PATH}/Pictures"

DOCUMENT = {
    "name": "Documents",
    "path": f"{PATH}/Documents",
    "description": "document",
    "rules": ["*.docx", "*.pdf", "*.txt"],
}

SCREENSHOT = {
    "name": "Screenshots",
    "path": f"{PATH}/Screenshots",
    "description": "screen shot",
    "rules": ["Screen Shot*.png"],
}

PICTURE = {
    "name": "Pictures",
    "path": f"{PATH}/Pictures",
    "description": "picture",
    "rules": ["*.png", "*.jpg"],
}

def main():
    button, values = gui()
    if button == "Cancel":
        return

    adjust_options(values)
    organize_desktop()

def organize_desktop():
    for file in os.listdir(PATH):
        if os.path.isfile(f"{PATH}/{file}"):
            print(f"Desktop has {file}")
            for file_type in [DOCUMENT, SCREENSHOT, PICTURE]:
                if fnmatch_any(file, *file_type['rules']):
                    move_to_folder(file_type, file)
                    break

def gui():
    layout = [      
        [sg.Text("Organize your desktop by moving files to proper folders", font=('Helvetica', 20), justification='center')], 
        get_folder_gui(DOCUMENT),
        get_folder_gui(SCREENSHOT),
        get_folder_gui(PICTURE),
        [sg.Submit(font=('Helvetica', 20)), sg.Cancel(font=('Helvetica', 20))]
    ]

    window = sg.Window('Desktorganizer').Layout(layout)
    button, values = window.Read()
    return button, values

def adjust_options(values):
    if values['Browse']:
        DOCUMENT['path'] = values['Browse']
    if values['Browse0']:
        SCREENSHOT['path'] = values['Browse0']
    if values['Browse1']:
        PICTURE['path'] = values['Browse1']

def get_folder_gui(folder):
    return [
        sg.Text(f"{folder['name']} Folder",
            size=(20, 1),
            font=('Helvetica', 20),
            auto_size_text=False,
            justification='left'),
        sg.InputText(f"{folder['path']}", font=('Helvetica', 20)),
        sg.FolderBrowse(font=('Helvetica', 20)),
    ]

def fnmatch_any(file, *args):
    for arg in args:
        if fnmatch.fnmatch(file, arg):
            return True
    return False

def move_to_folder(folder, file: str):
    print(f"{file} is a {folder['description']}!")
    is_directory(folder['path'])
    move(file, folder['path'])

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
