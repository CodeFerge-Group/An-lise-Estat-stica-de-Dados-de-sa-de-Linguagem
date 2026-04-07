import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração visual do sistema
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Análise Estatística - Saúde")
        self.geometry("500x400")

        # Rótulo de Título
        self.label = ctk.CTkLabel(self, text="Análise de Dados de Saúde", font=("Roboto", 24))
        self.label.pack(pady=20)

        # Botão para Carregar e Analisar
        self.btn_analisar = ctk.CTkButton(self, text="Executar Análise Estatística", command=self.executar_analise)
        self.btn_analisar.pack(pady=10)

        # Botão para Ver Correlação (Onde a estatística brilha!)
        self.btn_corr = ctk.CTkButton(self, text="Ver Correlação Peso x Pressão", command=self.mostrar_correlacao, fg_color="green")
        self.btn_corr.pack(pady=10)

        # Área de texto para exibir resultados
        self.resultado_texto = ctk.CTkTextbox(self, width=400, height=150)
        self.resultado_texto.pack(pady=20)

    def executar_analise(self):
        # Sua lógica que já estava pronta
        df = pd.read_csv('pacientes.csv')
        df['IMC'] = df['peso'] / np.power(df['altura'], 2)
        
        resumo = df.describe().to_string()
        
        self.resultado_texto.delete("0.0", "end")
        self.resultado_texto.insert("0.0", f"Resumo Estatístico:\n{resumo}")
        
        # Gerar o gráfico automático
        plt.bar(df['nome'], df['IMC'], color='skyblue')
        plt.title('IMC por Paciente')
        plt.show()

    def mostrar_correlacao(self):
        df = pd.read_csv('pacientes.csv')
        # Passo 2: Cálculo de Correlação de Pearson com NumPy
        correlacao = np.corrcoef(df['peso'], df['pressao_arterial'])[0, 1]
        
        self.resultado_texto.delete("0.0", "end")
        self.resultado_texto.insert("0.0", f"Análise de Correlação:\n\n"
                                          f"O índice de correlação entre Peso e Pressão é: {correlacao:.2f}\n"
                                          f"Isso indica uma relação forte entre os fatores.")

if __name__ == "__main__":
    app = App()
    app.mainloop()