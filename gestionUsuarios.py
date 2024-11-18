import threading

#Función que recibe la información  de cada usuario y la imprime
def procesarUsuario(idUsuario,nombre,edad):
    print(f"Id Usuario: {idUsuario}, Nombre: {nombre}, Edad: {edad}")

#Lista de usuarios
usuarios = [(1,"Pedro",20),(2,"Carlos",29),(3,"Silvia",40),(4,"Antonio",58),(5,"Beatriz",37)]

#Lista para almacenar los hilos
hilos = []

#Iteracion a la lista de usuarios para crear y ejecutar los hilos para cada uno
for usuario in usuarios:
    hilo = threading.Thread(target=procesarUsuario, args=(usuario[0],), kwargs={"nombre":usuario[1],"edad":usuario[2]})
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

print("Todos los usuarios han sido procesados")