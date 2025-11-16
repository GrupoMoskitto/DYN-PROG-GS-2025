import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Configurações de estilo para os gráficos
sns.set_theme(style="whitegrid")
sns.set_palette("viridis")

ORCAMENTO_TOTAL = 7000

def carregar_dados():
    try:
        df = pd.read_csv('funcionarios.csv', parse_dates=['data_nascimento', 'data_admissao'])
        return df
    except FileNotFoundError:
        print("Arquivo 'funcionarios.csv' não encontrado. Execute 'python gerar_funcionarios.py' primeiro.")
        exit(1)

def analisar_saude_mental(df):
    print("\nANÁLISE DE SAÚDE MENTAL - ODS 3: SAÚDE E BEM-ESTAR")

    # Análise por departamento
    print("\nMÉTRICAS POR DEPARTAMENTO:")
    dept_metrics = df.groupby('departamento').agg({
        'nivel_burnout': 'mean',
        'nivel_engajamento': 'mean',
        'satisfacao_trabalho': 'mean',
        'horas_extras_semanais': 'mean',
        'pausas_diarias': 'mean'
    }).round(1).sort_values('nivel_burnout', ascending=False)
    
    print("\n" + dept_metrics.to_string())
    
    # Análise de fatores de risco
    print("\nPRINCIPAIS FATORES DE RISCO:")
    print(df['fator_risco_principal'].value_counts().head(5))
    
    # Análise de eficácia das iniciativas
    print("\nEFICÁCIA DAS INICIATIVAS DE SAÚDE MENTAL:")
    for iniciativa in df['iniciativa_saude_mental'].unique():
        media_burnout = df[df['iniciativa_saude_mental'] == iniciativa]['nivel_burnout'].mean()
        print(f"- {iniciativa}: {media_burnout:.1f} de burnout médio")
    
    return df

dados_atividades = [
    {'atividade': 'Workshop Gestão de Tempo', 'custo': 1200, 'beneficio': 15},
    {'atividade': 'Sessões de Terapia (Pacote)', 'custo': 3000, 'beneficio': 40},
    {'atividade': 'Assinatura App Meditação', 'custo': 800, 'beneficio': 10},
    {'atividade': 'Aulas de Yoga (Mensal)', 'custo': 1500, 'beneficio': 20},
    {'atividade': 'Consultoria Ergonômica', 'custo': 2000, 'beneficio': 25},
    {'atividade': 'Plano de Saúde Mental Premium', 'custo': 4000, 'beneficio': 60},
]

def merge_sort(lista, chave='nivel_burnout', decrescente=True):
    if isinstance(lista, pd.DataFrame):
        return lista.sort_values(chave, ascending=not decrescente)
    
    if len(lista) <= 1:
        return lista
        
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave, decrescente)
    direita = merge_sort(lista[meio:], chave, decrescente)
    
    return merge(esquerda, direita, chave, decrescente)

def merge(esquerda, direita, chave, decrescente):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        left_val = esquerda[i][chave] if isinstance(esquerda, list) else esquerda.iloc[i][chave]
        right_val = direita[j][chave] if isinstance(direita, list) else direita.iloc[j][chave]
        
        if (left_val > right_val) == decrescente:
            resultado.append(esquerda[i] if isinstance(esquerda, list) else esquerda.iloc[i])
            i += 1
        else:
            resultado.append(direita[j] if isinstance(direita, list) else direita.iloc[j])
            j += 1
    
    # Adicionar elementos restantes
    while i < len(esquerda):
        resultado.append(esquerda[i] if isinstance(esquerda, list) else esquerda.iloc[i])
        i += 1
        
    while j < len(direita):
        resultado.append(direita[j] if isinstance(direita, list) else direita.iloc[j])
        j += 1
        
    # Se for DataFrame, converter de volta
    if isinstance(esquerda, pd.DataFrame) or isinstance(direita, pd.DataFrame):
        return pd.DataFrame(resultado)
    return resultado

def gerar_classificador_risco(limite_alto, limite_moderado):
    def classificar(score_burnout):
        if score_burnout >= limite_alto:
            return "Alto Risco"
        if score_burnout >= limite_moderado:
            return "Risco Moderado"
        return "Risco Baixo"
    return classificar

def analise_dp_knapsack(atividades, orcamento_total):
    memo = {}
    return resolver_knapsack(orcamento_total, atividades, len(atividades), memo)

def resolver_knapsack(orcamento, atividades, n, memo):
    chave = (n, orcamento)
    
    if chave in memo:
        return memo[chave]
        
    if n == 0 or orcamento == 0:
        return (0, [])

    item = atividades[n-1]
    custo = item['custo']
    beneficio = item['beneficio']
    
    if custo > orcamento:
        resultado = resolver_knapsack(orcamento, atividades, n-1, memo)
    else:
        benef_sem, itens_sem = resolver_knapsack(orcamento, atividades, n-1, memo)
        
        benef_com, itens_com = resolver_knapsack(
            orcamento - custo, atividades, n-1, memo
        )
        
        if beneficio + benef_com > benef_sem:
            resultado = (beneficio + benef_com, itens_com + [item['atividade']])
        else:
            resultado = (benef_sem, itens_sem)
    
    memo[chave] = resultado
    return resultado

def gerar_relatorio_ods(df, atividades_selecionadas):
    print("\nIMPACTO NOS OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL (ODS)")
    
    if not atividades_selecionadas:
        print("\nNenhuma atividade selecionada para análise.")
        return
    
    # Impacto no ODS 3: Saúde e Bem-estar
    reducao_burnout = sum(a.get('beneficio', 0) for a in atividades_selecionadas)
    print(f"\nODS 3: SAÚDE E BEM-ESTAR")
    print(f"- Redução média de burnout: {reducao_burnout}%")
    print(f"- Funcionários beneficiados: {len(df) if df is not None else 'N/A'}")
    
    # Impacto no ODS 8: Trabalho Decente e Crescimento Econômico
    print("\nODS 8: TRABALHO DECENTE E CRESCIMENTO ECONÔMICO")
    custo_total = sum(a.get('custo', 0) for a in atividades_selecionadas)
    print(f"- Investimento total: R$ {custo_total:,.2f}")
    if df is not None and len(df) > 0:
        print(f"- Custo por funcionário: R$ {custo_total/len(df):.2f}")
    
    print("\nATIVIDADES SELECIONADAS:")
    for atv in atividades_selecionadas:
        print(f"- {atv.get('atividade', 'Atividade sem nome')} "
              f"(Custo: R$ {atv.get('custo', 0):,.2f}, "
              f"Benefício: {atv.get('beneficio', 0)} pontos)")

def executar_analise_completa():
    # Carregar os dados primeiro
    df = carregar_dados()
    
    print("\nRELATÓRIO DE SAÚDE MENTAL NO AMBIENTE DE TRABALHO")
    print("ALINHADO AOS ODS 3 E 8")
    
    # Análise de risco de burnout
    df_risco = df.sort_values('nivel_burnout', ascending=False)
    df_risco['Nivel_Risco'] = pd.cut(
        df_risco['nivel_burnout'],
        bins=[0, 40, 70, 95],
        labels=['Baixo Risco', 'Risco Moderado', 'Alto Risco']
    )
    
    print("\nDISTRIBUIÇÃO DE RISCOS DE BURNOUT:")
    print(df_risco['Nivel_Risco'].value_counts())
    
    # Top 5 funcionários com maior risco
    print("\nFUNCIONÁRIOS COM MAIOR RISCO DE BURNOUT:")
    print(df_risco[['nome', 'departamento', 'cargo', 'nivel_burnout']].head().to_string(index=False))
    
    # Análise de investimento em bem-estar
    print("\nOTIMIZAÇÃO DE INVESTIMENTOS EM BEM-ESTAR")
    print("USANDO PROGRAMAÇÃO DINÂMICA")
    
    print(f"Orçamento Disponível: R$ {ORCAMENTO_TOTAL:,.2f}")
    
    beneficio, itens = analise_dp_knapsack(dados_atividades, ORCAMENTO_TOTAL)
    
    print("RESULTADO DA OTIMIZAÇÃO:")
    print(f"Benefício Total (Redução de Burnout): {beneficio} pontos")
    print("MELHORES OPÇÕES DE INVESTIMENTO:")
    
    if not itens:
        print("Nenhuma atividade pode ser selecionada com o orçamento disponível.")
    else:
        itens.reverse()
        atividades_selecionadas = []
        for item in itens:
            atividade = next(a for a in dados_atividades if a['atividade'] == item)
            atividades_selecionadas.append(atividade)
            print(f"- {item} (R$ {atividade['custo']:,.2f} | {atividade['beneficio']} pts)")
        
        gerar_relatorio_ods(df, atividades_selecionadas)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='departamento', y='nivel_burnout', data=df, errorbar=None)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('burnout_departamento.png')

    plt.figure(figsize=(10, 8))
    corr = df[['nivel_burnout', 'nivel_engajamento', 'satisfacao_trabalho', 
               'horas_extras_semanais', 'pausas_diarias']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.tight_layout()
    plt.savefig('matriz_correlacao.png')

if __name__ == "__main__":
    executar_analise_completa()