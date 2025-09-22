import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings("ignore")

# Configuração da página
st.set_page_config(
    page_title="Ministério Acolher - Dashboard de Visitantes",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta de cores do Ministério Acolher
CORES = {
    'verde_escuro': '#7dba52',
    'verde_claro': '#8fc866',
    'verde_limao': '#ccff4a',
    'branco': '#ffffff',
    'texto_claro': '#f0f0f0',
    'texto_escuro': '#31333F'
}

# CSS customizado aprimorado para modo escuro
st.markdown(f"""
<style>
    /* Estilos Gerais */
    .main {{
        padding-top: 2rem;
    }}
    body, [data-testid="stAppViewContainer"] {{
        color: {CORES['texto_escuro']};
    }}

    /* Header */
    .header-section {{
        background: linear-gradient(135deg, {CORES['verde_escuro']}, {CORES['verde_claro']});
        padding: 2rem;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
    }}

    /* Caixas de informação */
    .info-box {{
        background-color: {CORES['branco']};
        border-left: 5px solid {CORES['verde_escuro']};
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: {CORES['texto_escuro']};
    }}

    /* Títulos */
    h1, h2, h3 {{
        color: {CORES['verde_escuro']};
    }}

    /* Força a cor do texto nas métricas para branco */
    [data-testid="stMetric"] label, [data-testid="stMetric"] div, [data-testid="stMetric"] p {{
        color: white;
    }}

    /* Ajuste para dark mode */
    @media (prefers-color-scheme: dark) {{
        body, [data-testid="stAppViewContainer"] {{
            background-color: #1e1e1e !important;
            color: {CORES['texto_claro']} !important;
        }}
        h1, h2, h3 {{
            color: {CORES['branco']} !important;
        }}
        .info-box {{
            background-color: #2b2b2b;
            border-left: 5px solid {CORES['verde_limao']};
            color: {CORES['texto_claro']};
        }}
        /* Garante que o link no rodapé seja visível no modo escuro */
        .footer-link {{
            color: {CORES['verde_limao']} !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Tema customizado para os gráficos Plotly
plotly_template = go.layout.Template()
plotly_template.layout.paper_bgcolor = 'rgba(0,0,0,0)'
plotly_template.layout.plot_bgcolor = 'rgba(0,0,0,0)'
plotly_template.layout.font.color = CORES['texto_escuro']
plotly_template.layout.title.font.color = CORES['verde_escuro']
plotly_template.layout.xaxis.tickfont.color = CORES['texto_escuro']
plotly_template.layout.yaxis.tickfont.color = CORES['texto_escuro']
plotly_template.layout.xaxis.title.font.color = CORES['texto_escuro']
plotly_template.layout.yaxis.title.font.color = CORES['texto_escuro']

# Tema para modo escuro
plotly_template_dark = go.layout.Template()
plotly_template_dark.layout.paper_bgcolor = 'rgba(0,0,0,0)'
plotly_template_dark.layout.plot_bgcolor = 'rgba(0,0,0,0)'
plotly_template_dark.layout.font.color = CORES['texto_claro']
plotly_template_dark.layout.title.font.color = CORES['verde_limao']
plotly_template_dark.layout.xaxis.tickfont.color = CORES['texto_claro']
plotly_template_dark.layout.yaxis.tickfont.color = CORES['texto_claro']
plotly_template_dark.layout.xaxis.title.font.color = CORES['texto_claro']
plotly_template_dark.layout.yaxis.title.font.color = CORES['texto_claro']

# Usamos pio (plotly.io) para registrar os templates
pio.templates['custom_theme'] = plotly_template
pio.templates['custom_theme_dark'] = plotly_template_dark
pio.templates.default = 'custom_theme+custom_theme_dark'


@st.cache_data
def carregar_dados():
    """Carrega e processa os dados da planilha Excel"""
    try:
        if not os.path.exists('Cadastro_Visitantes.xlsx'):
            st.info("📊 Criando dados de exemplo para demonstração...")
            try:
                print("Tentando importar criar_dados_basicos...")
            except ImportError:
                criar_dados_basicos()
        
        df_original = pd.read_excel('Cadastro_Visitantes.xlsx')
        df = df_original.copy() # Trabalha com uma cópia para não alterar o original
        
        # Mapeamento de colunas originais para nomes padronizados
        colunas_mapeadas = {
            'Carimbo de data/hora': 'data_hora',
            'Quem está preenchendo a planilha?': 'preenchido_por',
            'Visita a Igreja Nova Vida de:': 'origem_visita',
            'Data da Visita': 'data_visita',
            'Culto': 'culto',
            'Nome do visitante ': 'nome', # Variação com espaço
            'Nome do visitante': 'nome',
            'Telefone com DDD': 'telefone',
            'Bairro onde mora ': 'bairro', # Variação com espaços
            'Bairro onde mora': 'bairro',
            'Cidade': 'cidade',
            'Como ele chegou até a Nova Vida?': 'como_chegou',
            'Faixa etaria': 'faixa_etaria',
            'Qual a necessidade do visitante?': 'necessidade',
            'Observações': 'observacoes',
            'Gênero': 'genero'
        }
        
        # Renomeia as colunas que existem no DataFrame
        df = df.rename(columns={k: v for k, v in colunas_mapeadas.items() if k in df.columns})

        # ### CORREÇÃO DEFINITIVA PARA COLUNAS DUPLICADAS DE 'pertence_igreja' ###
        # Identifica e consolida as colunas relacionadas a 'pertence_igreja'
        # Primeiro, verifica se as colunas originais existem no df_original
        original_col_1 = 'Pertence a alguma igreja ou religião?'
        original_col_2 = 'Pertence a alguma Igreja?'
        
        has_col_1 = original_col_1 in df_original.columns
        has_col_2 = original_col_2 in df_original.columns

        if has_col_1 and has_col_2:
            # Se ambas existirem, consolida-as em uma nova coluna 'pertence_igreja'
            # Preenche com o primeiro valor não nulo encontrado
            df['pertence_igreja'] = df_original[original_col_1].fillna(df_original[original_col_2])
        elif has_col_1:
            df['pertence_igreja'] = df_original[original_col_1]
        elif has_col_2:
            df['pertence_igreja'] = df_original[original_col_2]
        else:
            # Se nenhuma das colunas originais existir, cria uma coluna vazia
            df['pertence_igreja'] = ''

        # Remove as colunas originais que foram mapeadas e podem ter causado a duplicação
        # Isso garante que 'pertence_igreja' seja sempre uma Series única
        for col_orig in [original_col_1, original_col_2]:
            if col_orig in df.columns:
                df = df.drop(columns=[col_orig])

        if 'data_hora' in df.columns:
            df['data_hora'] = pd.to_datetime(df['data_hora'], errors='coerce')
        if 'data_visita' in df.columns:
            df['data_visita'] = pd.to_datetime(df['data_visita'], errors='coerce')
        
        # Garante que as colunas de texto sejam string e preenche NaNs antes de serem usadas
        for col in ['pertence_igreja', 'preenchido_por', 'como_chegou']:
            if col not in df.columns:
                df[col] = '' # Cria a coluna se não existir
            df[col] = df[col].astype(str).fillna('') # Converte para string e preenche NaNs

        df = df.dropna(how='all')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return pd.DataFrame()

def criar_dados_basicos():
    """Cria dados básicos se não conseguir carregar o script de exemplo"""
    dados_basicos = {
        'Carimbo de data/hora': ['15/01/2024 10:00:00'],
        'Quem está preenchendo a planilha?': ['Pastor João'],
        'Visita a Igreja Nova Vida de:': ['Indicação de amigo'],
        'Data da Visita': ['15/01/2024'],
        'Culto': ['Culto de domingo manhã'],
        'Nome do visitante': ['Visitante Exemplo'],
        'Telefone com DDD': ['(21) 99999-9999'],
        'Bairro onde mora': ['Centro'],
        'Cidade': ['Maricá'],
        'Como ele chegou até a Nova Vida?': ['Indicação de membro'],
        'Pertence a alguma igreja ou religião?': ['Não, não pertence a nenhuma igreja'],
        'Faixa etaria': ['26-35 anos'],
        'Qual a necessidade do visitante?': ['Orientação espiritual'],
        'Observações': ['Primeira visita']
    }
    df = pd.DataFrame(dados_basicos)
    df.to_excel('Cadastro_Visitantes.xlsx', index=False)

def criar_metricas_principais(df):
    """Cria as métricas principais do dashboard"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
        total_visitantes = len(df)
        st.metric(label="👥 Total de Visitantes", value=total_visitantes)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
        if 'data_visita' in df.columns:
            visitas_mes = len(df[df['data_visita'].dt.month == datetime.now().month])
            st.metric(label="📅 Visitas Este Mês", value=visitas_mes)
        else:
            st.metric(label="📅 Visitas Este Mês", value="N/A")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
        if 'cidade' in df.columns:
            cidades_unicas = df['cidade'].nunique()
            st.metric(label="🏘️ Cidades Alcançadas", value=cidades_unicas)
        else:
            st.metric(label="🏘️ Cidades Alcançadas", value="N/A")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
        # A coluna já deve ser string devido à correção em carregar_dados
        sem_igreja = len(df[df['pertence_igreja'].str.contains('Não', case=False, na=False)])
        st.metric(label="🙏 Sem Igreja", value=sem_igreja)
        st.markdown('</div>', unsafe_allow_html=True)

def criar_grafico_visitas_tempo(df):
    """Cria gráfico de visitas ao longo do tempo"""
    if 'data_visita' in df.columns and not df['data_visita'].isna().all():
        df_tempo = df.copy()
        df_tempo['data_visita'] = pd.to_datetime(df_tempo['data_visita'], errors='coerce')
        df_tempo = df_tempo.dropna(subset=['data_visita'])
        
        if not df_tempo.empty:
            visitas_por_data = df_tempo.groupby(df_tempo['data_visita'].dt.date).size().reset_index(name='quantidade')
            
            fig = px.line(
                visitas_por_data,
                x='data_visita',
                y='quantidade',
                title='📈 Evolução das Visitas ao Longo do Tempo',
                labels={'data_visita': 'Data da Visita', 'quantidade': 'Número de Visitantes'},
                color_discrete_sequence=[CORES['verde_escuro']]
            )
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_origem_visitas(df):
    """Cria gráfico de origem das visitas"""
    if 'origem_visita' in df.columns:
        origem_counts = df['origem_visita'].value_counts()
        
        if not origem_counts.empty:
            fig = px.pie(
                values=origem_counts.values, names=origem_counts.index,
                title='🌍 Origem dos Visitantes',
                color_discrete_sequence=[CORES['verde_escuro'], CORES['verde_limao'], CORES['verde_limao']]
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_faixa_etaria(df):
    """Cria gráfico de distribuição por faixa etária"""
    if 'faixa_etaria' in df.columns:
        faixa_counts = df['faixa_etaria'].value_counts()
        
        if not faixa_counts.empty:
            fig = px.bar(
                x=faixa_counts.index, y=faixa_counts.values,
                title='👶👨👴 Distribuição por Faixa Etária',
                color=faixa_counts.values,
                color_continuous_scale=[CORES['verde_limao'], CORES['verde_escuro']]
            )
            fig.update_layout(xaxis_title="Faixa Etária", yaxis_title="Quantidade")
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_necessidades(df):
    """Cria gráfico de necessidades dos visitantes"""
    if 'necessidade' in df.columns:
        necessidade_counts = df['necessidade'].value_counts().head(10)
        
        if not necessidade_counts.empty:
            fig = px.bar(
                x=necessidade_counts.values, y=necessidade_counts.index, orientation='h',
                title='💝 Principais Necessidades dos Visitantes',
                color=necessidade_counts.values,
                color_continuous_scale=[CORES['verde_limao'], CORES['verde_escuro']]
            )
            fig.update_layout(xaxis_title="Quantidade", yaxis_title="Necessidade")
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_cidades(df):
    """Cria gráfico de distribuição por cidades"""
    if 'cidade' in df.columns:
        cidade_counts = df['cidade'].value_counts().head(10)
        
        if not cidade_counts.empty:
            fig = px.bar(
                x=cidade_counts.index, y=cidade_counts.values,
                title='🏙️ Top 10 Cidades dos Visitantes',
                color=cidade_counts.values,
                color_continuous_scale=[CORES['verde_limao'], CORES['verde_escuro']]
            )
            fig.update_layout(xaxis_title="Cidade", yaxis_title="Quantidade")
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_pertence_igreja(df):
    """Cria gráfico de visitantes que pertencem ou não a alguma igreja"""
    # A coluna já deve ser string devido à correção em carregar_dados
    df_copy = df.copy()
    df_copy['categoria'] = 'Não informado'
    df_copy.loc[df_copy['pertence_igreja'].str.contains('sim|pertence', case=False, na=False), 'categoria'] = 'Pertence a alguma igreja'
    df_copy.loc[df_copy['pertence_igreja'].str.contains('não|nao', case=False, na=False), 'categoria'] = 'Não pertence'
    
    igreja_counts = df_copy['categoria'].value_counts()

    if not igreja_counts.empty:
        fig = px.pie(
            values=igreja_counts.values, names=igreja_counts.index,
            title='⛪ Situação Religiosa dos Visitantes',
            color_discrete_sequence=[CORES['verde_escuro'], CORES['verde_limao'], CORES['verde_limao']]
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

# NOVA FUNÇÃO: Análise de quem preencheu as planilhas
def criar_grafico_preenchimento_planilha(df):
    """Cria gráfico de quem mais preencheu as planilhas"""
    # A coluna já deve ser string devido à correção em carregar_dados
    preenchimento_counts = df['preenchido_por'].value_counts().head(10)
    
    if not preenchimento_counts.empty:
        fig = px.bar(
            x=preenchimento_counts.index,
            y=preenchimento_counts.values,
            title='📝 TOP 10 Quem Mais Preencheu as Planilhas de Visitantes',
            labels={'x': 'Responsável pelo Preenchimento', 'y': 'Quantidade de Registros'},
            color=preenchimento_counts.values,
            color_continuous_scale=[CORES['verde_limao'], CORES['verde_claro']]
        )
        fig.update_layout(
            xaxis_title="Responsável pelo Preenchimento",
            yaxis_title="Quantidade de Registros",
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("📝 Não há dados suficientes para mostrar quem preencheu as planilhas.")

# NOVA FUNÇÃO: Análise de como chegaram à igreja
def criar_grafico_como_chegou(df):
    """Cria gráfico de como os visitantes chegaram até a Nova Vida"""
    # A coluna já deve ser string devido à correção em carregar_dados
    chegada_counts = df['como_chegou'].value_counts().head(10)
    
    if not chegada_counts.empty:
        fig = px.pie(
            values=chegada_counts.values,
            names=chegada_counts.index,
            title='🚪 TOP 10 Como os Visitantes Chegaram até a Nova Vida',
            color_discrete_sequence=[CORES['verde_escuro'], CORES['verde_claro'], CORES['verde_limao'], '#9fd356', "#fefffd"]
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Quantidade: %{value}<br>Percentual: %{percent}<extra></extra>'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🚪 Não há dados suficientes para mostrar como os visitantes chegaram.")

def main():
    # Header com logos
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if os.path.exists("assets/Logo_Ministerio.png"):
            st.image("assets/Logo_Ministerio.png", width=120, use_container_width=False)
    with col2:
        st.markdown("""
        <div class="header-section">
            <h1>Ministério Acolher</h1>
            <h2>Igreja Nova Vida - Maricá</h2>
            <h3>📊 Dashboard de Análise de Visitantes 📊</h3>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        if os.path.exists("assets/Logo_Igreja.png"):
            st.image("assets/Logo_Igreja.png", width=120, use_container_width=False)
    
    df = carregar_dados()
    
    if df.empty:
        st.error("❌ Não foi possível carregar os dados. Verifique o arquivo 'Cadastro_Visitantes.xlsx'.")
        return
    
    # Sidebar
    if os.path.exists("assets/Logo_Ministerio.png"):
        st.sidebar.image("assets/Logo_Ministerio.png", width=100)
    st.sidebar.title("Ministério Acolher")
    st.sidebar.markdown("---")
    
    # Filtros
    st.sidebar.header("🔍 Filtros")
    if 'data_visita' in df.columns and not df['data_visita'].isna().all():
        df['data_visita'] = pd.to_datetime(df['data_visita'], errors='coerce')
        data_min = df['data_visita'].min().date()
        data_max = df['data_visita'].max().date()
        periodo = st.sidebar.date_input("Período:", value=(data_min, data_max), min_value=data_min, max_value=data_max)
        if len(periodo) == 2:
            df = df[(df['data_visita'].dt.date >= periodo[0]) & (df['data_visita'].dt.date <= periodo[1])]
    
    if 'cidade' in df.columns:
        cidades = ['Todas'] + sorted(df['cidade'].dropna().unique().tolist())
        cidade_selecionada = st.sidebar.selectbox("Cidade:", cidades)
        if cidade_selecionada != 'Todas':
            df = df[df['cidade'] == cidade_selecionada]

    # Conteúdo principal
    st.markdown("## 📊 Métricas Principais")
    criar_metricas_principais(df)
    
    st.markdown("## 💡 Insights Importantes")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""<div class="info-box"><h4>🎯 Foco de Evangelização</h4><p>Identifique as principais necessidades dos visitantes para direcionar melhor o discipulado.</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="info-box"><h4>📈 Crescimento da Igreja</h4><p>Cada visitante é uma oportunidade de transformação. O acompanhamento sistemático é fundamental.</p></div>""", unsafe_allow_html=True)
    
    st.markdown("## 📈 Análises Detalhadas")
    col1, col2 = st.columns(2)
    with col1:
        criar_grafico_origem_visitas(df)
    with col2:
        criar_grafico_pertence_igreja(df)
    
    col1, col2 = st.columns(2)
    with col1:
        criar_grafico_faixa_etaria(df)
    with col2:
        criar_grafico_necessidades(df)
    
    # NOVA SEÇÃO: Análises Adicionais
    st.markdown("## 🔍 Análises Adicionais")
    col1, col2 = st.columns(2)
    with col1:
        criar_grafico_preenchimento_planilha(df)
    with col2:
        criar_grafico_como_chegou(df)
    
    st.markdown("### 🌍 Distribuição Geográfica e Evolução Temporal")
    col1, col2 = st.columns(2)
    with col1:
        criar_grafico_cidades(df)
    with col2:
        criar_grafico_visitas_tempo(df)
    
    st.markdown("## 📋 Dados Detalhados")
    if st.checkbox("Mostrar tabela de dados"):
        colunas_exibir = ['nome', 'data_visita', 'cidade', 'faixa_etaria', 'necessidade', 'pertence_igreja', 'preenchido_por', 'como_chegou']
        colunas_disponiveis = [col for col in colunas_exibir if col in df.columns]
        st.dataframe(df[colunas_disponiveis] if colunas_disponiveis else df, use_container_width=True)
    
    # Rodapé
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem;">
        <h4 style="color: {CORES['verde_escuro']};">Ministério Acolher - Igreja Nova Vida Maricá</h4>
        <p><em>"Portanto, ide, ensinai todas as nações..."</em> - Mateus 28:19</p>
        <p>Desenvolvido por <strong><a href="https://www.instagram.com/tiagobombista" target="_blank" class="footer-link" style="color: {CORES['verde_escuro']}; text-decoration: underline;">@TiagoBombista</a></strong> com ❤️</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()