from tkinter import *
from functions import *

root = Tk()

move_file = Button(root, text="Move File", command=move_file)
move_file.pack()

open_file = Button(root, text="Open File", command=open_file)
open_file.pack()

copy_file = Button(root, text="Copy File", command=copy_file)
copy_file.pack()

del_file = Button(root, text="Delete File", command=del_file)
del_file.pack()

del_folder = Button(root, text="Delete Folder", command=del_folder)
del_folder.pack()

rename_file = Button(root, text="Rename File", command=rename_file)
rename_file.pack()

make_folder = Button(root, text="Make Folder", command=make_folder)
make_folder.pack()


root.title('File Explorer')
root.geometry('600x500')


root.mainloop()
