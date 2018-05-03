# Verificação do nome Silva no nome #

nome = str(input('\nDigite o seu nome completo: ')).upper().split()

if 'SILVA' in nome:
    print('Voce tem "Silva" no nome.')
else:
    print('Voce não tem "Silva" no nome.')

