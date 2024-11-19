import tkinter as tk
from tkinter import simpledialog, messagebox
from googletrans import Translator

# Função para copiar o texto para a área de transferência
def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Mantém a área de transferência atualizada

# Função para traduzir o texto de português para inglês
def translate_text():
    while True:
        try:
            # Solicita ao usuário o texto a ser traduzido
            text_to_translate = simpledialog.askstring("Input", "Digite o texto que deseja traduzir (em português):")
            
            if text_to_translate:
                # Inicializa o tradutor
                translator = Translator()
                
                # Traduz o texto
                translated = translator.translate(text_to_translate, src='pt', dest='en')
                
                # Cria uma nova janela para mostrar o texto traduzido e o botão de copiar
                result_window = tk.Toplevel(root)
                result_window.title("Translated Text")
                
                # Texto traduzido
                translated_text_label = tk.Label(result_window, text=translated.text, wraplength=400)
                translated_text_label.pack(pady=10)
                
                # Botão de copiar
                copy_button = tk.Button(result_window, text="Copiar", command=lambda: copy_to_clipboard(translated.text))
                copy_button.pack(pady=10)
                
                # Botão de OK para fechar a janela
                ok_button = tk.Button(result_window, text="OK", command=result_window.destroy)
                ok_button.pack(pady=10)
                
                # Espera até que a janela seja fechada
                result_window.wait_window()
            else:
                break  # Sai do loop se o usuário cancelar a entrada ou não inserir texto
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            break

# Cria a janela principal
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Chama a função para traduzir o texto
translate_text()