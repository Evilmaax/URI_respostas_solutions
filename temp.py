name=str(input('Write your name: ')) #Recebe o nome

def check(name): #Função para checar se o nome é elvis
    while(name!='elvis'): #Loop que fica pedindo o nome até ser digitado o correto
        print('You are not allowed!') #Mensagem avisando que não tem permissão
        name=str(input('Write your name: ')) #Recebe o nome novamente
    print('Welcome {}!'.format(name)) #Mensagem de boas vindas

check(name) #Função acima