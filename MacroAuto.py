import pyautogui
import time
import keyboard

def pressiona_teclas():
    # Simula a combinação de teclas "seta para esquerda" e "enter"
    pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.press('enter')

def executa_macro():
    # Inicia o loop para execução contínua do macro
    while True:
        pressiona_teclas()
        time.sleep(5)  # Intervalo de 5 segundos entre cada execução

def ativa_desativa_macro():
    # Função para ativar/desativar o macro com o atalho Fn + P
    atalho_ativar = 'f12'  # Substitua pelo seu atalho desejado (Fn + P)
    atalho_desativar = 'esc'  # Substitua pelo seu atalho desejado para desativar

    ativar = False

    while True:
        if keyboard.is_pressed(atalho_ativar) and not ativar:
            ativa_desativa_macro = True
            executa_macro()
        elif keyboard.is_pressed(atalho_desativar) and ativar:
            ativa_desativa_macro = False
            break

# Chama a função para ativar/desativar o macro
ativa_desativa_macro()
