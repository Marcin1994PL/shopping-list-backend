# <h1>shopping-list-backend</h1>
A Python Rest API for Shopping List application

# <h3>Software</h3>
Python 3.6.4 <br>
Django 1.11.8 <br>
Django Rest Framework 3.7.3 <br>
Django Rest Framework JWT 1.11.0 

<b>Przydatne komendy (należy być w folderze, gdzie znajduje się plik manage.py)<b>

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
