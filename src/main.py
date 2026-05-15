import argparse
from produto import Produto
from estoque import Estoque


def main():
    parser = argparse.ArgumentParser(
        description="Sistema de Gerenciamento de Inventário de Hardware"
    )

    subparsers = parser.add_subparsers(dest="comando")

    # CADASTRAR
    cadastrar = subparsers.add_parser(
        "cadastrar",
        help="Adiciona um novo componente"
    )

    cadastrar.add_argument("--id", required=True, help="Código do produto")
    cadastrar.add_argument("--nome", required=True, help="Nome do produto")
    cadastrar.add_argument("--categoria", required=True, help="Categoria")
    cadastrar.add_argument("--preco", type=float, required=True, help="Preço")
    cadastrar.add_argument("--qtd", type=int, required=True, help="Quantidade")

    # BUSCAR
    buscar = subparsers.add_parser(
        "buscar",
        help="Busca um produto pelo código"
    )

    buscar.add_argument("--id", required=True, help="Código do produto")

    # LISTAR
    subparsers.add_parser(
        "listar",
        help="Lista todos os produtos"
    )

    # REMOVER
    remover = subparsers.add_parser(
        "remover",
        help="Remove um produto"
    )

    remover.add_argument("--id", required=True, help="Código do produto")

    # ATUALIZAR
    atualizar = subparsers.add_parser(
        "atualizar",
        help="Atualiza a quantidade em estoque"
    )

    atualizar.add_argument("--id", required=True, help="Código do produto")
    atualizar.add_argument("--qtd", type=int, required=True, help="Nova quantidade")

    args = parser.parse_args()

    estoque = Estoque()

    try:
        if args.comando == "cadastrar":
            produto = Produto(
                codigo=args.id,
                nome=args.nome,
                categoria=args.categoria,
                preco=args.preco,
                quantidade=args.qtd
            )

            estoque.adicionar_produto(produto)

            print("Produto cadastrado com sucesso!")
            print(produto)

        elif args.comando == "buscar":
            produto = estoque.buscar_produto(args.id)

            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")

        elif args.comando == "listar":
            produtos = estoque.listar_produtos()

            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("=== ESTOQUE ===")

                for produto in produtos:
                    print(produto)

        elif args.comando == "remover":
            removido = estoque.remover_produto(args.id)

            if removido:
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado.")

        elif args.comando == "atualizar":
            estoque.atualizar_quantidade(args.id, args.qtd)
            print("Quantidade atualizada com sucesso!")

        else:
            parser.print_help()

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()