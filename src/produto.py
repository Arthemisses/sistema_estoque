class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        # Validações rápidas (Regras de Negócio)
        if preco < 0:
            raise ValueError("O preço deve ser positivo.")
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def __repr__(self):
        # Isso ajuda na estética quando você der um print no objeto
        return f"[{self.codigo}] {self.nome} - R$ {self.preco} (Qtd: {self.quantidade})"

if __name__ == "__main__":
    p = Produto("SC-001", "Transistor BC548", "Semicondutores", 0.50, 100)
    print(p)