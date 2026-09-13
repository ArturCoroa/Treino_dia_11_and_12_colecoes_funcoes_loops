# FUNÇÕES - O que aprendi hoje

# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Artur"))

# Função com coleção + loop (juntando tudo de hoje)
def filtrar_maiores_de_idade(lista_pessoas):
    maiores = []
    for pessoa in lista_pessoas:
        if pessoa["idade"] >= 18:
            maiores.append(pessoa["nome"])
    return maiores

galera = [
    {"nome": "Artur", "idade": 20},
    {"nome": "João", "idade": 15},
    {"nome": "Maria", "idade": 22}
]

print(f"Maiores: {filtrar_maiores_de_idade(galera)}")

# Função do seu questionário melhorada
def verificar_acesso(idade):
    if idade >= 18:
        return True
    else:
        return False

idade_digitada = 19
if verificar_acesso(idade_digitada):
    print("acesso liberado!")
else:
    print("acesso negado!")
