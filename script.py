import os

path = None
selected_path = input(
    "Enter the full path of the folder you want to sort (Leave empty for current folder):\n"
)


def check_path_existence(path):
    result = os.path.exists(path)
    return result


if selected_path == "":
    path = os.getcwd()
    print(f"sorting {path} ...")
else:
    while not check_path_existence(path=path):
        selected_path = input(
            "The directory path you have provide does not exists, please provide a full path"
        )
    else:
        path = selected_path
        print(f"sorting {path} ...")

print("Creating Pictures & Videos folder...")
try:
    pictures_folder = os.mkdir(f"{path}/Pictures")
    videos_folder = os.mkdir(f"{path}/Videos")
except PermissionError:
    print("You don't have permission to create the directory.")
