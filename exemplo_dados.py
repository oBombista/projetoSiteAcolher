"""
Script para criar dados de exemplo para teste do dashboard
Execute este script se não tiver a planilha Cadastro_Visitantes.xlsx
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def criar_dados_exemplo():
    """Cria dados de exemplo para teste do dashboard"""
    
    # Configurações
    np.random.seed(42)
    random.seed(42)
    
    # Dados de exemplo
    nomes = [
        "Ana Silva", "João Santos", "Maria Oliveira", "Pedro Costa", "Lucia Ferreira",
        "Carlos Lima", "Fernanda Rocha", "Roberto Alves", "Juliana Mendes", "Antonio Pereira",
        "Patricia Souza", "Marcos Rodrigues", "Cristina Barbosa", "Rafael Nascimento", "Tatiana Moreira",
        "Diego Carvalho", "Vanessa Dias", "Leandro Martins", "Camila Ribeiro", "Felipe Gomes"
    ]
    
    cidades = [
        "Maricá", "Niterói", "Rio de Janeiro", "São Gonçalo", "Itaboraí",
        "Tanguá", "Magé", "Duque de Caxias", "Nova Iguaçu", "Queimados"
    ]
    
    bairros = [
        "Centro", "Zumbi", "Itaipuaçu", "Ponta Negra", "Silvado",
        "Inoã", "Barra de Maricá", "Espraiado", "Bananal", "Jacaroá"
    ]
    
    origem_visita = [
        "Indicação de amigo", "Redes sociais", "Panfleto", "Evento na praça",
        "Indicação familiar", "Google/Busca online", "Cartaz", "Programa de rádio"
    ]
    
    cultos = [
        "Culto de domingo manhã", "Culto de domingo noite", "Culto de quarta-feira",
        "Culto de sexta-feira", "Culto especial"
    ]
    
    faixa_etaria = [
        "0-12 anos", "13-17 anos", "18-25 anos", "26-35 anos",
        "36-45 anos", "46-55 anos", "56-65 anos", "65+ anos"
    ]
    
    pertence_igreja = [
        "Não, não pertence a nenhuma igreja",
        "Sim, mas não está frequentando",
        "Sim, frequenta outra igreja",
        "Não informado"
    ]
    
    necessidades = [
        "Oração por saúde", "Ajuda financeira", "Orientação espiritual",
        "Aconselhamento familiar", "Oração por emprego", "Cura interior",
        "Libertação", "Aconselhamento conjugal", "Oração por filhos",
        "Direcionamento de vida", "Oração por conversão", "Apoio emocional"
    ]
    
    como_chegou = [
        "Indicação de membro", "Redes sociais", "Panfleto na rua",
        "Evento evangelístico", "Programa de rádio", "Google",
        "Cartaz no comércio", "Indicação de familiar"
    ]
    
    # Gera dados aleatórios
    n_registros = 150
    
    dados = []
    for i in range(n_registros):
        # Data aleatória nos últimos 6 meses
        data_base = datetime.now() - timedelta(days=random.randint(1, 180))
        
        registro = {
            'Carimbo de data/hora': data_base.strftime('%d/%m/%Y %H:%M:%S'),
            'Quem está preenchendo a planilha?': random.choice(['Pastor João', 'Diácono Pedro', 'Líder Maria', 'Evangelista Ana']),
            'Visita a Igreja Nova Vida de:': random.choice(origem_visita),
            'Data da Visita': data_base.strftime('%d/%m/%Y'),
            'Culto': random.choice(cultos),
            'Nome do visitante': random.choice(nomes),
            'Telefone com DDD': f"(21) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            'Bairro onde mora': random.choice(bairros),
            'Cidade': random.choice(cidades),
            'Como ele chegou até a Nova Vida?': random.choice(como_chegou),
            'Pertence a alguma igreja ou religião?': random.choice(pertence_igreja),
            'Faixa etaria': random.choice(faixa_etaria),
            'Qual a necessidade do visitante?': random.choice(necessidades),
            'Observações': random.choice(['', 'Pessoa muito receptiva', 'Interessada em estudos bíblicos', 'Precisa de acompanhamento'])
        }
        dados.append(registro)
    
    # Cria DataFrame
    df = pd.DataFrame(dados)
    
    # Salva como Excel
    df.to_excel('Cadastro_Visitantes.xlsx', index=False)
    print("✅ Arquivo 'Cadastro_Visitantes.xlsx' criado com sucesso!")
    print(f"📊 Total de registros: {len(df)}")
    print("\n📋 Resumo dos dados:")
    print(f"- Cidades únicas: {df['Cidade'].nunique()}")
    print(f"- Faixas etárias: {df['Faixa etaria'].nunique()}")
    print(f"- Necessidades: {df['Qual a necessidade do visitante?'].nunique()}")

if __name__ == "__main__":
    criar_dados_exemplo()
