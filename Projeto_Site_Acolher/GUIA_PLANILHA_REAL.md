# 📊 Guia para Usar Planilha Real no Deploy

## 🎯 Problema Resolvido

O deploy estava usando dados de exemplo em vez da sua planilha real. Agora você pode facilmente subir sua planilha real para o Streamlit Cloud.

## 🚀 Como Usar Sua Planilha Real

### 📋 Método 1: Automático (Recomendado)

1. **Execute o script preparador:**

   ```bash
   python subir_planilha_real.py
   ```

   Ou clique duas vezes em `preparar_deploy.bat`

2. **Escolha opção 1** (Preparar planilha real)

3. **O script irá:**

   - ✅ Encontrar sua planilha automaticamente
   - ✅ Fazer backup dos dados de exemplo
   - ✅ Preparar a planilha real
   - ✅ Dar instruções para o git

4. **Execute os comandos git:**

   ```bash
   git add .
   git commit -m "Adicionar planilha real dos visitantes"
   git push origin main
   ```

5. **Pronto!** O Streamlit Cloud fará redeploy automaticamente

### 📁 Método 2: Manual

1. **Renomeie sua planilha** para `Cadastro_Visitantes.xlsx`

2. **Substitua** o arquivo no repositório

3. **Faça commit:**
   ```bash
   git add Cadastro_Visitantes.xlsx
   git commit -m "Atualizar com planilha real"
   git push origin main
   ```

## 📋 Arquivos Reconhecidos

O script procura automaticamente por estes nomes:

- `Cadastro_Visitantes.xlsx`
- `cadastro_visitantes.xlsx`
- `visitantes.xlsx`
- `dados_visitantes.xlsx`

## ✅ Verificações Automáticas

### 🔍 O que o Sistema Verifica:

1. **Existência da planilha** - Procura por arquivos Excel
2. **Quantidade de dados** - Verifica se tem dados reais (>1 linha)
3. **Estrutura das colunas** - Confirma se tem as colunas esperadas
4. **Backup automático** - Salva dados de exemplo antes de substituir

### 📊 Mensagens do Sistema:

- ✅ **"Dados reais carregados com sucesso!"** - Planilha real funcionando
- ⚠️ **"Planilha encontrada mas com poucos dados"** - Poucos registros, usando exemplo
- 📊 **"Planilha não encontrada. Criando dados de exemplo"** - Sem planilha, usando exemplo

## 🔄 Alternar Entre Dados

### 📊 Para Voltar aos Dados de Exemplo:

```bash
python subir_planilha_real.py
# Escolha opção 2: Restaurar dados de exemplo
```

### 📋 Para Usar Planilha Real:

```bash
python subir_planilha_real.py
# Escolha opção 1: Preparar planilha real
```

## 🛠️ Solução de Problemas

### ❌ "Nenhuma planilha encontrada"

**Solução:**

1. Verifique se o arquivo está na pasta do projeto
2. Renomeie para `Cadastro_Visitantes.xlsx`
3. Execute o script novamente

### ❌ "Planilha com poucos dados"

**Solução:**

1. Verifique se a planilha tem dados reais
2. Confirme se não está vazia
3. Verifique se tem mais de 1 linha de dados

### ❌ "Erro no git push"

**Solução:**

1. Verifique se está no repositório correto
2. Confirme se tem permissões
3. Execute `git status` para ver o estado

## 📈 Estrutura da Planilha Esperada

### 📋 Colunas Necessárias:

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
- Faixa etaria
- Qual a necessidade do visitante?
- Observações

## 🎯 Benefícios

### ✅ Vantagens do Sistema:

1. **Automático** - Detecta planilha automaticamente
2. **Seguro** - Faz backup antes de alterar
3. **Flexível** - Aceita diferentes nomes de arquivo
4. **Verificação** - Confirma se tem dados reais
5. **Reversível** - Pode voltar aos dados de exemplo

### 📊 Resultado:

- **Dashboard real** com seus dados de visitantes
- **Gráficos precisos** baseados na realidade
- **Métricas corretas** da sua igreja
- **Análises verdadeiras** do crescimento

## 📞 Suporte

### 🆘 Problemas:

1. **Execute** `python subir_planilha_real.py` opção 3 para verificar arquivos
2. **Consulte** este guia
3. **Entre em contato** com o desenvolvedor

### 📧 Contato:

Para dúvidas sobre o processo de upload da planilha real.

---

_Desenvolvido com ❤️ para o crescimento do Reino de Deus_

**"E disse-lhes: Ide por todo o mundo, pregai o evangelho a toda criatura."** - Marcos 16:15
