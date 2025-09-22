"""
Script para criar dados de exemplo para o deploy no Streamlit Cloud
Este arquivo é executado automaticamente se não houver Cadastro_Visitantes.xlsx
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def criar_dados_exemplo():
    """Cria dados de exemplo para o dashboard"""
    
    # Configurações
    np.random.seed(42)
    random.seed(42)
    
    # Dados de exemplo
    nomes = [
        "Ana Silva", "João Santos", "Maria Oliveira", "Pedro Costa", "Lucia Ferreira",
        "Carlos Lima", "Fernanda Rocha", "Roberto Alves", "Juliana Mendes", "Antonio Pereira",
        "Patricia Souza", "Marcos Rodrigues", "Cristina Barbosa", "Rafael Nascimento", "Tatiana Moreira",
        "Diego Carvalho", "Vanessa Dias", "Leandro Martins", "Camila Ribeiro", "Felipe Gomes",
        "Gabriela Almeida", "Thiago Santos", "Larissa Costa", "Bruno Oliveira", "Isabela Lima",
        "Rafaela Souza", "Lucas Pereira", "Mariana Silva", "Gustavo Rocha", "Beatriz Alves"
    ]
    
    cidades = [
        "Maricá", "Niterói", "Rio de Janeiro", "São Gonçalo", "Itaboraí",
        "Tanguá", "Magé", "Duque de Caxias", "Nova Iguaçu", "Queimados",
        "Seropédica", "Japeri", "Belford Roxo", "São João de Meriti", "Nilópolis"
    ]
    
    bairros = [
        "Centro", "Zumbi", "Itaipuaçu", "Ponta Negra", "Silvado",
        "Inoã", "Barra de Maricá", "Espraiado", "Bananal", "Jacaroá",
        "Recanto de Itaipuaçu", "São José de Imbassaí", "Flamengo", "Copacabana", "Ipanema"
    ]
    
    origem_visita = [
        "Indicação de amigo", "Redes sociais", "Panfleto", "Evento na praça",
        "Indicação familiar", "Google/Busca online", "Cartaz", "Programa de rádio",
        "YouTube", "Instagram", "Facebook", "WhatsApp"
    ]
    
    cultos = [
        "Culto de domingo manhã", "Culto de domingo noite", "Culto de quarta-feira",
        "Culto de sexta-feira", "Culto especial", "Culto de jovens"
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
        "Direcionamento de vida", "Oração por conversão", "Apoio emocional",
        "Oração por família", "Cura de enfermidades", "Libertação de vícios"
    ]
    
    como_chegou = [
        "Indicação de membro", "Redes sociais", "Panfleto na rua",
        "Evento evangelístico", "Programa de rádio", "Google",
        "Cartaz no comércio", "Indicação de familiar", "YouTube",
        "Instagram", "Facebook", "WhatsApp"
    ]
    
    # Gera dados aleatórios
    n_registros = 200  # Mais registros para demonstrar melhor o dashboard
    
    dados = []
    for i in range(n_registros):
        # Data aleatória nos últimos 12 meses
        data_base = datetime.now() - timedelta(days=random.randint(1, 365))
        
        registro = {
            'Carimbo de data/hora': data_base.strftime('%d/%m/%Y %H:%M:%S'),
            'Quem está preenchendo a planilha?': random.choice(['Pastor João', 'Diácono Pedro', 'Líder Maria', 'Evangelista Ana', 'Pastora Cristina']),
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
            'Observações': random.choice(['', 'Pessoa muito receptiva', 'Interessada em estudos bíblicos', 'Precisa de acompanhamento', 'Muito abençoada', 'Voltará no próximo domingo'])
        }
        dados.append(registro)
    
    # Cria DataFrame
    df = pd.DataFrame(dados)
    
    # Salva como Excel
    df.to_excel('Cadastro_Visitantes.xlsx', index=False)
    print("✅ Dados de exemplo criados com sucesso para o deploy!")
    return df

if __name__ == "__main__":
    criar_dados_exemplo()
