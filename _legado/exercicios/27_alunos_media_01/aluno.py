class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.matricula = 0
        self.media_notas = 0.0

    def cadastrar_dados(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def cadastrar_media_notas(self, media):
        self.media_notas = media

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
        print(f"Média de Notas: {self.media_notas}")