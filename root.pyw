import tkinter

root = tkinter.Tk()
root.geometry("720x360")
root.title("Program Manager")


mb = tkinter.Menu()
mbfile = tkinter.Menu(mb)
mb.add_cascade(menu=mbfile, label="Session")

mbfile.add_command(label="Logout")
mbfile.add_command(label="Lock")
mbfile.add_separator()
mbfile.add_command(label="Shutdown")
mbfile.add_command(label="Reboot")

root.config(menu=mb)


root.mainloop()