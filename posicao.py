import time
import pyautogui

print("Mova o mouse para o elemento desejado.")
print("Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4} | Y: {y:4}", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nEncerrado.")

    novo email 120 , 190
    para 720 , 300
    ass 720, 350
    corpo 700, 390
    enviar 690, 250