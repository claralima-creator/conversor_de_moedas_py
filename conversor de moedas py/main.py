#pedindo valor
valor_bruto = input(("Digite o valor bruto para obter a conversão:"))

valor_bruto = valor_bruto.replace(',', '.')

valor_bruto = float(valor_bruto)

#formataca do dinheiro
print(f"R${valor_bruto:_.2f}".replace('.',',').replace('_','.'))

finalidade = input("Escolha para qual finalidade voçê deseja: Conta própia ou Investimento?").lower()

while finalidade not in ['conta propia', 'investimento']:
    finalidade = input('Opção inválida! Digite conta propia ou investimento:').lower()

if finalidade == 'conta propia':
    iof = valor_bruto * 0.035
    print(iof)
else:
    iof = valor_bruto * 0.011
    print(iof)

valor_liquido = (valor_bruto - iof)
print(valor_liquido)

moeda = input("Escolha qual a moeda deseja: USD ou EUR?").upper()

while moeda not in ['USD', 'EUR']:
    moeda = input('Opção inválida! Digite USD ou EUR').upper()

if moeda == 'USD':
    cotacao_comercial = 5.18
else:
    cotacao_comercial = 5.88

#APLICANDO SPREAD
if valor_bruto <= 1000:
   cotacao_cliente = cotacao_comercial * 1.04

elif valor_bruto >= 1000 and valor_bruto <= 5000:
   cotacao_cliente = cotacao_comercial * 1.03

else:
   cotacao_cliente = cotacao_comercial * 1.02

valor_convertido = valor_liquido / cotacao_cliente
print(valor_convertido)

print(f'[{"Conversão de moedas":=^38}]')

print(f'[{"Valor Bruto:":<20}R${valor_bruto:>15.2f}]')

print(f'[{"Tipo de finalidade:":<20}{finalidade:>17}]')

print(f'[{"Tipo de moeda:":<20}{moeda:>17}]')

print(f'[{"Valor Líquido:":<20}R${valor_liquido:>17.2f}]')

print(f'[{"Valor convertido:":<20}{moeda} {valor_convertido:>12.2f}]'.replace('.', ','))