# PDF Sorter

A simple Python script to sort all `.pdf` files from a given folder into a dedicated `pdf` subfolder.

---

## 📝 Features

* Automatically creates a `pdf/` folder inside the target directory
* Moves all `.pdf` files into that folder
* Works with the current folder or any custom path
* Ignores case (e.g. `.PDF`, `.Pdf`)

---

## 🚀 Usage

1. Run the script:

```bash
python pdf-sorter.py
```

2. Enter the full path of the folder you want to sort
   *(or just press Enter to use the current folder)*

---

## 🛠 Requirements

* Python 3.x
* No third-party dependencies

---

## 🔐 Permissions

Make sure you have write permission in the target directory — otherwise the script won't be able to create the `pdf/` folder or move files.

---

## 💡 Example

```
Enter the full path of the folder you want to sort (Leave empty for current folder):
/home/user/Downloads
```

All PDF files in `/home/user/Downloads` will be moved to `/home/user/Downloads/pdf`

---

### License
This project is under [MIT](LICENSE) License.
