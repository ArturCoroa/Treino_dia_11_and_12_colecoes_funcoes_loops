# COLEÇÕES - O que aprendi hoje

# LISTA - pode mudar, ordenada []
print("--- LISTA ---")
minhas_cores = ["azul", "preto", "vermelho"]
minhas_cores.append("verde") # adiciona
print(minhas_cores)
print(f"Primeira cor: {minhas_cores[0]}")

# TUPLA - não muda, ordenada ()
print("\n--- TUPLA ---")
coordenadas = (12.5, -38.7) # ex: latitude/longitude de Santo Amaro
print(coordenadas)

# SET - não repete, sem ordem {}
print("\n--- SET ---")
numeros = {1, 2, 2, 3, 3, 3}
print(numeros) # vai imprimir {1, 2, 3} - remove repetido

# DICIONÁRIO - chave e valor {}
print("\n--- DICIONÁRIO ---")
pessoa = {
    "nome": "Artur",
    "idade": 20,
    "cidade": "Santo Amaro"
}
print(pessoa["nome"])
pessoa["profissao"] = "Dev" # adiciona novo campo
print(pessoa)
