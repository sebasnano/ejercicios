monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad,
           'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en',
      persona['direccion'], 'y su número de teléfono es', persona['telefono'])

frutas = {'Plátano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else:
    print("Lo siento, la fruta", fruta, "no está disponible.")

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

trolley = {}
keep = True
while keep:
    item = input("Cual es el articulo: ")
    price = float(input(f"Introduce el valor de {item}: "))
    trolley[item] = price
    keep = input("Quieres continuar (Si/No): ") == "Si"
cost = 0
print("Lista de Compras")
for item in trolley.items():
    print(item, ' \t', price)
    cost += price
print(f"Coste total: {cost}")

traslater = {}
word = input(
    "Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in word.split(','):
    key, value = i.split(':')
    traslater[key] = value
sentence = input("Introduce una frase en español: ")
for i in sentence.split():
    if i in traslater:
        print(traslater[i], end=' ')
    else:
        print(i, end=' ')

bill = {}
charge = 0
earring = 0
more = ''
while more != 'T' and more != 't':
    if more == 'A':
        numBill = input("Numero de la factura: ")
        costBill = float(input("Costo de la factura: "))
        bill[numBill] = costBill
        earring += costBill
    if more == 'P':
        numBill = input("Numero de la factura: ")
        costBill = bill.pop(numBill, 0)
        charge += costBill
        earring -= costBill
    print(f"Recaudado: {charge}")
    print(f"Pendiente por cobrar: {earring}")
    more = input(
        f"Que quieres realizar: \n A-Añadir Factura \n P-Pagar una Existente \n T-Salir \n")

clients = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input("NIF del cliente: ")
        name = input("Nombre del cliente: ")
        addr = input("Direccion del cliente: ")
        phone = input("Numero del cliente: ")
        email = input("Email del cliente: ")
        vip = input("El Cliente es V.I.P (S/N): ")
        client = {'name': name, 'addres': addr, 'phone': phone,
                  'email': email, 'preferente': vip == 'S'}
        clients[nif] = client
    if opcion == '2':
        nif = input("NIF del cliente: ")
        if nif in clients:
            del clients[nif]
        else:
            print(f"No existe el NIF {nif}")
    if opcion == '3':
        nif = input("NIF del cliente: ")
        if nif in clients:
            print(f"NIT: {nif}")
            for key, value in clients[nif].items():
                print(f"{key.title()}: {value}")
        else:
            print(f"No existe el NIF del cliente {nif}")
    if opcion == '4':
        print("Lista de Clientes: ")
        for key, value in clients.items():
            print(key, value['name'])
    if opcion == '5':
        print("Lista de Clientes V.I.P.")
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['name'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción: ')

dataClients = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
listsClients = dataClients.split("\n")
directory = {}
listsFields = listsClients[0].split(";")
for i in listsClients[1:]:
    client = {}
    listInfo = i.split(";")
    for j in range(1, len(listsFields)):
        if listsFields[j] == 'descuento':
            listInfo[j] = float(listInfo[j])
        client[listsFields[j]] = listInfo[j]
    directory[listInfo[0]] = client
print(directory)
