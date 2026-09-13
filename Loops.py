# LOOPS - O que aprendi hoje

# for - quando sei quantas vezes quero repetir
print("--- FOR ---")
frutas = ["maçã", "banana", "manga"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

# while - quando não sei quantas vezes
print("\n--- WHILE ---")
contador = 0
while contador < 3:
    print(f"Contando: {contador}")
    contador += 1

# loop com condição (bem útil pro seu questionário)
print("\n--- FOR COM IF ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} é par")
