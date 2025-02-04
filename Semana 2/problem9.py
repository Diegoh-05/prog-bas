def generar_pares_impares(limite):
    pares= []
    impares= []
    for i in range(1, limite + 1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares
limite = 56
pares, impares = generar_pares_impares(limite)
print("Numeros pares:", pares)
print("Numeros impares:", impares)