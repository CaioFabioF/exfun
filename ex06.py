def horas(h,m):
    a = h
    if h > 12:
        a = h - 12
        if a <= 0 :
            a = a * -1
            print(f'{a}:{m} A.M')
        else :
            print(f'{a}:{m} P.M')
    else: 
        print(f'{a}:{m} A.M')
while True:
    c = int(input('Digite apenas as horas: '))
    d = int(input('Digite apenas os minutos: '))
    horas(c,d)
    e = str(input('Deseja continuar?[S/N]: '))
    if e in 'Nn':
        break