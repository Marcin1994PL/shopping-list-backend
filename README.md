# <h1>shopping-list-backend</h1>
A Python Rest API for Shopping List application

# <h3>Software</h3>
Python 3.6.4 <br>
Django 1.11.8 <br>
Django Rest Framework 3.7.3 <br>
django-allauth 0.34<br>
django-rest-auth 0.9.2<br>

<b>Przydatne komendy (należy być w folderze, gdzie znajduje się plik manage.py)</b>

Uruchamianie serwera:
```
python manage.py runserver
```

Po każdej zmianie modelu nalezy zrobić migracje. Pierwsze makemigrations tworzy także domyślne tabele w bazie, jak np. User:

```
python manage.py makemigrations
python manage.py migrate
```

Uruchamianie shella (można za jego pomocą przeglądać bazę):
```
python manage.py shell
```

Tworzenie superużytkownika (do zarządzania bazą z poziomu przeglądarki localhost:8000/admin):
```
python manage.py createsuperuser
```

Jak się zmieni kod, a ma się uruchomiony serwer, nie trzeba go restartować, jedynie trzeba pamiętać o zapisaniu pliku.


<h1>Endpointy do rejestracji i logowania </h1>
POST na rejestracje <br>
<code>/api/users/</code> <br>
POST na logowanie <br>
<code>/api/users/login</code> <br>
POST na utworzenie nowej grupy <br>
<code>/api/groups/</code> <br>
<br>
<h3>Przykładowe kolekcje dołączone w folderze "collections"</h3>
