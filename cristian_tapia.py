
GENERO=("Ficción","No Ficción","Ciencia")
lista_libros=[]
lista_ventas=[]
def Registra_libro():
    titulo=input("Ingrese título del libro ").lower()
    Autor=input("Ingrese autor del libro ").lower()
    Genero=input("Ingrese género del libro ").lower()
    precioLibro=input("Ingrese precio del libro ").lower()

    lista_libros.append({
        "Titulo":titulo,
        "Autor": Autor,
        "Genero":Genero,
        "Precio del Libro":precioLibro
    })
    return

def Listar_libros():
    for i in lista_libros:
        print(i)

def Registrar_venta():
    while True:
        op=int(input("1. Ingresar venta o presiona ENTER para imprimir ventas "))
        if op==1:
            titulo=input("Ingresa titulo a vender ")
            for titulo in lista_libros:
                print("Se ha encontrado el libro")
            cantidad=int(input("Ingrese cantidad a vender "))
            precio=int(input("Ingrese precio a vender "))
            precioTotal=cantidad*precio
            lista_ventas.append({
                "Titulo":titulo,
                "Catidad":cantidad,
                "Precio unitario":precio,
                "Precio Total":precioTotal
            })
        elif op=="":
            print("***********************")
            print(lista_ventas)
            print("***********************")
            break
   
    
    

def Imprimir_reporte():
    op=input("Ingrese género o pulsa ENTER para imprimir todas las ventas ")
    if op=="":
        for i in lista_ventas:
            print(i)

def Generar_txt():
    print("")
    
        









while True:
    print("1. Registrar libro")
    print("2. Listar todos los libros")
    print("3. Registrar venta")
    print("4. Imprimir reporte de ventas")
    print("5. Generar txt")
    print("6. Salir ")

    op=int(input("Ingrese opción "))

    if op==1:
        Registra_libro()
    elif op==2:
        Listar_libros()
    elif op==3:
        Registrar_venta()
    elif op==4:
        Imprimir_reporte()
    elif op==5:
        Generar_txt()
    elif op==6:
        break
    else:
        print("Ingrese opció válida")