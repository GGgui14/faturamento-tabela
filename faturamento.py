import pyautogui
import time
import pyperclip
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Usuario\Desktop\GUILHERME ESCOLA\IFSC G\Python\Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)


