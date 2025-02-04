def interes_compuesto(P, r, t, n=1):
    A = P * (1 + r/n) ** (n * t)
    return A
monto_final = interes_compuesto(1500, 0.55, 5)
interes_ganado = monto_final - 1500
print(f"Monto final: {monto_final:.2f}")  
print(f"Interés ganado: {interes_ganado:.2f}")  