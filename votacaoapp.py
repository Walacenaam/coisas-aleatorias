import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados dinâmicos
candidatos = {}
eleitores = {}

# Interface principal
janela = tk.Tk()
janela.title("Sistema de Votação Dinâmico")
janela.geometry("400x500")

# Variável de seleção
var_candidato = tk.StringVar()

# Função para adicionar novo candidato
def adicionar_candidato():
    nome = entry_novo_candidato.get().strip().lower()
    if nome and nome not in candidatos:
        candidatos[nome] = 0
        atualizar_opcoes_voto()
        entry_novo_candidato.delete(0, tk.END)
        messagebox.showinfo("Sucesso", f"Candidato '{nome.capitalize()}'cadastrado.!")
    else:
        messagebox.showwarning("Aviso", "Nome inválido ou já existente.")

# Função para atualizar botões de votação
def atualizar_opcoes_voto():
    var_candidato.set("")
    for widget in frame_opcoes.winfo_children():
        widget.destroy()
    for nome in candidatos.keys():
        tk.Radiobutton(frame_opcoes, text=nome.capitalize(), variable=var_candidato, value=nome).pack(anchor="w")

# Função para registrar voto
def registrar_voto():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    candidato = var_candidato.get()

    if not nome or not cpf or not candidato:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os dados.")
        return

    if cpf in eleitores:
        messagebox.showerror("Duplicidade", "Este CPF já foi registrado, não é permitido votar duas vezes.")
        return

    eleitores[cpf] = nome
    candidatos[candidato] += 1
    messagebox.showinfo("Sucesso", f"Voto computado para {candidato.capitalize()}!")
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    atualizar_placar()

# Função para atualizar placar
def atualizar_placar():
    texto = ""
    total = sum(candidatos.values())
    for nome, qtd in candidatos.items():
        porc = (qtd / total * 100) if total > 0 else 0
        texto += f"{nome.capitalize()}: {qtd} voto(s) ({porc:.1f}%)\n"
    texto += f"\nTotal de eleitores: {len(eleitores)}"
    label_resultado.config(text=texto)

# Função para exportar CSV e mostrar gráfico
def mostrar_grafico():
    total = sum(candidatos.values())
    dados = []
    for nome, qtd in candidatos.items():
        porc = (qtd / total * 100) if total > 0 else 0
        dados.append({'Candidato': nome.capitalize(), 'Votos': qtd, 'Porcentagem': round(porc, 1)})

    df = pd.DataFrame(dados)
    df.to_csv("resultado_votacao.csv", index=False)

    sns.set_theme(style="darkgrid")
    sns.barplot(data=df, x="Candidato", y="Votos", palette="viridis")
    plt.title("Resultado da Votação", fontweight="bold")
    plt.ylabel("Votos")
    plt.xlabel("Candidato")
    plt.tight_layout()
    plt.show()

# Interface gráfica
tk.Label(janela, text="Nome do Eleitor:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="CPF:").pack()
entry_cpf = tk.Entry(janela)
entry_cpf.pack()

tk.Label(janela, text="Escolha seu candidato:").pack()
frame_opcoes = tk.Frame(janela)
frame_opcoes.pack()

tk.Button(janela, text="Votar", command=registrar_voto).pack(pady=5)
tk.Button(janela, text="Ver Gráfico", command=mostrar_grafico).pack(pady=5)

label_resultado = tk.Label(janela, text="", justify="left", font=("Arial_black", 10))
label_resultado.pack(pady=10)

tk.Label(janela, text="Adicionar novo candidato:").pack()
entry_novo_candidato = tk.Entry(janela)
entry_novo_candidato.pack()
tk.Button(janela, text="Adicionar", command=adicionar_candidato).pack(pady=5)

janela.mainloop()
