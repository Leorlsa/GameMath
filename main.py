import tkinter as tk
import random
import pygame

# Inicia o mixer do pygame
pygame.mixer.init()

# Carrega os sons
success_sound = pygame.mixer.Sound("acertou.mp3")
error_sound = pygame.mixer.Sound("errou.mp3")
success_sound.set_volume(0.2)
error_sound.set_volume(0.2)
def criar_calculo():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operacao = random.choice(["+", "-", "*"])
    calculo_label.config(text=f"{a} {operacao} {b} = ")
    if operacao == "+":
        resultado_atual = a + b
    elif operacao == "-":
        resultado_atual = a - b
    else:
        resultado_atual = a * b
    return resultado_atual

def verificar_resposta():
    global pontos, resultado_atual,tempo_restante
    try:
        resposta = int(resposta_entry.get())
    except ValueError:
        resultado_label.config(text="Resultado: Erro")
        # Toca o som de erro
        error_sound.play()
    else:
        if resposta == resultado_atual:
            resultado_label.config(text="Resultado: Correto!")
            pontos += 1
            tempo_restante +=2
            success_sound.play()
        else:
            resultado_label.config(text="Resultado: Incorreto")
            # Toca o som de erro
            error_sound.play()
    pontos_label.config(text=f"Pontos: {pontos}")
    resposta_entry.delete(0, tk.END)
    resultado_atual = criar_calculo()

def atualizar_cronometro():
    global tempo_restante,restart_button
    if tempo_restante > 0:
        tempo_restante -= 1
        cronometro_label.config(text=f"Tempo restante: {tempo_restante}")
        janela.after(1000, atualizar_cronometro)

    else:
        cronometro_label.config(text="Tempo esgotado!")
        resposta_entry.config(state=tk.DISABLED)
        enviar_button.config(state=tk.DISABLED)


# Cria a janela
janela = tk.Tk()

# Define as dimensões da janela
largura = 400
altura = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela / 2) - (largura / 2)
y = (altura_tela / 2) - (altura / 2)
janela.geometry(f"{largura}x{altura}+{int(x)}+{int(y)}")

# Adiciona um título
janela.title("GameMath")

# Cria um label com o cálculo
calculo_label = tk.Label(janela, text="2 + 2 = ")

# Cria uma entrada para a resposta
resposta_entry = tk.Entry(janela)

# Cria uma label para o resultado
resultado_label = tk.Label(janela, text="Resultado: ")

# Cria um label para os pontos
pontos_label = tk.Label(janela, text="Pontos: 0")

#restart_button = tk.Button(janela, text="Reiniciar", command=reiniciar_jogo)
#restart_button.grid(row=3, column=1, padx=10, pady=10)
#restart_button.config(state="disabled")
# Cria um label para o cronômetro

cronometro_label = tk.Label(janela, text="Tempo restante: 5")
resposta_entry.bind('<Return>', lambda event: verificar_resposta())
# Cria um botão de envio
enviar_button = tk.Button(janela, text="Enviar", command=verificar_resposta)

# Define a posição dos widgets na janela
calculo_label.grid(row=0, column=0, padx=10, pady=10)
resposta_entry.grid(row=0, column=1, padx=10, pady=10)
resultado_label.grid(row=1, column=0, padx=10, pady=10)
pontos_label.grid(row=1, column=1, padx=10, pady=10)
cronometro_label.grid(row=2, column=0, padx=10, pady=10)
enviar_button.grid(row=3, column=0, padx=10, pady=10)
# Centraliza a janela
largura_janela = 350
altura_janela = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = int((largura_tela / 2) - (largura_janela / 2))
posicao_y = int((altura_tela / 2) - (altura_janela / 2))
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

# Inicia os valores
resultado_atual = criar_calculo()
pontos = 0
tempo_restante = 30

# Inicia o cronômetro
atualizar_cronometro()

# Inicia a janela
janela.mainloop()