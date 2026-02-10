import os
import shutil


def check_path_existence(path):
    return os.path.exists(path) and os.path.isdir(path)


def create_folders(path):
    try:
        os.makedirs(os.path.join(path, "pdf"), exist_ok=True)
        return True
    except PermissionError:
        print("You don't have permission to create the directory.")
        return False


def sort_files(path):
    target_dir = path
    if not create_folders(path=target_dir):
        return
    print(f"sorting {target_dir} ...")
    files_count = 0
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        if filename.lower().endswith(".pdf") and os.path.isfile(file_path):
            print(f"moving {filename} to {os.path.join(target_dir, 'pdf')}...")
            shutil.move(
                os.path.join(target_dir, filename),
                os.path.join(target_dir, "pdf", filename),
            )
            files_count += 1
    if files_count == 0:
        print("No PDF files found in the folder.")
    else:
        print("===========================")
        print("Files sorted successfully!")
        print("Total files moved: ", files_count)


def main():
    user_input = input(
        "Enter the full path of the folder you want to sort (Leave empty for current folder):\n"
    )

    if user_input == "":
        target_dir = os.getcwd()
        sort_files(target_dir)
    else:
        while not check_path_existence(path=user_input):
            user_input = input(
                "The directory path you have provided does not exist, please provide a full path\n"
            )
        target_dir = user_input
        sort_files(target_dir)


# 👇 This is the guard
if __name__ == "__main__":
    main()
