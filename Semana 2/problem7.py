def analizar_numero(n, m):
    if n % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    if n % m == 0:
        multiplo = f"{n} es multiplo de {m}"
    else:
        multiplo = f"{n} no es múltiplo de {m}"
    return f"{n} es {tipo}, {multiplo}."
print(analizar_numero(25, 3))