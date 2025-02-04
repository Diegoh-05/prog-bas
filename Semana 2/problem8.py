import math
def calcular_area_y_circunferencia(r):
    area= math.pi * r ** 2
    circunferencia = 2 * math.pi * r
    return area, circunferencia
radio =10
area, circunferencia = calcular_area_y_circunferencia(radio)
print(f"Área: {area:.2f}")  
print(f"Circunferencia: {circunferencia:.2f}")  