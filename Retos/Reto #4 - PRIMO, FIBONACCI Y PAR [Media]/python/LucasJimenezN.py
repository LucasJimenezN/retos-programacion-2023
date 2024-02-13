"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""
import math

def Fibbonachi(num):
    prev_2 = 0
    prev_1 = 1
    if num < 0:
        return False
    if num < 1:
        return True

    while True:
        aux = prev_1
        prev_1 = prev_1 + prev_2
        prev_2 = aux
        if prev_1 == num:
            return True
        else:
            if prev_1 > num:
                return False


def Primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def LucasJimenezN(num):
    par = True if num % 2 == 0 else False

    fibonacci = Fibbonachi(num)

    primo = Primo(num)

    print(
        f"{num} {'es' if primo else 'no es'} primo, "
        f"{'es' if fibonacci else 'no es'} fibonacci, "
        f"es {'par' if par else 'impar'}.")


LucasJimenezN(8)
LucasJimenezN(2)
LucasJimenezN(7)
