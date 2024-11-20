def forevermore(msg):
    for c in range(1,msg+1):
        print(f'{c} '*c)
forevermore(int(input('Digite um número pra ser feito a ordem numérica: ')))     