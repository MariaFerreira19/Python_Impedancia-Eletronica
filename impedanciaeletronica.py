import math

f = float(input("Digite a frequência do sinal (Hz): "))
R = float(input("Qual é a resistência (ohms)? "))
C = float(input("E a capacitância? (farads): "))
L = float(input("Por fim, digite a indutância (henrys): "))

Xc = 1 / (2 * math.pi * f * C)
Xl = 2 * math.pi * f * L

Z = math.sqrt(R**2 + (Xl - Xc)**2)

print(f"A frequência é: {f:.2f} Hz")
print(f"A resistência é: {R:.2f} ohms")
print(f"A reatância do capacitor é: {Xc:.2f} ohms")
print(f"A reatância da bobina é: {Xl:.2f} ohms\n")
print(f"Impedância total: {Z:.2f} ohms")
