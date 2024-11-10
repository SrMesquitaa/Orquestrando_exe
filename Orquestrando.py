from pathlib import Path
import os
import customtkinter as ctk
from tkinter import messagebox, Label, Frame, Listbox, END
from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk
from datetime import datetime  # Para lidar com datas
import subprocess #para verificar scripts

print("Iniciando a aplicação...")

# Caminhos das imagens e arquivos
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\leonardo.mesquita\Documents\DESENVOLVIMENTO LEO\build\assets\frame0")

# Função para gerenciar arquivos no caminho relativo
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Cria a janela principal e define suas propriedades
window = Tk()
window.geometry("1000x600")  # Ajustei a largura para acomodar os novos elementos
window.configure(bg="#FFFFFF")
window.title("Orquestrando")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Posiciona o canvas e imagens da interface original
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(420.0, 320.0, image=image_image_1)

canvas.create_rectangle(0.0, 0.0, 40.0, 600.0, fill="#FFFFFF", outline="")
canvas.create_rectangle(40.0, 0.0, 800.0, 40.0, fill="#FFFFFF", outline="")

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(103.0, 105.0, image=image_image_2)

# Botões da interface esquerda (Botoes ainda não definidos)
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
button_1.place(x=5.0, y=234.0, width=31.0, height=31.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
button_2.place(x=5.0, y=394.0, width=31.0, height=31.0)

Configuração = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=Configuração, borderwidth=0, highlightthickness=0, command=lambda: print("button_configuracao clicked"), relief="flat")
button_3.place(x=5.0, y=561.0, width=31.0, height=31.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=lambda: print("button_4 clicked"), relief="flat")
button_4.place(x=5.0, y=354.0, width=31.0, height=31.0)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("button_5 clicked"), relief="flat")
button_5.place(x=5.0, y=314.0, width=31.0, height=31.0)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(image=button_image_6, borderwidth=0, highlightthickness=0, command=lambda: print("button_6 clicked"), relief="flat")
button_6.place(x=5.0, y=274.0, width=31.0, height=31.0)

canvas.create_text(305.0, 162.0, anchor="nw", text="Galeria de Scripts", fill="#000000", font=("Roboto CondensedRegular", 32 * -1))
canvas.create_rectangle(103.0, 215.0, 737.0, 524.0, fill="#FFFFFF", outline="")

# -------------------- Funções e Interface do Codigo Primário --------------------

# Função para executar um script Python
def run_script(script_path):
    os.system(f"python {script_path}")
    messagebox.showinfo("Execução", f"Script '{script_path}' executado com sucesso!")
    check_logs()

# Função para listar scripts em um diretório
def list_scripts(directory):
    scripts = [f for f in os.listdir(directory) if f.endswith('.py')]
    return scripts

# Função para exibir scripts na interface
def display_scripts(scripts):
    listbox_scripts.delete(0, END)
    for script in scripts:
        listbox_scripts.insert(END, script)

# Função para verificar logs e exibir o status
def check_logs():
    # Limpa os resultados anteriores
    for widget in log_frame.winfo_children():
        widget.destroy()
        
    today = datetime.now().strftime("%Y-%m-%d")
    directory_map = {
        r"D:\Dados\Analytics\gerenciais\Dados\cigam_arezzo\logs\11_2024": "Arezzo",
        r"D:\Dados\Analytics\gerenciais\Dados\cigam_vans\logs\11_2024": "Vans",
        r"D:\Dados\Analytics\gerenciais\Dados\taylor_magrella\logs\11_2024": "Magrella",
        r"D:\Dados\Analytics\gerenciais\Dados\trier_farmacia\logs\11_2024": "Farmácia",
        r"D:\Dados\Analytics\gerenciais\Dados\varejofacil_toqueto\logs\11_2024": "TQT"
    }
    for directory in directories:
        directory_name = directory_map.get(directory, os.path.basename(directory))  # Mapeia o nome do diretório
        for file in os.listdir(directory):
            if file.endswith('.log') and today in file:
                with open(os.path.join(directory, file), 'r') as log_file:
                    content = log_file.read()
                    icon = "✅" if "Processo finalizado com sucesso." in content else "❌"
                    log_label = Label(log_frame, text=f"{directory_name}: {icon}", font=("San Francisco", 10))
                    log_label.pack(side="left", padx=10)

    vendas_file_path = r"D:\Dados\Crocs\Projeto_01\vendas_retarguarda\vendas_modificados\lojas\vendas_11_2024"
    
    #Verificar se "Vendas_2024" CROCS foi atualizado hj
    if os.path.exists(vendas_file_path):
        modified_time = datetime.fromtimestamp(os.path.getmtime(vendas_file_path))
        modified_date = modified_time.strftime("%Y-%m-%d")
    #Status "OK" ou "Fail"
        vendas_status = "OK" if modified_date == today else "FAIL"
        vendas_icon = "✅" if vendas_status == "OK" else "❌"   
    #Adicionar na interface 
        vendas_label = Label(log_frame, text=f"Crocs Loja: {vendas_icon}", font=("San Francisco", 10))
        vendas_label.pack(anchor="w", pady=2)
    # Exibe o status no console para debug
        print(f"Vendas_11_2024: {vendas_status}")  
    else:
    # Se o arquivo não existir, exibe uma mensagem de erro
     vendas_label = Label(log_frame, text="Crocs Loja: ❌", 
     font=("San Francisco", 10))
     vendas_label.pack(anchor="w", pady=2)
     print("Vendas_11_2024: Arquivo não encontrado")

# Configurações de CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Diretórios dos logs e scripts
directories = [
    r"D:\Dados\Analytics\gerenciais\Dados\cigam_arezzo\logs\11_2024",
    r"D:\Dados\Analytics\gerenciais\Dados\cigam_vans\logs\11_2024",
    r"D:\Dados\Analytics\gerenciais\Dados\taylor_magrella\logs\11_2024",
    r"D:\Dados\Analytics\gerenciais\Dados\trier_farmacia\logs\11_2024",
    r"D:\Dados\Analytics\gerenciais\Dados\varejofacil_toqueto\logs\11_2024"
]

# Diretório onde estão os scripts
scripts_directory = r"D:\Dados\Analytics\gerenciais\grc"

# Interface da seção de scripts e logs (posição à direita)
script_label = Label(window, text="Scripts Disponíveis:", font=("San Francisco", 12))
script_label.place(x=810, y=50)

listbox_scripts = Listbox(window, height=20, width=40, font=("San Francisco", 10))  # Aumentei a altura para exibir mais scripts e mudei a fonte
listbox_scripts.place(x=810, y=80)

# Bind para executar script ao clicar duas vezes
listbox_scripts.bind("<Double-Button-1>", lambda event: run_script(os.path.join(scripts_directory, listbox_scripts.get(listbox_scripts.curselection()))))

# Cria um frame para os resultados dos logs, permitindo exibição lado a lado
log_frame = Frame(window, bg="#FFFFFF")
log_frame.place(x=150, y=280)  # Centralizando o frame

# Carrega scripts do diretório de scripts e exibe na interface
all_scripts = list_scripts(scripts_directory)
display_scripts(all_scripts)

# Checa logs ao iniciar
check_logs()

# Executa a interface
window.mainloop