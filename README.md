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

POST na rejestracje  <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/add</code> <br>

POST na logowanie  <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/login</code> <br>

PUT na edycje uzytkownika <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/edit</code> <br>

GET na dane uzytkownika <b> DONE </b> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/detail</code> <br>

GET na grupy użytkownika <font color="red">TODP</font> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/groups/</code> <br>

DELETE na usunięcie się z grupy <font color="red">TODP</font> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/groups/{idGroup}</code> <br>

GET na listy użytkownika <font color="red">TODP</font> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/user/lists</code> <br>

POST na utworzenie nowej grupy <font color="red">TODP</font> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/</code> <br>

GET na listę dostępnych grup <font color="red">TODP</font> <br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/</code> <br>

POST na dodanie się do grupy <font color="red">TODP</font><br>
<ul>
  <li>User</li>
</ul>
<code>/api/groups/join</code><br>

GET na czlonkow grupy <font color="red">TODP</font><br>
<ul>
  <li>Members</li>
</ul>
<code>/api/groups/members</code><br>

DELETE usunięcie członka grupy <font color="red">TODP</font><br>
<ul>
  <li>Group Owner</li>
</ul>
<code>/api/groups/members/{idUser}</code><br>

POST na dodanie nowej listy w ramach grupy <font color="red">TODP</font><br>
<ul>
  <li>Member</li>
</ul>
<code>/api/groups/{idGroup}/lists/</code> <br>

GET na listę <font color="red">TODP</font> <br>
<ul>
  <li>Member</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/ </code> <br>

DELETE na listę <font color="red">TODP</font> <br>
<ul>
  <li>List Owner</li>
  <li>Group Owner</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/ </code> <br>

POST na dodanie nowego itemu do listy <font color="red">TODP</font><br>
<ul>
  <li>List Owner</li>
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/ <br>
  
PUT na edycje itemu w liście <font color="red">TODP</font> <br>
<ul>
  <li>List Owner - wszystko, pod warunkiem, że item !isBought</li> 
  <li>Member - change from isBought = False to isBought = True</li> 
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/{idItem} </code> <br>

DELETE na usunięcie itemu z listy <font color="red">TODP</font> <br>
<ul>
  <li>List Owner - pod warunkiem, że item !isBought</li> 
</ul>
<code>/api/groups/{idGroup}/lists/{idList}/items/{idItem} </code> <br>

<br>
<h3>Przykładowe kolekcje dołączone w folderze "collections"</h3>
