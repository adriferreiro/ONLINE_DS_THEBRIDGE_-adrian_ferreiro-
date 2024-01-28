#imports
#variables y constantes globales
#definicion de funciones 
#definicion de clases
#codigo principal
'''Si haces un from funcines import * traes todas las variables, si pones from funciones import variable (traes esa variable)'''
'''from sys import path
path.append(".\\")''' #para traer funciones de otras carpetas. seria un import libreria.funciones as fn siendo librerias la carperta donde se guarda y funciones el archivo
import numpy as np

def crea_tablero(dimensiones):
    return np.full(dimensiones, " ")

tam_tablero = input("¿Qué tamaño quieres (ancho,alto)? ")
lista_dimensiones = [int(elemento) for elemento in tam_tablero.split(",")]
print(crea_tablero(lista_dimensiones))
'''if __name__ ==" __main__":
    print(crea tablero) '''#añades este codigo en caso de que queiras comprobar una funcion en el archivo funciones pero no quieres que se ejecute en el programa principal