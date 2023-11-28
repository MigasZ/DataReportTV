from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Coordenadas do mouse - X: {x}, Y: {y}")

# Cria um ouvinte do mouse
with Listener(on_click=on_click) as listener:
    listener.join()
