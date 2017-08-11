class Tree:
    def __init__(self, info):
        self.info = info
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.info, self.direita.info = self.direita.info, self.info
        aux = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(aux, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.info, self.esquerda.info = self.esquerda.info, self.info
        aux = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, aux)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def insere(self, info):
        if info <= self.info:
            if not self.esquerda:
                self.esquerda = Tree(info)
            else:
                self.esquerda.insere(info)
        else:
            if not self.direita:
                self.direita = Tree(info)
            else:
                self.direita.insere(info)
        self.executaBalanco()

    def imprimeArvore(self, indent=0):
        print(" " * indent + str(self.info))
        if self.esquerda:
            self.esquerda.imprimeArvore(indent + 2)
        if self.direita:
            self.direita.imprimeArvore(indent + 2)
