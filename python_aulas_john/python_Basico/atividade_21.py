# Atividade 21
fahrenheit = float(input("Digite a temperatura em Fahrenheit (°F): "))
celsius = (fahrenheit - 32) / 1.8 
print(f"{fahrenheit}°F = {celsius:.1f}°C")
if celsius < 0:
    print(f"Brr!!! Está frio aqui!")
# Digite a temperatura em Fahrenheit (°F): 132
# 132.0°F = 55.6°C
# Digite a temperatura em Fahrenheit (°F): 25
# 25.0°F = -3.9°C
# Brr!!! Está frio aqui!