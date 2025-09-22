"""
Script para atualizar os dados do dashboard
Permite substituir ou adicionar dados à planilha Cadastro_Visitantes.xlsx
"""

import pandas as pd
import shutil
from datetime import datetime
import os

def fazer_backup():
    """Faz backup da planilha atual"""
    if os.path.exists('Cadastro_Visitantes.xlsx'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f'backup_Cadastro_Visitantes_{timestamp}.xlsx'
        shutil.copy2('Cadastro_Visitantes.xlsx', f'backups/{backup_name}')
        print(f"✅ Backup criado: backups/{backup_name}")
        return True
    return False

def criar_pasta_backups():
    """Cria pasta de backups se não existir"""
    if not os.path.exists('backups'):
        os.makedirs('backups')
        print("📁 Pasta 'backups' criada")

def atualizar_planilha(novo_arquivo):
    """
    Atualiza a planilha principal com novos dados
    
    Args:
        novo_arquivo (str): Caminho para o novo arquivo Excel
    """
    try:
        # Cria pasta de backups
        criar_pasta_backups()
        
        # Faz backup do arquivo atual
        fazer_backup()
        
        # Carrega o novo arquivo
        novo_df = pd.read_excel(novo_arquivo)
        
        # Verifica se já existe um arquivo principal
        if os.path.exists('Cadastro_Visitantes.xlsx'):
            # Carrega dados existentes
            df_existente = pd.read_excel('Cadastro_Visitantes.xlsx')
            
            # Combina os dados (remove duplicatas baseado no nome e data)
            df_combinação = pd.concat([df_existente, novo_df], ignore_index=True)
            
            # Remove duplicatas baseado em nome e data da visita
            if 'Nome do visitante' in df_combinação.columns and 'Data da Visita' in df_combinação.columns:
                df_combinação = df_combinação.drop_duplicates(
                    subset=['Nome do visitante', 'Data da Visita'], 
                    keep='last'
                )
                print(f"🔄 Dados combinados. Total de registros únicos: {len(df_combinação)}")
            else:
                print(f"🔄 Dados combinados. Total de registros: {len(df_combinação)}")
        else:
            df_combinação = novo_df
            print(f"📊 Novo arquivo criado com {len(df_combinação)} registros")
        
        # Salva o arquivo atualizado
        df_combinação.to_excel('Cadastro_Visitantes.xlsx', index=False)
        
        print(f"✅ Planilha atualizada com sucesso!")
        print(f"📈 Total de registros: {len(df_combinação)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao atualizar planilha: {str(e)}")
        return False

def substituir_planilha(novo_arquivo):
    """
    Substitui completamente a planilha principal
    
    Args:
        novo_arquivo (str): Caminho para o novo arquivo Excel
    """
    try:
        # Cria pasta de backups
        criar_pasta_backups()
        
        # Faz backup do arquivo atual
        fazer_backup()
        
        # Copia o novo arquivo
        shutil.copy2(novo_arquivo, 'Cadastro_Visitantes.xlsx')
        
        # Verifica quantos registros tem
        df = pd.read_excel('Cadastro_Visitantes.xlsx')
        print(f"✅ Planilha substituída com sucesso!")
        print(f"📈 Total de registros: {len(df)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao substituir planilha: {str(e)}")
        return False

def main():
    """Interface principal do script"""
    print("=" * 50)
    print("  MINISTÉRIO ACOLHER - ATUALIZADOR DE DADOS")
    print("  Igreja Nova Vida de Maricá")
    print("=" * 50)
    print()
    
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar dados à planilha existente")
        print("2. Substituir completamente a planilha")
        print("3. Ver estatísticas da planilha atual")
        print("4. Listar backups disponíveis")
        print("5. Sair")
        print()
        
        opcao = input("Digite sua opção (1-5): ").strip()
        
        if opcao == "1":
            arquivo = input("Digite o caminho do arquivo Excel com novos dados: ").strip()
            if os.path.exists(arquivo):
                atualizar_planilha(arquivo)
            else:
                print("❌ Arquivo não encontrado!")
            print()
            
        elif opcao == "2":
            arquivo = input("Digite o caminho do arquivo Excel para substituir: ").strip()
            if os.path.exists(arquivo):
                confirmar = input("⚠️  Isso substituirá todos os dados atuais. Confirma? (s/n): ").strip().lower()
                if confirmar == 's':
                    substituir_planilha(arquivo)
                else:
                    print("❌ Operação cancelada.")
            else:
                print("❌ Arquivo não encontrado!")
            print()
            
        elif opcao == "3":
            if os.path.exists('Cadastro_Visitantes.xlsx'):
                try:
                    df = pd.read_excel('Cadastro_Visitantes.xlsx')
                    print(f"📊 Estatísticas da planilha atual:")
                    print(f"   - Total de registros: {len(df)}")
                    if 'Cidade' in df.columns:
                        print(f"   - Cidades únicas: {df['Cidade'].nunique()}")
                    if 'Data da Visita' in df.columns:
                        df['Data da Visita'] = pd.to_datetime(df['Data da Visita'], errors='coerce')
                        print(f"   - Período: {df['Data da Visita'].min().date()} até {df['Data da Visita'].max().date()}")
                    print()
                except Exception as e:
                    print(f"❌ Erro ao ler planilha: {str(e)}")
            else:
                print("❌ Planilha não encontrada!")
            print()
            
        elif opcao == "4":
            if os.path.exists('backups'):
                backups = [f for f in os.listdir('backups') if f.endswith('.xlsx')]
                if backups:
                    print("📁 Backups disponíveis:")
                    for backup in sorted(backups, reverse=True)[:10]:  # Mostra os 10 mais recentes
                        print(f"   - {backup}")
                else:
                    print("📁 Nenhum backup encontrado.")
            else:
                print("📁 Pasta de backups não existe.")
            print()
            
        elif opcao == "5":
            print("👋 Até logo! Que Deus abençoe o ministério!")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.")
            print()

if __name__ == "__main__":
    main()
