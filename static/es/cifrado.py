# Cifrado Cesar

TAM_MAX_CLAVE = 26

def obtenerModo():
    while True:
        print('Deseas encriptar o desencriptar un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d'.split():
            return modo
        else:
            print('Ingrese "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    print('Ingrese su mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingrese el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave = -clave
    traduccion = ''

    for letra in mensaje:
        if letra.isalpha():
            num = ord(letra)
            num += clave

            if letra.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letra.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduccion += chr(num)
        else:
            traduccion += letra
    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
clave = obtenerClave()

print('Tu texto traducido es:')
print(obtenerMensajeTraducido(modo, mensaje, clave))
