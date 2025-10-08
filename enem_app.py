import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página com ícone, título e layout
st.set_page_config(
    page_title="Painel Educacional - ENEM 2024",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para a capa/apresentação
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E40AF;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subheader {
        font-size: 1.5rem;
        color: #374151;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .info-box {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1E40AF;
        margin-bottom: 1.5rem;
    }
    .highlight {
        background-color: #FFFBEB;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Função para carregar dados
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# Função para plotar gráfico de barras das notas
def plot_bar_notas(df, colunas_notas):
    fig, axs = plt.subplots(1, len(colunas_notas), figsize=(15,4))
    if len(colunas_notas) == 1:
        axs = [axs]
    for i, col in enumerate(colunas_notas):
        axs[i].hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
        axs[i].set_title(f'Distribuição {col}')
        axs[i].set_xlabel('Nota')
        axs[i].set_ylabel('Frequência')
    plt.tight_layout()
    st.pyplot(fig)

# Função para plotar gráfico de pizza/rosca de língua estrangeira
def plot_pizza_lingua(df):
    contagem = df['LÍNGUA ESTRANGEIRA'].value_counts()
    labels = contagem.index.tolist()
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        contagem,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops=dict(width=0.4)
    )
    ax.set_title('Distribuição Língua Estrangeira')
    st.pyplot(fig)

# Função para plotar média de nota final redação por município (gráfico de barras)
def plot_bar_media_redacao(df):
    medias = df.groupby('NOME MUN. PROVA')['NOTA FINAL REDAÇÃO'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(10,6))
    medias.plot(kind='barh', color='coral', ax=ax)
    ax.set_xlabel('Média Nota Final Redação')
    ax.set_ylabel('Município')
    ax.set_title('Média da Nota Final de Redação por Município')
    st.pyplot(fig)

# Função para plotar gráficos de barras para presença nas provas
def plot_bar_presenca(df, col_presenca, titulo):
    contagem = df[col_presenca].value_counts()
    fig, ax = plt.subplots()
    contagem.plot(kind='bar', color='mediumseagreen', ax=ax)
    ax.set_title(titulo)
    ax.set_xlabel('Status')
    ax.set_ylabel('Quantidade')
    st.pyplot(fig)

# --- Início da aplicação ---

# Navegação entre páginas na sidebar
page = st.sidebar.selectbox('Navegação', ['Apresentação', 'Dashboard'])

if page == 'Apresentação':
    # Cabeçalho principal estilizado da capa
    st.markdown('<div class="main-header">🎓 Painel de Análise do ENEM 2024 - Espírito Santo</div>', unsafe_allow_html=True)

    # Duas colunas com informações do projeto e pessoas
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>📊 Sobre o Projeto</h3>
            <p>Esta aplicação apresenta um <span class="highlight">MVP (Produto Mínimo Viável)</span> desenvolvido como parte 
            da avaliação da disciplina de Cloud Computing para produtos de dados na Pós-graduação em Mineração de Dados.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background-color: #EFF6FF; padding: 1.5rem; border-radius: 10px; text-align: center;">
            <h4>👨‍🏫 Professor</h4>
            <p><strong>Maxwell Monteiro</strong></p>
            <h4>👨‍🎓 Aluno</h4>
            <p><strong>Uéliton José de Oliveira</strong></p>
        </div>
        """, unsafe_allow_html=True)

    # Objetivo do Projeto
    st.markdown('<div class="subheader">🎯 Objetivo do Projeto</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #F0FDF4; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #10B981;">
        <p>O objetivo principal é criar um <strong>painel interativo</strong> para análise e visualização dos resultados 
        do ENEM 2024 no estado do Espírito Santo. A aplicação permitirá:</p>
        <ul>
            <li>📈 Análise comparativa das notas por área de conhecimento</li>
            <li>🏫 Visualização do desempenho por escola e município</li>
            <li>📊 Identificação de padrões e tendências educacionais</li>
            <li>🎯 Benchmarking com médias estaduais e nacionais</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Fonte dos Dados
    st.markdown('<div class="subheader">📁 Fonte dos Dados</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #FEF3C7; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #F59E0B;">
        <p>Os dados utilizados neste projeto são <strong>públicos e oficiais</strong>, obtidos através do:</p>
        <p>🏛️ <strong>Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)</strong></p>
        <p>📊 <strong>Microdados do ENEM 2024</strong> contendo:</p>
        <ul>
            <li>🔬 Ciências da Natureza</li>
            <li>🌍 Ciências Humanas</li>
            <li>📝 Linguagens e Códigos</li>
            <li>🧮 Matemática</li>
            <li>✍️ Redação</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

else:
    # Carrega dados
    df = load_data('/workspaces/ENEM-2024-NEW-VERSION/ENEM_ES_2024_modificado.csv')

    # Sidebar - filtros
    st.sidebar.header('Filtros')

    # Filtro Código Escola
    cod_escolas = ['Todos'] + sorted(df['CÓD. ESCOLA'].dropna().unique().astype(str).tolist())
    cod_escola_sel = st.sidebar.selectbox('Código da Escola', cod_escolas)
    if cod_escola_sel != 'Todos':
        df = df[df['CÓD. ESCOLA'].astype(str) == cod_escola_sel]

    # Filtro Município
    municipios = ['Todos'] + sorted(df['NOME MUN. PROVA'].dropna().unique().tolist())
    municipio_sel = st.sidebar.selectbox('Município da Prova', municipios)
    if municipio_sel != 'Todos':
        df = df[df['NOME MUN. PROVA'] == municipio_sel]

    # Filtros de Presença em CN, CH, LC e MT
    for prova, label in zip(['PRESENÇA EM CN', 'PRESENÇA EM CH', 'PRESENÇA EM LC', 'PRESENÇA EM MT'],
                        ['Presença CN', 'Presença CH', 'Presença LC', 'Presença MT']):
        opcao = st.sidebar.selectbox(f'Filtro {label}', ['Todos', 'Presente', 'Faltou', 'Eliminado'])
        if opcao != 'Todos':
            df = df[df[prova] == opcao]

    # Filtros de notas na sidebar para cada área e para redação
    st.sidebar.header('Filtros de Notas')
    cols_notas = ['NOTA EM CN', 'NOTA EM CH', 'NOTA EM LC', 'NOTA EM MT', 'NOTA FINAL REDAÇÃO']

    for col in cols_notas:
        col_series = pd.to_numeric(df[col], errors='coerce')
        min_val = float(np.nanmin(col_series))
        max_val = float(np.nanmax(col_series))
        faixa = st.sidebar.slider(
            f'Faixa de {col}', 
            min_value=0.0, 
            max_value=1000.0, 
            value=(min_val, max_val), 
            step=1.0
        )
        df = df[(col_series >= faixa[0]) & (col_series <= faixa[1])]

    # ----- Seção Principal -----
    st.title('Dashboard ENEM 2024 - Escolas Estaduais do Espírito Santo')

    # 1) Tabela descritiva da base de dados (numérica)
    st.header('Descrição Estatística dos Dados')
    st.dataframe(df.describe())

    # 2) Gráficos
    st.header('Visualizações')

    # Gráficos de barras para distribuição das notas
    st.subheader('Distribuição das Notas - CN, CH, LC, MT')
    plot_bar_notas(df, ['NOTA EM CN', 'NOTA EM CH', 'NOTA EM LC', 'NOTA EM MT'])

    # Gráfico de pizza/rosca para Língua Estrangeira
    st.subheader('Distribuição Língua Estrangeira')
    plot_pizza_lingua(df)

    # Gráfico de barras para médias da Redação por município
    st.subheader('Média da Nota Final de Redação por Município')
    plot_bar_media_redacao(df)

    # Gráficos de barras para distribuição de presença
    st.subheader('Distribuição de Presença nas Provas')
    plot_bar_presenca(df, 'PRESENÇA EM CN', 'Presença em Ciências da Natureza')
    plot_bar_presenca(df, 'PRESENÇA EM CH', 'Presença em Ciências Humanas')
    plot_bar_presenca(df, 'PRESENÇA EM LC', 'Presença em Linguagens e Códigos')
    plot_bar_presenca(df, 'PRESENÇA EM MT', 'Presença em Matemática')

