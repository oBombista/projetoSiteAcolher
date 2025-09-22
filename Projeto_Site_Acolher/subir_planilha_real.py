"""
Script para preparar a planilha real para o deploy
Este script ajuda a subir a planilha real para o repositório GitHub
"""

import os
import shutil
from datetime import datetime

def preparar_planilha_real():
    """Prepara a planilha real para o deploy"""
    
    print("🔄 Preparando planilha real para deploy...")
    print("=" * 50)
    
    # Verifica se existe uma planilha real
    arquivos_planilha = [
        'Cadastro_Visitantes.xlsx',
        'cadastro_visitantes.xlsx',
        'visitantes.xlsx',
        'dados_visitantes.xlsx'
    ]
    
    planilha_encontrada = None
    for arquivo in arquivos_planilha:
        if os.path.exists(arquivo):
            planilha_encontrada = arquivo
            break
    
    if not planilha_encontrada:
        print("❌ Nenhuma planilha encontrada!")
        print("📋 Arquivos procurados:")
        for arquivo in arquivos_planilha:
            print(f"   - {arquivo}")
        print("\n💡 Dica: Renomeie sua planilha para 'Cadastro_Visitantes.xlsx'")
        return False
    
    print(f"✅ Planilha encontrada: {planilha_encontrada}")
    
    # Faz backup dos dados de exemplo se existirem
    if os.path.exists('dados_exemplo_backup.py'):
        os.remove('dados_exemplo_backup.py')
    
    if os.path.exists('dados_exemplo.py'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f'dados_exemplo_backup_{timestamp}.py'
        shutil.copy2('dados_exemplo.py', backup_name)
        print(f"📁 Backup dos dados de exemplo: {backup_name}")
    
    # Copia a planilha real para o nome correto
    if planilha_encontrada != 'Cadastro_Visitantes.xlsx':
        shutil.copy2(planilha_encontrada, 'Cadastro_Visitantes.xlsx')
        print(f"📋 Planilha copiada para: Cadastro_Visitantes.xlsx")
    
    # Cria um arquivo de dados de exemplo vazio (para não sobrescrever)
    with open('dados_exemplo.py', 'w', encoding='utf-8') as f:
        f.write('''
"""
Dados de exemplo desabilitados - usando planilha real
"""

def criar_dados_exemplo():
    """Dados de exemplo desabilitados - usando planilha real"""
    print("ℹ️ Usando dados reais da planilha Cadastro_Visitantes.xlsx")
    return None
''')
    
    print("✅ Planilha real preparada para deploy!")
    print("\n📋 Próximos passos:")
    print("1. git add .")
    print("2. git commit -m 'Adicionar planilha real dos visitantes'")
    print("3. git push origin main")
    print("\n🚀 O Streamlit Cloud fará redeploy automaticamente!")
    
    return True

def restaurar_dados_exemplo():
    """Restaura os dados de exemplo"""
    
    print("🔄 Restaurando dados de exemplo...")
    
    # Procura por backup dos dados de exemplo
    backups = [f for f in os.listdir('.') if f.startswith('dados_exemplo_backup_')]
    
    if backups:
        # Pega o backup mais recente
        backup_mais_recente = sorted(backups)[-1]
        shutil.copy2(backup_mais_recente, 'dados_exemplo.py')
        print(f"✅ Dados de exemplo restaurados de: {backup_mais_recente}")
    else:
        print("❌ Nenhum backup de dados de exemplo encontrado")
        return False
    
    return True

def main():
    """Interface principal"""
    
    print("🏛️ Ministério Acolher - Preparador de Deploy")
    print("Igreja Nova Vida de Maricá")
    print("=" * 50)
    print()
    
    while True:
        print("Escolha uma opção:")
        print("1. Preparar planilha real para deploy")
        print("2. Restaurar dados de exemplo")
        print("3. Verificar arquivos atuais")
        print("4. Sair")
        print()
        
        opcao = input("Digite sua opção (1-4): ").strip()
        
        if opcao == "1":
            preparar_planilha_real()
            print()
            
        elif opcao == "2":
            restaurar_dados_exemplo()
            print()
            
        elif opcao == "3":
            print("📁 Arquivos atuais:")
            arquivos = ['Cadastro_Visitantes.xlsx', 'dados_exemplo.py']
            for arquivo in arquivos:
                if os.path.exists(arquivo):
                    tamanho = os.path.getsize(arquivo)
                    print(f"   ✅ {arquivo} ({tamanho} bytes)")
                else:
                    print(f"   ❌ {arquivo} (não encontrado)")
            print()
            
        elif opcao == "4":
            print("👋 Até logo!")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.")
            print()

if __name__ == "__main__":
    main()
