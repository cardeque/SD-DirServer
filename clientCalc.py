import rpyc
from constRPYC import *
from server

class Client:
    conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = conn_directory.root.exposed_lookup("ServerCalculadora")
    if address == 'error':
        print(port)
    else:
        print(f"Conexão: {address}:{port}")

        n1 = int(input("Número[1]: "))
        n2 = int(input("Número[2]: "))

        conn_server = rpyc.connect(address, port)

        soma = conn_server.root.soma(n1, n2)
        subi = conn_server.root.sub(n1, n2)
        mult = conn_server.root.mult(n1, n2)
        divi = conn_server.root.div(n1, n2)

        print("Soma:{} \nSubtração: {} \nMultiplicação: {} \nDivisão: {}".format(soma, subi, mult, divi))