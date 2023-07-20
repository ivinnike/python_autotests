# Python autotests
Пример автотестов на pytest + requests

<div id="header" align="center">
  <img src="https://media.giphy.com/media/8UGGp7rQvfhe63HrFq/giphy.gif" width="300"/>
</div>

<h3> Написан код на Python для 3-х запросов с выводом ответа по документации Покемонов:</h3>
    
    - Создание покемона (**POST /pokemons**)
    - Смена имени покемона (**PUT /pokemons**)
    - Поймать покемона в покебол (**POST /trainers/add_pokeball**)

<h3> Написаны два Автотеста, используя PyTest, которые проверяют: </h3>

- что ответ запрос **GET /trainers** приходит с кодом 200
- что в ответе приходит строчка с именем моего тренера
