  
from No import No


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def insere(self, novo_dado):
        novo_no = No(novo_dado)
        novo_no.anterior = self.topo
        self.topo = novo_no
        self.tamanho = self.tamanho + 1

    def remove(self):
        assert self.topo, "Impossível remover valor de uma Pilha que está vazia!!!"
        self.topo = self.topo.anterior
        self.tamanho = self.tamanho - 1

  