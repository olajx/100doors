def doors (n):
    doors = [False] * n                         # ajtók száma (tömb segítségével)
    

    for i in range(n):                          #végigmegyek a külső cikluson 100-ig
        for j in range(i, n, i+1):              # belső ciklus i lépésszámlálóval
            doors[j] = not doors[j]             # megcseréli a tárolt értéket
    
                                                # eredmény kiírása
    help=''                                     # string, ami segít a kiírásban
    for k, door in enumerate(doors, start=1):   #enumerate fv segítségével listázom az elemeket
        if door == True:                        # ha az ajtó nyitva, hozzáfűzöm a help változóhoz
            help+=str(k) + ", "
    
    print("The following doors are open:",help[0:len(help)-2]) 
           
doors(100)