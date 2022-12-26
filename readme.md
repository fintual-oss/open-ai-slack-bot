# Open AI Slack Bot

Un pequeño proyecto en Python para crear un bot que te permita interactuar en Slack con OpenAI: Dall-E y ChatGPT

## Requirements

- Python 3.9 >
- VSCode o editor de preferencia.
- Instalar librerías con pip. En el tutorial usamos pyenv para crear virtualenvs que puedas usar diferenciados por proyecto. Para instalar `pyenv` sigue las instrucciones a continuación.

## VSCode

Para ir probando avances del código usamos la Interactive window de VSCode, que se activa instalando las extensiones recomendadas de python y jupyter notebook en VSCode (al iniciar un proyecto en python te va a abrir un cuadro de diálogo en donde te ofrece instalarlas y debes aceptar).

## Pyenv

1. Abre una terminal [command+space bar y tipea ‘terminal’] y ejecuta

`brew install pyenv pyenv-virtualenv`

2. En tu home, abre `pyenv`.zshrc (o créalo si no te aparece con nano ~/.zshrc) o .bashrc, y agrega las siguientes lineas, al final del archivo.

`eval "$(pyenv init -)"`

`eval "$(pyenv virtualenv-init -)"`

3. Cierra la terminal y abre una nueva.

4. Verifica la correcta instalación de `pyenv`

 `pyenv -v`

5. Instala una versión de python para que esté disponible en los ambientes virtuales que crees:

 `pyenv install 3.9.9`


6. [Opcional] Setear versión como global (la que se usará por defecto cuando abras python sin un ambiente virtual específico)

    - Setea esta version como la global.

    `pyenv global 3.9.9`

    - Verifica que quede configurada, cerrando la terminal, abriendo otra y ejecutando

    `which python # salida: /Users/[username]/.pyenv/shims/python`


7. Crea un ambiente virtual con el nombre de tu entorno y la versión que instalaste:

 `pyenv virtualenv 3.9.9 fintualist-3.9.9`



Ahora cada vez que quieras para usar tu ambiente virtual, ejecuta en tu consola:

 `pyenv activate fintualist-3.9.9`

y para desactivarlo

 `pyenv deactivate`

Para instalar paquetes en tu ambiente virtual, instálalos con `pip`
