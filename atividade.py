def manipula_produto(u, v, k):
  k = 0.9*k
  p = v, u, k
  return p

código = input("\enentrar com o codigo do produto: ")
produto = input("\enentrar com o nome do produto: ")
preço = float(input("\enentrar com o preço do produto: "))

detalhes_produto = manipula_produto(produto, código, preço)
print("\nDetalhes do produto:")
print("\Código do produto: ", detalhes_produto[0])
print("Produto: ", detalhes_produto[1])
print("Preço do produto com desconto de 10%: R$ ", detalhes_produto[2])