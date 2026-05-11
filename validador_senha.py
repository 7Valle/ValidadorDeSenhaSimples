#  Projeto: Validador de senha simples
#  Regras:
#  - A senha deve ter no mínimo 8 caracteres.
#  - A senha não pode ser 12345678
#  O resultado esperado é dizer se a senha é valida ou não

password = input('Dgite uma senha: ')

if len(password) >= 8 and password != '12345678':
    print('\nSenha válida!')
elif len(password) < 8:
    print('Senha inválida, menos de 8 caracteres.')
elif password == '12345678':
    print('Senha inválida, é uma sequência')