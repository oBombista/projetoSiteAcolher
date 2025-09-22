import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')

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
    'branco': '#ffffff'
}

# CSS customizado
# CSS customizado com suporte a tema claro e escuro
# CSS customizado com suporte a tema claro e escuro (ajustado)

st.markdown(f"""
<style>
    .main {{
        padding-top: 2rem;
    }}

    /* Header fixo com texto branco */
    .header-section {{
        background: linear-gradient(135deg, {CORES['verde_escuro']}, {CORES['verde_claro']});
        padding: 2rem;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
    }}

    /* Cards de métricas */
    .metric-card {{
        background: linear-gradient(135deg, {CORES['verde_escuro']}, {CORES['verde_claro']});
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }}

    /* Caixas de informação */
    .info-box {{
        background-color: {CORES['branco']};
        border-left: 5px solid {CORES['verde_escuro']};
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: black;
    }}

    /* Sidebar */
    .sidebar .sidebar-content {{
        background: linear-gradient(180deg, {CORES['verde_escuro']}, {CORES['verde_claro']});
        color: white;
    }}

    /* Títulos */
    h1, h2, h3 {{
        color: {CORES['verde_escuro']};
    }}

    /* Ajuste para dark mode */
    @media (prefers-color-scheme: dark) {{
        body, [data-testid="stAppViewContainer"] {{
            background-color: #1e1e1e !important;
            color: #f0f0f0 !important;
        }}
        h1, h2, h3 {{
            color: {CORES['verde_limao']} !important;
        }}
        .info-box {{
            background-color: #2b2b2b;
            border-left: 5px solid {CORES['verde_limao']};
            color: white;
        }}
    }}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def carregar_dados():
    """Carrega e processa os dados da planilha Excel"""
    try:
        # Verifica se o arquivo existe, se não, cria dados de exemplo
        if not os.path.exists('Cadastro_Visitantes.xlsx'):
            st.info("📊 Criando dados de exemplo para demonstração...")
            # Importa e executa o script de dados de exemplo
            try:
                from dados_exemplo import criar_dados_exemplo
                criar_dados_exemplo()
            except:
                # Se não conseguir importar, cria dados básicos
                criar_dados_basicos()
        
        # Carrega a planilha Excel
        df = pd.read_excel('Cadastro_Visitantes.xlsx')
        
        # Renomeia as colunas para facilitar o trabalho
        colunas_mapeadas = {
            'Carimbo de data/hora': 'data_hora',
            'Quem está preenchendo a planilha?': 'preenchido_por',
            'Visita a Igreja Nova Vida de:': 'origem_visita',
            'Data da Visita': 'data_visita',
            'Culto': 'culto',
            'Nome do visitante': 'nome',
            'Telefone com DDD': 'telefone',
            'Bairro onde mora': 'bairro',
            'Cidade': 'cidade',
            'Como ele chegou até a Nova Vida?': 'como_chegou',
            'Pertence a alguma igreja ou religião?': 'pertence_igreja',
            'Faixa etaria': 'faixa_etaria',
            'Qual a necessidade do visitante?': 'necessidade',
            'Observações': 'observacoes'
        }
        
        df = df.rename(columns=colunas_mapeadas)
        
        # Converte datas
        if 'data_hora' in df.columns:
            df['data_hora'] = pd.to_datetime(df['data_hora'], errors='coerce')
        if 'data_visita' in df.columns:
            df['data_visita'] = pd.to_datetime(df['data_visita'], errors='coerce')
        
        # Remove linhas completamente vazias
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
        total_visitantes = len(df)
        st.metric(
            label="👥 Total de Visitantes",
            value=total_visitantes,
            delta=f"{total_visitantes} pessoas alcançadas"
        )
    
    with col2:
        if 'data_visita' in df.columns:
            visitas_mes = len(df[df['data_visita'].dt.month == datetime.now().month])
            st.metric(
                label="📅 Visitas Este Mês",
                value=visitas_mes,
                delta=f"{visitas_mes} novas visitas"
            )
        else:
            st.metric(label="📅 Visitas Este Mês", value="N/A")
    
    with col3:
        if 'cidade' in df.columns:
            cidades_unicas = df['cidade'].nunique()
            st.metric(
                label="🏘️ Cidades Alcançadas",
                value=cidades_unicas,
                delta=f"{cidades_unicas} cidades"
            )
        else:
            st.metric(label="🏘️ Cidades Alcançadas", value="N/A")
    
    with col4:
        if 'pertence_igreja' in df.columns:
            sem_igreja = len(df[df['pertence_igreja'].str.contains('Não', case=False, na=False)])
            st.metric(
                label="🙏 Sem Igreja",
                value=sem_igreja,
                delta=f"{sem_igreja} pessoas"
            )
        else:
            st.metric(label="🙏 Sem Igreja", value="N/A")

def criar_grafico_visitas_tempo(df):
    """Cria gráfico de visitas ao longo do tempo"""
    if 'data_visita' in df.columns and not df['data_visita'].isna().all():
        df_tempo = df.copy()
        df_tempo['data_visita'] = pd.to_datetime(df_tempo['data_visita'], errors='coerce')
        df_tempo = df_tempo.dropna(subset=['data_visita'])
        
        if not df_tempo.empty:
            # Agrupa por data
            visitas_por_data = df_tempo.groupby(df_tempo['data_visita'].dt.date).size().reset_index()
            visitas_por_data.columns = ['data', 'quantidade']
            
            fig = px.line(
                visitas_por_data, 
                x='data', 
                y='quantidade',
                title='📈 Evolução das Visitas ao Longo do Tempo',
                color_discrete_sequence=[CORES['verde_escuro']]
            )
            fig.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                title_font_color=CORES['verde_escuro']
            )
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_origem_visitas(df):
    """Cria gráfico de origem das visitas"""
    if 'origem_visita' in df.columns:
        origem_counts = df['origem_visita'].value_counts()
        
        if not origem_counts.empty:
            fig = px.pie(
                values=origem_counts.values,
                names=origem_counts.index,
                title='🌍 Origem dos Visitantes',
                color_discrete_sequence=[CORES['verde_escuro'], CORES['verde_claro'], CORES['verde_limao']]
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_faixa_etaria(df):
    """Cria gráfico de distribuição por faixa etária"""
    if 'faixa_etaria' in df.columns:
        faixa_counts = df['faixa_etaria'].value_counts()
        
        if not faixa_counts.empty:
            fig = px.bar(
                x=faixa_counts.index,
                y=faixa_counts.values,
                title='👶👨👴 Distribuição por Faixa Etária',
                color=faixa_counts.values,
                color_continuous_scale=[CORES['verde_claro'], CORES['verde_escuro']]
            )
            fig.update_layout(
                xaxis_title="Faixa Etária",
                yaxis_title="Quantidade",
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_necessidades(df):
    """Cria gráfico de necessidades dos visitantes"""
    if 'necessidade' in df.columns:
        necessidade_counts = df['necessidade'].value_counts().head(10)
        
        if not necessidade_counts.empty:
            fig = px.bar(
                x=necessidade_counts.values,
                y=necessidade_counts.index,
                orientation='h',
                title='💝 Principais Necessidades dos Visitantes',
                color=necessidade_counts.values,
                color_continuous_scale=[CORES['verde_claro'], CORES['verde_escuro']]
            )
            fig.update_layout(
                xaxis_title="Quantidade",
                yaxis_title="Necessidade",
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_cidades(df):
    """Cria gráfico de distribuição por cidades"""
    if 'cidade' in df.columns:
        cidade_counts = df['cidade'].value_counts().head(10)
        
        if not cidade_counts.empty:
            fig = px.bar(
                x=cidade_counts.index,
                y=cidade_counts.values,
                title='🏙️ Top 10 Cidades dos Visitantes',
                color=cidade_counts.values,
                color_continuous_scale=[CORES['verde_limao'], CORES['verde_escuro']]
            )
            fig.update_layout(
                xaxis_title="Cidade",
                yaxis_title="Quantidade",
                plot_bgcolor='white',
                paper_bgcolor='white'
            )
            st.plotly_chart(fig, use_container_width=True)

def criar_grafico_pertence_igreja(df):
    """Cria gráfico de visitantes que pertencem ou não a alguma igreja"""
    if 'pertence_igreja' in df.columns:
        igreja_counts = df['pertence_igreja'].value_counts()
        
        if not igreja_counts.empty:
            # Simplifica as respostas
            igreja_simplificado = []
            for resposta in igreja_counts.index:
                if pd.isna(resposta):
                    igreja_simplificado.append('Não informado')
                elif 'sim' in str(resposta).lower() or 'pertence' in str(resposta).lower():
                    igreja_simplificado.append('Pertence a alguma igreja')
                elif 'não' in str(resposta).lower() or 'nao' in str(resposta).lower():
                    igreja_simplificado.append('Não pertence')
                else:
                    igreja_simplificado.append('Outro')
            
            df_igreja = pd.DataFrame({
                'categoria': igreja_simplificado,
                'quantidade': igreja_counts.values
            })
            df_igreja = df_igreja.groupby('categoria')['quantidade'].sum()
            
            fig = px.pie(
                values=df_igreja.values,
                names=df_igreja.index,
                title='⛪ Situação Religiosa dos Visitantes',
                color_discrete_sequence=[CORES['verde_escuro'], CORES['verde_claro'], CORES['verde_limao']]
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

def main():
    # Header com logos
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        try:
            st.image("assets/Logo_Ministerio.png", width=120)
        except:
            st.markdown("🏛️")
    
    with col2:
        st.markdown("""
        <div class="header-section">
            <h1>Ministério Acolher</h1>
            <h2>Igreja Nova Vida - Maricá</h2>
            <h3>📊 Dashboard de Análise de Visitantes</h3>
            <p>Transformando vidas através do amor de Cristo</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        try:
            st.image("assets/Logo_Igreja.png", width=120)
        except:
            st.markdown("⛪")
    
    # Carrega os dados
    df = carregar_dados()
    
    if df.empty:
        st.error("❌ Não foi possível carregar os dados da planilha. Verifique se o arquivo 'Cadastro_Visitantes.xlsx' existe e está no formato correto.")
        return
    
    # Sidebar com informações
    st.sidebar.markdown(f"""
    <div style="background: linear-gradient(135deg, {CORES['verde_escuro']}, {CORES['verde_claro']}); 
                padding: 1rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 1rem;">
        <h3>📈 Sobre o Dashboard</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Logos na sidebar
    col_sidebar1, col_sidebar2 = st.sidebar.columns(2)
    with col_sidebar1:
        try:
            st.image("assets/Logo_Ministerio.png", width=80)
        except:
            st.markdown("🏛️")
    with col_sidebar2:
        try:
            st.image("assets/Logo_Igreja.png", width=80)
        except:
            st.markdown("⛪")
    
    st.sidebar.markdown("""
    ### 🎯 Objetivos do Ministério Acolher:
    - **Acolher** novos visitantes com amor
    - **Integrar** pessoas à família da igreja  
    - **Discipular** através de relacionamentos
    - **Transformar** vidas com o evangelho
    
    ### 📊 Métricas Importantes:
    - Total de visitantes alcançados
    - Origem das visitas
    - Necessidades identificadas
    - Distribuição geográfica
    - Perfil demográfico
    """)
    
    # Filtros
    st.sidebar.markdown("### 🔍 Filtros")
    
    # Filtro por período
    if 'data_visita' in df.columns and not df['data_visita'].isna().all():
        df['data_visita'] = pd.to_datetime(df['data_visita'], errors='coerce')
        data_min = df['data_visita'].min().date()
        data_max = df['data_visita'].max().date()
        
        periodo = st.sidebar.date_input(
            "Selecione o período:",
            value=(data_min, data_max),
            min_value=data_min,
            max_value=data_max
        )
        
        if len(periodo) == 2:
            df = df[(df['data_visita'].dt.date >= periodo[0]) & 
                   (df['data_visita'].dt.date <= periodo[1])]
    
    # Filtro por cidade
    if 'cidade' in df.columns:
        cidades = ['Todas'] + sorted(df['cidade'].dropna().unique().tolist())
        cidade_selecionada = st.sidebar.selectbox("Cidade:", cidades)
        
        if cidade_selecionada != 'Todas':
            df = df[df['cidade'] == cidade_selecionada]
    
    # Métricas principais
    st.markdown("## 📊 Métricas Principais")
    criar_metricas_principais(df)
    
    # Seção de insights
    st.markdown("## 💡 Insights Importantes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="info-box">
            <h4>🎯 Foco de Evangelização</h4>
            <p>Baseado nos dados coletados, podemos identificar as principais necessidades dos visitantes e direcionar melhor nossos esforços de discipulado.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="info-box">
            <h4>📈 Crescimento da Igreja</h4>
            <p>Cada visitante representa uma oportunidade de transformação. O acompanhamento sistemático nos ajuda a não perder nenhuma dessas oportunidades.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Gráficos principais
    st.markdown("## 📈 Análises Detalhadas")
    
    # Primeira linha de gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        criar_grafico_origem_visitas(df)
    
    with col2:
        criar_grafico_pertence_igreja(df)
    
    # Segunda linha de gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        criar_grafico_faixa_etaria(df)
    
    with col2:
        criar_grafico_necessidades(df)
    
    # Terceira linha de gráficos
    st.markdown("### 🌍 Distribuição Geográfica")
    criar_grafico_cidades(df)
    
    # Gráfico de evolução temporal
    st.markdown("### 📅 Evolução Temporal")
    criar_grafico_visitas_tempo(df)
    
    # Tabela de dados
    st.markdown("## 📋 Dados Detalhados")
    
    if st.checkbox("Mostrar tabela de dados"):
        # Seleciona colunas importantes para exibição
        colunas_exibir = ['nome', 'data_visita', 'cidade', 'faixa_etaria', 'necessidade', 'pertence_igreja']
        colunas_disponiveis = [col for col in colunas_exibir if col in df.columns]
        
        if colunas_disponiveis:
            st.dataframe(df[colunas_disponiveis], use_container_width=True)
        else:
            st.dataframe(df, use_container_width=True)
    
    # Rodapé
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: {CORES['verde_escuro']}; padding: 2rem;">
        <h4>Ministério Acolher - Igreja Nova Vida Maricá</h4>
        <p><em>"Portanto, ide, ensinai todas as nações, batizando-as em nome do Pai, e do Filho, e do Espírito Santo."</em> - Mateus 28:19</p>
        <p>Desenvolvido por <strong> <a href="https://www.instagram.com/tiagobombista" target="_blank" style="color: {CORES['verde_escuro']}; text-decoration: underline;">@TiagoBombista</a></strong> com ❤️ para o crescimento do Reino de Deus</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
