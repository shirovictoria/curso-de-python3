"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida 
"""
peso = float(input('Digite qual é o seu peso: '))
altura = int(input('Digite qual é a sua altura: '))
imc = peso / altura
if imc < 18.5:
    print(f'O seu IMC é de {imc:.2f}, você tá abaixo do peso ideal!')
elif imc >=18.5 and imc <=25:
    print(f'O seu IMC é de {imc:.2f}, você tá com o peso ideal!')
elif imc >= 25 and imc <=30:
    print(f'O seu IMC é de {imc:.2f}, você tá com sobrepeso! ')
elif imc >= 30 and imc <=40:
    print(f'O seu IMC é de {imc:.2f}, você tá com obesidade!')
else:
    print(f'O seu IMC é de {imc:.2f}, você tá com obesidade morbida!')
