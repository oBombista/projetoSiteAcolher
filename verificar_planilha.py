"""
Script para verificar se a planilha está sendo enviada corretamente
"""

import os
import pandas as pd

def verificar_planilha():
    """Verifica se a planilha está presente e acessível"""
    
    print("🔍 Verificando planilha no repositório...")
    print("=" * 50)
    
    # Lista todos os arquivos
    print("📁 Arquivos na pasta atual:")
    try:
        arquivos = os.listdir('.')
        for arquivo in sorted(arquivos):
            print(f"   {arquivo}")
    except Exception as e:
        print(f"❌ Erro ao listar arquivos: {e}")
        return False
    
    # Procura por arquivos Excel
    print("\n📊 Arquivos Excel encontrados:")
    arquivos_excel = [f for f in arquivos if f.endswith('.xlsx')]
    
    if arquivos_excel:
        for arquivo in arquivos_excel:
            try:
                tamanho = os.path.getsize(arquivo)
                print(f"   ✅ {arquivo} ({tamanho} bytes)")
                
                # Tenta ler a planilha
                try:
                    df = pd.read_excel(arquivo)
                    print(f"      📋 Colunas: {len(df.columns)}")
                    print(f"      📊 Registros: {len(df)}")
                    print(f"      📝 Primeiras colunas: {list(df.columns[:3])}")
                except Exception as e:
                    print(f"      ❌ Erro ao ler planilha: {e}")
                    
            except Exception as e:
                print(f"   ❌ Erro ao verificar {arquivo}: {e}")
    else:
        print("   ❌ Nenhum arquivo Excel encontrado!")
        return False
    
    # Verifica especificamente a planilha esperada
    print("\n🎯 Verificação específica:")
    arquivos_esperados = [
        'Cadastro_Visitantes.xlsx',
        'cadastro_visitantes.xlsx',
        'visitantes.xlsx',
        'dados_visitantes.xlsx'
    ]
    
    planilha_encontrada = None
    for arquivo in arquivos_esperados:
        if os.path.exists(arquivo):
            planilha_encontrada = arquivo
            print(f"✅ {arquivo} - ENCONTRADO!")
            break
        else:
            print(f"❌ {arquivo} - Não encontrado")
    
    if planilha_encontrada:
        print(f"\n🎉 Planilha encontrada: {planilha_encontrada}")
        
        # Verifica o conteúdo
        try:
            df = pd.read_excel(planilha_encontrada)
            print(f"📊 Total de registros: {len(df)}")
            print(f"📋 Total de colunas: {len(df.columns)}")
            
            # Verifica se tem as colunas esperadas
            colunas_esperadas = [
                'Carimbo de data/hora',
                'Nome do visitante',
                'Cidade',
                'Data da Visita'
            ]
            
            print("\n🔍 Verificação de colunas:")
            for coluna in colunas_esperadas:
                if coluna in df.columns:
                    print(f"   ✅ {coluna}")
                else:
                    print(f"   ❌ {coluna} - Não encontrada")
            
            # Mostra algumas colunas disponíveis
            print(f"\n📝 Colunas disponíveis:")
            for i, coluna in enumerate(df.columns[:10]):  # Primeiras 10 colunas
                print(f"   {i+1}. {coluna}")
            
            if len(df.columns) > 10:
                print(f"   ... e mais {len(df.columns) - 10} colunas")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao ler planilha: {e}")
            return False
    else:
        print("\n❌ Nenhuma planilha esperada encontrada!")
        return False

def criar_planilha_teste():
    """Cria uma planilha de teste para verificar se o sistema funciona"""
    
    print("\n🧪 Criando planilha de teste...")
    
    dados_teste = {
        'Carimbo de data/hora': ['15/01/2024 10:00:00'],
        'Quem está preenchendo a planilha?': ['Pastor João'],
        'Visita a Igreja Nova Vida de:': ['Indicação de amigo'],
        'Data da Visita': ['15/01/2024'],
        'Culto': ['Culto de domingo manhã'],
        'Nome do visitante': ['Visitante Teste'],
        'Telefone com DDD': ['(21) 99999-9999'],
        'Bairro onde mora': ['Centro'],
        'Cidade': ['Maricá'],
        'Como ele chegou até a Nova Vida?': ['Indicação de membro'],
        'Pertence a alguma igreja ou religião?': ['Não, não pertence a nenhuma igreja'],
        'Faixa etaria': ['26-35 anos'],
        'Qual a necessidade do visitante?': ['Orientação espiritual'],
        'Observações': ['Teste de planilha']
    }
    
    try:
        df = pd.DataFrame(dados_teste)
        df.to_excel('Cadastro_Visitantes.xlsx', index=False)
        print("✅ Planilha de teste criada: Cadastro_Visitantes.xlsx")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar planilha de teste: {e}")
        return False

def main():
    """Interface principal"""
    
    print("🔍 Verificador de Planilha - Ministério Acolher")
    print("=" * 50)
    
    # Verifica se a planilha existe
    sucesso = verificar_planilha()
    
    if not sucesso:
        print("\n❓ Deseja criar uma planilha de teste? (s/n)")
        resposta = input().strip().lower()
        
        if resposta == 's':
            criar_planilha_teste()
            print("\n🔄 Verificando novamente...")
            verificar_planilha()
    
    print("\n" + "=" * 50)
    print("✅ Verificação concluída!")

if __name__ == "__main__":
    main()
