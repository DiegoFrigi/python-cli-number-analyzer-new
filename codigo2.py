import math
#raio
r = float(input("Escreva um valor para o raio: "))
#altura
h = float(input("Escreva uma valor para a altura: "))
area1 = 2 * math.pi * r * h
area2 = 2 * math.pi * r ** 2
area_total = round(area1 + area2, 2)
print(f"A área desse cilindro é de {area_total} cm^2")

if area_total >= 200:
    print("Área grande")
else:
    print("Área pequena")

