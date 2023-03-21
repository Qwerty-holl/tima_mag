# tima_mag
Blog with Django3
Я немного пошел дальше из исходной задачи и улучшить сайт показав больше своих способностей.
Данный сайт реализован как влог с новостями, есть меню в котором имеются: Главная, О нас, Новости и Контакты.
Шаблоны страниц сделаны из  template tag
При создании новой новости как и по условию производится с помощью одного запроса, так при помощи одного запроса производится изменение (update) и удаление (delete) записей в базе. При выполениние использована одна база данных
Есть возможности редактирования при помощи стандартного администратора
Перемещение между вкладками открываю соотвествующие html-шаблоны (определяется исходя из URL текущей страницы)
Данный проект реализован двумя приложениями
На странице не одно меню, при нажатии на кнопко "подробнее" на странице новостей , открывается вся новость (используется <int:pk>)
При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
Главная страница
![image](https://user-images.githubusercontent.com/119942030/226587846-6e1accfa-475b-4a21-87d3-7ad26048aa37.png)
Переход на страницу новостей
![image](https://user-images.githubusercontent.com/119942030/226587943-93552b8a-f4d9-4dd3-8a29-5589918ebc2f.png)
Переход по кнопке "подробнее"
![image](https://user-images.githubusercontent.com/119942030/226588044-8e72d193-6800-4dc4-a9cf-dd8a5f16889f.png)
Переход по кнопке "добавить статью"
![image](https://user-images.githubusercontent.com/119942030/226588290-e6406c73-28ed-440a-bdd3-2914b501c1b4.png)
Заполненый вид формы
![image](https://user-images.githubusercontent.com/119942030/226593567-887b1604-608e-4ba8-9607-5cfd39949e9f.png)
После добавления новости, переадресация на стр. с новостями где мы видим, что наша новость добавилась
![image](https://user-images.githubusercontent.com/119942030/226593628-adece8dd-869f-45c3-81b5-4f126238b199.png)
При нажатии"Подробнее" мы можем увидеть все поля которые мы заполнили
![image](https://user-images.githubusercontent.com/119942030/226593936-d54ebded-f694-48d8-bb86-36e84b8ec49c.png)
Тест отправки заявки для "обратно связи"
![image](https://user-images.githubusercontent.com/119942030/226594815-c4ca857f-cc48-4253-9cfc-f8934f76cdd2.png)
После нажатия отправляется письмо с данными:
![image](https://user-images.githubusercontent.com/119942030/226594970-261f5988-1394-40c0-9b41-27146f321285.png)
После заполнения происходит переадресация на страницу новостей.
При выполненни использовали только только Django и стандартную библиотеку Python.

