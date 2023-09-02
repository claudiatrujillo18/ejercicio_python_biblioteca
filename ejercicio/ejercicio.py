#función 1

i=0
libros=[]

print("Ingrese el número de libros a listar")
numero=int(input())


while i<numero:
    print("Ingrese el nombre del libro")
    libros.append(input())
    i+=1


print(f"el nombre de libro es:{libros}")
