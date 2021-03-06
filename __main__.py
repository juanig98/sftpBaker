import os
import paramiko
from settings import *

if __name__ == "__main__":

    # Set log file
    log = open(logs_path + "log_" + date + ".log", "w")
    log.write(timestamp + "Iniciando copía\n")
    log.write(timestamp + "Fecha: " + date + "\n")

    try:
        client = paramiko.SSHClient()  # Declaracion de paramiko
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Establecimiento de politicas de host
        
        if require_assign_permission:
            client.connect(conection["host"], username=conection["user_ssh"], password=conection["passwd_ssh"], key_filename=private_key_path)  # Establecimiento de conexión SSH
            log.write(timestamp + "La conexión SSH se estableció correctamente\n")

            # Inicio de sesión SSH mediante Canal
            session = client.get_transport().open_session()

            if session.active:  # Si está activa
                session.exec_command("chmod 777 -R " + remote_path)  # Conceder permisos (Caso necesario donde la conexión ssh y ftp sea de distintos usuarios con distintos permisos)
                log.write(timestamp + "Se han otorgado los permisos correctamente\n")
                client.close()  # Cierre de la conexion SSH
                log.write(timestamp + "La conexión SSH ha finalizado\n")
        
        log.write(timestamp + "Iniciando conexión SFTP\n")
        client.connect(conection["host"], username=conection["user_ftp"], password=conection["passwd_ftp"], key_filename=private_key_path)  # Establecimiento de conexión SFTP

        # Inicio de sesión SFTP
        sftp_client = client.open_sftp()
        log.write(timestamp + "La conexión SFTP se estableció correctamente\n")
        # Transferencia de archivo
        sftp_client.get(
            remote_path + remote_filename,  # Path de host
            local_path + local_filename,  # Path de receptor
        )

        log.write(timestamp + "El backup se copió existosamente\n")
        log.write(timestamp + "Info: \n\tArchivo remoto: " + remote_path + remote_filename + "\n\tArchivo local: " + local_path + local_filename + "\n")
        sftp_client.close()  # Cierre de sesión SFTP
        log.write(timestamp + "Sesión finalizada\n")

    except paramiko.ssh_exception.AuthenticationException as e:
        log.write(timestamp + "La conexión falló. \nDetalles: " + str(e) + "\n")
    except Exception as e:
        log.write(timestamp + "El programa falló. \nDetalles: " + str(e) + "\n")
    finally:
        log.write(timestamp + "El programa finalizó")
        log.close()
