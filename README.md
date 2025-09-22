# 🏛️ Ministério Acolher - Dashboard de Visitantes

Dashboard interativo para análise de dados de visitantes da Igreja Nova Vida de Maricá, desenvolvido com Streamlit.

## 🎯 Objetivo

Este dashboard foi criado para ajudar o Ministério Acolher a:

- Analisar padrões de visitantes
- Identificar necessidades da comunidade
- Acompanhar o crescimento da igreja
- Direcionar melhor os esforços de evangelização

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Arquivo `Cadastro_Visitantes.xlsx` na raiz do projeto

### Instalação Rápida (Windows)

1. Clone ou baixe este projeto
2. Execute o arquivo `instalar_e_executar.bat`
3. O script irá:
   - Verificar se o Python está instalado
   - Instalar todas as dependências automaticamente
   - Criar dados de exemplo se necessário
   - Iniciar o dashboard

### Instalação Manual

1. Clone ou baixe este projeto
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o dashboard:

```bash
streamlit run app.py
```

4. Abra seu navegador em `http://localhost:8501`

### Dados de Exemplo

Se você não tiver a planilha `Cadastro_Visitantes.xlsx`, pode criar dados de exemplo executando:

```bash
python exemplo_dados.py
```

## 🔄 Atualização de Dados

### Atualização Semanal (Recomendado)

**Método mais fácil:**

1. Clique duas vezes em `atualizar_dados.bat`
2. Escolha "Atualização rápida"
3. Digite o caminho da nova planilha
4. Pronto! Backup automático + dados atualizados

**Método via linha de comando:**

```bash
python atualizar_rapido.py "caminho/para/nova_planilha.xlsx"
```

### Recursos de Atualização

- ✅ **Backup automático** antes de cada alteração
- ✅ **Combinação de dados** (adicionar à planilha existente)
- ✅ **Substituição completa** (nova planilha)
- ✅ **Verificação de duplicatas**
- ✅ **Estatísticas detalhadas**
- ✅ **Histórico de backups**

📖 **Guia completo:** Consulte `GUIA_ATUALIZACAO.md` para instruções detalhadas

## 📊 Funcionalidades

### Métricas Principais

- Total de visitantes
- Visitas do mês atual
- Cidades alcançadas
- Pessoas sem igreja

### Gráficos e Análises

- **Origem dos Visitantes**: Gráfico de pizza mostrando de onde vêm os visitantes
- **Situação Religiosa**: Distribuição entre quem pertence ou não a alguma igreja
- **Faixa Etária**: Perfil demográfico dos visitantes
- **Necessidades**: Principais necessidades identificadas
- **Distribuição Geográfica**: Top 10 cidades dos visitantes
- **Evolução Temporal**: Gráfico de linha mostrando o crescimento ao longo do tempo

### Filtros Interativos

- Filtro por período de datas
- Filtro por cidade
- Visualização de dados detalhados

## 🎨 Design

O dashboard utiliza a paleta de cores oficial do Ministério Acolher:

- Verde Escuro: `#7dba52`
- Verde Claro: `#8fc866`
- Verde Limão: `#ccff4a`
- Branco: `#ffffff`

## 📁 Estrutura do Projeto

```
Projeto_Site_Acolher/
├── app.py                           # Aplicação principal
├── requirements.txt                 # Dependências Python
├── README.md                       # Este arquivo
├── GUIA_ATUALIZACAO.md             # Guia completo de atualização
├── COMO_USAR.txt                   # Instruções simples
├── Cadastro_Visitantes.xlsx        # Dados dos visitantes
├── exemplo_dados.py                # Script para criar dados de exemplo
├── atualizar_dados.py              # Script de atualização completa
├── atualizar_rapido.py             # Script de atualização rápida
├── atualizar_dados.bat             # Script batch para atualização
├── instalar_e_executar.bat         # Script de instalação automática
├── run_dashboard.bat               # Script para executar o dashboard
├── backups/                        # Pasta de backups automáticos
├── .streamlit/
│   └── config.toml                 # Configurações do Streamlit
└── assets/
    ├── Logo_Igreja.png             # Logo da Igreja Nova Vida
    └── Logo_Ministerio.png         # Logo do Ministério Acolher
```

## 📋 Estrutura dos Dados

O dashboard espera uma planilha Excel com as seguintes colunas:

- Carimbo de data/hora
- Quem está preenchendo a planilha?
- Visita a Igreja Nova Vida de:
- Data da Visita
- Culto
- Nome do visitante
- Telefone com DDD
- Bairro onde mora
- Cidade
- Como ele chegou até a Nova Vida?
- Pertence a alguma igreja ou religião?
- Faixa etária
- Qual a necessidade do visitante?
- Observações

## 🔧 Personalização

Para personalizar o dashboard:

1. Modifique as cores em `app.py` (variável `CORES`)
2. Adicione novos gráficos criando funções similares às existentes
3. Ajuste os filtros na sidebar conforme necessário

## 📞 Suporte

Para dúvidas ou sugestões, entre em contato com a equipe de desenvolvimento.

---

_Desenvolvido com ❤️ para o crescimento do Reino de Deus_

**"Portanto, ide, ensinai todas as nações, batizando-as em nome do Pai, e do Filho, e do Espírito Santo."** - Mateus 28:19
