# 📊 Guia de Atualização - Dashboard Ministério Acolher

## 🔄 Como Atualizar os Dados Semanalmente

### 📋 Processo Recomendado

1. **Receba a nova planilha** (via WhatsApp, email, etc.)
2. **Salve na pasta do projeto** ou anote o caminho
3. **Execute a atualização** usando um dos métodos abaixo
4. **Verifique o dashboard** para confirmar que tudo está funcionando

---

## 🚀 Métodos de Atualização

### ⚡ Método 1: Atualização Rápida (Recomendado)

**Para quando você quer apenas substituir a planilha atual:**

1. **Clique duas vezes** em `atualizar_dados.bat`
2. **Escolha opção 2** (Atualização rápida)
3. **Digite o caminho** do novo arquivo Excel
4. **Pronto!** O backup é feito automaticamente

**Ou via linha de comando:**

```bash
python atualizar_rapido.py "caminho/para/nova_planilha.xlsx"
```

### 🔧 Método 2: Atualização Completa

**Para quando você quer mais controle:**

1. **Clique duas vezes** em `atualizar_dados.bat`
2. **Escolha opção 1** (Atualização completa)
3. **Siga o menu interativo:**
   - Opção 1: Adicionar dados à planilha existente
   - Opção 2: Substituir completamente a planilha
   - Opção 3: Ver estatísticas da planilha atual
   - Opção 4: Listar backups disponíveis

### 📁 Método 3: Manual

**Para usuários avançados:**

1. **Faça backup manual** da planilha atual
2. **Substitua** o arquivo `Cadastro_Visitantes.xlsx`
3. **Execute** `streamlit run app.py`

---

## 💾 Sistema de Backups

### 🔒 Backup Automático

- **Sempre** é feito backup antes de qualquer alteração
- **Pasta:** `backups/`
- **Formato:** `backup_Cadastro_Visitantes_AAAAMMDD_HHMMSS.xlsx`
- **Retenção:** Manter pelo menos 4 backups (1 mês)

### 📁 Estrutura de Backups

```
backups/
├── backup_Cadastro_Visitantes_20240115_143022.xlsx
├── backup_Cadastro_Visitantes_20240122_091545.xlsx
├── backup_Cadastro_Visitantes_20240129_162030.xlsx
└── backup_Cadastro_Visitantes_20240205_104512.xlsx
```

---

## 📋 Checklist Semanal

### ✅ Antes da Atualização

- [ ] Nova planilha recebida
- [ ] Verificar se o arquivo não está corrompido
- [ ] Confirmar que tem as colunas corretas
- [ ] Fazer backup manual (opcional, pois é automático)

### ✅ Durante a Atualização

- [ ] Executar script de atualização
- [ ] Verificar se não houve erros
- [ ] Confirmar número de registros
- [ ] Verificar se backup foi criado

### ✅ Após a Atualização

- [ ] Executar o dashboard (`streamlit run app.py`)
- [ ] Verificar se os dados aparecem corretamente
- [ ] Testar filtros e gráficos
- [ ] Confirmar que as logos estão aparecendo
- [ ] Documentar qualquer problema encontrado

---

## 🛠️ Solução de Problemas

### ❌ Erro: "Arquivo não encontrado"

**Solução:** Verifique o caminho do arquivo e se ele realmente existe

### ❌ Erro: "Planilha corrompida"

**Solução:**

1. Abra o arquivo no Excel para verificar
2. Salve novamente como .xlsx
3. Tente novamente

### ❌ Erro: "Colunas diferentes"

**Solução:**

1. Verifique se a planilha tem as colunas corretas
2. Compare com a planilha anterior
3. Ajuste as colunas se necessário

### ❌ Dashboard não mostra dados novos

**Solução:**

1. Pare o Streamlit (Ctrl+C)
2. Execute novamente: `streamlit run app.py`
3. Limpe o cache do navegador (F5)

---

## 📞 Suporte

### 🆘 Problemas Técnicos

- Verifique os logs de erro
- Consulte este guia
- Entre em contato com o desenvolvedor

### 📧 Contato

Para dúvidas sobre o processo de atualização ou problemas técnicos.

---

## 📈 Dicas Importantes

### 💡 Boas Práticas

1. **Sempre** faça backup antes de alterações importantes
2. **Teste** o dashboard após cada atualização
3. **Mantenha** os backups organizados
4. **Documente** qualquer problema encontrado
5. **Treine** outras pessoas da equipe no processo

### 🎯 Objetivos

- **Manter** dados sempre atualizados
- **Preservar** histórico de visitantes
- **Facilitar** análise de crescimento
- **Melhorar** acompanhamento pastoral

---

_Desenvolvido com ❤️ para o crescimento do Reino de Deus_

**"E disse-lhes: Ide por todo o mundo, pregai o evangelho a toda criatura."** - Marcos 16:15
