# import rpyc
#
# from constRPYC import *
#
# class Client:
#     conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
#     (address, port) = conn_directory.root.exposed_lookup("ServerCrypt")
#
#     if address == 'error':
#         print(port)
#     else:
#         print(f"Conexão: {address}:{port}")
#         conn_server = rpyc.connect(address, port)
#         operation = str(input("[1] Encriptar\n[2] Decifrar\n[3] Cancelar\n"))
#
#         if operation == "1" or operation == "2":
#             if operation == "1":
#                 text = input("Mensagem: ")
#                 (encText, pub_key) = conn_server.root.exposed_encrypt(text)
#                 print(f"Mensagem encriptada: {encText}\n Chave pública: {pub_key}")
#                 file = open("enc_message.txt", 'w')
#                 file.write(encText)
#                 file.close()
#             else:
#                 # text = input("Encripted message: ")
#                 msg = input("Entre a mensagem:")
#                 print(f"Mensagem: {msg}")
#                 pub_key = input("Chave publica: ")
#                 text = conn_server.root.exposed_decrypt(msg, pub_key)
#                 print(f"Mensagem: {text}")
#         else:
#             print("Adeus!")


import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCrypt")
    if address == 'error':
        print(port)
    else:
        print(f"Conexão: {address}:{port}")
        conn_server = rpyc.connect(address, port)
        operation = str(input("Encriptar[1]:\nDecifrar[2]:\nCancelar[3]:\n"))
        if operation == "1" or operation == "2":
            if operation == "1":
                text = input("Mensagem: ")
                (encText, pub_key) = conn_server.root.exposed_encrypt(text)
                print(f"Encriptada:{encText}\n Chave publica: {pub_key}")
                file = open("enc_message.txt", 'w')
                file.write(encText)
                file.close()
            else:
                enc_message = input("Entre a mensagem encriptada: ")
                print(f"Mensagem encriptada: {enc_message}")
                pub_key = input("Chave Publica:")
                text = conn_server.root.exposed_decrypt(enc_message, pub_key)
                print(f"Mensagem: {text}")
        else:
            print("Adeus!")
