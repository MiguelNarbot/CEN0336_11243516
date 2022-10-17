

co = float(input('Coloque o valor do cateto oposto:')) #a função "input" permite alocar os dados para serem trabalhados. A float permite que qualquer número seja colocado e não de erro. 
ca = float(input('Coloque o valor do cateto adjacente:')) #a função "input" permite alocar os dados para serem trabalhados. A float permite que qualquer número seja colocado e não de erro. 

x = int(co) #a função expõe que o número necessita ser inteiro para ser utilizado na função "z". 
y = int(ca) #a função expõe que o número necessita ser inteiro para ser utilizado na função "z". 

hipotenusa= (ca*2+co*2)**(1/2) #quadrado da hipotenusa. Função básica.

if x == co:                           #se x for igual número inteiro (int) printar 'é inteiro'.
    print(co, 'é inteiro')   
else:
    print ('O número precisa ser inteiro!')  #se não for igual ao inteiro, printar 'o número precisa ser inteiro'.

if y == ca:                          #se y for igual número inteiro (int) printar 'é inteiro'.
    print(ca, 'é inteiro')
else:
    print ('O número precisa ser inteiro!')  #se não for igual ao inteiro, printar 'o número precisa ser inteiro'.

if co<0 or ca<0:
  print('O número precisa ser positivo!')    #condição para acontecer o problema. Precisam ser números positívos. 

if x == co and y == ca:         #se forem inteiros e positivos printar:
    print("O quadrado da hipotenusa para o retângulo, cuja os lados são",co, 'e', ca,'é:', round(hipotenusa))
else:
    print ('Para o caso de String e Float não é possivel calcular')  #se não forem inteiros e positivos printar:
 

