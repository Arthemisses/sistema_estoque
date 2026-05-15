import json
import os
from produto import Produto


class Estoque:
    def __init__(self, arquivo="data/estoque.json"):
        self.arquivo = arquivo

        # O projeto exige dois vetores
        self.produtos_nao_ordenados = []
        self.produtos_ordenados = []

        self._carregar_dados()

    def adicionar_produto(self, produto):
        # Evita códigos duplicados
        if self.buscar_produto(produto.codigo):
            raise ValueError("Já existe um produto com esse código.")

        # 1. Adiciona no vetor não ordenado (Complexidade O(1))
        self.produtos_nao_ordenados.append(produto)

        # 2. Adiciona no vetor ordenado mantendo a ordem (Complexidade O(n))
        self._inserir_ordenado(produto)

        self._salvar_dados()

    def _inserir_ordenado(self, novo_produto):
        """Implementação manual de inserção em lista ordenada."""
        posicao = 0

        for i, p in enumerate(self.produtos_ordenados):
            if novo_produto.codigo > p.codigo:
                posicao = i + 1
            else:
                break

        self.produtos_ordenados.insert(posicao, novo_produto)

    def buscar_produto(self, codigo):
        for produto in self.produtos_ordenados:
            if produto.codigo == codigo:
                return produto

        return None

    def listar_produtos(self):
        return self.produtos_ordenados

    def remover_produto(self, codigo):
        produto = self.buscar_produto(codigo)

        if not produto:
            return False

        self.produtos_nao_ordenados.remove(produto)
        self.produtos_ordenados.remove(produto)

        self._salvar_dados()

        return True

    def atualizar_quantidade(self, codigo, quantidade):
        produto = self.buscar_produto(codigo)

        if not produto:
            raise ValueError("Produto não encontrado.")

        if quantidade < 0:
            raise ValueError("Quantidade inválida.")

        produto.quantidade = quantidade

        self._salvar_dados()

    def _salvar_dados(self):
        os.makedirs(os.path.dirname(self.arquivo), exist_ok=True)

        dados = []

        for produto in self.produtos_nao_ordenados:
            dados.append({
                "codigo": produto.codigo,
                "nome": produto.nome,
                "categoria": produto.categoria,
                "preco": produto.preco,
                "quantidade": produto.quantidade
            })

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def _carregar_dados(self):
        if not os.path.exists(self.arquivo):
            return

        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados:
                produto = Produto(
                    item["codigo"],
                    item["nome"],
                    item["categoria"],
                    item["preco"],
                    item["quantidade"]
                )

                self.produtos_nao_ordenados.append(produto)
                self._inserir_ordenado(produto)

        except json.JSONDecodeError:
            pass