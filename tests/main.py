import argparse

def main():
    parser = argparse.ArgumentParser(description="sistema de Estoque de Hardware")
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Comando: Cadastrar
    cadastrar = subparsers.add_parser("cadastrar", help="Adiciona um novo componente")
    cadastrar.add_argument("--nome", required=True, help="Nome do componente")
    cadastrar.add_argument("--preco", type=float, required=True, help="Preço unitário")
    cadastrar.add_argument("--qtd", type=int, required=True, help="Quantidade inicial")

    # Comando: Buscar
    buscar = subparsers.add_parser("buscar", help="Busca componente por código")
    buscar.add_argument("--id", required=True, help="Código do produto (ex: SC-001)")

    args = parser.parse_args()

    # Lógica de roteamento
    if args.comando == "cadastrar":
        print(f"Cadastrando {args.nome}...")
        # Aqui você chamaria: estoque.adicionar(Produto(args.nome, ...))
    elif args.comando == "buscar":
        print(f"Buscando ID: {args.id}")

if __name__ == "__main__":
    main()