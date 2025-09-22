@echo off
echo ========================================
echo  MINISTÉRIO ACOLHER - ATUALIZADOR
echo  Igreja Nova Vida de Maricá
echo ========================================
echo.
echo Este script permite atualizar os dados do dashboard
echo com uma nova planilha semanal.
echo.
echo Opcoes:
echo 1. Atualizacao completa (menu interativo)
echo 2. Atualizacao rapida (apenas substituir)
echo.
set /p opcao="Escolha uma opcao (1 ou 2): "

if "%opcao%"=="1" (
    echo.
    echo Iniciando atualizacao completa...
    python atualizar_dados.py
) else if "%opcao%"=="2" (
    echo.
    echo Iniciando atualizacao rapida...
    python atualizar_rapido.py
) else (
    echo.
    echo Opcao invalida!
)

echo.
pause
