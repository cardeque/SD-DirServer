import rpyc
from constRPYC import *

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCalculadora")
    if address == 'error':
        print(port)
    else:
        print(f"Conexão: {address}:{port}")

        nA = int(input("Número[1]: "))
        nB = int(input("Número[2]: "))

        conn_server = rpyc.connect(address, port)

        soma = conn_server.root.soma(nA, nB)
        subi = conn_server.root.sub(nA, nB)
        mult = conn_server.root.mult(nA, nB)
        divi = conn_server.root.div(nA, nB)

        print("Soma:{} \nSubtração: {} \nMultiplicação: {} \nDivisão: {}".format(soma, subi, mult, divi))