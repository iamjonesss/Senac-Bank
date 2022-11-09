#ALGORITMO FEITO POR JOÃO SOUZA

#Importações
import os
from time import sleep


class SenacBank():
    def __init__(self):
        self.titular = ''
        self.numero = ''
        self.saldo = 0


    def Opcoes(self):
        while True:
            os.system('cls')
            print('+-------------------- ESCOLHA UMA OPERAÇÃO --------------------+')
            print(' 1- Criar conta; \n 2- Mostrar dados da conta; \n 3- Depositar; \n 4- Sacar; \n 0- Encerrar; \n ')
            
            escolha = input('Digite a enumeração que deseja: ')
            
            if (escolha == '1'):
                usuario = input('Digite o nome do Titular: ')
                senha = int(input('Digite o número de identificação de três dígitos: '))
                deposito = float(input('Digite um depósito inicial: '))
                self.titular = usuario
                self.numero = senha
                self.saldo = deposito
                
                print('Finalizando cadastro...')
                sleep(3)
                print('Cadastro finalizado!')
                sleep(2)
            
            elif (escolha == '2'):
                
                if (self.titular == '' and self.numero == ''):
                    print('Nenhum cliente cadastrado.')
                    sleep(3)
                
                else:
                    print('+--------------------------------------------------+')
                    print('-> DADOS DA CONTA')
                    print(f'| NOME: {self.titular} \n| NÚMERO DA CONTA: {self.numero}\n| SALDO: {self.saldo}')
                    sleep(3)
                
            elif (escolha == '3'):
                deposito = float(input('Digite quanto quer depositar: '))
                self.saldo = self.saldo + deposito
                
                print('Verificando saldo atual...')
                sleep(2)
                print('Depositando...')
                sleep(1)
                print(f'Depósito feito com sucesso!\n | Saldo atual: {self.saldo}')
                sleep(5)
                
            elif (escolha == '4'):
                saque = float(input('Digite o valor que deseja retirar: '))
                
                if (saque > self.saldo):
                    print('Saldo insuficiente, por favor tentar novamente\n | Saldo atual: {self.saldo}')
                    sleep(5)
                
                else:
                    self.saldo = self.saldo - saque
                    print('Processando dados...')
                    sleep(2)
                    print('Finalizando processo...')
                    sleep(3)
                    print(f'\n| Saldo atual: {self.saldo}')
                    sleep(5)
                
            elif (escolha == '0'):
                break
            
            else:
                print('Hm, não encontramos função para o que foi selecionado. :(')
                sleep(5)
                
                
banco = SenacBank()
banco.Opcoes()