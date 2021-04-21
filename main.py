num = int(input('Digite um numero: '))

soma = 0
cont = 0
for c in range(1, num+1):
    if c % 2 == 0:   
      soma = soma + c
      cont = cont + 1    
      print(c)
print('A sequencia de 1 a {} possui {} numeros pares e a soma entre eles é {}'.format(num,cont,soma))


