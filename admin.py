import openpyxl
from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ss = openpyxl.load_workbook('prueba.xlsx')
sheet = ss.get_sheet_by_name('Inventario')
ingredientes = sheet['F2':'F24'].value

root = Tk()
root.title('Moras Dulces')

Label(root, text="Ingredientes Moras", fg="darkblue", font=("Times New Roman",28,"bold italic")).pack()

Label(root, text=ingredientes, fg="black", font=("Times New Roman", 20,"bold italic")).pack()
mensaje = StringVar()
mensaje.set("Bienvenida Dolores")
monitor = Label(root,textvar = mensaje, justify='left')
monitor.pack(side="left")

root.mainloop()