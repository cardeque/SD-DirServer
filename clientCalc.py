import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCalculadora")
    if address == 'error':
        print(port)
    else:
        print(f"Conexão: {address}:{port}")

        numA = int(input("Número[1]: "))
        numB = int(input("Número[2]: "))

        conn_server = rpyc.connect(address, port)
        soma = conn_server.root.soma(numA, numB)
        subi = conn_server.root.sub(numA, numB)
        mult = conn_server.root.multi(numA, numB)
        divi = conn_server.root.divi(numA, numB)

        print("Soma: {}\nSubitração: {}\nMultiplicação: {}\nDivisão: {}".format(soma, subi, mult, divi))
