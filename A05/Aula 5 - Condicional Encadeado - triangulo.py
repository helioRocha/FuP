print 'Digite o primeiro lado'
lado1 = input()

print 'Digite o segundo lado'
lado2 = input()

print 'Digite o terceiro lado'
lado3 = input()

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0 or lado1 >= lado2 + lado3 or lado2 >= lado3 + lado1 or lado3 >= lado2 + lado1:
	print 'Nao e um triangulo'
else:
	if lado1 == lado2 and lado2 == lado3:
		print 'Triangulo Equilatero!'
	else:
		if lado1 <> lado2 and lado2 <> lado3 and lado1 <> lado3:
			print 'Triangulo Escaleno!'
		else:
			print 'Triangulo Isoceles!'


