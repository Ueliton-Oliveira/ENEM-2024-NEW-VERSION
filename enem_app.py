import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px 
import matplotlib as mp

st.set_page_config(
    page_title="PAINEL ENEM 2024 - ESPÍRITO SANTO",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* Fundo da sidebar com degradê azul suave */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #E3F2FD 0%, #BBDEFB 100%);
}

/* Cor padrão dos textos */
[data-testid="stSidebar"] * {
    color: #0D47A1 !important;
}

/* BOTÕES — estilo claro e leve */
div.stButton > button {
    background-color: #FFFFFF !important; /* branco leve */
    color: #0D47A1 !important;
    border: 1px solid #90CAF9 !important;
    border-radius: 10px !important;
    padding: 6px 12px !important;
    font-weight: 600 !important;
    width: 100%;
    transition: all 0.2s ease-in-out;
}

/* Ao passar o mouse */
div.stButton > button:hover {
    background-color: #E3F2FD !important;
    color: #0D47A1 !important;
    border-color: #64B5F6 !important;
}

/* Margem entre os botões */
div.stButton {
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


if "page" not in st.session_state:
    st.session_state.page = "Capa"

def navigate(to):
    st.session_state.page = to

#--------------SIDEBAR--------------
with st.sidebar:
    st.markdown("Navegação")
    st.button("&#x1F4D8; Capa", on_click=navigate, args=("Capa",))
    st.button("&#x1F465; Presenças", on_click=navigate, args=("Presenças",))
    st.button("&#128292; Línguas Estrangeiras", on_click=navigate, args=("Línguas",))
    st.button("&#x1F4CA; Resultados", on_click=navigate, args=("Resultados",))
    st.button("&#x1F4C8; Médias", on_click=navigate, args=("Médias",))

if st.session_state.page == "Capa":
    st.markdown("""
    <style>
    .capa-container {
        background: linear-gradient(135deg, #f5fafd 60%, #e3f0fb 100%);
        border-radius: 18px;
        padding: 3rem 2rem 2rem 2rem;
        margin-top: 2rem;
        box-shadow: 0 0 18px #e3e9f7;
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }
    .capa-title {
        color: #154178;
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 1.2rem;
    }
    .capa-section-title {
        color: #1976d2;
        font-size: 1.32rem;
        font-weight: 700;
        margin-top: 1.6rem;
        margin-bottom: 0.4rem;
    }
    .capa-text {
        color: #212f3c;
        font-size: 1.04rem;
        line-height: 1.7;
        text-align: justify;
        margin-bottom: 1rem;
    }
    .capa-note {
        color: #004d40;
        background: #e6fffa;
        border-left: 6px solid #00897b;
        border-radius: 6px;
        padding: 0.8rem 1rem;
        margin: 1.3rem 0;
        font-size: 0.97rem;
    }
    .capa-source {
        color: #425265;
        font-size: 0.99rem;
        margin-top: 12px;
        text-align: right;
    }
    </style>
    <div class="capa-container">
        <div class="capa-title">
            Painel de Análise do ENEM 2024 - Espírito Santo
        </div>
        <div class="capa-section-title">Sobre o projeto</div>
        <div class="capa-text">
            <strong>Objetivo:</strong> painel interativo para análise e visualização dos resultados do ENEM 2024 no estado do Espírito Santo:
        </div>
        <div class="capa-text">
            • Visualizar presenças e ausências nas áreas de conhecimento<br>
            • Visualizar quantidade de alunos para cada Língua Estrangeira<br>
            • Visualizar os resultados nas áreas e redação<br>
            • Visualizar notas médias por área, município e código de escola
        </div>
        <div class="capa-note">
            <strong>Observação importante:</strong> O código da escola indica a escola onde o aluno concluiu o Ensino Médio. Os gráficos mostram a média dos resultados dos alunos que finalizaram o Ensino Médio em cada escola, identificada pelo respectivo código.<br>
            A base de dados do INEP não fornece o nome da escola, motivo pelo qual apenas o código é apresentado.
        </div>
        <div class="capa-text">
            <strong>Fonte de Dados:</strong> Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
        </div>
        <div class="capa-text">
            <strong>Microdados do ENEM 2024:</strong> CN, CH, LC, MT, Redação
        </div>
        <div class="capa-source">
            Desenvolvido por SRE-Cariacica<br>
            Uéliton J. Oliveira
        </div>
    </div>
    """, unsafe_allow_html=True)
