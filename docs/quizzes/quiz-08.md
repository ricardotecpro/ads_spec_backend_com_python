# Quiz 08 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Como se acessa o valor associado à chave "nome" no dicionário `d`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">d.nome</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! d["nome"]">d["nome"]</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">d(nome)</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">d -> nome</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que acontece se fizermos `d["chave"] = valor` e a chave já existir?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Cria uma chave duplicada</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Gera um erro</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Atualiza o valor existente">Atualiza o valor existente</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ignora o comando</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual método retorna uma lista de tuplas (chave, valor)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">.all()</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">.list()</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! .items()">.items()</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">.pairs()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual a saída de `d.get("chave_inexistente")`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">KeyError</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! None">None</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">False</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">0</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. As chaves de um dicionário devem ser:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Strings apenas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Objetos mutáveis (como listas)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Objetos imutáveis (strings, números, tuplas) e únicas">Objetos imutáveis (strings, números, tuplas) e únicas</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ordenadas alfabeticamente</div>
  <div class="quiz-feedback"></div>
</div>

