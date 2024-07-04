from roman_funcs import to_roman

z = 84
cas = f"{z:04d}"

print (cas)


millares = int(cas[0]) * 1000
centenas = int(cas[1]) * 100
decenas = int(cas[2]) * 10
unidades = int(cas[3]) * 1

print(f"{millares},{centenas},{decenas},{unidades}")
