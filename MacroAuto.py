import pyautogui
import time
from pynput import keyboard

def pressiona_teclas():
    # Simula a combinação de teclas "seta para a direita" e "enter"
    pyautogui.press('right')
    time.sleep(0.2)
    pyautogui.press('enter')

def executa_macro():
    # Inicia o loop para execução contínua do macro
    ciclos = 0

    while True:
        pressiona_teclas()
        ciclos += 1

        if ciclos >= 150:
            pyautogui.press('f5')  # Pressiona a tecla F5 para dar refresh
            time.sleep(10)  # Espera 20 segundos
            pyautogui.click() # Clica para voltar à seleção
            ciclos = 0  # Reseta o contador de ciclos

        time.sleep(24)  # Intervalo de 24 segundos entre cada execução

def on_activate():
    global ativar
    if not ativar:
        ativar = True
        executa_macro()
    else:
        ativar = False
        listener.stop()

# Variável para controlar se o macro está ativado ou não
ativar = False

# Função para ativar/desativar o macro com o atalho F12
atalho_ativar = keyboard.Key.f12  # Substitua pelo seu atalho desejado (F12)

def on_press(key):
    if key == atalho_ativar:
        on_activate()

# Cria um ouvinte de teclado
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
