import random as rd

class File:
    def __init__(self):
        self.data = []
    def enfiler(self,elt):
        self.data.append(elt)
    def longueur(self):
        return len(self.data)
    def est_vide(self):
        return self.longueur()==0
    def defiler(self):
        return self.data.pop(0)
    def dernier(self):
        return self.data[-1]


class Server:
    def __init__(self):
        self.prochain_service = rd.randint(1,5)
    def maj_tps(self):
        self.prochain_service += rd.randint(3,10)

class Client:
    def __init__(self):
        self.temps_arrivee = 0
        self.temps_attente = 0

t= 10
liste_servers = []
liste_fin_client = []
for i in range(5):
    liste_servers.append(Server())

file_attente = File()

for i in range(10):
    tp_client = Client()
    tp_client.temps_arrivee(i)
    file_attente.enfiler(tp_client)

def check_server(t,liste_servers,file_attente):
    global liste_fin_client
    for server in liste_servers:
        if t == server.prochain_service:
            server.maj_tps()
            if not file_attente.est_vide():
                current_client = file_attente.defiler()
                current_client.temps_attente = (t -  current_client.temps_arrivee) + (server.prochain_service - t)
                liste_fin_client.append(current_client)
    return liste_servers,file_attente


for t in range(30):
    check_server(t,liste_servers,file_attente)







def check_defiler(t,liste_servers,file_attente):
    pass