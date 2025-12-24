# preco = [50,150,200,300,80]

# for item in preco:
#     if (item > 150):
#         item2 = item * 0.10
#         item3 = item - item2
#         print(f'''preco do produto é: {item}
#                 com o desconto fica :{item3} ''')
#     else:
#         print(f'Os itens a seguir mantiveram seu preço:{item}')


#Sensor de Temperatura com for:

# temps = [25, 38, 42, 30, 45, 22]

# for i in temps:
#     if (i > 40):
#         print(f'Alerta:{i}ºC - Superaquecimento')
#     elif (i>= 30 and i<=40):
#         print(f'Sistema Ok:{i}ºC - Estável.')
#     else:
#         print(f'{i}ºC - Fria')    


#Acumulador com for :
# vendas = [100.50,200.00, 50.25,300.75]
# total = 0

# for i in vendas:
#  total += i
# print(total)


#Fechamento de Caixa:
# vendas = [100,-20,50,-10,300,-5]
# s_v = 0 
# s_e = 0

# for i in vendas:
#     if (i > 0):
#         s_v += i
#     else:
#         s_e += i 
# total = s_v + s_e
# print(f'Vendas concluidas = {s_v}')
# print(f'Vendas estornadas = {s_e}')
# print(f'Faturamento dia:{total}')


#localizador de itens:

# alunos = [1020,5040,3020,9080,1020,4050]
# ocor=0 

# for i in alunos:
#     if(i == 1020):
#         ocor += 1
# print(f'O aluno 1020 teve {ocor} ocorrencias.')

#Filtro de Acesso 
# age = [15,22,18,14,30,12,19]
# aut = []
# for i in age:
#     if ( i >= 18):
#         aut.append(i)
# print (aut)

#maior nota
n = [7.5,9.2,6.0,10.0,8.5]
mn = [0]

for i in n:
    if (mn < i):
        mn = i
print(mn)
