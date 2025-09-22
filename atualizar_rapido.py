"""
Script de atualização rápida - apenas substitui a planilha
Use este script quando receber uma nova planilha semanal
"""

import pandas as pd
import shutil
from datetime import datetime
import os
import sys

def atualizar_rapido():
    """Atualização rápida da planilha"""
    
    # Verifica se foi passado um arquivo como argumento
    if len(sys.argv) > 1:
        novo_arquivo = sys.argv[1]
    else:
        novo_arquivo = input("Digite o caminho do novo arquivo Excel: ").strip()
    
    if not os.path.exists(novo_arquivo):
        print(f"❌ Arquivo não encontrado: {novo_arquivo}")
        return False
    
    try:
        # Cria pasta de backups se não existir
        if not os.path.exists('backups'):
            os.makedirs('backups')
        
        # Faz backup da planilha atual
        if os.path.exists('Cadastro_Visitantes.xlsx'):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f'backups/backup_Cadastro_Visitantes_{timestamp}.xlsx'
            shutil.copy2('Cadastro_Visitantes.xlsx', backup_name)
            print(f"✅ Backup criado: {backup_name}")
        
        # Substitui a planilha
        shutil.copy2(novo_arquivo, 'Cadastro_Visitantes.xlsx')
        
        # Mostra estatísticas
        df = pd.read_excel('Cadastro_Visitantes.xlsx')
        print(f"✅ Planilha atualizada com sucesso!")
        print(f"📈 Total de registros: {len(df)}")
        
        if 'Cidade' in df.columns:
            print(f"🏘️  Cidades: {df['Cidade'].nunique()}")
        
        if 'Data da Visita' in df.columns:
            df['Data da Visita'] = pd.to_datetime(df['Data da Visita'], errors='coerce')
            print(f"📅 Período: {df['Data da Visita'].min().date()} até {df['Data da Visita'].max().date()}")
        
        print("\n🚀 Agora você pode executar o dashboard:")
        print("   streamlit run app.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔄 Atualização Rápida - Ministério Acolher")
    print("=" * 40)
    atualizar_rapido()
