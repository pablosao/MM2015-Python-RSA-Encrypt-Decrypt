# -*- coding: utf-8 -*-

#      Nombre: Encriptación RSA
#       Fecha:  11 de noviembre de 2020
#  Creado por:
#              Pablo Sao
#              Mirka Monzón
# Descripción: El programa genera las llaves (pública y privada) para
#              encriptar el texto contenido en un archivo .txt
#
# Referencias:
#
# mnicat. (2020). RSA Encryption/Decryption with python. Extraído de: https://gist.github.com/hotpotcookie/1ad09de58c28789bba8a88cbb60d6ca5

import zlib
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from pathlib import Path

def genera_key(path="."):
    """
    Método para generación de llave privada y publica. La llave privada es exportada a la ruta
    enviada y la publica es retornada.
    :param path: ruta donde se almacenará la llave privada
    :return: llave publica en formato PEM
    """
    private_path = path + '/private_key.pem'

    #Generate a public/ private key pair using 4096 bits key length (512 bytes)
    new_key = RSA.generate(4096, e=65537)

    #Llave privada en formato PEM
    private_key = new_key.exportKey("PEM")

    # Llave publica en formato PEM
    public_key = new_key.publickey().exportKey("PEM")

    #Exportando llave privada en el path pasado al metodo
    private_key_path = Path(private_path)
    private_key_path.touch(mode=0o600)
    private_key_path.write_bytes(private_key)


    #public_key_path = Path('./files/public.pem')
    #public_key_path.touch(mode=0o664)
    #public_key_path.write_bytes(public_key)

    return public_key


def Encrypt(mensaje, public_key):
    """
    Encriptado de mensaje
    :param mensaje: mensaje a encriptar de tipo byte
    :param public_key: llave publica a utilizar para encriptar mensaje
    :return: mensaje encriptado codificado en base64
    """

    # Importando la llave publica
    rsa_key = RSA.importKey(public_key)

    # encriptación utilizando PKCS1_OAEP
    rsa_key = PKCS1_OAEP.new(rsa_key)

    #Comprimiendo el mensaje
    blob = zlib.compress(mensaje)

    # Para determinar el tamaño del fragmento, se determina la longitud de la
    # clave privada utilizada en bytes y reste 42 bytes (cuando utilice PKCS1_OAEP).
    # Los datos estarán cifrados en trozos
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = bytearray()

    while not end_loop:
        #Fragmento
        chunk = blob[offset:offset + chunk_size]

        # Si el fragmento de datos es menor que el tamaño del fragmento definito,
        # se completa con "". Indicando que llegamos al final del archivo, por lo
        # que terminamos el ciclo
        if len(chunk) % chunk_size != 0:
            end_loop = True
            chunk += bytes(chunk_size - len(chunk))

        # Se agrega el fragmento cifrado a la variable que contiene todo el documento
        # cifrado
        encrypted += rsa_key.encrypt(chunk)

        # Se aumenta el desplazamiento hacia el siguiente fragmento
        offset += chunk_size

    #Retornando el mensaje encriptado con codificación en Base 64
    return base64.b64encode(encrypted)


def Decrypt(mensaje, private_key):
    """
    Obtención del mensaje, utilizando la llave privada para desencriptación
    :param mensaje: mensaje a desencriptar
    :param private_key: llave privada para desencriptar el mensaje
    :return: Mensaje desencriptado y descomprimido
    """
    # Cargando llabbe privada
    rsakey = RSA.importKey(private_key)

    # Utilización de PKCS1_OAEP para desencripción
    rsakey = PKCS1_OAEP.new(rsakey)

    # Decodificando mensaje a Base 64
    encrypted_blob = base64.b64decode(mensaje)

    # Se desencriptara el mensaje en fragmentos, por lo que se determina el tamaño
    # del fragmento
    chunk_size = 512
    offset = 0
    decrypted = bytearray()

    while offset < len(encrypted_blob):

        # Fragmento a desencriptar
        chunk = encrypted_blob[offset: offset + chunk_size]

        # Juntando fragmento desencritpado al mensaje final
        decrypted += rsakey.decrypt(chunk)

        # Padando al siguiente fragmento para desencriptado
        offset += chunk_size

    # Retornando mensaje descomprimido
    return zlib.decompress(decrypted)