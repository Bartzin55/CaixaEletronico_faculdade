import string

def verificarsenha(senha, confirmasenha): #verificado de senha do banco
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numero = string.digits
    caracteresespeciais = '"!@#$%&*()-_=+/[]{}?:.,'
    erro = 0

    if not any(i in senha for i in maiusculas):
        print('Ao menos um letra maiúscula;')
        erro += 1
    
    if not any(i in senha for i in minusculas):
        print('Ao menos uma letra minúscula;')
        erro += 1
    
    if not any(i in senha for i in numero):
        print('Ao menos um numeral;')
        erro += 1
    
    if not any(i in senha for i in caracteresespeciais):
        print(f'Ao menos um dos seguintes caracteres especiais dentro dos parênteses: ( {caracteresespeciais} ) ;')
        erro += 1
    
    if len(senha) < 8:
        print('Mínimo de 8 dígitos.')
        erro += 1
    
    if confirmasenha != senha:
        print('A senha e a confirmação serem iguais.')
        erro += 1
    
    if erro == 0:
        return True
    else:
        return False
    
def verificarsenhacartao(senhacartao): #verificando senah do cartão
    erro = 0
    if len(senhacartao) != 4:
        print('Ter exatamente 4 dígitos;')
        erro += 1
    if not senhacartao.isdigit():
        print('Ser somente numérica;')
        erro += 1
    if erro != 0:
        return False
    else:
        return True