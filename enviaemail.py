import time
import pyautogui

# Configurações de segurança e velocidade do PyAutoGUI
pyautogui.FAILSAFE = True  # Jogue o mouse para o canto superior esquerdo para abortar a qualquer momento
pyautogui.PAUSE = 1.0      # Pausa de 1 segundo entre cada comando

print("Iniciando a automação na página do Outlook aberta...")

# ==========================================
# 1. ALTERNAR PARA A JANELA DO NAVEGADOR (SEM ALTERAR O TAMANHO)
# ==========================================
# Alterna para a janela do Chrome sem redimensioná-la
pyautogui.hotkey("alt", "tab")
time.sleep(1)

# Reseta o zoom do navegador para 100% caso tenha mudado
pyautogui.hotkey("ctrl", "0")
time.sleep(0.5)

# ==========================================
# 2. CRIAR E PREENCHER O E-MAIL
# ==========================================

# A. Clicar no botão "Novo email" 
print("Clicando no botão 'Novo email'...")
pyautogui.click(x=120, y=190)  # <-- Ajuste a coordenada X e Y se necessário
time.sleep(2)

# B. Clicar no campo "Para" (Destinatário)
print("Preenchendo destinatário...")
pyautogui.click(x=720, y=300)  # <-- Ajuste a coordenada X e Y se necessário
time.sleep(2)
pyautogui.write("adrieli.fidelis@gmail.com", interval=0.05)
pyautogui.press("tab") 

# C. Clicar no campo "Assunto"
print("Preenchendo o campo de assunto...")
pyautogui.click(x=720, y=350)  # <-- Ajuste a coordenada X e Y se necessário
time.sleep(2)
pyautogui.write("Relatório Automático - PyAutoGUI", interval=0.05)
pyautogui.press("tab")  # Vai para o corpo do e-mail

# D. Clicar no Corpo do E-mail
print("Preenchendo a mensagem...")
pyautogui.click(x=700, y=390)  # <-- Ajuste a coordenada X e Y se necessário
time.sleep(2)

mensagem = """TE AMO S2"""
pyautogui.write(mensagem, interval=0.02)

# ==========================================
# 3. ENVIAR O E-MAIL
# ==========================================
time.sleep(1)
print("Enviando o e-mail...")

# Clicar no botão "Enviar" por coordenadas
pyautogui.click(x=690, y=250)  # <-- Ajuste a coordenada X e Y se necessário

print("Processo concluído com sucesso!")