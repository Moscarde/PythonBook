x= 0

while x < 10:
  x+=1
  print("x=",x)
  if x ==5:
    break
    # sai do laço


y=0

while y < 10:
  y+=1
  if y == 5:
    continue
    # nao executa o que está abaixo
  print("y=",y)


nome = "Gabriel"

for letra in nome:
  if letra == "r":
    break
  else:
    print(letra)

nome2= "Laura"

for letra in nome2:
  if letra == "u":
    continue
  else:
    print(letra)