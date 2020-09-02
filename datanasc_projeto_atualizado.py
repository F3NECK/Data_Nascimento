#################################################################
#                     datanasc_projeto atualizado               #
#                data da ultima modificação: 02/09/20           #
#                         ass: Felipe Magno                     #
#################################################################


#esse arquivo foi inspirado na aula de analise e programação do prof Neo
#porem contendo umas alteraçôes pra deixar o projeto mais dinamico para interação

#entrada

name= input('qual é o seu nome: ')                      #<- com a varivavel eu posso guardar uma informação pra poder puxar ela em alguma ocasiao necessaria
datanasc = int(input('ensira o nome que vc nasceu: '))  #<- input tipo inteiro para que possa fazer a subtração na hora do processamento
ano = int(input('ano que estamos: '))                   #o mesmo ocorre aqui.

#processamento

#aqui é onde a maquina vai "interpretar" oque vc colocou na entrada fazendo os calculos e etc.

idade= ano - datanasc  #<- com os dados da entrada a maquina vai processar e fazer as contas para dar o resultado
dia= idade * 365       #<- aqui pego um dado do precessamento e regato ele fazendo uma operação matematica de multiplicação
hora = dia * 24        #<- horas vividas
minuto = hora * 60     #<- minutos vividos

#saida

#aqui a maquina mostrará na tela os resultados do procesamentos por meio de uma impressao da concatenação feita no programa

print('a idade de %s' %name,"é %s" %idade, "e seus dias vividos são %s" %dia)  #<-- com o comando print eu ordeno para a maquinar "imprimir"
                                                                               # os dados concatenados

