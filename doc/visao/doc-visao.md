# Documento de visão

## StarScience

### Histórico da Revisão

| Data       | Versão    | Descrição                                         | Autor                         |
| :--------- | :-------- | :------------------------------------------------ | :---------------------------- |
| 27/10/2022 | **`1.0`** | Versão Inicial                                    | Lucas G, Lucas N, Italo, Davi |
| 07/11/2022 | **`1.1`** | Doc. visão StarScience                            | Lucas G, Davi, Lucas N, Italo |
| 03/12/2022 | **`1.2`** | Atualizações referentes à sessão dos casos de uso | Lucas N, Davi                 |
| 04/04/2023 | **`2.0`** | Revisão para utilização em 2023.1                 | Joana Fernandes               |

### 1. Objetivo do Projeto

O projeto **StarScience** tem como objetivo ser uma rede social específica para acadêmicos ou pessoas interessadas em discussões sobre artigos científicos de modo que também sirva para aqueles que desejam apenas procurar artigos de sua preferência.

### 2. Descrição do problema

| \_\_                        | \_\_                                                                                                                                                                         |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **_O problema_**            | Falta de acesso simplificado e organização de artigos científicos da comunidade em geral.                                                                                    |
| **_afetando_**              | Estudantes, pesquisadores e qualquer pessoa que queira achar e organizar artigos para determinada área.                                                                      |
| **_cujo impacto é_**        | Dificuldade em encontrar artigos e organizar os que já foram lidos e avaliados.                                                                                |
| **_Uma boa solução seria_** | Uma plataforma para organização de artigos científicos por usuário, onde será muito mais simples e didático encontrar trabalhos acadêmicos por determinada área e/ou assunto. |

### 3. Descrição dos usuários

| Nome          | Descrição                                                                                     | Responsabilidades                                                                                                   |
| :------------ | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| Administrador | Responsável por gerenciar a plataforma.                                                       | Gerenciar artigos, usuários, comentários e cadastrar categorias                                                     |
| Usuário       | Visualizar artigos científicos, comentar, curtir e salvar artigos. | Administrar sua conta. Gerenciar artigos, comentários, sua biblioteca de artigos salvos e suas curtidas em artigos. |

### 4. Descrição do ambiente dos usuários

Ambiente simplificado para fácil usabilidade e fácil localização de conteúdo.

Os artigos podem ser postados ou vistos a qualquer horário, assim sendo o sistema deve ter a capacidade de estar habilitado
a receber requisições 24 horas por dia, durante os 7 dias da semana.

### 5. Principais necessidades dos usuários

- Cientistas e pessoas que procuram artigos têm dificuldade de encontrar plataformas para conversação simplificada e troca de informações sobre artigos científicos,  pois em sua maioria são fóruns não tão amigáveis.

- Ambiente propício a agregar artigos científicos de diversos tipos e áreas em um único local.

- Possibilidade de salvar os artigos em uma biblioteca dentro da plataforma, com filtros personalizados para uma melhor busca e um ambiente de discussão aprimorado.

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

- O site será capaz de selecionar os artigos através de um sistema de leitura e pesquisa por tags, utilizando referências, palavras chaves, data. Terá uma interface amigável e de fácil navegação. Seção para comentários aprimorada, com local para discussão dos artigos. Parte focada em visualização de artigos pessoais e artigos curtidos e/ou salvos pelo usuário para fácil busca posterior. Facilidade de publicação.

- Ao se cadastrar, o usuário terá um breve tutorial de utilização da plataforma, desde a pesquisa e leitura até a publicação de artigos.

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
| NF01 | Precisão  | Os resultados apresentados pelo sistema devem ser precisos e consistentes, refletindo corretamente as informações dos artigos científicos. | Funcionalidade | Desejavel |
| NF02 | Adequação | O sistema deve atender às necessidades dos usuários, fornecendo funcionalidades relevantes para busca, organização e interação com os artigos científicos. | Funcionalidade | Obrigatório |
| NF03 | Disponibilidade | O sistema deve estar disponível para uso de forma contínua, com um tempo de inatividade mínimo planejado. | Confiabilidade | Desejavel |
| NF04 | Tolerância a falhas | O sistema deve ser capaz de lidar com falhas, minimizando o impacto nos usuários e garantindo a recuperação adequada. | Confiabilidade | Desejavel |
| NF05 | Compreensibilidade | A interface do usuário deve ser fácil de entender e utilizar, mesmo para usuários sem experiência técnica, proporcionando uma experiência intuitiva. | Usabilidade | Desejavel |
| NF06 | Eficiência de uso| O sistema deve permitir que os usuários realizem suas tarefas de forma eficiente, sem a necessidade de realizar ações desnecessárias ou complexas.| Usabilidade | Desejavel |
| NF07 | Tempo de resposta| O sistema deve responder rapidamente às ações dos usuários, proporcionando tempos de resposta curtos em operações como busca por artigos e carregamento de páginas.| Eficiência de desempenho | Desejavel |
| NF08 | Utilização de recursos| O sistema deve ser otimizado para minimizar o consumo de recursos computacionais, como processamento, memória e largura de banda.| Eficiência de desempenho | Desejavel |
| NF09 | Interoperabilidade| O sistema deve ser capaz de interoperar com outros sistemas e plataformas, permitindo a integração com fontes externas de artigos científicos e serviços relacionados.| Compatibilidade | Obrigatório |
| NF10 | Confidencialidade| O sistema deve garantir a proteção dos dados pessoais dos usuários e das informações confidenciais contidas nos artigos científicos.| Segurança | Obrigatório |
| NF11 | Integridade| O sistema deve garantir a integridade dos dados, evitando alterações não autorizadas ou corrupção dos artigos e informações relacionadas| Segurança | Obrigatório |

### 10. Requisitos Arquiteturalmente Significantes (RAS)
| Nome | Descrição |
| :----- | :-------------------------- |
| Escalabilidade | A capacidade do sistema de lidar com um grande número de usuários simultâneos e a carga de publicação e busca de artigos é um aspecto fundamental na definição da arquitetura. Isso envolve a consideração de escalabilidade vertical (aumento da capacidade dos recursos existentes) e escalabilidade horizontal (distribuição do sistema em múltiplos servidores). |
| Segurança | A implementação de medidas de segurança robustas, como autenticação, autorização e criptografia de dados, requer considerações arquiteturais adequadas. A arquitetura deve ser projetada de forma a garantir a proteção adequada dos dados dos usuários e mitigar riscos de ataques cibernéticos. |
| Confiabilidade | A arquitetura do sistema deve ser projetada com foco na confiabilidade, minimizando o tempo de inatividade e evitando falhas críticas que possam resultar em perda de dados ou interrupção dos serviços. Isso pode envolver a implementação de redundância, balanceamento de carga e estratégias de recuperação de falhas. |
| Integração | A capacidade de integração com outras fontes de artigos científicos e bases de dados é um aspecto arquitetural importante. Isso requer a definição de interfaces, protocolos e mecanismos de troca de dados que permitam a importação e atualização de conteúdo de fontes externas confiáveis. |
