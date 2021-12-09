import time

# Helpers
# Configuración de días
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_of_week_spanish = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado', 'domingo']
date = time.strftime('%Y-%m-%d')
timestamp = time.strftime('%Y-%m-%d %I:%M:%S : ')
day = days_of_week_spanish[days_of_week.index(time.strftime('%A'))]

# Hora de copia
hour = '21h00m'

# Control de asignación de permisos
require_assign_permission = False

# Localización de los logs
logs_path = '/path/folder/logs'

# Localización del backup remoto
remote_path = '/path/folder/server'

# Localización del backup local
local_path = '/path/repository/local'

# Nombre del archivo remoto
remote_filename = 'filename'

# Nombre del archivo local
local_filename = 'filename'

# Path a private key
private_key_path = ""

# Credenciales de acceso 
conection = {
    'host': 'hots',
    'user_ssh': 'user_ssh',
    'passwd_ssh': 'passwd_ssh',
    'user_ftp': 'user_ftp',
    'passwd_ftp': 'passwd_ftp'
}