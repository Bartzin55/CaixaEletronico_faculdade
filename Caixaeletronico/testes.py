import DataBaseContas

id_usuario = '1'
cartao, data, cvv = DataBaseContas.coletardadocartao(id_usuario)

print(cartao, data, cvv)