def magnetic(msg):
    for c in range(1,msg+1):
        for a in range(1,c+1):
            print(f'{a}',end=' ')
        print()
magnetic(100)