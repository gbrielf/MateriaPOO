import json
import os

class Carrinho:
    def __init__(self, arquivo_estoque, arquivo_pedidos):
        self.carrinho = []
        self.arquivo_do_estoque = arquivo_estoque
        self.arquivo_dos_pedidos = arquivo_pedidos
        
        # Verifica se o arquivo de estoque existe, se não, cria com um conteúdo vazio
        if not os.path.exists(self.arquivo_do_estoque):
            print(f"{self.arquivo_do_estoque} não encontrado. Criando arquivo...")
            with open(self.arquivo_do_estoque, 'w') as f:
                json.dump([], f)  # Inicializa o arquivo com uma lista vazia (ou pode inicializar de outra forma)
                
    def adicionar_produto(self, produto_id, quantidade, cliente_id):
        with open(self.arquivo_do_estoque, 'r') as f:
            estoque = json.load(f)
        produto = next((p for p in estoque if p['id'] == produto_id), None)
        if not produto:
            print(f"Produto com ID {produto_id} não encontrado.")
            return
        if produto['quantidade'] < quantidade:
            print("Quantidade insuficiente no estoque.")
            return
        self.carrinho.append({
            "id": produto['id'],
            "nome": produto['nome'],
            "preco": produto['preco'],
            "quantidade": quantidade,
            "cliente_id": cliente_id
        })
        print(f"{quantidade}x {produto['nome']} adicionados ao carrinho.")
        with open('carrinho.json', 'w') as f:
            json.dump(self.carrinho, f, indent=4)

    def fechar_pedido(self, cliente_id):
        if not self.carrinho:
            print("Carrinho está vazio. Adicione itens antes de fechar o pedido.")
            return
        with open(self.arquivo_do_estoque, 'r') as f:
            estoque = json.load(f)
        for item in self.carrinho:
            produto = next((p for p in estoque if p['id'] == item['id']), None)
            if produto:
                produto['quantidade'] -= item['quantidade']
        with open(self.arquivo_do_estoque, 'w') as f:
            json.dump(estoque, f, indent=4)

        pedido = {
            "pedido_id": len(self.carregar_pedidos()) + 1,
            "cliente_id": cliente_id,
            "itens": self.carrinho
        }
        pedidos = self.carregar_pedidos()
        pedidos.append(pedido)

        with open(self.arquivo_dos_pedidos, 'w') as f:
            json.dump(pedidos, f, indent=4)

        print("Pedido finalizado com sucesso!")
        self.carrinho = []  # Limpar o carrinho

        # Limpar o arquivo carrinho.json (opcional)
        if os.path.exists('carrinho.json'):
            os.remove('carrinho.json')
    
    def ver_pedidos(self):
        pedidos = self.carregar_pedidos()
        
        if not pedidos:
            print("Você ainda não fez nenhum pedido.")
            return
        print("Seus pedidos:")
        for pedido in pedidos:
            if cliente_id is None or pedido["cliente_id"] == cliente_id:
                print(f"Pedido ID: {pedido['pedido_id']}")
                for item in pedido['itens']:
                    print(f"  - {item['nome']}: {item['quantidade']} x R${item['preco']:.2f}")
                print()
    
    def carregar_pedidos(self):
        # Carrega os pedidos, cria o arquivo se não existir
        if not os.path.exists(self.arquivo_dos_pedidos):
            with open(self.arquivo_dos_pedidos, 'w') as f:
                json.dump([], f)
            return []
        with open(self.arquivo_dos_pedidos, 'r') as f:
            return json.load(f)
