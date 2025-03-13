#Janela para selecionar a pasta  do nosso computador
import os #para os arquivos
from tkinter.filedialog import askdirectory #para abrir janelas no windows
import shutil #para passar o arquivo para pasta backup
import datetime

nome_pasta_selecionada = askdirectory() #abre a tela dos arquivos e a pasta que você seleciona, é colocada na variável
lista_arquivos = os.listdir(nome_pasta_selecionada) #agora com a funcionalidade da "os.listdir", criamos uma lista com os arquivos da pasta

#fazer backup que estão nessa pasta
nome_pasta_backup = "backup"
nome_completo_pasta_backup = nome_pasta_selecionada+"/"+nome_pasta_backup
if not os.path.exists(nome_completo_pasta_backup):
    os.makedirs(nome_completo_pasta_backup)#criação da pasta backup

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S")   



#laço para fazer backup
for arquivo in lista_arquivos:
    nome_arq = nome_pasta_selecionada + "/" + arquivo
    nome_final = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"
    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"):
        os.makedirs(f"{nome_completo_pasta_backup}/{data_atual}")
    if "." in arquivo:
        shutil.copy2(nome_arq, nome_final)
    elif "backup" != arquivo:
        shutil.copytree(nome_arq, nome_final)
