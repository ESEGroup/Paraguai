# Paraguai
Repositório do grupo de desenvolvedores do Sistema de Agendamento UFRJ.

# Instalando Dependencias

OBS: Em algumas distros, os comandos do virtualenv, pip, etc, para o Python3 tem um 3 na frente: virtualenv3, pip3, python3

Primeiro, instale o Python 3 e o virtualenv.
1. Instale o Python 3 e o virtualenv.
2. Vá para a pasta do projeto
3. Crie um ambiente usando `virtualenv ./env`
4. Inicie o ambiente virtual usando `source ./env/bin/activate`
5. Instale as dependencias usando `pip install -r requirements.txt`

## Instalando o bower e dependencias front-end
1. Instale o bower (precisa do Node, NPM e git): https://bower.io/
2. No diretório do projeto, rode `bower install`

# Rodando o servidor

1. Vá para a pasta do projeto
2. Comece o ambiente virtual usando `source ./env/bin/activate`
3. Comece o servidor usando `python app.py`
4. Visite a página `http://127.0.0.1:5000`
