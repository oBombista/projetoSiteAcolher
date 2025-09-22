@echo off
echo ========================================
echo  MINISTÉRIO ACOLHER - PREPARAR DEPLOY
echo  Igreja Nova Vida de Maricá
echo ========================================
echo.
echo Este script prepara a planilha real para o deploy
echo no Streamlit Cloud.
echo.
echo Opcoes:
echo 1. Preparar planilha real para deploy
echo 2. Verificar arquivos atuais
echo.
set /p opcao="Escolha uma opcao (1 ou 2): "

if "%opcao%"=="1" (
    echo.
    echo Preparando planilha real...
    python subir_planilha_real.py
    echo.
    echo Próximos passos:
    echo 1. git add .
    echo 2. git commit -m "Adicionar planilha real dos visitantes"
    echo 3. git push origin main
    echo.
    echo O Streamlit Cloud fará redeploy automaticamente!
) else if "%opcao%"=="2" (
    echo.
    echo Verificando arquivos...
    python subir_planilha_real.py
) else (
    echo.
    echo Opcao invalida!
)

echo.
pause
