# Inicializando dignidade como uma variável global
dignidade = 10


def dentro_condicoes(mulher, gorda, bonita, legal, gostosa, generosa, educada, simpática, gosta):
    global dignidade

    # Verifica se a pessoa é considerada "gostosa"
    if gostosa:
        return True

    # Verifica se a pessoa é considerada "simpática"
    if simpática:
        return True

    # Verifica as condições com base nos atributos fornecidos
    if not mulher and gorda:
        return False

    if mulher and gorda:
        if bonita and legal:
            return True
        elif not bonita and legal:
            dignidade -= 5
            return False
        elif bonita and not legal:
            return True

    if mulher and not gorda:
        if bonita and legal:
            return True
        elif not bonita and not legal:
            dignidade -= 2
            return False
        elif bonita and not legal:
            return True

    if mulher and generosa and educada and simpática:
        return True

    # Considera se o usuário gosta da pessoa
    if gosta:
        return True

    # Retorna False se nenhuma das condições acima for atendida
    return False


# Função para coletar entrada do usuário
def coletar_dados_usuario():
    global dignidade

    # Coletando informações do usuário
    mulher = input("A pessoa é mulher? (sim/não): ").strip().lower() == 'sim'
    gorda = input("A pessoa é gorda? (sim/não): ").strip().lower() == 'sim'
    bonita = input("A pessoa é bonita? (sim/não): ").strip().lower() == 'sim'
    legal = input("A pessoa é legal? (sim/não): ").strip().lower() == 'sim'
    gostosa = input("A pessoa é gostosa? (sim/não): ").strip().lower() == 'sim'
    generosa = input("A pessoa é generosa? (sim/não): ").strip().lower() == 'sim'
    educada = input("A pessoa é educada? (sim/não): ").strip().lower() == 'sim'
    simpática = input("A pessoa é simpática? (sim/não): ").strip().lower() == 'sim'
    gosta = input("Você gosta da pessoa? (sim/não): ").strip().lower() == 'sim'

    # Chamando a função com as respostas do usuário
    resultado = dentro_condicoes(mulher, gorda, bonita, legal, gostosa, generosa, educada, simpática, gosta)

    # Exibindo o resultado
    print(f"O resultado da avaliação é: {'Dentro' if resultado else 'Fora'}")
    print(f"Dignidade atual: {dignidade}")


# Executar a função de coleta de dados do usuário
coletar_dados_usuario()
