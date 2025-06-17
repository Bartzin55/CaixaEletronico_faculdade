import DataBaseContas, VerificadorDeSenha, funcoesbasicas, ExcluirConta, GeradorDeCartao, time, os, locale, string, sys

locale.setlocale(locale.LC_ALL, '') # Seta a localização para a padrão do usuário

numero = string.digits
SENHADISPOSITIVO = '384969177772794' # senha para usar caso ocaixa eletronico seja bloqueado

loginfeito = False
while True:

    #Abaixo, título pra ficar bonitinho
    os.system('cls')
    print('###########################################################################################################################################################')
    print('#                                                                                                                                                         #')
    print('#                                                                CAIXA ELETRÔNICO 24 HORAS                                                                #')
    print('#                                                                                                                                                         #')
    print('###########################################################################################################################################################')
    #menu
    print('\nDigite o caractere referente ao que você deseja fazer:')
    print('\n1 - Criar conta;')
    print('2 - Entrar;')
    print('\n\n\n\n\n')
    print('10 - Desligar Caixa.')
    escolha = input('\nDigite: ')


    match escolha:
        case '1': #Criação de conta
            funcoesbasicas.line() # uma linha só pra ficar bonitinho
            print('Obrigado por escolher o nosso banco.\n')
            condicao = False

            while condicao == False:
                os.system('cls')
                funcoesbasicas.line()
                print('Preeencha os dados abaixo para criar sua conta.\n')
                nome = input('Nome completo: ').strip()
                senha = input('Senha: ')
                confirmasenha = input('Confirmação de senha: ')
                funcoesbasicas.smallline()
                
                if nome == '' or any(i in nome for i in numero): #verifica se o usuário deixou o nome em branco ou se colocou números no nome
                    cancelaroutentar = input('Atenção: Nome inválido, Pressione ENTER para tentar novamente ou digite qualquer coisa para cacncelar a operação...\n')
                    if cancelaroutentar == '':
                        os.system('cls')
                    else:
                        condicao = True
                
                else:
                    condicao = VerificadorDeSenha.verificarsenha(senha, confirmasenha) # função para verificar se a senha cumpre os requisitos mais informações no arquivo "VerificadorDeSenha"
                    if condicao == True: #função acima retorna o valor booleano "True" caso a senha inserida cumpra todos os requisitos
                        DataBaseContas.adicionarconta(nome, senha) # função para adicionar a conta com o nome e a senha na database, mais informações no arquivo "DataBaseContas" 
                        idusuario = DataBaseContas.coletarid(nome) # coleta o id que acabou de ser criado para mostrá-lo ao usuário
                        os.system('cls')
                        print('Conta criada. Você já pode acessá-la.')
                        print(f'Seu ID de usuário é: {idusuario}. Salve este número em um lugar seguro, obrigado.')
                        funcoesbasicas.line()
                        time.sleep(5)
                        print('Pressione ENTER para fazer login em sua nova conta...')
                        input()
                        condicao = True

                    else:
                        cancelaroutentar = input('\nAtenção: Sua senha não cumpre os requisitos acima, pressione ENTER para tentar novamente, ou digite qualquer coisa para cancelar a operação...\nDigite:')
                        if cancelaroutentar != '':
                            condicao = True


        case '2':
            tentativa = 5
            os.system('cls')
            funcoesbasicas.line()
            print('Bem vindo de volta.')

            while loginfeito == False: #tentativas de login
                entradaidusuario = input('\nDigite seu ID de usuário (somente números), ou digite 0 para cancelar: ')
                if entradaidusuario == '0':
                    break
                senha = input('\nDigite sua senha: ')
                try:
                    idusuario = int(entradaidusuario)
                except ValueError:
                    print('Digite somente números. Pressione ENTER para tentar novamente...')
                    funcoesbasicas.line()
                    input()
                    os.system('cls')
                    break

                condicao = DataBaseContas.verificalogin(idusuario, senha)
                
                if condicao == True:
                    os.system('cls')
                    funcoesbasicas.line()
                    print('                                                                     Login bem sucedido.')
                    funcoesbasicas.line()
                    time.sleep(3)
                    os.system('cls')
                    funcoesbasicas.line()
                    loginfeito = True

                else:
                    tentativa -= 1
                    if tentativa != 0:
                        os.system('cls')
                        funcoesbasicas.line()
                        print(f'Usuário ou senha incorretos ou não existentes. Você tem {tentativa} tentativas restantes.')#mostra a quantidade de tentativas restantes até que o programa feche
                    else:
                        senhadigitada = None
                        while senhadigitada != SENHADISPOSITIVO:
                            os.system('cls')
                            funcoesbasicas.line()
                            print()
                            print('                                             TENTATIVAS ESGOTADAS, NECESSÁRIO REINICIAR O CAIXA ELETRÔNICO.\n                                                                    CONTATE O GERENTE.')
                            print()
                            funcoesbasicas.line()
                            print('\n\n\n')
                            senhadigitada = input('Senha de reinício: ')
                            if senhadigitada == SENHADISPOSITIVO:
                                print('reiniciando o dispositivo...')
                                time.sleep(5)
                                os.system('cls')

                            else:
                                print('Senha incorreta. Tente novamente...')
                                time.sleep(3)
                        break

            #LOGADO, OPERAÇÕES COM A CONTA REAL
            tempo = funcoesbasicas.time()
            while loginfeito == True:
                os.system('cls')
                nomeusuario = DataBaseContas.coletarnome(idusuario)
                saldoatual = DataBaseContas.coletarsaldo(idusuario)

                funcoesbasicas.line()
                print(f'Bem vindo {nomeusuario}! | Login efetuado em {tempo}')
                print(f"Saldo atual: {locale.currency(saldoatual, grouping=True)}")
                print('\nEscolha o que deseja fazer.\n\n1 - Depositar valor;\n2 - Sacar valor;\n3 - Transferir valor para outra conta;\n\n4 - Consultar dados do cartão de crédito;\n5 - Criar cartão de crédito;\n\n6 - Sair da conta.\n\n7 - Excluir conta')
                escolha = input('Digite: ')

                match escolha:

                    case '1': #depositar valor
                        os.system('cls')
                        funcoesbasicas.line()
                        print('você pode digitar o valor inteiro, ou usar ponto (.) ou vírgula (,) para separar os valores decimais.')
                        entradavalor = input('Digite o valor que deseja depositar: ').replace(',', '.')
                        try:
                            valor = float(entradavalor)
                        except ValueError:
                            print('Valor inválido, tente novamente.')
                            time.sleep(4)
                            continue

                        if valor <= 0:
                            print('Valor inválido, tente novamente.')
                            time.sleep(4)

                        else:
                            DataBaseContas.depositarvalor(idusuario, valor)
                            novosaldo = DataBaseContas.coletarsaldo(idusuario)
                            print(f'{locale.currency(valor, grouping=True)} depositado na sua conta com sucesso, seu saldo agora é de {locale.currency(novosaldo, grouping=True)}')
                            print('\nPressione ENTER para voltar...')
                            input()
                            os.system('cls')   

                    case '2': #sacar valor
                        os.system('cls')
                        funcoesbasicas.line()
                        saldo = DataBaseContas.coletarsaldo(idusuario)
                        entradasaldorequerido = input('Digite o valor que você deseja sacar: ').replace(',', '.')
                        try:
                            saldorequerido = float(entradasaldorequerido)
                        except ValueError:
                            os.system('cls')
                            funcoesbasicas.line()
                            print('Valor inválido, digite apenas números.')
                            time.sleep(4)
                            continue

                        if saldo < saldorequerido: #verifica se o valor digitado pelo usuario é menor do que ele tem na conta
                            os.system('cls')
                            funcoesbasicas.line()
                            print('Saldo insuficiente, operação cancelada...')
                            time.sleep(4)
                        
                        else:
                            print(f'Sacando {locale.currency(saldorequerido, grouping=True)}')
                            DataBaseContas.sacarvalor(idusuario, saldorequerido)
                            time.sleep(4)


                    case '3':
                        os.system('cls')
                        funcoesbasicas.line()
                        entradaiddestino = input('Digite o ID do usuário que você deseja realizar a transferência, digite "0" para cancelar a operação: ')
                        try:
                            iddestino = int(entradaiddestino)
                        except ValueError:
                            print('Atenção, digite apenas números.')
                            time.sleep(4)
                            continue

                        if iddestino == 0:
                            os.system('cls')
                            funcoesbasicas.line()
                            print('Operação cancelada...')
                            time.sleep(4)


                        elif iddestino == idusuario:
                            os.system('cls')
                            funcoesbasicas.line()
                            print('Você digitou seu próprio ID. Operação cancelada.')
                            time.sleep(4)
                        
                        else:
                            entradavalor = input('Digite o valor que você deseja enviar ao usuário: ')
                            try:
                                valor = float(entradavalor)
                            except:
                                print('\nAtenção, Digite apenas números.')
                                time.sleep(4)
                                continue

                            if valor < -1:
                                funcoesbasicas.line()
                                print('Entrada inválida, operação cancelada.')
                                time.sleep(4)

                            elif valor > saldoatual:
                                os.system('cls')
                                funcoesbasicas.line()
                                print('Saldo insuficiente para realizar transferência, operação cancelada...')
                                time.sleep(4)
                            
                            else:
                                resultado = DataBaseContas.verifica_id_existe(iddestino)

                                if resultado == True:
                                    nomedestino = DataBaseContas.coletarnome(iddestino)
                                    funcoesbasicas.line()
                                    print(f'Transfernido {locale.currency(valor, grouping=True)} para {nomedestino}, ID {iddestino}...')
                                    DataBaseContas.depositarvalor(iddestino, valor)
                                    DataBaseContas.sacarvalor(idusuario, valor)
                                    time.sleep(4)

                                else:
                                    os.system('cls')
                                    funcoesbasicas.line()
                                    print('Usuário não encontrado, Operação cancelada.')
                                    time.sleep(4)
                        continue
                    
                    case '4':
                        entrada = None

                        os.system('cls')
                        numerocartao, data_validade, cvv = DataBaseContas.coletardadoscartao(idusuario)
                        funcoesbasicas.line()
                        if numerocartao == None:
                            print('Você não possui um Cartão de Crédito, você pode requisitar um nesse Caixa.')
                            time.sleep(5)
                        
                        else:
                            cartaoformatado = f'{numerocartao[:4]} {numerocartao[4:8]} {numerocartao[8:12]} {numerocartao[12:]}'
                            print('Abaixo os dados do seu Cartão de Crédito.\n')
                            print()
                            print('#####################################################')
                            print('#                                                   #')
                            print(f'#      Número do cartão: {cartaoformatado}        #')
                            print(f'#      Data de validade: {data_validade}                    #')
                            print(f'#      CVV: {cvv}                                     #')
                            print('#                                                   #')
                            print('#####################################################')


                            while entrada != '':
                                entrada = input('\nPressione ENTER para continuar...')


                    case '5':
                        os.system('cls')
                        numerocartao, data_validade, cvv = DataBaseContas.coletardadoscartao(idusuario)
                        funcoesbasicas.line()
                        if numerocartao != None:
                            print('Você já possui um Cartão de Crédito, você pode consultar os dados dele neste Caixa.')
                            time.sleep(4)

                        else:
                            senhacartao = input('Digite a senha que você deseja (numérica de 4 dígitos), ou digite 0 para cancelar a operação: ')
                            if senhacartao == '0':
                                funcoesbasicas.line()
                                print('Operação cancelada...')

                            else:
                                condicao = VerificadorDeSenha.verificarsenhacartao(senhacartao)

                                if condicao == False:
                                    print('Sua senha não cumpre os requisitos acima, tente novamente')
                                    time.sleep(5)
                                    os.system('cls')
                            
                                else:
                                    numerocartao, validade, cvv = GeradorDeCartao.gerarcartao(idusuario, senhacartao)
                                    DataBaseContas.inserircartao(numerocartao, validade, cvv, senhacartao, idusuario)
                                    print('Cartão criado com sucesso, abaixo as informações dele.')
                                    cartaoformatado = f'{numerocartao[:4]} {numerocartao[4:8]} {numerocartao[8:12]} {numerocartao[12:]}'
                                    print(f'Número do cartão: {cartaoformatado};\nValidade: {validade};\nCVV: {cvv}.')
                                    input('Pressione ENTER para continuar...\n')
                        continue

                    case '6':
                        os.system('cls')
                        funcoesbasicas.line()
                        print('                                                                            Saindo...')
                        funcoesbasicas.line()
                        time.sleep(3)
                        os.system('cls')
                        loginfeito = False

                    case '7':
                        os.system('cls')
                        funcoesbasicas.line()
                        print('Para excluir a sua conta, você deve inserir os dados abaixo e deve inserir o ID de uma conta para enviar todo o seu saldo atual, caso você tenha algum saldo.')
                        entradaidusuario = input('Digite seu ID de usuário: ')
                        
                        try:
                            idusuarioexclusao = int(entradaidusuario)
                        except ValueError:
                            print('ID inválido, operação cancelada.')
                            time.sleep(4)
                            os.system('cls')
                            continue

                        senha = input('Digite sua senha: ')
                        confirmasenha  = input('Confirme sua senha: ')
                        condicao = ExcluirConta.excluirconta(idusuarioexclusao, senha, confirmasenha)
                        
                        if condicao == False:
                            print('ID ou senha incorretos ou confirmação incorreta; operação cancelada.')
                            funcoesbasicas.line()
                            time.sleep(4)
                            os.system('cls')
                        
                        else:
                            funcoesbasicas.line()
                            print(f"Seu saldo atual: {locale.currency(saldoatual, grouping=True)}")
                            if saldoatual == 0: #se o usuário tiver algum dinheiro na cconta, antes de excluir ele será obrigado a transferir o dinheiro para outra conta. Caso ele não tenha dinheiro, ele poderá excluir a conta diretamente.
                                funcoesbasicas.line()
                                print('                                                 <<CONFIRMAÇÃO FINAL>>')
                                confirmacaofinal = input('Digite "EXCLUIR CONTA" para confirmar a exclusão, digite qualquer outra coisa para cancelar.\nDigite: ')
                                condicao = ExcluirConta.confirmacaofinal(confirmacaofinal) # função que verifica se o usuário digitou exatamente EXCLUIR CONTA. Pormotivos de segurança, nem mesmo se o usuário digitar excluir conta com minúsculo , será aceito.
                                if condicao == False:
                                    print('Operação cancelada.')
                                    funcoesbasicas.line()
                                    time.sleep(4)
                                    os.system('cls')
                                
                                else:
                                    DataBaseContas.deletar_usuario(idusuario) #função que finalmente, realmente exclui a conta, entrando na DataBase e excluindo a linha com as informações
                                    print('Sua conta foi excluída e o saldo foi transferido para a conta que você requisitou, você será deslogado em alguns segundos...')
                                    time.sleep(10)
                                    os.system('cls')
                                    condicao = False
                                    loginfeito = False #desloga o usuário mudando a condição do while
                            
                            else:
                                funcoesbasicas.line()
                                iddestino = input('Digite o ID de uma conta para transferir seu saldo bancário antes da exclusão: ')
                                resposta = ExcluirConta.verificaiddestino(iddestino, idusuario)
                                
                                if resposta == 1:
                                    print('O ID digitado não existe, operação cancelada.')
                                    funcoesbasicas.line()
                                    time.sleep(4)
                                    os.system('cls')
                                
                                elif resposta == 2:
                                    print('O ID digitado é o mesmo que o ID de origem, operação cancelada.')
                                    funcoesbasicas.line()
                                    time.sleep(4)
                                    os.system('cls')

                                else:
                                    confirmacao = input(f'Você vai transferir todo o saldo para {resposta}, ID {iddestino}, por favor  confirme com "SIM" ou digite qualquer outra coisa para cancelar: ')
                                    condicao = ExcluirConta.confirmacaotransferencia(confirmacao)
                                    if condicao == False:
                                        print('Operação cancelada.')
                                        time.sleep(4)
                                        os.system('cls')
                                    
                                    else:
                                        os.system('cls')
                                        funcoesbasicas.line()
                                        print('                                                 <<CONFIRMAÇÃO FINAL>>')
                                        confirmacaofinal = input('Digite "EXCLUIR CONTA" para confirmar a exclusão, digite qualquer outra coisa para cancelar: ')
                                        condicao = ExcluirConta.confirmacaofinal(confirmacaofinal)
                                        if condicao == False:
                                            print('Operação cancelada.')
                                            funcoesbasicas.line()
                                            time.sleep(4)
                                            os.system('cls')
                                        else:
                                            DataBaseContas.deletar_usuario(idusuario)
                                            print('Sua conta foi excluída e o saldo foi transferido para a conta que você requisitou, você será deslogado em alguns segundos...')
                                            time.sleep(10)
                                            os.system('cls')
                                            loginfeito = False
                                            condicao = False
                        continue

                    case _:
                        funcoesbasicas.line()
                        print('Escolha inválida, tente novamente.')
                        funcoesbasicas.line()
                        time.sleep(3)
                        os.system('cls')

        case '10':
            os.system('cls')
            funcoesbasicas.line()
            senhadigitada = input('Digite a senha admin: ')
            if senhadigitada == SENHADISPOSITIVO:
                print('Desligando...')
                time.sleep(2)

                DataBaseContas.fechar_conexão()
                sys.exit()
                
            else:
                print('Senha incorreta.')
                time.sleep(4)
                continue

        case _:
            print('\nEscolha inválida, tente novamente...')
            funcoesbasicas.line()
            time.sleep(3)
            continue
    continue