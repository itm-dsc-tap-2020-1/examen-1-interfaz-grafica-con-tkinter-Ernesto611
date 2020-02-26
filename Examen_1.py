import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

def calif():
    calificacion=0
    if re1.get()=="Con la sociedad":
        calificacion+=20
    if re2.get()=="El hombre":
        calificacion+=20
    if re3.get==1:
        calificacion+=20
    if re4.get==2:
        calificacion+=20  
    if opcion_1a.get()==1 or opcion_3a.get()==1:
        calificacion+=20  
    if (opcion_2a.get()==1 or opcion_4a.get()==1 or opcion_5a.get()==1) and (opcion_1a.get()==1 or opcion_3a.get()==1):
        calificacion-=20
    ventana2=tk.Tk()
    ventana2.title("Calificacion")
    pree1=ttk.Label(ventana2, text="Tu calificación es: "+str(calificacion)+" %' de 100 %'")
    pree1.grid(column=0, row=0)


ventana=tk.Tk()
ventana.title("Examen")

pre1=ttk.Label(ventana, text="1.- ¿Con que se relacionan las ciencias sociales? ")
pre1.grid(column=0, row=0)
re1=tk.StringVar()
re1Capturado=ttk.Entry(ventana, width=12, textvariable=re1)
re1Capturado.grid(column=1, row=0)

pre2=ttk.Label(ventana, text="2.- ¿Cual es el objeto de estudio de las ciencias sociales? ")
pre2.grid(column=0, row=1)
re2=tk.StringVar()
re2Capturado=ttk.Entry(ventana, width=12, textvariable=re2)
re2Capturado.grid(column=1, row=1)

pre3=ttk.Label(ventana, text="3.- Es un metodo que utilizan las ciencias sociales: ")
pre3.grid(column=0, row=2)   
re3=tk.IntVar()
radio1a=tk.Radiobutton(ventana, text="Encuestas", variable=re3, value=1)
radio1a.grid(column=0, row=3, sticky=tk.W)
radio2a=tk.Radiobutton(ventana, text="Asesinato", variable=re3, value=2)
radio2a.grid(column=1, row=3, sticky=tk.W)
radio3a=tk.Radiobutton(ventana, text="Interrogatorios", variable=re3, value=3)
radio3a.grid(column=2, row=3, sticky=tk.W)

pre4=ttk.Label(ventana, text="4.- ¿Que movimiento social defendia la apliacación de la razon? ")
pre4.grid(column=0, row=4)   
re4=tk.IntVar()
radio1b=tk.Radiobutton(ventana, text="Naranja", variable=re4, value=1)
radio1b.grid(column=0, row=5, sticky=tk.W)
radio2b=tk.Radiobutton(ventana, text="Ilustración", variable=re4, value=2)
radio2b.grid(column=1, row=5, sticky=tk.W)
radio3b=tk.Radiobutton(ventana, text="Ciudadano", variable=re4, value=3)
radio3b.grid(column=2, row=5, sticky=tk.W)

pre5=ttk.Label(ventana, text="5.- Son diferentes clases de ciencias sociales: ")
pre5.grid(column=0, row=6)
opcion_1a=tk.IntVar()
casilla_1a=tk.Checkbutton(ventana, text="Evolución de sociedad", variable=opcion_1a)
casilla_1a.deselect()
casilla_1a.grid(column=0, row=7, sticky=tk.W)
opcion_2a=tk.IntVar()
casilla_2a=tk.Checkbutton(ventana, text="Lectura y escritura", variable=opcion_2a)
casilla_2a.deselect()
casilla_2a.grid(column=1, row=7, sticky=tk.W)
opcion_3a=tk.IntVar()
casilla_3a=tk.Checkbutton(ventana, text="Interacción entre personas", variable=opcion_3a)
casilla_3a.deselect()
casilla_3a.grid(column=2, row=7, sticky=tk.W)
opcion_4a=tk.IntVar()
casilla_4a=tk.Checkbutton(ventana, text="Baile interpretativo", variable=opcion_4a)
casilla_4a.deselect()
casilla_4a.grid(column=3, row=7, sticky=tk.W)
opcion_5a=tk.IntVar()
casilla_5a=tk.Checkbutton(ventana, text="Programación modular", variable=opcion_5a)
casilla_5a.deselect()
casilla_5a.grid(column=4, row=7, sticky=tk.W)

cal=ttk.Button(ventana, text="Calificar", command=calif)
cal.grid(column=0, row=9)

ventana.mainloop()