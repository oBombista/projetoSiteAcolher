@echo off
echo ========================================
echo  Ministerio Acolher - Dashboard
echo  Igreja Nova Vida de Marica
echo ========================================
echo.
echo Verificando se Python esta instalado...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado! Por favor, instale o Python 3.8 ou superior.
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python encontrado!
echo.
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Erro ao instalar dependencias!
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas com sucesso!
echo.
echo Verificando se existe a planilha de dados...
if not exist "Cadastro_Visitantes.xlsx" (
    echo ⚠️  Planilha Cadastro_Visitantes.xlsx nao encontrada!
    echo.
    echo Deseja criar dados de exemplo para teste? (S/N)
    set /p resposta=
    if /i "%resposta%"=="S" (
        echo Criando dados de exemplo...
        python exemplo_dados.py
        echo.
    ) else (
        echo Por favor, coloque o arquivo Cadastro_Visitantes.xlsx na pasta do projeto.
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo  Iniciando o Dashboard...
echo ========================================
echo.
echo Para acessar o dashboard, abra seu navegador em:
echo http://localhost:8501
echo.
echo Para parar o servidor, pressione Ctrl+C
echo.
streamlit run app.py
