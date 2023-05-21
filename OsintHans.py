#!/usr/bin/env python3
#Author: Hans Saldias
import webbrowser
from time import sleep
from colorama import init, Fore, Style
init()


def buscar_nombre():
    webbrowser.open_new(
    'https://www.nombrerutyfirma.com/'
    )

def buscar_patente():
    webbrowser.open_new(
        'https://patenteschile.cl/'
        )
    
def buscar_datosPersona():
    webbrowser.open_new(
        'https://webmii.com/?language=es'
        )

def busqueda_googleDork():
    nombre=input('ingrese nombre: ')
    nombre=(f'\"{nombre}\"')
    webbrowser.open_new(
        'https://www.google.com/search?q=' + nombre
        )

def menu():
    while True:
        print(Style.BRIGHT,Fore.LIGHTGREEN_EX+"""
        hola este scrip esta echo para busqueda de:
    
        personas para encontrar rut

        direccion y algunos datos mas 
        """.capitalize())
        print("\n"*3)
        print("""
        crate by: Hans Saldias

                [1]        Buscar direccion, rut con el nombre (mejor opcion °)

                [2]        Buscar patente vehivulo (direccion y de quien es )

                [3]        Buscar datos de personas (funciona aveces)

                [4]        Busqueda con Google Dorks (esta busqueda es mia 
                            un modo de aser google dorking (buscar a lo hacker))

                [5]        Presiona 5 para salir del Script.. gracias
        """)
        op=int(input("Ingrese opcion: "))

        if op == 1:
            buscar_nombre()
        elif op == 2:
            buscar_patente()
        elif op == 3:
            buscar_datosPersona()
        elif op == 4:
            busqueda_googleDork()
        elif op == 5:
            print("\nGracias por ocupar mi script crador: Hans Saldias.....·\n")
            break
        else:
            while True:
                print("opcion no valida, intente otra vez")
                sleep(3)
                return menu()
    


menu()

            