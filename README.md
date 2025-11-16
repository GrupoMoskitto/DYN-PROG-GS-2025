# Sistema de Gestão de Saúde Ocupacional

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/SEU_LINK_AQUI?usp=sharing)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-blue?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-blue?logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-blue?logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)

## Equipe
- [Gabriel Couto Ribeiro](https://github.com/rouri404) - RM559579
- [Gabriel Kato Peres](https://github.com/kato8088) - RM560000
- [João Vitor de Matos Araujo](https://github.com/joaomatosq) - RM559246

## Visão Geral

O Sistema de Gestão de Saúde Ocupacional é uma solução desenvolvida como parte do projeto acadêmico de Gestão de Sistemas. Esta ferramenta tem como propósito principal otimizar a gestão da saúde mental no ambiente corporativo, com ênfase na prevenção da síndrome de burnout e na promoção de práticas organizacionais saudáveis.

## Objetivos Estratégicos

O sistema foi projetado para atender aos seguintes objetivos estratégicos:

1. **Identificação Proativa**
   - Detecção precoce de sinais de esgotamento profissional
   - Monitoramento contínuo de indicadores de saúde mental

2. **Gestão Baseada em Dados**
   - Análise preditiva de riscos psicossociais
   - Geração de insights acionáveis para a gestão de pessoas

3. **Conformidade e Sustentabilidade**
   - Alinhamento com os Objetivos de Desenvolvimento Sustentável (ODS) da ONU
   - Adequação às melhores práticas de saúde ocupacional

## Funcionalidades Principais

### 1. Análise de Saúde Ocupacional
- Geração de relatórios analíticos por departamento e cargo
- Identificação de padrões de risco psicossocial
- Monitoramento de indicadores-chave de desempenho (KPIs) de bem-estar

### 2. Gestão de Intervenções
- Sistema de recomendações baseado em evidências
- Priorização de ações por impacto e viabilidade
- Análise de custo-benefício para iniciativas de saúde ocupacional

### 3. Conformidade Regulatória
- Alinhamento com as diretrizes da OIT sobre saúde e segurança no trabalho
- Suporte aos Objetivos de Desenvolvimento Sustentável (ODS) da ONU
   - **ODS 3**: Assegurar uma vida saudável e promover o bem-estar
   - **ODS 8**: Trabalho decente e crescimento econômico

## Arquitetura e Metodologia

### Stack Tecnológica

| Componente | Tecnologia |
|------------|------------|
| Linguagem | Python 3.8+ |
| Análise de Dados | Pandas, NumPy |
| Visualização | Matplotlib, Seaborn |
| Otimização | Algoritmo Knapsack |
| Geração de Relatórios | CSV, Markdown |

### Abordagem Metodológica

1. **Coleta e Ingestão de Dados**
   - Geração de dados sintéticos para análise
   - Validação e normalização de entradas

2. **Processamento e Análise**
   - Aplicação de técnicas de mineração de dados
   - Identificação de correlações e padrões

3. **Geração de Insights**
   - Desenvolvimento de recomendações baseadas em evidências
   - Priorização de ações estratégicas

## Estrutura de Dados

### Esquema do Conjunto de Dados

O arquivo `funcionarios.csv` segue o seguinte esquema de dados:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id_func | Integer | Identificador único do colaborador |
| nome | String | Nome completo |
| email | String | Endereço de e-mail corporativo |
| departamento | String | Área organizacional |
| cargo | String | Função organizacional |
| data_nascimento | Date | Data de nascimento (YYYY-MM-DD) |
| data_admissao | Date | Data de admissão (YYYY-MM-DD) |
| nivel_burnout | Integer [0-100] | Índice de esgotamento profissional |
| nivel_engajamento | Integer [0-100] | Nível de engajamento organizacional |
| satisfacao_trabalho | Integer [0-100] | Índice de satisfação profissional |
| horas_extras_semanais | Integer | Média semanal de horas extras |
| pausas_diarias | Integer | Média diária de pausas realizadas |

### Garantia de Qualidade

- Validação de integridade referencial
- Verificação de consistência de faixas de valores
- Geração de dados sintéticos com distribuição realista

## Guia de Implementação

1. Clone o repositório:
   ```bash
   git clone https://github.com/GrupoMoskitto/DYN-PROG-GS-2025.git
   cd DYN-PROG-GS-2025
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate  # Windows
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o `app.py`:
   ```bash
   python app.py
   ```

5. **Inicialização do Sistema**
   ```bash
   python app.py
   ```

## Impacto Organizacional

### Alinhamento com os ODS da ONU

#### ODS 3: Boa Saúde e Bem-estar
- **3.4** Redução de mortes prematuras por doenças não transmissíveis
- **3.4.2** Taxa de mortalidade por suicídio (prevenção do burnout)
- **3.d** Fortalecimento da capacidade de gestão de riscos à saúde

#### ODS 8: Trabalho Decente e Crescimento Econômico
- **8.5** Emprego pleno e produtivo para todos
- **8.8** Proteção dos direitos trabalhistas
- **8.8.1** Taxas de frequência de acidentes de trabalho

### Métricas de Desempenho

| Categoria | Métrica | Frequência |
|-----------|---------|------------|
| Saúde Ocupacional | Taxa de Burnout | Mensal |
| Engajamento | NPS Interno | Trimestral |
| Desempenho | Satisfação no Trabalho | Semestral |
| Bem-estar | Frequência de Pausas | Semanal |
| Carga de Trabalho | Horas Extras | Mensal |