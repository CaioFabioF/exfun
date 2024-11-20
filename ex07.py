def pagarP(p,a=0):
    if a == 0 :
        print(f'O valor a ser pago é: R${p:.2f}')
    else:
        m = 0.03
        a = (a*0.1)
        p = p + (p*m) + a
        print(f'O valor a ser pago é de R${p:.2f}')
pagarP(1340,70)