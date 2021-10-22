def registra_nome(sobrenome_pai, sobrenome_mae, nome_bebe):
  primeiro_nome = nome_bebe
  segundo_nome = sobrenome_mae
  sobrenome = sobrenome_pai
  return primeiro_nome + " " + segundo_nome +  " " + sobrenome 

nome_da_crianca = registra_nome("Parrilla", "Siqueira", "Jordania")
print("\nBebê registrado como: ", nome_da_crianca)