import rpyc
from socket import gethostbyname,gethostname
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class ServerCalculadora(rpyc.Service): #alterar ServerCalculadora para o nome do servidor
    value = []

    def soma(self, num1, num2):
        print(f"{num1} + {num2}")
        return num1+num2

    def sub(self, num1, num2):
        print(f"{num1} / {num2}")
        return num1-num2

    def mult(self, num1, num2):
        print(f"{num1} * {num2}")
        return num1*num2

    def div(self, num1, num2):
        print(f"{num1} / {num2}")
        return num1/num2



if __name__ == "__main__":
    server = ThreadedServer(ServerCalculadora, port = 20202) #alterar o ServerCalculadora para o nome do servidor
    conn = rpyc.connect(host=DIR_SERVER, port=DIR_PORT)
    my_address = gethostbyname(gethostname())
    (reg, token) = conn.root.exposed_register("ServerCalculadora", my_address, 20202)
    # print (reg) #precisa ser alterado para receber o token/senha de alteração
    if reg:
        print(f"Primeira vez conectado. Token: {token}")
        server.start()
    else:
        print("Reiniciando")
        option = str(input("1) Atualizar serviço.\n2) Remover seviço.\n3) Cancelar\n"))
        if option == "1" or option == "2":
            if option == "1" :
                token = str(input("Token: "))
                update = conn.root.exposed_update_register("Calculadora", my_address, 20202, token)
                if update:
                    print("Atualizando")
                    server.start()
                else:
                    print("Token invalido")
            else:
                token = str(input("Token: "))
                remove = conn.root.exposed_unregister("Calculadora", token)
                if remove:
                    print("Serviço removido")
                else:
                    print("Token invalido")
        else:
            print("Adeus!")
