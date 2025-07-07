🐍 Projeto: Backup de Pastas em Python
Este repositório contém um projeto simples e funcional em Python que realiza o backup automático de arquivos e pastas do seu computador. A aplicação possui uma interface gráfica para seleção da pasta de origem e organiza os backups por data e hora.

📦 Funcionalidades
Interface gráfica para seleção da pasta (via tkinter);

Criação automática de uma pasta backup;

Cópia de arquivos e subpastas mantendo a estrutura original;

Organização dos backups em pastas nomeadas com data e hora;

Evita duplicação da pasta de backup.

💻 Tecnologias Utilizadas
Python 3

Módulos: os, shutil, datetime, tkinter

▶️ Como Executar
Certifique-se de ter o Python 3 instalado.

Clone o repositório ou baixe o arquivo .py.

Execute o script em um terminal com:

bash
Copiar
Editar
python nome_do_arquivo.py
Uma janela será aberta para você selecionar a pasta que deseja fazer backup.

O backup será salvo dentro da própria pasta selecionada, em uma subpasta chamada backup.

📂 Exemplo de Estrutura Final
yaml
Copiar
Editar
📁 MinhaPastaSelecionada
 ┣ 📁 backup
 ┃ ┗ 📁 2025-07-07 21-30-15
 ┃   ┣ 📄 arquivo.txt
 ┃   ┗ 📁 subpasta
 ┃     ┗ 📄 outro_arquivo.docx
📫 Contato
Vinícius Andrade
📧 vinandrade.santos@gmail.com
