# tima_mag
Blog with Django3
Данный сайт реализован как влог с новостями, есть меню в котором имеются: Главная, О нас, Новости и Контакты.
Шаблоны страниц сделаны из  template tag
При создании новой новости как и по условию производится с помощью одного запроса, так при помощи одного запроса производится изменение (update) и удаление (delete) записей в базе. При выполениние использована одна база данных
Есть возможности редактирования при помощи стандартного администратора
Перемещение между вкладками открываю соотвествующие html-шаблоны (определяется исходя из URL текущей страницы)
Данный проект реализован двумя приложениями
На странице не одно меню, при нажатии на кнопко "подробнее" на странице новостей , открывается вся новость (используется <int:pk>)
При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
![image](https://user-images.githubusercontent.com/119942030/226587846-6e1accfa-475b-4a21-87d3-7ad26048aa37.png)
![image](https://user-images.githubusercontent.com/119942030/226587943-93552b8a-f4d9-4dd3-8a29-5589918ebc2f.png)
Переход по кнопке "подробнее"
![image](https://user-images.githubusercontent.com/119942030/226588044-8e72d193-6800-4dc4-a9cf-dd8a5f16889f.png)
Переход по кнопке "добавить статью"
![image](https://user-images.githubusercontent.com/119942030/226588290-e6406c73-28ed-440a-bdd3-2914b501c1b4.png)
После заполнения происходит переадресация на страницу новостей.
Вкладка "Контакты" при отравке , отправляет смс на почту 
При выполненни использовали только только Django и стандартную библиотеку Python.

