import csv

def valid_word(word):
    return word.isalpha() and 0<len(word)<20

def valid_number(word):
    return word.isdigit()

def valid_sueldo(sueldo):
    return sueldo.isdigit() and 400000<=int(sueldo) <100000000

def get_cargo():
    while True:
        cargo = input("escriba el cargo que efectua en el restaurante(mesero/cajero/cocinero): ").strip()
        cargo= cargo.lower()
        if valid_word(cargo) and cargo == "mesero":
            return cargo
        elif valid_word(cargo) and cargo == "cocinero":
            return cargo
        elif valid_word(cargo) and cargo == "cajero":
            return cargo
        else:
            print("Escriba una de las opciones dentro del parentesus")

def get_name():
    while True:
        nombre = input("Esciba el nombre: ").strip()

        if valid_word(nombre):
            return nombre
        else:
            print("ingrese un valor correcto")


def get_apellido():
    while True:
        apellido = input("Esciba el apellido: ").strip()

        if valid_word(apellido):
            return apellido
        else:
            print("ingrese un valor correcto")

def get_sueldo_bruto():
    while True:
        sueldo_bruto = input("escriba el sueldo bruto(desde $400.000 y sin puntos o comillas, solo numeros): ").strip()

        if valid_sueldo(sueldo_bruto):
            sueldo_bruto = int(sueldo_bruto)
            return sueldo_bruto
        
        else:
            print("escriba un sueldo valido")



   




def grabar_usuarios(users):

    with open("usuarios.csv", "w", newline="") as archivo_csv:
        fields= ["user_id", "cargo", "nombre", "apellido","sueldo_bruto","sueldo_liquido"]
        escritor = csv.DictWriter(archivo_csv, fieldnames=fields)
        escritor.writeheader()

        for id, user_info in users.items():
            escritor.writerow({
                "user_id": id,
                "cargo": user_info["cargo"],
                "nombre": user_info["nombre"],
                "apellido": user_info["apellido"],
                "sueldo_bruto": user_info["sueldo_bruto"],
                "sueldo_liquido": user_info["sueldo_liquido"],


            })


def cargar_usuarios():
    users = {}

    try:

        with open("usuarios.csv", "r") as archivo_csv:
            lector = csv.DictReader(archivo_csv)

            for fila in lector:
                id = int(fila["user_id"])
            try:
                users[id] = {
                    "cargo": fila["cargo"],
                    "nombre": fila["nombre"],
                    "apellido": fila["apellido"],
                    "sueldo_bruto": fila["sueldo_bruto"],
                    "sueldo_liquido":fila["sueldo_liquido"],
                } 
            except KeyError:
                print("fila no encontrada")
                
    except FileNotFoundError:
        print("lista de usuarios no encontrada en csv")

    return users


def imprimir_planilla(users):
     
    cargo_buscar = input("escriba un cargo a buscar y se imprimira todos los agentes de esa area: ").strip()

    if users:
        for id, user_info in users.items():
            if user_info["cargo"] == cargo_buscar:
                print(f"ID del usuario: {id}, nombre del usuario: {user_info['nombre']}, apellido : {user_info['apellido']}, cargo :{user_info['cargo']}, sueldo_bruto: ${user_info['sueldo_bruto']}, sueldo_liquido: ${user_info['sueldo_liquido']} ")
                print("")
            elif not user_info["cargo"]:
                print("el cargo que busca no existe")
    else:
        print("no hay usuarios que buscar")

    
def enlistar_trabajadores(users):
    if users:
        for id, user_info in users.items():
            print(f"ID del usuario: {id}, nombre del usuario: {user_info['nombre']}, apellido : {user_info['apellido']}, cargo :{user_info['cargo']}, sueldo_bruto: ${user_info['sueldo_bruto']}, sueldo_liquido: ${user_info['sueldo_liquido']} ")
    else:
        print("no hay usuarios para mostrar")

def main():
    users = cargar_usuarios()
    id = max(users.keys(), default=0) + 1

    while True:
        print("")
        print("Menu de registro de trabajadores")
        print("1-Registrar trabajadores")
        print("2-listar todos los trabajadores")
        print("3-imprimir planilla")
        print("4-salir del programa")

        opcion = input("escriba la opcion que desea: ").strip()




        if valid_number(opcion) and int(opcion)== 1:
            nombre = get_name()
            apellido = get_apellido()
            cargo = get_cargo()
            sueldo_bruto = get_sueldo_bruto()
            sueldo_liquido = None

            if sueldo_bruto:
                sueldo_liquido = int(sueldo_bruto * (0.93*0.90))
                print("se hizo el decuento de salud (%7 del sueldo bruto y el descuento de AFP (10 por ciento del sueldo bruto))")
                print(f"quedando como sueldo liquido: ${sueldo_liquido}")

                


            

            users[id]={
                "nombre": nombre,
                "apellido": apellido,
                "cargo": cargo,
                "sueldo_bruto": sueldo_bruto,
                "sueldo_liquido":sueldo_liquido
            }
            print("usuario fue grabado exitosamente")

            id = id + 1

            grabar_usuarios(users)


        elif valid_number(opcion) and int(opcion)== 2:
            enlistar_trabajadores(users)

        elif valid_number(opcion) and int(opcion)== 3:
            imprimir_planilla(users)

        elif valid_number(opcion) and int(opcion)== 4:
            break
    
main()