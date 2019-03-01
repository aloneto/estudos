class sendToDvr(object):
    def __init__ (self):
        print ("construtor chamado com sucesso")

    def cadastra(self,ip,user,senha,canal):
        self.ip = ip
        self.user = user
        self.senha = senha
        self.canal = canal

    def set_Funcion(self,input):
        if input == '*':
            print ("asterisco digitado")

    def envia(self):
        print("enviando para ", self.ip, self.user, self.senha, self.canal)




dvr1 = sendToDvr()
dvr1.cadastra ('192.168.2.101','admin','aaa',1)
dvr1.envia()
dvr1.set_Funcion('*')
#dvr2 = sendToDvr('192.168.2.102','admin','aaa',1)



