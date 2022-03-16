#SOLICITAÇÃO DE APONTAMENTO COM TECNOLOGIA INDEPENDENTE E GRATUÍTA (RH - Folha).

#TIRAR SENHA DO E-MAIL ANTES DE SUBIR PARA YOUTUBE OU GITHUB.

#INTRODUÇÃO - O QUE PRECISA SABER SOBRE APONTAMENTO:
#O que é o apontamento?
#Quais são as formas de fazer o apontamento?

#ALGUNS PRINCÍPIOS DE APONTAMENTO.
# a) Padrão/princípio Constitucional e norma coletiva (HE a 60%);
# b) DSR +  Limite de tolerância;
# c) Jornada de trabalho de cada trabalhador/banco de horas (cargo de confiança e etc.).
# d) Noção de como funciona isso na folha de salários.


#PARTE PRÁTICA - normalmente o RH precisar AVISAR/SOLICITAR (por e-mail, chat interno ou WhastApp). 
# Vamos fazer por e-mail:







# 1) ENTRAR NO E-MAIL. Para isso: 
import pyautogui    
import pyperclip
import time

# 2) clicar na tecla do Windows:
pyautogui.press("win")

# 3) clicar na pesquisa, e digitar "chrome", dar um enter e abrir uma janela para internet com o endereço do meu e-mail:
time.sleep(1)
pyautogui.click
time.sleep(1)
pyautogui.write ("chrome")
time.sleep(1)
pyautogui.press ("enter")
time.sleep(15)

# 4) Entrar no site do hotmail e dentro do meu e-mail pessoal:
pyperclip.copy("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1647279053&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d3fe00b5a-fe8f-7fa7-4d5c-6d66110ea1af&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
pyautogui.hotkey ("ctrl", "v")
pyautogui.press ("enter")
time.sleep(5)
pyperclip.copy("tavaresvalter@hotmail.com")
pyautogui.hotkey ("ctrl", "v")
time.sleep (2)
pyautogui.press ("enter")
time.sleep (5)
pyperclip.copy("123VouTrocar")
pyautogui.hotkey ("ctrl", "v")
time.sleep (2)
pyautogui.press ("enter")

# 5) Escrever um novo e-mail solicitando o apontamento:
time.sleep (25)
pyautogui.click (x=168, y=168)
time.sleep (10)
pyperclip.copy("tavaresvalter@hotmail.com")
pyautogui.hotkey ("ctrl", "v")
time.sleep (2)
#pyperclip.copy("teste@gmail.com")
#pyautogui.hotkey ("ctrl", "v")
#time.sleep (3)
pyautogui.press ("tab")
time.sleep (3)
pyperclip.copy("Apontamento dos colaboradores para fechamento da folha de salários.")
pyautogui.hotkey ("ctrl", "v")
time.sleep (3)
pyautogui.press ("tab")
time.sleep (5)
texto = """
Prezados,
Como sabem, todo o mês é necessário ajustar (abonos) e enviar os apontamentos dos colaborados ao RH.
Essas informações de horas extras, faltas, atrasos, e etc., farão parte da folha de salários,
e consequentemente do valor líquido do salário de cada colaborador(a).
Diante disso, pedimos, por gentileza, que enviem esses apontamentos ao RH o quanto antes para fecharmos a folha.

Grato, 
Valter Fernandes Tavares
Departamento de Recursos Humanos
"""
pyperclip.copy (texto)  
pyautogui.hotkey ("ctrl", "v")

time.sleep (25)

# 6) Enviar o e-mail:
pyautogui.click (x=347, y=651)




