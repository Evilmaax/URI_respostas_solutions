while True:
    try:
        expressao = input()
        n1, n2, z = 0, 0, 0
        pilha = []

        for x in expressao:
            if x == '(':
                n1 +=1
                pilha.append('(')
            elif x == ')':
                n2 += 1
                if len(pilha) != 0:
                    pilha.pop(0)
                else:
                    break

        if len(pilha) == 0 and n1 == n2:
            print('correct')
        else:
            print('incorrect')

    except EOFError:
        break