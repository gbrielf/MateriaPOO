import json

class Carrinho:
    def __init__(self,id):
        self.id_cliente = id
        self.itens = []
    #"id_cliente": cls.cliente_id, "id": produto_selecionado.id, "descricao": produto_selecionado.descricao, "quantidade": qntd, "preco": produto_selecionado.preco, "total_a_pagar": qntd*produto_selecionado.preco
    def adicionar_produto(cls, dados):
        required_keys = ["id_cliente","id", "descricao","quantidade", "preco", "total_a_pagar"]  # Sem "id_categoria"
        for key in required_keys:
            if key not in dados:
                raise ValueError(f"Chave ausente: {key}")
        dados.setdefault("id_categoria", None)  # Adiciona id_categoria se estiver ausente
        cls.itens.append(dados)
        cls.salvar()

class Carrinhos:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        # calcula o id do objeto
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        obj.id = id + 1    
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
    @classmethod
    def listar(cls):
        # abre a lista do arquivo
        cls.abrir()
        # retorna a lista para a UI
        return cls.objetos[:]
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()        
    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo clientes.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> clientes_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["id_categoria"])
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    


