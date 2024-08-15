import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("720x360")
root.title("Program Manager")


mb = tkinter.Menu()
mbfile = tkinter.Menu(mb)
mb.add_cascade(menu=mbfile, label="Session")

mbfile.add_command(label="Sign out")
mbfile.add_command(label="Lock")
mbfile.add_separator()
mbfile.add_command(label="Sleep")
mbfile.add_command(label="Shut down")
mbfile.add_command(label="Restart")

root.config(menu=mb)

tree = ttk.Treeview()
tree.pack(fill=tkinter.BOTH, expand=True)

root.mainloop()