import random

#fazer verificação da senha | fazer opção de alterar dados (renda e etc)
#fazer abstração de codigo na parte da class Client

class Purchase:
    category = ''
    value = 0.0
    date = ''

class Client:
    def __init__(self, name, phone, cpf, income, credit_card, monthly_limit, available_credit, password):
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.income = income
        self.credit_card = credit_card
        self.monthly_limit = monthly_limit
        self.available_credit = available_credit
        self.password = password
        self.purchases = []

    def addPurchase(self, purchase):
        self.purchases.append(purchase)

    def printData(self):
        print(f'\nNome: {self.name}')
        print(f'CPF: {self.cpf}')
        print(f'Nº do cartão: {self.credit_card}')
        print(f'Nº do telefone: {self.phone}\n')

    def getCard(self):
        return self.credit_card

    def getPassword(self):
        return self.password

admin_user = ''
admin_password = ''

clients = []

#verifica se o usuário deseja realizar uma operação bancária
def operation():
    operation = input('\nVocê deseja realizar uma operação (S/N): ').upper()

    if operation == 'S':
        getOption()
    else:
        print('\nPrograma Encerrado')
        quit()

#
def getOption():
    option = input('\nSelecione uma opção: \n|0| - Sair; |1| - Cadastro; |2| - Adicionar Custos; |3| - Extrato; - ')

    if option == '0':
        print('\nPrograma Encerrado')
        quit()

    elif option == '1':
        registration()

    elif option == '2':
        monthlyPurchases()
    
    elif option == '3':
        bankStatement()

    else:
        print('\nDigite uma opção válida!')
        getOption()

def validateCPF(cpf):

    if len(cpf) == 11 and cpf != cpf[::-1]:

        cpf_numbers = []
        calc = 0

        for i in range(9):
            cpf_numbers.append(int(cpf[i]))
            calc += cpf_numbers[i] * (10 - i)

        if (calc * 10) % 11 == int(cpf[-2]):
            cpf_numbers.clear()
            calc = 0

            for j in range(10):
                cpf_numbers.append(int(cpf[j]))
                calc += cpf_numbers[j] * (11 - j)

            if (calc * 10) % 11 == int(cpf[-1]):
                return True

        else:
           print('\nCPF inválido!')
           return False  
    else:
        print('\nO CPF deve ter obrigatoriamente 11 números. E não podem ser todos iguais!')
        return False

def verifyData(client):

    #verifica se o user digitou ao menos dois nomes
    if client.name.find(' ') == -1:
        print('\nVocê precisa digitar o seu nome completo!')
    
    #verifica se o cpf digitado tem pelo menos 10 dígitos
    if len(client.phone) < 10:
        print('\nNº de telefone inválido! Ex: 05499024340')

def creditCardGenerator():
    
    credit_card = ''

    for i in range(16):
        random_number = random.randint(0,9)
        credit_card += str(random_number)

    return credit_card

#realiza o cadastro do cartão do cliente
def registration():
    
    while True:

        print('\nEsta operação só pode ser realizada por administradores. Entre como um!')

        input_admin_user = input('\nUsuário: ')
        input_admin_password = input('Senha: ')
            
        if input_admin_password == admin_password and input_admin_user == admin_user:

            print(f'\nEntrou como administrador ({admin_user})')
            print('\nDigite os dados para o cadastro do cartão!')

            name = input('\nNome Completo: ')
            phone = input('Nº de Telefone: ')
            cpf = input('CPF: ')
            income = float(input('Renda Mensal (R$): '))
            password = input('Senha: ') 

            if validateCPF(cpf):
                print('\nCadastro realizado com sucesso!')

                credit_card = creditCardGenerator()
                monthly_limit = income * 0.85 #crédito mensal é igual a 85% da renda mensal
                available_credit = monthly_limit

                client = Client(name, phone, cpf, income, credit_card, monthly_limit, available_credit, password)
                    
                clients.append(client)

                print(f'\nNúmero do Cartão: {credit_card}\nLimite de Crédito: R${monthly_limit:.2f}')

                operation()

            break

        else:
            print('\nUsuário ou senha do administrador incorretos!')

def getClient(card, psw):
    for obj in clients:
        if obj.getCard() == card:
            if obj.getPassword() == psw:
                return obj
    #return False
            
#registra os custos mensais do cliente
def monthlyPurchases():

    #enquanto o user não digitar o nº do cartão e/ou a senha corretos, o programa continuará repetindo
    while True:

        card = input('\nNúmero do seu cartão: ')
        password = input('Senha: ')

        client = getClient(card, password)
        
        if client:
            
            print('\nDespesas Mensais')

            client.printData()
            
            #faz com que o user não precise repetir o processo de login, caso adicione um custo na sequência da outra
            while True:
                purchase = Purchase()

                purchase.category = input('Categoria: ')

                while True:
                    purchase.value = abs(float(input('Valor: R$')))

                    if client.available_credit > purchase.value:
                        client.available_credit += -purchase.value

                        purchase.date = input('Data: ')
                        break

                    else:
                        print('\nCrédito Insuficiente!\n')
                        
                
                print(f'\nCrédito Atual: R$ {client.available_credit:.2f}')

                client.addPurchase(purchase)

                if input('\nDeseja adicionar mais algum gasto? (S/N): ').upper() != 'S':
                    operation()
                    break
            break
        else:
            print('\nOs dados estão incorretos. Tente novamente!')

#gera o extrato mensal do cliente
def bankStatement():
    while True:

        card = input('\nNúmero do seu cartão: ')
        password = input('Senha: ')

        client = getClient(card, password)
        
        if client:
            
            print('\nExtrato Mensal')

            client.printData()

            for obj in client.purchases:                
                print(f'{obj.category.capitalize()} - R${obj.value:.2f} - {obj.date}')
            
            print(f'\nCrédito Limite (mês): R${client.monthly_limit:.2f}')
            print(f'Crédito Gasto: R${client.monthly_limit - client.available_credit:.2f}')
            print(f'Crédito Restante: R${client.available_credit:.2f}')

            operation()
            break

operation()