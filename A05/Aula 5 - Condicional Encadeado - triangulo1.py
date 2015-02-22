print 'Digite o primeiro lado'
lado1 = input()

print 'Digite o segundo lado'
lado2 = input()

print 'Digite o terceiro lado'
lado3 = input()

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 and lado1 > 0 and lado2 > 0 and lado3 > 0:
	print 'E Triangulo!'
	if lado1 == lado2 and lado2 == lado3:
		print 'Equilatero!'
	elif lado1 <> lado2 and lado2 <> lado3 and lado1 <> lado3:
		print 'Escaleno!'
	else:
		print 'Isoceles!'
else:
	print 'Nao e triangulo'
