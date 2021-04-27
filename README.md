# Script para copia de archivos

Este script está creado para la clonación de archivos de un servidor a un repositorio local mediante el uso de ssh y sftp

## Uso

1. Clonar el repositorio: `git clone https://github.com/juanig98/sftpBaker.git`
2. Crear el environment: `python3 -m venv env`
3. Instalar librerías: `pip install -r requirements.txt`
4. Copiar archivo de configuración: `cp example.py settings.py` 
5. Configurar [settings.py](./settings.py)
6. Ejecución: `python .` (o `python __main__.py`)

## Configuración 

```python
# Hora de copia
hour = "21h00m"

# Localización del backup remoto
remote_path = PATH/TO/REMOTE/FILE

# Localización del backup local
local_path = PATH/TO/REPOSITORY/LOCAL

# Nombre del archivo remoto
remote_filename = REMOTE.FILENAME

# Nombre del archivo local
local_filename = LOCAL.FILENAME

# Credenciales de acceso 
conection = {
    "host": HOST/HOSTNAME,
    "user_ssh": USER SSH,
    "passwd_ssh": PASSWORD SSH,
    "user_ftp": USER FTP,
   "passwd_ftp": PASSWORD FTP
}
```