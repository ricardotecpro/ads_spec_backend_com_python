# Quiz 08 - Dicionários

1. Como se acessa o valor associado à chave "nome" no dicionário `d`?

    - [ ] d.nome
    - [x] d["nome"]
    - [ ] d(nome)
    - [ ] d -> nome

2. O que acontece se fizermos `d["chave"] = valor` e a chave já existir?

    - [ ] Cria uma chave duplicada
    - [ ] Gera um erro
    - [x] Atualiza o valor existente
    - [ ] Ignora o comando

3. Qual método retorna uma lista de tuplas (chave, valor)?

    - [ ] .all()
    - [ ] .list()
    - [x] .items()
    - [ ] .pairs()

4. Qual a saída de `d.get("chave_inexistente")`?

    - [ ] KeyError
    - [x] None
    - [ ] False
    - [ ] 0

5. As chaves de um dicionário devem ser:

    - [ ] Strings apenas
    - [ ] Objetos mutáveis (como listas)
    - [x] Objetos imutáveis (strings, números, tuplas) e únicas
    - [ ] Ordenadas alfabeticamente
