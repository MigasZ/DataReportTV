import pyautogui
import time
import keyboard

def pressiona_teclas():
    # Simula a combinação de teclas "seta para a esquerda" e "enter"
    pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.press('enter')

def executa_macro():
    # Inicia o loop para execução contínua do macro
    while True:
        pressiona_teclas()
        time.sleep(24)  # Intervalo de 5 segundos entre cada execução

def ativa_desativa_macro():
    # Função para ativar/desativar o macro com o atalho F12
    atalho_ativar = 'f12'  # Substitua pelo seu atalho desejado (F12)

    ativar = False

    while True:
        if keyboard.is_pressed(atalho_ativar) and not ativar:
            ativar = True
            executa_macro()
        elif keyboard.is_pressed(atalho_ativar) and ativar:
            ativar = False
            break

# Chama a função para ativar/desativar o macro
ativa_desativa_macro()
