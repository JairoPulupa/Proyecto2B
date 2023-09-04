import numpy as np
import sympy as sp
import tkinter as tk
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
while True:
    print("==================")
    print("Calculadora basica")
    print("==================")
#Impreme en pantalla los comentarios que estan entre comillas 
    print("¿Bienvenido en que te puedo ayudar?")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Derivar")
    print("6.- Integrar")
    print("7.- Transformada de Laplace")
#Creamos una variable opcion con entrada de datos desde el teclado donde segun el parametro que escoga y escriba me llevara a una sentencia condicional if
    opcion=int(input("Porfavor ingresa una opcion: "))
    if opcion==1:
        print("\nHas elegido suma\n")
        acum=0
        x=int(input("Cuantos numeros desea ingresar?: "))
        ciclo=0
        while ciclo<x:
            y=float(input("Ingrese un numero: "))
            acum += y
            ciclo += 1
        print("El resultado de la suma es:",acum)
    elif opcion==2:
        print("\nHas elegido resta\n")
        x = int(input("¿Cuántos números desea ingresar?: "))
        ciclo = 0
        if x > 0:
            acum = float(input("Ingrese el primer número: "))
            ciclo += 1
            while ciclo < x:
                y = int(input("Ingrese un número: "))
                acum -= y
                ciclo += 1
        else:
            acum = 0
        print("El resultado de la resta es:",acum)          
    elif opcion==3:
        print("\nHas elegido multiplicacion\n")
        acum=1
        x=int(input("Cuantos numeros desea ingresar?: "))
        ciclo=0
        while ciclo<x:
            y=float(input("Ingrese un numero: "))
            acum *= y
            ciclo += 1
        print("El resultado de la multiplica es:",acum)
    elif opcion==4:
        print("\nHas elegido division\n")
        acum=None
        x=int(input("Cuantos numeros desea ingresar?: "))
        ciclo=0
        while ciclo<x:
            y=int(input("Ingrese un numero: "))
            if acum is None:
                acum = y
            else:
                acum /= y
                ciclo += 1
        print("El resultado de la division es:",acum)
    elif opcion==5:
        #Al haber hecho una entrada del # 5 desde el teclado este saldra una interfaz donde se colocara la funcion a derivar e integrar
        print("Porfavor escribe la funcion a derivar en la siguiente interfaz :D")
        def derivada():
            try:
                x = symbols('x') #Declarar variable independiente
                fun_escrita = funcion.get()
                f = parse_expr(fun_escrita) #parse_expr es utilizado para convertir las funciones ingresadas por el usuario en expresiones de derivadas e integrales
                derivada = diff(f,x)
                etiqueta.configure(text=derivada)
            except:
                etiqueta.configure(text="Introduce la función correctamente")
        ventana= tk.Tk()
        ventana.geometry('600x360')
        ventana.title("Calculadora Basica")
        anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="green")
        anuncio.pack()
        funcion = Entry(ventana, font=("Arial", 15))
        funcion.pack()
        etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
        etiqueta.pack()
        boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=derivada)
        boton1.pack()
        def _quit(): #Función salir
            ventana.quit()     # detiene mainloop
            ventana.destroy()  # elimina la ventana de la memoria
        button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
        button3.pack()
        ventana.mainloop()
    elif opcion==6:
        print("Porfavor escribe la funcion a integrar en la siguiente interfaz :D")
        def integral():
            try:
                x = symbols('x') #Declarar variable independiente
                fun_escrita2 = funcion.get()
                g = parse_expr(fun_escrita2)
                integral = integrate(g,x)
                etiqueta.configure(text=integral)
            except:
                etiqueta.configure(text="Introduce la función correctamente")
        ventana= tk.Tk()
        ventana.geometry('600x360')
        ventana.title("Calculadora Basica")
        anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="purple")
        anuncio.pack()
        funcion = Entry(ventana, font=("Arial", 15))
        funcion.pack()
        etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
        etiqueta.pack()
        boton1 = Button(ventana, text="Integrar Función", font=("Arial", 15), command=integral)
        boton1.pack()
        def _quit(): #Función salir
            ventana.quit()     # detiene mainloop
            ventana.destroy()  # elimina la ventana de la memoria
        button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
        button3.pack()
        ventana.mainloop()
    elif opcion==7:
        print("Porfavor escribe la funcion de t en la siguiente interfaz :D")

        def calcular_transformada():
            funcion = entrada_funcion.get()
            try:
                s, t = sp.symbols('s t')
                def f(t):
                    return sp.sympify(funcion)
                F = sp.laplace_transform(f(t), t, s)
                resultado.set(F[0])
            except Exception as e:
                resultado.set("Error: " + str(e))
        ventana = tk.Tk()
        ventana.title("Calculadora Basica")
        ventana.geometry("600x360")
        resultado = tk.StringVar()
        label_funcion = Label(ventana, text="Ingrese la función f(t):",font=("Arial", 15), fg="brown")
        label_funcion.pack()
        entrada_funcion = Entry(ventana, font=("Arial", 15))
        entrada_funcion.pack()
        etiqueta = Label(ventana, text="Resultado:", font=("Arial", 15), fg="red")
        etiqueta.pack()
        button1= Button(ventana, text="Calcular Transformada de Laplace",font=("Arial", 14), command=calcular_transformada)
        button1.pack()
        etiqueta_resultado = Label(ventana, textvariable=resultado)
        etiqueta_resultado.pack()
        def _quit(): #Función salir
            ventana.quit()     # detiene mainloop
            ventana.destroy()  # elimina la ventana de la memoria
        button3 = Button(master=ventana, text="Salir", font=("Arial", 14), command=_quit)
        button3.pack()
        ventana.mainloop()
    opcion = input("¿Desea realizar otra operación? (si/no): ")
    if opcion.lower() != "si":
        print("Ok,espero haberte ayudado <3")
        break
    


