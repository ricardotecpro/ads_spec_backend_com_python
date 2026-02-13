from aluno import Aluno

def main():
    aluno_obj = Aluno()

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = int(input("Digite o número de matrícula: "))

    aluno_obj.cadastrar_dados(nome, idade, matricula)

    media = float(input("Digite a média de notas: "))
    aluno_obj.cadastrar_media_notas(media)

    aluno_obj.exibir_informacoes()

if __name__ == "__main__":
    main()