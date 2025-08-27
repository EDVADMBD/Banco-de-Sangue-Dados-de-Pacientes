
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("dados_pacientes.csv")

# Renomear colunas para facilitar o acesso
df.columns = ['id_paciente', 'idade', 'altura', 'peso', 'tipo_sanguineo', 'estado_civil']

# Título do dashboard
st.title("📊 Dashboard Interativo - Dados de Pacientes")

# Seção 1: Distribuições de idade, altura e peso
st.header("Distribuições de Idade, Altura e Peso")

col1, col2, col3 = st.columns(3)

with col1:
    fig1, ax1 = plt.subplots()
    sns.histplot(df['idade'], bins=20, kde=True, ax=ax1, color='skyblue')
    ax1.set_title("Distribuição de Idade")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    sns.histplot(df['altura'], bins=20, kde=True, ax=ax2, color='lightgreen')
    ax2.set_title("Distribuição de Altura")
    st.pyplot(fig2)

with col3:
    fig3, ax3 = plt.subplots()
    sns.histplot(df['peso'], bins=20, kde=True, ax=ax3, color='salmon')
    ax3.set_title("Distribuição de Peso")
    st.pyplot(fig3)

# Seção 2: Contagens por tipo sanguíneo e estado civil
st.header("Contagens por Tipo Sanguíneo e Estado Civil")

col4, col5 = st.columns(2)

with col4:
    fig4, ax4 = plt.subplots()
    df['tipo_sanguineo'].value_counts().plot(kind='bar', ax=ax4, color='orchid')
    ax4.set_title("Contagem por Tipo Sanguíneo")
    st.pyplot(fig4)

with col5:
    fig5, ax5 = plt.subplots()
    df['estado_civil'].value_counts().plot(kind='bar', ax=ax5, color='gold')
    ax5.set_title("Contagem por Estado Civil")
    st.pyplot(fig5)

# Seção 3: Mapa de calor de correlação
st.header("Mapa de Calor de Correlação entre Variáveis Numéricas")

fig6, ax6 = plt.subplots()
sns.heatmap(df[['idade', 'altura', 'peso']].corr(), annot=True, cmap='coolwarm', ax=ax6)
ax6.set_title("Correlação entre Idade, Altura e Peso")
st.pyplot(fig6)
