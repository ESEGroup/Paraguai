# Paraguai
Repositório do grupo de desenvolvedores do Sistema de Agendamento UFRJ.

# Instalando Dependências

OBS: Em algumas distros, os comandos do virtualenv, pip, etc, para o Python3 tem um 3 no final: virtualenv3, pip3, python3

## Instalando Python
1. Baixe a versão mais recente em https://www.python.org/

## Instalando Virtualenv
1. Verifique sua versão do Python
1.1. Se Python 2 >= 2.7.9 ou Python 3 >= 3.4, você já terá o pip instalado e poderá instalar o virtualenv pelo comando: 'pip install virtualenv'
1.2. Se for outra versão, deverá instalar o pip seguindo as instruções em https://pip.pypa.io/en/stable/installing/ para então instalar o virtualenv: https://virtualenv.pypa.io/en/stable/installation/)

## Instalando Flask
1. Com o pip instalado, basta usar o comando: 'pip install Flask'

# Criando o ambiente virtual
1. Vá para a pasta do projeto
2. Crie um ambiente virtual usando `virtualenv ./env`
3. Instalar quaisquer dependências necessárias usando `pip install -r requirements.txt`

# Rodando o servidor
1. Vá para a pasta do projeto
4. Inicie o ambiente virtual usando `source ./env/bin/activate` (no Windows: executar 'activate.bat')
3. Comece o servidor usando `python app.py`
4. Visite a página `http://127.0.0.1:5000`