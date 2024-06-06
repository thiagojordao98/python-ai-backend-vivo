# Sistema Bancário 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Badge License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

Este é um projeto de um sistema bancário simples desenvolvido como desafio durante o Bootcamp da Vivo Python AI Backend Developer. Ele permite ao usuário realizar depósitos, saques, visualizar o extrato e salvar o extrato em um arquivo de texto. O sistema inclui restrições para depósitos e saques, como limites diários e máximos de retirada.

## Funcionalidades

1. **Depósito**: Permite ao usuário depositar dinheiro na conta.
2. **Saque**: Permite ao usuário sacar dinheiro da conta com limite de saques diários e limite máximo por saque.
3. **Extrato**: Exibe o histórico de transações e o saldo atual.
4. **Salvar Extrato**: Salva o extrato em um arquivo de texto.
5. **Sair**: Encerra o sistema.

## Como usar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/thiagojordao98/challenge-bank-system.git
   cd challenge-bank-system
   ```

2. **Execute o script Python**:

   ```bash
   python bank-system.py
   ```

3. **Siga as instruções no menu**:

   O sistema consiste de um menu com as seguintes opções:

   ```
   Escolha uma opção:
   1 - Depósito
   2 - Saque
   3 - Extrato
   4 - Salvar Extrato
   5 - Sair
   ```

   - Digite o número correspondente à ação que deseja realizar e pressione Enter.
   - Siga as instruções para cada opção.

## Exemplo de Uso

1. **Depósito**: Digite `1` e informe o valor do depósito. O valor será adicionado ao saldo e registrado no extrato.

2. **Saque**: Digite `2` e informe o valor do saque. O sistema verificará as regras e, se tudo estiver correto, o valor será subtraído do saldo e registrado no extrato.

3. **Extrato**: Digite `3` para visualizar todas as transações realizadas e o saldo atual.

4. **Salvar Extrato**: Digite `4` para salvar o extrato em um arquivo `extrato.txt`.

5. **Sair**: Digite `5` para encerrar o sistema.

## Estrutura do Código

O código é composto por uma classe `Banco` e uma função principal `main`.

- **Classe Banco**:
  - `__init__`: Inicializa o saldo, extrato, limite de saques e contador de saques realizados.
  - `deposito`: Realiza depósitos na conta, verificando se o valor é positivo.
  - `saque`: Realiza saques, verificando limites e saldo disponível.
  - `mostrar_extrato`: Exibe o extrato das transações e o saldo atual.
  - `salvar_extrato`: Salva o extrato em um arquivo de texto.

- **Função main**: Gerencia o loop principal do programa, exibindo o menu e chamando os métodos apropriados da classe `Banco` com base na escolha do usuário.

## Funções adicionais
- [x] Salvar Extrato
- [x] Salvar data das operações
