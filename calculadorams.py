# REGRA GERAL

from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Coleta de informações do usuário
nome_completo = input("Digite o seu nome completo: ")
sexo = input("Digite o seu sexo (F/M): ")
data_nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
data_entrada_servico_publico = input("Digite a sua data de entrada no serviço público (dd/mm/aaaa): ")
averbacao = input("Averbar (incluir) outros períodos de contribuição.\n(Deixe em branco para não incluir outros períodos.)Tempo em anos:")
import re

while True:
    email = input("Digite seu email: ")

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("\n\033[1;30;47mAs informações descritas aqui são apenas orientativas.\033[m")
        break
    else:
        print("Email inválido! Por favor, digite um email válido.")

with open('usuarios.txt', 'a') as arquivo:
    arquivo.write(f"Nome: {nome_completo}\nE-mail: {email}\n")

# Conversão das datas
data_nascimento = date.fromisoformat(data_nascimento.split("/")[2] + "-" + data_nascimento.split("/")[1] + "-" + data_nascimento.split("/")[0])
data_entrada_servico_publico = date.fromisoformat(data_entrada_servico_publico.split("/")[2] + "-" + data_entrada_servico_publico.split("/")[1] + "-" + data_entrada_servico_publico.split("/")[0])
data_atual = date.today()

# Cálculo da idade e do tempo de contribuição
idade = relativedelta(data_atual, data_nascimento).years
tempo_contribuicao = relativedelta(data_atual, data_entrada_servico_publico).years
if averbacao:
    averbacao = int(averbacao)
else:
    averbacao = 0

tempo_contribuicao += averbacao

# Verificação de direito à aposentadoria
if sexo.upper() == "F":
    idade_minima = 62
    tempo_contribuicao_minimo = 25
else:
    idade_minima = 65
    tempo_contribuicao_minimo = 25

tem_direito_por_idade = idade >= idade_minima
tem_direito_por_tempo_servico = tempo_contribuicao >= tempo_contribuicao_minimo
tem_direito_por_idade_e_tempo_servico = tem_direito_por_idade and tem_direito_por_tempo_servico

if tem_direito_por_idade_e_tempo_servico:
    print("\n\033[0;37;46mREGRA GERAL\033[m\n\033[1;30;47m\n{},\n\033[m Você tem direito a se aposentar segundo a REGRA GERAL da EC 103/19 em \033[0;30;43m2023.\033[m".format(nome_completo.split()[0]))
else:
    data_aposentadoria = data_atual + relativedelta(years=idade_minima - idade or tempo_contribuicao_minimo - tempo_contribuicao, months=0, days=0)
    print("\n\033[0;37;46mREGRA GERAL\033[m\n\033[1;30;47m{},\npela REGRA GERAL da EC 103/19\nA data prevista para você se aposentar é\033[0;30;43m {}.\033[m".format(nome_completo.split()[0], data_aposentadoria.strftime("%d/%m/%Y")))

# REGRA DOS PONTOS

# Convertendo as datas para o tipo datetime
data_nasc = datetime.strptime(data_nascimento.strftime("%d/%m/%Y"), "%d/%m/%Y")
data_entra_servico = datetime.strptime(data_entrada_servico_publico.strftime("%d/%m/%Y"), "%d/%m/%Y")
data_atual = datetime.now()

# calculando o total de pontos
total_pontos = (data_atual - data_nasc).days // 365 + (data_atual - data_entra_servico).days // 365
if averbacao:
   total_pontos += int(averbacao)

print(f"\033[0;37;46m\nREGRA DE TRANSIÇÃO POR PONTOS.\033[m\n\033[1;30;47mTotal de pontos: {total_pontos}\033[m")
if sexo.upper() == "M":
    if total_pontos <= 84:
        print("\033[0;30;47mVocê não tem direito a regra de transição por pontos.\033[m")
    elif total_pontos >= 100:
        print("\033[0;30;47mVocê já tem direito a se aposentar pela regra de transição por pontos.\033[m")
    elif total_pontos == 99:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2024')}.\033[m")
    elif total_pontos == 98:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2025')}.\033[m")
    elif total_pontos == 97:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2026')}.\033[m")
    elif total_pontos == 96:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2027')}.\033[m")
    elif total_pontos == 95:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2028')}.\033[m")
    elif total_pontos == 93 or total_pontos == 94:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2029')}.\033[m")
    elif total_pontos == 91 or total_pontos == 92:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2030')}.\033[m")
    elif total_pontos == 89 or total_pontos == 90:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2031')}.\033[m")
    elif total_pontos == 87 or total_pontos == 88:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2032')}.\033[m")
    elif total_pontos == 85 or total_pontos == 86:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2033')}.\033[m")
if sexo.upper() == "F":
    if total_pontos <= 79:
        print("\033[0;30;47mVocê não tem direito a se aposentar pela regra de transição por pontos.\033[m")
    elif total_pontos >= 90:
        print("\033[0;30;47mVocê já tem direito a se aposentar pela regra de transição por pontos.\033[m")
    elif total_pontos == 89:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2024')}.\033[m")
    elif total_pontos == 88:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2025')}.\033[m")
    elif total_pontos == 87:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2026')}.\033[m")
    elif total_pontos == 86:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2027')}.\033[m")
    elif total_pontos == 85:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2028')}.\033[m")
    elif total_pontos == 84:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2029')}.\033[m")
    elif total_pontos == 83:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2030')}.\033[m")
    elif total_pontos == 82:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2031')}.\033[m")
    elif total_pontos == 81:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2032')}.\033[m")

    elif total_pontos == 80:
        print(f"\033[1;30;47mPela regra de transição por pontos, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/2033')}.\033[m")

# REGRA DO PEDÁGIO 100%

# Cálculo da idade e do tempo de contribuição

idade = relativedelta(data_atual, data_nascimento).years
tempo_contribuicao = relativedelta(data_atual, data_entrada_servico_publico).years

# Verificação do direito à aposentadoria
if sexo.upper() == "M":
    idade_minima = 60
    tempo_contribuicao_minimo = 35
else:
    idade_minima = 57
    tempo_contribuicao_minimo = 30

if averbacao:
    averbacao = int(averbacao)
else:
    averbacao = 0

tempo_contribuicao += averbacao

if idade >= idade_minima and tempo_contribuicao >= tempo_contribuicao_minimo:
    print("\033[0;37;46m\nREGRA DE PEDÁGIO 100%\033[m\n\033[1;30;47m\nVocê já tem direito a aposentadoria pela regra de transição de pedágio em \033[1;30;43m2023.\033[m\033[1;30;39m\n\nPara maiores informações contate nosso departamento jurídico\033[m")
else:
    anos_restantes = max(idade_minima - idade, 0) + max(tempo_contribuicao_minimo - tempo_contribuicao, 0)
    data_aposentadoria = data_atual + relativedelta(days=anos_restantes*365*2)
   
    print(f"\033[0;37;46m\nREGRA DE PEDÁGIO 100%\033[m\n\033[1;30;47mPela regra de transição por pedágio 100%, você terá direito a aposentadoria em\033[1;30;43m {data_aposentadoria.strftime('%d/%m/%Y')}.\033[1;30;39m\n\nPara maiores informações contate nosso departamento jurídico\033[m")