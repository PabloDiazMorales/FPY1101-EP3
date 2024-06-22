import os
biblioteca = []

def registrar ():
    try: 
        titulo = input ("Ingresa el titulo del libro: ")
        Autor = input ("Ingresa el autor del libro: ")
        publicacion = input ("Ingresa el año de publicacion: ")
        SKU = input ("ingrese rut: ")
        imprimir_prestamo = float (input ("imprimir reporte de prestamos: "))
        if titulo == "" or Autor == "" or publicacion == "" or SKU <= 0:
           print ("reporte de prestamo")

        Solicitud = {
            'titulo' : titulo,
            'autor' : Autor,
            'publicacion' : publicacion,
            'SKU' : SKU,
        }

        biblioteca.append (Solicitud)
        print ("Solicitud exitosa")
    except ValueError:
        print ("todos los datos deben ser ingresados")  

def Solicitud() :
    if biblioteca == "":
        print ("para prestar un libro: ") 
    else: 
        for Solicitud in biblioteca: 
            print (f"titulo: (titulo['titulo'])") #pendiente///

def imprimir_prestamo ()=
    try:
        op = int (input {"prestar libro"}) 
        if op == 1:
            with open ("prestar libro", "w") as archivo 
                for solicitud in biblioteca :
                    archivo.write("solicitud: "titulo ()) #pendiente///  
            print ("Solicitud ingresada con exito: ", os getcwd())
        elif op == 2:
            SKU = input ("Ingrese el SKU del libro: ").lower ()
            with open (f"planilla_(libro) .txt",) as archivo
                for Solicitud in biblioteca:
                    if Solicitud {'titulo'} .lower () == titulo:
            print ("Solicitud de prestamo exitoso" , os.getcwd())
        else:
            print ("Libro no disponible, intente nuevamente")
    except ValueError
        print ("Error en la busqueda libro no existe, intente nuevamente") 
def menu ()=
    while True=
        try=
            print ("\n****biblioteca***\n") 
            print ("1. Registro libro\n2. Presta libro\3. Listar todos los libros\4. Imprimir reporte de prestamo\5. Salir del programa")
            op = int (input ("Ingrese Una Opcion: \t")) 
            if op == 1 :
                registro ()
            elif op == 2:
                prestar libro ()
            elif op == 3:
                listar ()
            elif op == 4:
                imprimir_prestamo
            elif op == 5:
                print ("Salir del programa...")
                break
            else:
                print ("Opcion no valida, intente nuevamente")
             



