valor1 = input()
valor2 = input()

mmc = 1
divisor = 2

#print valor1 , ',', valor2, '|', divisor

while valor1 <> 1 or valor2 <> 1:
	if valor1%divisor==0 and valor2%divisor==0:
		print valor1 , ',', valor2, '|', divisor
		#aux = input()
		valor1 = valor1/divisor
		valor2 = valor2/divisor
		mmc = mmc * divisor
		
	elif valor1%divisor==0:
		print valor1 , ',', valor2, '|', divisor
		#aux = input()
		valor1 = valor1/divisor
		mmc = mmc * divisor
	elif valor2%divisor==0:
		print valor1 , ',', valor2, '|', divisor
		#aux = input()
		valor2 = valor2/divisor
		mmc = mmc * divisor
	else:
		divisor = divisor + 1
print valor1 , ',', valor2, '|', '1'
print mmc
