valor1 = input()
valor2 = input()

if valor1 >= valor2:
	mmc = valor1
else:
	mmc = valor2

while mmc%valor1 <> 0 or mmc%valor2 <> 0:
	mmc = mmc + 1

print mmc
