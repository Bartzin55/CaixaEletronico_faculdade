# Caixa Eletrônico em Python

## Descrição

Este projeto é uma simulação de um caixa eletrônico (ATM) desenvolvido em Python para o trabalho da A3 (trabalho de faculdade). O programa permite a criação de contas de usuário, login com validação de senha, operações de saque, depósito e transferência, além de implementar um sistema de bloqueio por tentativas excessivas de senha incorreta.

A aplicação também simula funcionalidades típicas de um caixa eletrônico físico, como a geração de número de cartão, CVV, data de validade e uma senha específica para desbloqueio do terminal (representando o acesso de um gerente).

## Funcionalidades

- Criação de contas com nome, senha e cartão.
- Login com validação de ID e senha.
- Consultas de saldo.
- Saques e depósitos.
- Transferências entre contas.
- Bloqueio automático do terminal após múltiplas tentativas de senha incorreta, com desbloqueio apenas com senha master do gerente do banco.
- Implementação de banco de dados em SQLite.

## Requisitos

- Python 3.x

## Como Executar

1. Faça o download de todos os arquivos do projeto e mantenha-os na mesma pasta.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal com o comando:

```bash
python main.py
```

## Estrutura do Projeto

```
CaixaEletronico/
├── DataBaseContas.py
├── FuncoesBasicas.py
├── GeradorCartao.py
├── Login.py
├── VerificadorDeSenha.py
├── main.py
└── contas.sqlite3 (gerado automaticamente após a primeira execução)
```

## Observações

Este projeto tem fins puramente educacionais. Não possui implementações de segurança para uso real em produção.

## Autor

Luiz Otávio Bartilheiro de Sousa / Rafaela de Souza Vasconcelos – Projeto de faculdade em Python / A3 - UNA / Programação de Soluções Computacionais.
