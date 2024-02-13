"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 """
import hashlib
import random


def PasswordHashConvert(password_string):
    return hashlib.md5(password_string.encode()).hexdigest()

print(PasswordHashConvert(""))
print(PasswordHashConvert("Hola"))
print(PasswordHashConvert("Hello"))

def PasswordHashGenerator(length=8, capitals=False, numerals=False, symbols=False):

    total_characters = list(range(97, 123))

    if capitals:
        total_characters += list(range(65, 90))

    if numerals:
        total_characters += list(range(48, 58))

    if symbols:
        total_characters += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))

    final_length = 8 if length < 8 else 16 if length > 16 else length

    password = ""
    for i in range(final_length):
        password = password + str(random.choice(total_characters))

    hash_password = PasswordHashConvert(password)
    return password, hash_password

print(PasswordHashGenerator())