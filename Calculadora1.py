#Lower ==> para tratar variações de maiúsculas e minúsculas
#startswith ==> permite verificar se uma string começa com um determinado prefixo.

while True:
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operador = input('Digite a expresão que deseja fazer +(Mais) -(Menos) /(Divisão)  *(multiplicação): ')
    numero_validos = None
    operadores_permitidos = '+-/*'
    
    numero_1_float = 0 # declarando uma variavel 
    numero_2_float = 0 # declarando uma variavel 
    try:
        numero_1_float = float(numero_1) # Verificar se o numero é float
        numero_2_float = float(numero_2) # Verificar se o numero é float
        numero_validos = True # retornar se for valido 
    except:
        numero_validos = None # retornar caso não seja valido 
    
    if numero_validos is None: # Caso não seja valido mandar digitar novamente 
        print("Digite um numero valido por favor!!!")
        continue # continuar looping
    
    if operador not in operadores_permitidos: # verificar os operadores 
        print("Digite um operador permitido")
        continue # continuar looping

    if len(operador) > 1: # verificar se digitou apenas um operador 
        print("Digite apenas um  operador")
        continue # continuar looping
    #####
    print('Resultado da sua conta, segue o resultado')
    if operador == '+':
        print(numero_1_float + numero_2_float) # Adição
    elif operador == '-':
        print(numero_1_float - numero_2_float) # Subtração
    elif operador  == '*':
        print(numero_1_float * numero_2_float) # Multiplicação
    elif operador == '/':
        print(numero_1_float / numero_2_float) # Divisão
    else:
        print('Erro novo') # Possivel erro
    #####
    sair = input('Voce quer sair? [s]im ').lower().startswith('s') # verificar se po usuario deseja continuar
    if sair is True:
        break
        print("encerrado")