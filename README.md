# <h1>shopping-list-backend</h1>
A Python Rest API for Shopping List application

# <h3>Software</h3>
Python 3.6.4 <br>
Django 1.11.8 <br>
Django Rest Framework 3.7.3 <br>

<b>Przydatne komendy (należy być w folderze, gdzie znajduje się plik manage.py)</b>


Na początku tworzymy bazę i tabalę:

```
python manage.py makemigrations
python manage.py migrate
```

Uruchamianie serwera:
```
python manage.py runserver
```

Uruchamianie shella (można za jego pomocą przeglądać bazę, ale polecam localhost:8000/admin):
```
python manage.py shell
```

Tworzenie superużytkownika (do zarządzania bazą z poziomu przeglądarki localhost:8000/admin):
```
python manage.py createsuperuser
```

Jak się zmieni kod, a ma się uruchomiony serwer, nie trzeba go restartować, jedynie trzeba pamiętać o zapisaniu pliku.


<h1>Endpointy do rejestracji i logowania </h1>

![#c5f015](https://placehold.it/15/c5f015/000000?text=+)
POST na rejestracje  <b> DONE </b> <br><br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/add</code> <br>

![#c5f015](https://placehold.it/15/c5f015/000000?text=+)
POST na logowanie  <b> DONE </b> <br><br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/login</code> <br><br>

![#c5f015](https://placehold.it/15/c5f015/000000?text=+)
PUT na edycje uzytkownika <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/edit</code> <br><br>

![#c5f015](https://placehold.it/15/c5f015/000000?text=+)
GET na dane uzytkownika <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/detail</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
GET na grupy użytkownika <b>TODO</b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/groups/</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
DELETE na usunięcie się z grupy <b>TODO</b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/groups/{idGroup}</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
GET na listy użytkownika <b>TODO</b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/lists</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
POST na utworzenie nowej grupy <b>TODO</b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
GET na listę dostępnych grup <b>TODO</b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
POST na dodanie się do grupy <b>TODO</b><br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/join</code><br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
GET na czlonkow grupy <b>TODO</b><br>
<ul>
  <li>Members</li>
</ul>
<code>/api/groups/members</code><br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
DELETE usunięcie członka grupy <b>TODO</b><br>
<ul>
  <li>Group Owner</li>
</ul>
<code>/api/groups/members/{idUser}</code><br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
POST na dodanie nowej listy w ramach grupy <b>TODO</b><br>
<ul>
  <li>Member</li>
</ul>
<code>/api/groups/{idGroup}/lists/</code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
GET na listę ![#f03c15] <b>TODO</b> <br>
<ul>
  <li>Member</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/ </code> <br><br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
DELETE na listę <b>TODO</b> <br>
<ul>
  <li>List Owner</li>
  <li>Group Owner</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/ </code> <br> <br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
POST na dodanie nowego itemu do listy <b>TODO</b><br>
<ul>
  <li>List Owner</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/ <br> <br>
  
![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
PUT na edycje itemu w liście <b>TODO</b> <br>
<ul>
  <li>List Owner - wszystko, pod warunkiem, że item !isBought</li> 
  <li>Member - change from isBought = False to isBought = True</li> 
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/{idItem} </code> <br>

![#f03c15](https://placehold.it/15/f03c15/000000?text=+)
DELETE na usunięcie itemu z listy <b>TODO</b> <br>
<ul>
  <li>List Owner - pod warunkiem, że item !isBought</li> 
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/{idItem} </code> <br>

<br>
<h3>Przykładowe kolekcje dołączone w folderze "collections"</h3>
