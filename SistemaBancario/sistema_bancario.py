import os

def menu():
   return f"""
   {'='*10} Menu {'='*10}

      [1] Deposito
      [2] saque
      [3] extrato
      [4] Sair

   {'='*26}
   """

saldo = 0
limite = 500 #limite de valor por saque
numero_saques = 0
LIMITE_SAQUES = 3 #limites de saques diarios
opcao = 0 #para a escolha das opções

while opcao != 4:
   opcao = int(input(menu())) #chama a função e disponibiliza ao usuario escolher a opçao
   if opcao == 1:
      valor = float(input('Digite o valor a ser Depositado: R$'))
      if valor == 0:
        print('Não pode ser depositado tal valor!')
        input()
        os.system('cls')
      else:
        saldo+= valor
        print(f'Saldo atual é de R${saldo:.2f}')
        input()
        os.system('cls')
   elif opcao == 2:
      valor = float(input('Digite o valor a ser sacado: R$'))
      if valor > limite or numero_saques == LIMITE_SAQUES:
        if valor > limite and numero_saques < LIMITE_SAQUES:
            print(f'Valor máximo a ser sacado é de R$500,00 ! \nSaldo Atual de {saldo:.2f}')
            input()
            os.system('cls')
        elif valor < limite and numero_saques >= LIMITE_SAQUES:
            print(f'O número máximo de saques por dia é 3')
            input()
            os.system('cls')
        else:
            print('O Limite diario é de 3 Saque de no máximo R$500.00! \nSaldo Atual de {saldo:.2f}')
            input()
            os.system('cls')
      elif valor <= saldo:
        saldo-= valor
        numero_saques+= 1
        print(f'Saque no valor de R${valor:.2f} bem sucessido! \nSaldo Atual R${saldo:.2f} \nNúmero de Saques feitos {numero_saques}')
        input()
        os.system('cls')
      else:
        print(f'Saldo insuficiente! \nSaldo atual R${saldo:.2f}')
        input()
        os.system('cls')
   elif opcao == 3:
        print(f'O Saldo atual é de R${saldo:.2f}')
        input()
        os.system('cls')
   elif opcao == 4:
        print('Fim da sessão!')
        input()
        os.system('cls')
        break
   else:
        print('ERRO!')
        input()
        os.system('cls')



