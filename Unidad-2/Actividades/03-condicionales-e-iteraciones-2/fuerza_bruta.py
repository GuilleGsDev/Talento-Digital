from string import ascii_lowercase
from getpass import getpass

password = getpass("Ingrese la contraseña: ").lower()
intentos = 0

for caracter in password:
    for letra in ascii_lowercase:
        intentos += 1
        if caracter == letra:
            break

print(f"La contraseña fue forzada en {intentos} intentos")