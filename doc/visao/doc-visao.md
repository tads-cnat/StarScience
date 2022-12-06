# Documento de visão

## StarScience

### Histórico da Revisão

| Data       | Versão    | Descrição                                         | Autor                         |
| :--------- | :-------- | :------------------------------------------------ | :---------------------------- |
| 27/10/2022 | **`1.0`** | Versão Inicial                                    | Lucas G, Lucas N, Italo, Davi |
| 07/11/2022 | **`1.1`** | Doc. visão StarScience                            | Lucas G, Davi, Lucas N, Italo |
| 03/12/2022 | **`1.2`** | Atualizações referentes à sessão dos casos de uso | Lucas N, Davi                 |

### 1. Objetivo do Projeto

O projeto **StarScience** tem como objetivo ser uma rede social específica para acadêmicos ou pessoas interessadas em discussões sobre artigos científicos de modo para que também sirva para aquele que deseja apenas procurar artigos de sua
preferência.

### 2. Descrição do problema

| \_\_                        | \_\_                                                                                                                                                                         |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **_O problema_**            | Falta de acesso simplificado e organização de artigos científicos da comunidade no geral.                                                                                    |
| **_afetando_**              | Estudantes, pesquisadores e qualquer pessoa que queira achar e organizar artigos para determinada área.                                                                      |
| **_cujo impacto é_**        | Dificuldade de encontrar os artigos que procura, e organizar os artigos já lidos e avaliados.                                                                                |
| **_Uma boa solução seria_** | Uma plataforma para organização de artigos científicos por usuário, onde será muito mais simples e didático encontrar trabalhos acadêmicos para determinada área ou assunto. |

### 3. Descrição dos usuários

| Nome          | Descrição                                                                                     | Responsabilidades                                                                                                   |
| :------------ | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| Administrador | Responsável por gerenciar a plataforma.                                                       | Gerenciar artigos, usuários, comentários e cadastrar categorias                                                     |
| Usuário       | Visualizar artigos científicos, interagir com eles através de comentários, curtidas e salvos. | Administrar sua conta. Gerenciar artigos, comentários, sua biblioteca de artigos salvos e suas curtidas em artigos. |

### 4. Descrição do ambiente dos usuários

Por se tratar de um site voltado a área acadêmica no geral, é normal que tenham uma área minimamente confortável,
com acesso a um computador e adequada para leitura.

Os artigos podem ser postados ou vistos a qualquer horário, assim sendo o sistema deve ter a capacidade de estar habilitado
a receber requisições 24 horas por dia, durante os 7 dias da semana.

### 5. Principais necessidades dos usuários

- Cientistas e pessoas que procuram artigos têm dificuldade de encontrar plataformas para conversação simplificada e troca de informações sobre artigos científicos, em busca da troca de informações os usuários recorrem a fóruns que não são amigáveis em sua maioria.

- Ao levantar os requisitos e necessidades do usuário através de pesquisas para o futuro desenvolvimento de uma plataforma que agrega artigos científicos em um único local, será possível efetuar a criação desse ambiente mais propício.

- Maior facilidade de encontrar os artigos e salvar numa biblioteca, filtros personalizados para uma melhor busca e um ambiente de discussão aprimorado.

### 6. Alternativas concorrentes

https://sci-hub.se/

- Negativo(s) - O site viola os direitos autorais dos artigos e não tem um sistema de busca que funcione.
- Positivo(s) - Maior site encontrado que reúne artigos científicos.

https://scielo.org/pt/

- Negativo(s) - É voltado apenas para consumo de artigos específicos que a Scielo dá suporte.
- Positivo(s) - É uma das maiores bibliotecas online para consumo de artigos.

https://www.elsevier.com/pt-br/solutions/scopus

- Positivo(s) - É uma base de dados muito bem feita de resumos e citações de artigos para jornais/revistas acadêmicos.

### 7. Visão geral do produto

- O site será capaz de selecionar os artigos através de um sistema de leitura e pesquisa por tags, utilizando referências, palavras chaves, data. Terá uma interface amigável e de fácil navegação. Seção para comentários aprimorada, com local para discussão dos artigos. Parte focada em visualização de artigos pessoais e artigos curtidos pelo usuário para fácil busca no futuro. Facilidade de publicação.

- Ao se cadastrar, o usuário terá um breve tutorial de utilização da plataforma passando, desde a pesquisa e leitura, até a publicação de artigos.

### 8. Requisitos Funcionais

| Código | Nome                    | Descrição                                                                                          |
| :----- | :---------------------- | :------------------------------------------------------------------------------------------------- |
| F01    | Cadastrar Comentário    | O usuário pode comentar qualquer artigo postado no site.                                           |
| F02    | Salvar Artigo           | O usuário pode adicionar artigos à sua biblioteca pessoal para ler/reler depois.                   |
| F03    | Curtir Artigo           | O usuário logado pode curtir artigos postados que irão para a sua aba de "Curtidos" no seu perfil. |
| F04    | Gerenciar Conta         | O usuário tem acesso a sua conta/perfil cadastrada para alterar livremente.                        |
| F05    | Visualizar Perfil       | O usuário pode visualizar outros perfis.                                                           |
| F06    | Cadastrar Artigo        | O usuário posta e mantém a integridade do artigo.                                                  |
| F07    | Sair do Sistema         | O usuário pode encerrar seu login saindo do sistema                                                |
| F08    | Entrar no Sistema       | O usuário pode entrar no sistema                                                                   |
| F09    | Buscar Artigo           | O usuário pode realizar uma rápida pesquisa por nomes de artigos                                   |
| F10    | Cadastrar Área          | O usuário realiza ações referente a inserção, integridade e persistência de áreas                  |
| F11    | Gerenciar Usuário       | Usuário pode realizar ações referentes a persistência e integridade de usuário cadastrado          |
| F12    | Cadastrar Administrador | Um administrador pode inserir novos administradores no sistema                                     |
| F13    | Visualizar Salvos       | O usuário ver a lista de artigos que salvou                                                        |
| F14    | Cadastrar-se            | Uma pessoa pode realizar cadastro caso não seja membro da plataforma                               |
| F15    | Filtrar por Área        | O usuário na ação de buscar por artigo tem a opção de filtrar artigos por área                     |
| F16    | Cadastrar Subárea       | Gerência subáreas relacionadas a uma área                                                          |

### 9. Requisitos não-funcionais

| Código | Nome                        | Descrição                                                                                                         | Categoria   | Classificação |
| :----- | :-------------------------- | :---------------------------------------------------------------------------------------------------------------- | :---------- | :------------ |
| NF01   | Controle de acesso Usuário  | Segurança                                                                                                         | Segurança   | Obrigatório   |
| NF02   | Tempo de resposta           | A comunicação entre o servidor e cliente tem de ser rápido                                                        | Performance | Desejável     |
| NF03   | Design responsivo e prático | Uso de design responsivo e prático na interface gráfica, de modo que faça a navegação seja tranquila e didática.  | Usabilidade | Obrigatório   |
| NF04   | Atendimento a lei LGPD      | Atendimento a lei LGPD na divulgação dos artigos, somente deixando links para os artigos da sua fonte verdadeira. | Legal       | Obrigatório   |
