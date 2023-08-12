#Segunda parte: Solo fines de semana.
n=0
fecha=''
tb=5.0
costtal=0.0

n=int(input('Ingresa la cantidad de boletas a comprar:' ))
fecha=input("La boleta es para finde semana?(si o no)")
if fecha=='si':
  costtal=tb*1.20
else:
  costtal=tb
palco=input("Escribe A, B, C, según el palco:")
if palco=='A':
  costtal+=tb*.1
elif palco=='B':
  costtal+=tb*.05
print("El costo total a pagar:", costtal*n)

#Tercer parte: Descuentos cantidad de boletas
if n>=5 and n<=10:
  costtal=costtal*.9
if n>=15 and n<=20:
  costtal=costtal*.85
if n>=25:
  costtal=costtal*.8
print("costo total es: ", costtal*n)