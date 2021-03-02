import psycopg2
import random
import hashlib
import os
from decimal import Decimal
from database import conn, cur

class Client:
    def __init__(self, client_id, name, cpf, phone, income, credit_card, monthly_limit, available_credit, salt, key):
        self.id = client_id
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.income = income
        self.credit_card = credit_card
        self.monthly_limit = monthly_limit
        self.available_credit = available_credit
        self.salt = salt
        self.key = key

    def getId(self):
        return self.id

    def setId(self, client_id):
        self.id = client_id
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getCPF(self):
        return self.cpf

    def setCPF(self, cpf):
        self.cpf = cpf    

    def getIncome(self):
        return self.income

    def setIncome(self, income):
        self.income = Decimal(income)

    def getCreditCard(self):
        return self.credit_card

    def setCreditCard(self, credit_card):
        self.credit_card = credit_card

    def getMonthlyLimit(self):
        return self.monthly_limit

    def setMonthlyLimit(self, monthly_limit):
        self.monthly_limit = Decimal(monthly_limit) 

    def getAvailableCredit(self):
        return self.available_credit

    def setAvailableCredit(self, available_credit):
        self.available_credit = Decimal(available_credit)

    def setSalt(self, salt):
        self.salt = salt
    
    def getSalt(self):
        return self.salt

    def setKey(self, key):
        self.key = key
    
    def getKey(self):
        return self.key

    def printData(self):
        print(f'\nNome: {self.name}')
        print(f'CPF: {self.cpf}')
        print(f'Nº do cartão: {self.credit_card}')
        print(f'Nº do telefone: {self.phone}')

class Admin:
    def __init__(self, admin_id, name, salt, key):
        self.id = admin_id
        self.name = name
        self.salt = salt
        self.key = key

    def getId(self):
        return self.id

    def setId(self, admin_id):
        self.id = admin_id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setSalt(self, salt):
        self.salt = salt
    
    def getSalt(self):
        return self.salt

    def setKey(self, key):
        self.key = key
    
    def getKey(self):
        return self.key

class Purchase:
    def __init__(self, purchase_id, category, price, date):
        self.id = purchase_id
        self.category = category
        self.price = price
        self.date = date

    def getId(self):
        return self.id

    def setId(self, purchase_id):
        self.id = purchase_id

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = Decimal(price)

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

class Request:
    def __init__(self, request_id, client_id, admin_id, new_income, new_monthly_limit, new_available_credit, status):
        self.request_id = request_id
        self.client_id = client_id
        self.admin_id = admin_id
        self.new_income = new_income
        self.new_monthly_limit = new_monthly_limit
        self.new_available_credit = new_available_credit
        self.status = status

    def getRequestId(self):
        return self.request_id

    def setRequestId(self, request_id):
        self.request_id = request_id

    def getClientId(self):
        return self.client_id

    def setClientId(self, client_id):
        self.client_id = client_id

    def getAdminId(self):
        return self.admin_id

    def setAdminId(self, admin_id):
        self.admin_id = admin_id

    def getNewIncome(self):
        return self.new_income

    def setNewIncome(self, new_income):
        self.new_income = Decimal(new_income)

    def getNewMonthlyLimit(self):
        return self.new_monthly_limit

    def setNewMonthlyLimit(self, new_monthly_limit):
        self.new_monthly_limit = Decimal(new_monthly_limit)

    def getNewAvailableCredit(self):
        return self.new_available_credit

    def setNewAvailableCredit(self, new_available_credit):
        self.new_available_credit = Decimal(new_available_credit)

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getId(self):
        return self.request_id

    def setId(self, request_id):
        self.request_id = request_id

def login():
    print('\nBem vindo ao CCbank! | Realize o login')

    while True:
        user = input('\nUsername: ')
        password = input('Senha: ')

        if getAdmin(user, password) != -1:
            admin = getAdmin(user, password)
            print(f'\nEntrou como administrador ({admin.getName()})')

            getOption(admin)
            break
        
        elif getClient(user, password) != -1:
            client = getClient(user, password)
            print(f'\nOlá, {client.getName()}!')

            getOption(client)
            break

        else:
            print('\nNão há nenhuma conta cadastrada com esses dados! Tente novamente.')

#direciona o usuário para a operação desejada
def getOption(account):
    if type(account) == Admin:
        option = input('\nSelecione uma opção: \n|00| - Fechar Sistema; |0| - Deslogar; |1| - Cadastro do Administrador; |2| - Cadastro de Clientes; ' 
        + '|3| - Listar Clientes; \n|4| - Verificar Pedidos de Mudança de Limite; |5| - Alterar Dados do Cliente; |6| - Deletar Cliente - ')

        if option == '00':
            print('\nPrograma Encerrado')
            quit()

        elif option == '0':
            print('\nDeslogado com sucesso!')
            login()

        elif option == '1':
            adminRegistration(account)

        elif option == '2':
            clientRegistration(account)

        elif option == '3':
            printAllClients(account)

        elif option == '4':
            checkRequests(account)

        elif option == '5':
            alterClientAccount(account)

        elif option == '6':
            deleteClient(account)

        else:
            print('\nDigite uma opção válida!')
            getOption(account)

    elif type(account) == Client:
        option = input('\nSelecione uma opção: \n|00| - Fechar Sistema; |0| - Sair; |1| - Adicionar Gastos; |2| - Extrato; ' 
        + '|3| - Requisitar Mudança de Limite; |4| - Alterar Senha; - ')

        if option == '00':
            print('\nPrograma Encerrado')
            quit()

        elif option == '0':
            print('\nDeslogado com sucesso!')
            login()

        elif option == '1':
            monthlyPurchasesRegistration(account)

        elif option == '2':
            generateBankStatement(account)
        
        elif option == '3':
            requestLimitChange(account)

        elif option == '4':
            changePassword(account)

        else:
            print('\nDigite uma opção válida!')
            getOption(account)

def clientRegistration(admin):
    print('\nDigite os dados para o cadastro do cartão do cliente!')

    name = input('\nNome Completo: ')
    phone = input('Nº de Telefone: ')

    while True:
        cpf = input('CPF: ')

        if validateCPF(cpf):
            income = Decimal(float(input('Renda Mensal (R$): ')))

            while True:
                password = input('Senha: ')

                if validatePassword(password):
                    salt = os.urandom(32)
                    key = hashPassword(password, salt)

                    credit_card = creditCardGenerator()
                    monthly_limit = income * Decimal(0.85)
                    available_credit = monthly_limit

                    cur.execute('''INSERT INTO client (name, cpf, phone, income, credit_card, monthly_limit, available_credit, salt, key_pass) VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (name, cpf, phone, income, credit_card, monthly_limit, available_credit, salt, key))

                    conn.commit()

                    print('\nCadastro realizado com sucesso!')

                    print(f'\nNúmero do Cartão: {credit_card}\nLimite de Crédito: R${monthly_limit:.2f}')
                    print(f'\nATENÇÃO! O número do cartão ({credit_card}) é o seu username.')

                    getOption(admin)
                    break
                
                else:
                    print('\nA senha deve conter mais que 6 dígitos! Tente novamente.\n')

            break

        else:
            print('\nCPF inválido ou já cadastrado previamente! Tente novamente.\n')

def adminRegistration(admin):
    print('\nDigite os dados para a criação de um novo administrador!')

    name = input('\nUsuário: ')
    
    while True:
        password = input('Senha: ')

        if validatePassword(password):
            salt = os.urandom(32)
            key = hashPassword(password, salt)

            cur.execute('''INSERT INTO administrator (name, salt, key_pass) VALUES (%s, %s, %s)''', (name, salt, key))
            conn.commit()

            print('\nAdministrador cadastrado com sucesso!')
            break

        else:
            print('\nA senha deve conter mais que 6 dígitos! Tente novamente.\n')

    getOption(admin)

def printAllClients(admin):
    print('\nListagem de todos os clientes: ')
    
    cur.execute("SELECT name, cpf, credit_card FROM client;")

    clients = cur.fetchall()
    
    if len(clients) > 0:
        print('\nCPF \t\t Nome \t\t\t Número do Cartão')

        for client in clients:
            print(f'{client[1]} \t {client[0]} \t\t {client[2]}')
    else:
        print('\nNão há nenhum cliente cadastrado no sistema!')

    getOption(admin)

#função que realiza o processo de análise para aprovar ou negar a mudança de limite mensal dos clientes que requisitaram.
def checkRequests(admin):
    print('\nAnalise o pedido de mudança no limite de crédito dos clientes!')

    cur.execute("SELECT * FROM limit_increase_request WHERE status = 'análise';")
    requests = cur.fetchall()

    if len(requests) > 0:
        print('\nCartão       |        Cliente')

        for request in requests:
            cur.execute(f"SELECT name, credit_card FROM client WHERE client_id = {request[1]}")
            client_data = cur.fetchone()

            print(f'{client_data[1]}     {client_data[0]}')

        verify = input('\nVocê deseja análisar a mudança de limite de crédito de algum cliente? (S/N): ').upper()

        if verify == 'S':
            client = getClientByCreditCard()

            if client != -1:
                request = getRequestByClient(client)
                
                if request != -1:
                    print(f'\nDados da Requisição do {client.getName()}:')
                    print(f'\nRenda Atual: R${client.getIncome():.2f}')
                    print(f'Limite de Crédito Atual: R${client.getMonthlyLimit():.2f}')
                    print(f'\nNova Renda: R${request.getNewIncome():.2f}')
                    print(f'Novo Limite de Crédito: R${request.getNewMonthlyLimit():.2f}')

                    approval = input(f'\nVocê deseja aprovar essa requisição feita pelo cliente, {client.getName()}? (S/N): ').upper()

                    if approval == 'S':
                        status = 'aprovado'

                        cur.execute(f"""UPDATE client SET income = {request.getNewIncome()}, monthly_limit = {request.getNewMonthlyLimit()}, 
                        available_credit = {request.getNewAvailableCredit()} WHERE client_id = {client.getId()};""")

                        print('\nRequisição Aprovada! Novo limite de crédito definido.')
           
                    else:
                        status = 'negado'
                        print('\nRequisição Negada!')
                    
                    cur.execute(f"UPDATE limit_increase_request SET admin_id = {admin.getId()}, status = '{status}' WHERE request_id = {request.getId()};")
                    print('real status:', status)
                    conn.commit()
            
            else:
                print('\nNenhum cliente encontrado! Tente novamente.')

    else:
        print('\nNão há nenhuma requisição no momento!')
    
    getOption(admin)    

#retorna a requisição do cliente informado no parâmetro, ou -1 caso não encontre requisição daquele cliente
def getRequestByClient(client):
    cur.execute(f"SELECT * FROM limit_increase_request WHERE client_id = {client.getId()}")
    request = cur.fetchone()

    if request is not None:
        dictionary = returnRequestDictionary(request)

        request = Request(dictionary['id'], dictionary['client_id'], dictionary['admin_id'], dictionary['new_income'], 
            dictionary['new_monthly_limit'], dictionary['new_available_credit'], dictionary['status'])

        return request

    return -1

def alterClientAccount(admin):
    while True:
        client = getClientByCreditCard()
        
        if client != -1:
            print('\nDados atuais:')
    
            client.printData()

            print('\nFaça as alterações desejadas!')

            name = input('\nNome Completo: ')
            phone = input('Nº de Telefone: ')

            while True:
                cpf = input('CPF: ')

                if cpf == client.getCPF() or validateCPF(cpf):
                    alter = input('\nVocê tem certeza que deseja salvar as alterações? (S/N): ').upper()
                    
                    if alter == 'S':
                        cur.execute(f"UPDATE client SET name = '{name}', phone = '{phone}', cpf = '{cpf}' WHERE client_id = {client.getId()};")
                        conn.commit()
                        
                        print('\nDados salvos com sucesso!')
                        break #quebra o segundo while

                else:
                    print('\nCPF inválido ou já cadastrado previamente! Tente novamente.\n')

            break #quebra o primeiro while

        else:
            print('\nNenhum cliente encontrado! Tente novamente.')

    getOption(admin)

def deleteClient(admin):
    while True:
        print('\nDigite o número do cartão do cliente que será apagado!')

        client = getClientByCreditCard()
        
        if client != -1:
            client.printData()

            delete = input(f'\nVocê tem certeza que deseja apagar o cliente {client.getName()}? (S/N): ').upper()

            if delete == 'S':
                request = getRequestByClient(client)

                if request != -1:
                    if request.getStatus() == 'análise':
                        cur.execute(f"DELETE FROM limit_increase_request WHERE client_id = '{request.getClientId()}';")

                cur.execute(f"DELETE FROM client WHERE client_id = '{client.getId()}';")
                conn.commit()

                print('\nCliente deletado com sucesso!')
                break

            else:
                print('\nOperação cancelada!')
                    
        else:
            print('\nNenhum cliente encontrado! Tente novamente.')

    getOption(admin)

#registra os custos mensais do cliente
def monthlyPurchasesRegistration(client): 
    print('\nDespesas Mensais:')

    client.printData()
    
    #faz com que o user não precise repetir o processo de login, caso adicione um custo na sequência da outra
    while True:
        print('\nRegistre uma compra.')

        available_credit = client.getAvailableCredit()

        category = input('\nCategoria: ').capitalize()

        #enquanto o custo for menor que R$0.00, o custo não é registrado
        while True:
            price = Decimal(float(input('Valor: R$')))
            
            if price <= 0:
                print('\nO valor da compra precisa ser maior que R$0.00')
                break

            else:
                if available_credit >= price:
                    available_credit = available_credit - price

                    date = input('Data: ')
                    
                    cur.execute(f"""INSERT INTO purchase (client_id, category, price, date) VALUES ({client.getId()}, 
                    '{category}', {price}, '{date}');""")

                    cur.execute(f"UPDATE client SET available_credit = '{available_credit}' WHERE client_id = {client.getId()};")

                    conn.commit()
                    
                    client.setAvailableCredit(available_credit)
                else:
                    print('\nCrédito Insuficiente!')
                
                break

        print(f'\nCrédito Disponível: R${available_credit:.2f}')

        if input('\nDeseja registrar mais algum gasto? (S/N): ').upper() != 'S':
            getOption(client)
            break

#gera o extrato mensal do cliente
def generateBankStatement(client):
    print('\nExtrato Mensal')

    client.printData()
    
    print('\nDespesas: \n')

    cur.execute(f"SELECT category, price, date FROM purchase WHERE client_id = '{client.getId()}';")

    purchases = cur.fetchall()
    
    if len(purchases) > 0:
        for purchase in purchases:              
            print(f'{purchase[0]} - R${purchase[1]:.2f} - {purchase[2]}')

    else:
        print('Não há nenhuma despesa registrada!')

    limit = client.getMonthlyLimit()
    available_credit = client.getAvailableCredit()

    print(f'\nCrédito Limite (mês): R${limit:.2f}')
    print(f'Crédito Gasto: R${limit - available_credit:.2f}')
    print(f'Crédito Disponível: R${available_credit:.2f}')

    getOption(client)

#função para o cliente pedir um novo limite
def requestLimitChange(client):
    cur.execute(f"SELECT status FROM limit_increase_request ORDER BY request_id DESC") # 
    status = cur.fetchone()[0]
    print(status, 'type:', type(status))

    checkStatusRequest(client, status)

    if status != "análise":
        new_request = input('\nDeseja solicitar nova mudança de limite? (S/N): ').upper()

        if new_request == 'S':
            checkStatusRequest(client, None)

    getOption(client)

def changePassword(client):
    change = input(f'\n{client.getName()}, você deseja alterar sua senha? (S/N): ').upper()

    if change == 'S':
        while True:
            password = input('\nSenha atual: ')
            key = hashPassword(password, client.getSalt())

            saved_key = client.getKey()

            if key == saved_key:
                while True:
                    new_password = input('Nova senha: ')

                    if validatePassword(new_password):
                        if new_password != password:
                            salt = os.urandom(32)
                            new_key = hashPassword(new_password, salt)

                            cur.execute('''UPDATE client SET salt=%s, key_pass=%s WHERE client_id=%s''', (salt, new_key, client.getId()))
                            conn.commit()

                            print('\nSenha alterada com sucesso!')
                            break
                        
                        else:
                            print('\nSua nova senha deve ser diferente da senha atual!\n')
                    
                    else:
                        print('\nA senha deve conter mais que 6 dígitos! Tente novamente.\n')

                break
            
            else:
                print('\nSenha incorreta! Tente novamente.')

    getOption(client)

#retorna o cliente com os dados passados nos parametros
def getClient(credit_card, password):
    cur.execute(f"SELECT * FROM client WHERE credit_card = '{credit_card}';")

    data = cur.fetchone()

    if data is not None:
        dictionary = returnClientDictionary(data)

        salt = dictionary['salt']
        key = dictionary['key']

        new_key = hashPassword(password, salt)

        if new_key == key:
            client = Client(dictionary['id'], dictionary['name'], dictionary['cpf'], dictionary['phone'], dictionary['income'], dictionary['credit_card'],
                    dictionary['monthly_limit'], dictionary['available_credit'], salt, key)

            return client
    
    return -1

#retorna o cliente pelo seu cartão de crédito
def getClientByCreditCard():
    credit_card = input('\nNúmero do cartão: ')

    cur.execute(f"SELECT * FROM client WHERE credit_card = '{credit_card}';")
    data = cur.fetchone()

    if data is not None:
        dictionary = returnClientDictionary(data)

        client = Client(dictionary['id'], dictionary['name'], dictionary['cpf'], dictionary['phone'], dictionary['income'], dictionary['credit_card'],
                    dictionary['monthly_limit'], dictionary['available_credit'], dictionary['salt'], dictionary['key'])

        return client 

    return -1

#retorna o admin com os dados passados nos parametros
def getAdmin(user, password):
    cur.execute(f"SELECT * FROM administrator WHERE name = '{user}';")

    data = cur.fetchone()

    if data is not None:
        dictionary = returnAdminDictionary(data)

        salt = bytes(dictionary['salt'])
        key = bytes(dictionary['key'])

        new_key = hashPassword(password, salt)

        if new_key == key:
            admin = Admin(dictionary['id'], dictionary['name'], salt, key)

            return admin

    return -1

def checkStatusRequest(client, status):
    if status is None:
        print(f'\n{client.getName()}, requisite uma mudança no limite de crédito do seu cartão!')

        income = client.getIncome()
        new_income = Decimal(float(input('\nInsira sua renda mensal: R$')))
        
        if new_income != income:
            new_monthly_limit = new_income * Decimal(0.85)
            new_available_credit = client.getAvailableCredit() + (new_monthly_limit - client.getMonthlyLimit())

            print('new available credit type:', type(new_available_credit))

            status = 'análise'

            if new_available_credit > 0:
                cur.execute(f"""INSERT INTO limit_increase_request (client_id, new_income, new_monthly_limit, new_available_credit, status) VALUES (
                    {client.getId()},
                    {new_income},
                    {new_monthly_limit},
                    {new_available_credit},
                    '{status}');
                """)

                conn.commit()

                print('\nSua requisição está em análise. Aguarde!')
                    
            elif new_available_credit < 0:
                print('\nPedido Negado! Baseado em seus gastos desse mês, seu crédito disponível ficaria menor que zero.')
            
        else:
            print('\nPedido Negado! É necessário inserir uma renda diferente da cadastrada previamente.')
    
    elif status == 'aprovado':
                print(f'\nSua requisição para mudança de limite foi APROVADA!')
                print(f'Seu novo limite mensal é R${client.getMonthlyLimit():.2f} e você tem R${client.getAvailableCredit():.2f} de crédito disponível!')

    elif status == 'negado':
        print(f'\nSua requisição para mudança de limite foi NEGADA!')
    
    else:
        print('\nSua requisição está em análise. Aguarde!')

def creditCardGenerator():
    while True:
        credit_card = ''

        for i in range(16):
            random_number = random.randint(0,9)
            credit_card += str(random_number)

        cur.execute("SELECT credit_card FROM client;")
        credit_cards = cur.fetchall()

        if credit_card not in credit_cards:
            return credit_card

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

                cur.execute("SELECT cpf FROM client;")
                all_cpf = cur.fetchall()

                if cpf not in all_cpf:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False

def validatePassword(password):
    if len(password) < 6:
        return False
    else:
        return True

def returnClientDictionary(data):
    dictionary = {'id': data[0],'name': data[1], 'cpf': data[2], 'phone': data[3], 'income': data[4], 'credit_card': data[5],
     'monthly_limit': data[6], 'available_credit': data[7], 'salt': bytes(data[8]), 'key': bytes(data[9])}

    return dictionary

def returnAdminDictionary(data):
    dictionary = {'id': data[0],'name': data[1], 'salt': bytes(data[2]), 'key': bytes(data[3])}

    return dictionary

def returnRequestDictionary(data):
    dictionary = {'id': data[0],'client_id': data[1], 'admin_id': data[2], 'new_income': data[3], 'new_monthly_limit': data[4],
     'new_available_credit': data[5], 'status': data[6]}

    return dictionary

def hashPassword(password, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256', # the hash digest algorithm for HMAC
        password.encode('utf-8'),  # convert the password to bytes
        salt,
        100000, # number of iterations of SHA-256 (recommended to use at least 100,000) 
    )
    return key

login()

cur.close()
conn.close()