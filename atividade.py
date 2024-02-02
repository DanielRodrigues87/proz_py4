import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Por favor, insira um ano válido.")
        except ValueError:
            print("Erro: Insira um valor numérico.")

def main():
    nome_completo = input("Digite o nome completo: ")
    
    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"\nNome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __name__ == "__main__":
    main()
