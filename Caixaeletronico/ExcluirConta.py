import locale, DataBaseContas, time, os

def excluirconta(idusuario, senha, confirmasenha):
        if senha != confirmasenha:
            return False

        condicao = DataBaseContas.verificalogin(idusuario, senha)
        if condicao == False:
            return False

def verificaiddestino(iddestino, idusuario):
    condicao = DataBaseContas.verifica_id_existe(iddestino)
    if condicao == False:
        return 1 #erro para se o ID não existe

    if iddestino == idusuario:
        return 2 #erro para se digita o próprio id
    
    else:
        nomedestino = DataBaseContas.coletarnome(iddestino)
        return nomedestino

def confirmacaotransferencia(confirmacao):
    if confirmacao != 'SIM':
        return False
    else:
        return True


def confirmacaofinal(confirmacaofinal):
    if confirmacaofinal != 'EXCLUIR CONTA':
        return False
    else:
         return True

# DataBaseContas.depositarvalor(iddestino, saldoatual)
# DataBaseContas.sacarvalor(idusuario, saldoatual)
# DataBaseContas.deletar_usuario(idusuario)
# print('Sua conta foi excluída e o saldo foi transferido para a conta que você requisitou, você será deslogado em 10 ssegundos...')
