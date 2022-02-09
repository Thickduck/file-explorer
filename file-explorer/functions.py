from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
import shutil
import easygui
import os


def open_window():
    content = easygui.fileopenbox()
    return content


def open_file():
    str = open_window()
    os.startfile(str)


def copy_file():
    source = open_window()
    dest = filedialog.askdirectory()

    shutil.copy(source, dest)
    mb.showinfo('confirmation', "Item(s) copied")


def del_file():
    src = open_window()
    if os.path.exists(src):
        os.remove(src)
        mb.showinfo('Task finished successfully', "File Deleted")
    else:
        mb.showerror('Error', "The file is not found!")


def del_folder():
    src = filedialog.askdirectory()
    if os.path.exists(src):
        os.rmdir(src)
        mb.showinfo('Task finished successfully', "Folder Deleted")
    else:
        mb.showerror('Error', "The folder is not found!")


def rename_file():
    src = open_window()
    path = os.path.dirname(src)
    ext = os.path.splitext(src)[1]
    name = input('Enter a new name for the file:\n')

    new_path = os.path.join(path, name+ext)

    conf = input(str(name)+" is the name you choose? Y/N\n")
    conf = conf.lower()
    if conf == 'y':
        os.rename(src, new_path)
    else:
        pass

    mb.showinfo('Task finished successfully', "File Renamed")
    exit()


def move_file():
    src = open_window()
    dest = filedialog.askdirectory()

    shutil.move(src, dest)
    mb.showinfo('confirmation', "Item(s) moved")


def make_folder():
    path = filedialog.askdirectory()
    name = input('Enter a name for the folder:\n')
    if os.path.exists(path):
        os.mkdir(os.path.join(path, name))
        mb.showinfo('confirmation', "Folder created")
    else:
        mb.showerror('Error', "The folder is not found!")
    exit()


