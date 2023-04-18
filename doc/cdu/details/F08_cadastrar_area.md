# **Projeto StarScience**

## Especificação do caso de uso - Cadastrar Área - F08
### Histórico da Revisão 

|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 04/12/2022 | 1.00 | Primeira versão | Lucas Nithael |

### 1. Resumo 

Este caso de uso é responsável por Inserção, persistência e integridade das áreas

### 2. Atores 

Administradores

### 3. Pré-condições

O usuário deve estar cadastrado e ser um membro administrador da plataforma

### 4.Pós-condições

Quando inserida ou alterada as áreas devem ser vistas pelos os usuários comuns, bem como não vista quando removida

### 5. Fluxos de evento

#### 5.1. Fluxo Principal 
|  Ator  | Sistema |
|:-------|:------- |
|1.  Aciona a opção de inserir uma nova área.|
||2.  Apresenta uma caixa para o referido nome da área||
|3. Preenche a caixa com nome||
||4.  Grava o nome dentro da caixa||
|5. Cadastra||
||6.  Mostra a área na lista de áreas cadastradas||
|7. Visualiza uma de configuração em cada área e clica||
||8. Apresenta um menu com as opções para alterações e remoção||


#### 5.2. Fluxo de exceção
     a)Caso tentativa de cadastro com algum campo obrigatório vazio, lançar mensagem pedindo para que seja preenchido
          
### 6. Prototipos de Interface

`A ser desenvolvido pelo aluno.`
