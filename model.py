class Pessoa:
    def pessoa(self,nome,senha):
        self.nome=nome
        self.senha=senha
pessoas=[]

def add_pessoa(nome, senha):
    id = len(pessoas) + 1
    nova_pessoa = Pessoa(id, nome, senha)
    pessoas.append(nova_pessoa)