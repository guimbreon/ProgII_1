# Projeto BirthPlanOO

## Contexto
O projeto BirthPlanOO aborda questões no Serviço Nacional de Saúde (SNS) de Portugal relacionadas com a organização e otimização dos serviços de maternidade. Apesar do elevado financiamento, o SNS enfrenta desafios organizacionais significativos que afetam os serviços de saúde materna e neonatal. Este projeto visa desenvolver uma aplicação de software para auxiliar os hospitais na gestão eficiente dos cuidados de maternidade.

## Objetivo
Desenvolver a aplicação BirthPlanOO usando Python 3. O software apoia as equipas de enfermagem no encaminhamento de grávidas para os serviços de maternidade e ajuda a gerir a atribuição de assistência ao parto a médicos especialistas, hospitais e equipas.

## Funcionalidades
1. **Dados de Entrada**:
    - **Lista de Médicos**: Um ficheiro que detalha os médicos disponíveis e seus horários.
    - **Calendário**: Um ficheiro que contém o calendário atual de assistências.
    - **Pedidos**: Um ficheiro que lista novos pedidos de assistência.

2. **Dados de Saída**:
    - **Lista de Médicos Atualizada**: Reflete as novas atribuições e horários.
    - **Calendário Atualizado**: Inclui novas assistências atribuídas e remove tarefas concluídas.

3. **Funcionalidade**:
    - O programa processa os ficheiros de entrada, atualiza os calendários e a disponibilidade dos médicos, e gera novos ficheiros de saída.
    - Prioriza os pedidos com base na urgência e disponibilidade dos médicos.
    - Lida com exceções para inconsistências entre os nomes dos ficheiros e os cabeçalhos.

## Exemplos de Ficheiros de Entrada
- `doctors14h00.txt`
  ```
  Organization: SmartH
  Hour: 14h00
  Day: 08:12:2023
  Doctors:
  Manuel Frias, 2, 14h25, 85, 36h28
  Carlos Sousa, 3, 12h10, 60, 28h34
  ```
- `schedule14h00.txt`
  ```
  Organization: SmartH
  Hour: 14h00
  Day: 08:12:2023
  Schedule:
  14h00, Anabela Rocha, Carlos Sousa
  14h25, Daniela Silva, Manuel Frias
  ```
- `requests14h30.txt`
  ```
  Organization: SmartH
  Hour: 14h30
  Day: 08:12:2023
  Mothers:
  Zulmira Zacarias, 33, red, low
  ```

## Exemplos de Ficheiros de Saída
- Lista de médicos atualizada: `doctors14h30.txt`
- Calendário atualizado: `schedule14h30.txt`

## Desenvolvimento
### Estrutura do Projeto
- A aplicação é composta por classes relevantes para a resolução do projeto.
- O programa principal, `refresh.py`, contém uma função chamada `plan` que assegura o funcionamento correto da aplicação.

### Tratamento de Erros
- **Erro de Cabeçalho de Ficheiro**: Lança uma exceção se houver uma inconsistência entre o nome do ficheiro e o cabeçalho quanto ao âmbito (doctors, schedule ou requests).

### Linguagem
- Linguagem de entrada/saída: Inglês
- Documentação e comentários no código: Inglês (usando notação camelCase)

## Execução
Execute o software usando o comando:
```sh
python3 refresh.py inputFile1 inputFile2 inputFile3
```
- `inputFile1`: Ficheiro da lista de médicos
- `inputFile2`: Ficheiro do calendário de assistências
- `inputFile3`: Ficheiro da lista de pedidos de assistência

Os ficheiros de saída serão criados no mesmo diretório dos ficheiros de entrada e do código, nomeados de acordo com a hora atualizada.

## Grupos e Submissão
### Formação de Grupos
- Grupos de exatamente 2 alunos.
- Registo dos grupos via o site Moodle da disciplina.

### Submissão
- Submeter um ficheiro ZIP nomeado `birthPlanGroupN.zip` (N é o número do grupo).
- Incluir:
    - Relatório de implementação (`relGroupN.pdf`)
    - Ficheiros de código fonte
    - Ficheiros de teste usados

### Estrutura do Relatório
1. Número do grupo
2. Detalhes dos membros (nome e número de aluno)
3. Detalhes das contribuições de cada membro
4. Funções extra implementadas (se aplicável)
5. Funcionalidades não implementadas (se aplicável)
6. Erros conhecidos (se aplicável)

### Avaliação
- **Completude**: 1 ponto se completo e funcional, 0 caso contrário.
- **Correção Pragmática**: 60%
- **Correção Semântica**: 20%
- **Documentação**: 10%
- **Legibilidade**: 5%
- **Relatório de Implementação**: 5%

Submeter a solução via o site Moodle da disciplina até ao prazo: **5 de abril de 2024, 23:00 (hora de Lisboa)**. Submissões tardias não serão consideradas.

## Integridade Académica
- O projeto deve ser trabalho original dos membros do grupo.
- Discussão de abordagens é encorajada, mas a partilha de código é proibida.
- Software de deteção de plágio será usado para assegurar a originalidade.