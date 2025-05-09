import tkinter as tk
from tkinter import messagebox
from database.queries import (
    list_monitorias_com_info, horas_por_disciplina, media_horas_por_aluno,
    quantidade_monitorias, menor_hora, maior_hora
)
from database.update_delete import atualizar_monitoria, excluir_monitoria

def exibir_resultado(texto):
    output.delete('1.0', tk.END)
    output.insert(tk.END, texto)

def btn_listar_monitorias():
    dados = list_monitorias_com_info()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_horas_disciplina():
    dados = horas_por_disciplina()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_media_aluno():
    dados = media_horas_por_aluno()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_quantidade_monitorias():
    dados = quantidade_monitorias()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_menor_hora():
    dados = menor_hora()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_maior_hora():
    dados = maior_hora()
    texto = "\n".join(str(linha) for linha in dados)
    exibir_resultado(texto)

def btn_atualizar():
    try:
        id_mon = int(entry_id.get())
        novas_horas = int(entry_horas.get())
        atualizar_monitoria(id_mon, novas_horas=novas_horas)
        messagebox.showinfo("Sucesso", "Monitoria atualizada!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def btn_excluir():
    try:
        id_mon = int(entry_id.get())
        excluir_monitoria(id_mon)
        messagebox.showinfo("Sucesso", "Monitoria excluída!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Interface
root = tk.Tk()
root.title("Sistema de Monitorias")
root.geometry("600x500")

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Listar Monitorias", command=btn_listar_monitorias).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Horas por Disciplina", command=btn_horas_disciplina).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Média por Aluno", command=btn_media_aluno).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Quantidade Monitorias", command=btn_quantidade_monitorias).grid(row=1, column=1, padx=5)
tk.Button(frame_botoes, text="Menor Horário", command=btn_menor_hora).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_botoes, text="Maior Horário", command=btn_maior_hora).grid(row=2, column=1, padx=5)

frame_acao = tk.Frame(root)
frame_acao.pack(pady=10)

tk.Label(frame_acao, text="ID Monitoria:").grid(row=0, column=0)
entry_id = tk.Entry(frame_acao)
entry_id.grid(row=0, column=1)

tk.Label(frame_acao, text="Novas Horas:").grid(row=1, column=0)
entry_horas = tk.Entry(frame_acao)
entry_horas.grid(row=1, column=1)

tk.Button(frame_acao, text="Atualizar", command=btn_atualizar).grid(row=2, column=0, pady=5)
tk.Button(frame_acao, text="Excluir", command=btn_excluir).grid(row=2, column=1, pady=5)

output = tk.Text(root, height=15, width=70)
output.pack(pady=10)

root.mainloop()
