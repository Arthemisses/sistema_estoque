from produto import Produto

class Estoque:
    def __init__(self):
        # O projeto exige dois vetores
        self.produtos_nao_ordenados = []
        self.produtos_ordenados = []

    def adicionar_produto(self, produto):
        # 1. Adiciona no vetor não ordenado (Complexidade O(1))
        self.produtos_nao_ordenados.append(produto)

        # 2. Adiciona no vetor ordenado mantendo a ordem (Complexidade O(n))
        self._inserir_ordenado(produto)

    def _inserir_ordenado(self, novo_produto):
        """Implementação manual de inserção em lista ordenada."""
        # Encontra a posição correta para manter o vetor ordenado pelo código
        posicao = 0
        for i, p in enumerate(self.produtos_ordenados):
            if novo_produto.codigo > p.codigo:
                posicao = i + 1
            else:
                break

        # Insere o produto na posição encontrada, deslocando os outros
        self.produtos_ordenados.insert(posicao, novo_produto)