#reto 1
def triangle(base:float, height:float, lado_1:float, lado_2:float, lado_3:float):
    if lado_1 == lado_2 == lado_3:
        print('Es un trinagulo equilatero')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Es un triangulo isósceles')
    else:
        print('Es un triangulo escaleno')
    return (base * height) / 2


#reto 2
def juego():
    import random
    contador = 0

    while contador < 3:
        victorias_pc = 0
        victorias_usuario = 0
        lista_opciones = ['piedra','papel','tijera']
        jugador_usuario = input('Selecciona entre:\n piedra\n papel\n tijera\n\t')
        jugador_pc = random.choice(lista_opciones)
        
        if jugador_pc == jugador_usuario:
            print(f'La pc y tu han seleccionado la misma opcion {jugador_pc}')
        elif jugador_pc == 'piedra' and jugador_usuario == 'tijera':
            victorias_pc += 1
            contador += 1
            print(f'Ha ganado la PC con {jugador_pc} y tu has perdido con {jugador_usuario}')
        elif jugador_pc == 'piedra' and jugador_usuario == 'papel':
            victorias_usuario += 1
            contador += 1
            print(f'Has ganado con {jugador_usuario} y la PC ha perdido con {jugador_pc}')
        elif jugador_pc == 'papel' and jugador_usuario == 'tijera':
            victorias_usuario += 1
            contador += 1
            print(f'Has ganado con {jugador_usuario} y la PC ha perdido con {jugador_pc}')
        elif jugador_pc == 'papel' and jugador_usuario == 'piedra':
            victorias_pc += 1
            contador += 1
            print(f'Ha ganado la PC con {jugador_pc} y tu has perdido con {jugador_usuario}')
        elif jugador_pc == 'tijera' and jugador_usuario == 'papel':
            victorias_usuario += 1
            contador += 1
            print(f'Has ganado con {jugador_usuario} y la PC ha perdido con {jugador_pc}')
        elif jugador_pc == 'tijera' and jugador_usuario == 'piedra':
            victorias_pc += 1
            contador += 1
            print(f'Ha ganado la PC con {jugador_pc} y tu has perdido con {jugador_usuario}')
        
    if victorias_pc > victorias_usuario:
        print('\n')
        print('Ha ganado la PC')
    else:
        print('\n')
        print('¡Has ganado!')


#reto 3
def conversor():
    opcion = int(input('Quieres: \n1. Pasar millas a km \n2. Pasar kms a millas\n'))
    MILLA = 1.609344
    if opcion == 1:
        cant = float(input('Ingrese las millas a convertir a kms: '))
        return round(cant * MILLA, 2)
    else:
        cant = float(input('Ingrese las kms a convertir a millas: '))
        return round(cant/MILLA, 2)


#reto 4
def calculador_volumenes():
    import math
    figura = int(input('De que figura quieres calcular el volumén:\n1. Cilindro\n2. Cubo\n3. Rectangulo\n4. Esfera\n'))
    
    if figura == 1:
        PI = math.pi
        radio = float(input('Ingrese el radio del cilindro:\n'))
        altura = float(input('ingrese la altura del cilindro:\n'))
        print(f'{PI * radio**2 * altura} cm^3 es el volumén del cilindro')
    
    elif figura == 2:
        lado = float(input('Ingrese un lado del cubo:\n'))
        print(f'{lado**3} cm^3 es el volumén del cubo')
    
    elif figura == 3:
        base = float(input('Ingrese la base del rectangulo:\n')) 
        ancho = float(input('Ingrese el ancho del rectangulo:\n')) 
        altura = float(input('Ingrese la altura del rectangulo:\n')) 
        print(f'{base * ancho * altura} cm^3 es el volumén del rectangulo')
    
    elif figura == 4:
        PI = math.pi
        radio = float(input('Ingrese el radio de la esfera:\n'))
        print(f'{(4/3) * PI * radio**3} cm^3 es el volumén de la esfera')
    
    else:
        print('La figura no esta dentro de las opciones')


#reto5
def rangos():
    limite_superior = int(input('ingrese el limite superior:\n'))
    limite_inferior = int(input('ingrese el limite inferior:\n'))
    n_comparador = int(input('ingrese un número entero:\n'))
    cont = 0

    while cont< 1:
        if limite_inferior < n_comparador < limite_superior:
            print(n_comparador)
            cont += 1
        else:
            print('El número entero se encuentra fuera los limites')
            n_comparador = int(input('ingrese un número entero:\n'))


def run():
    print(triangle(2,3,2,3,4))
    juego()
    print(conversor())
    calculador_volumenes()
    rangos()


if __name__=='__main__':
    run()