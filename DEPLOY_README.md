# 🚀 Deploy no Streamlit Cloud - Dashboard Ministério Acolher

## 📋 Checklist para Deploy

### ✅ Arquivos Necessários

Certifique-se de que estes arquivos estão no repositório:

- [x] `app.py` - Aplicação principal
- [x] `requirements.txt` - Dependências Python
- [x] `packages.txt` - Dependências do sistema (opcional)
- [x] `.streamlit/config.toml` - Configurações do Streamlit
- [x] `.streamlit/secrets.toml` - Configurações sensíveis
- [x] `dados_exemplo.py` - Script para criar dados de exemplo
- [x] `.gitignore` - Arquivos a serem ignorados
- [x] `assets/Logo_Ministerio.png` - Logo do Ministério
- [x] `assets/Logo_Igreja.png` - Logo da Igreja

### ✅ Configurações do Repositório

1. **Subir para GitHub:**

   ```bash
   git add .
   git commit -m "Deploy dashboard Ministério Acolher"
   git push origin main
   ```

2. **No Streamlit Cloud:**
   - Repository: `seu-usuario/seu-repositorio`
   - Branch: `main`
   - Main file path: `app.py`

## 🔧 Solução de Problemas Comuns

### ❌ Erro: "Error installing requirements"

**Soluções:**

1. **Verifique o requirements.txt:**

   ```
   streamlit>=1.28.0
   pandas>=2.0.0
   plotly>=5.0.0
   openpyxl>=3.1.0
   numpy>=1.24.0
   ```

2. **Adicione packages.txt (se necessário):**

   ```
   # Deixe vazio ou adicione pacotes do sistema
   ```

3. **Verifique a estrutura de pastas:**
   ```
   seu-repositorio/
   ├── app.py
   ├── requirements.txt
   ├── packages.txt
   ├── .streamlit/
   │   ├── config.toml
   │   └── secrets.toml
   ├── assets/
   │   ├── Logo_Ministerio.png
   │   └── Logo_Igreja.png
   └── dados_exemplo.py
   ```

### ❌ Erro: "File not found"

**Solução:**

- Certifique-se de que as logos estão na pasta `assets/`
- Verifique se o arquivo `dados_exemplo.py` está na raiz

### ❌ Erro: "Import error"

**Solução:**

- Verifique se todas as dependências estão no `requirements.txt`
- Use versões compatíveis (>= em vez de ==)

## 🎯 Configurações Recomendadas

### 📁 Estrutura Final do Repositório

```
ministerio-acolher-dashboard/
├── app.py                    # ✅ Aplicação principal
├── requirements.txt          # ✅ Dependências
├── packages.txt             # ✅ Pacotes do sistema
├── dados_exemplo.py         # ✅ Dados de exemplo
├── .gitignore              # ✅ Arquivos ignorados
├── README.md               # ✅ Documentação
├── .streamlit/
│   ├── config.toml         # ✅ Configurações
│   └── secrets.toml        # ✅ Configurações sensíveis
└── assets/
    ├── Logo_Ministerio.png # ✅ Logo do Ministério
    └── Logo_Igreja.png     # ✅ Logo da Igreja
```

### ⚙️ Configurações do Streamlit Cloud

1. **App URL:** `https://seu-app.streamlit.app`
2. **Repository:** `https://github.com/seu-usuario/seu-repositorio`
3. **Branch:** `main`
4. **Main file path:** `app.py`

## 📊 Funcionalidades no Deploy

### ✅ O que Funciona

- Dashboard completo com todos os gráficos
- Logos do Ministério e da Igreja
- Dados de exemplo automáticos
- Filtros interativos
- Design responsivo
- Métricas em tempo real

### 📝 Dados no Deploy

- **Dados de exemplo:** 200 registros simulados
- **Período:** Últimos 12 meses
- **Cidades:** 15 cidades da região
- **Necessidades:** 15 tipos diferentes
- **Faixas etárias:** 8 categorias

## 🔄 Atualização de Dados

### 💡 Para Dados Reais

1. **Substitua** o arquivo `dados_exemplo.py` por sua planilha real
2. **Renomeie** sua planilha para `Cadastro_Visitantes.xlsx`
3. **Faça commit** e push das alterações
4. **O Streamlit Cloud** fará redeploy automaticamente

### 📋 Processo de Atualização

```bash
# 1. Substitua a planilha
cp sua_planilha.xlsx Cadastro_Visitantes.xlsx

# 2. Faça commit
git add Cadastro_Visitantes.xlsx
git commit -m "Atualização de dados - $(date)"

# 3. Faça push
git push origin main
```

## 🆘 Suporte

### 📞 Problemas Técnicos

1. **Verifique os logs** no Streamlit Cloud
2. **Consulte** este guia
3. **Entre em contato** com o desenvolvedor

### 🔗 Links Úteis

- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Deploy Guide](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)
- [Troubleshooting](https://docs.streamlit.io/streamlit-community-cloud/troubleshooting)

---

_Desenvolvido com ❤️ para o crescimento do Reino de Deus_

**"E disse-lhes: Ide por todo o mundo, pregai o evangelho a toda criatura."** - Marcos 16:15
