peso = float(input('Digite o peso da pessoa: '))
altura = float(input('Digite a altura da pessoa em metros:'))

imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f}, você está com o peso ideal. '.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}, você está com sobrepeso, procure acompanhamento médico. '.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f}, você está com obesidade, procure acompanhamento médico.'.format(imc))
elif imc >=40:
    print('Seu IMC é {:.2f}, você está com obesidade mórbida, procure ajuda médica'.format(imc))