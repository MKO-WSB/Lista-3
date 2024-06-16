Opis
Ten skrypt automatyzuje testowanie API przy użyciu narzędzia curl. Testuje wybrane endpointy publicznego API, wysyła żądania HTTP i sprawdza poprawność odpowiedzi, w tym statusy HTTP oraz kluczowe elementy w odpowiedziach JSON.


Wymagania
curl musi być zainstalowany na systemie
Python 3.x (do uruchomienia skryptu)


Skrypt
Skrypt wysyła żądania GET do trzech endpointów API:
https://jsonplaceholder.typicode.com/posts/1
https://jsonplaceholder.typicode.com/users/1
https://jsonplaceholder.typicode.com/todos/1
Sprawdza status odpowiedzi HTTP oraz kluczowe elementy w odpowiedziach JSON (id, title, userId).

Uruchomienie skryptu
Aby uruchomić skrypt, uruchom konsolę w lokalizacji skryptu i użyj polecenia:
python3 SkryptGET.py


Dokumentacja skryptu
Skrypt weryfikuje odpowiedzi i wyświetla wyniki testów w czytelny sposób (np. "Test 1: PASSED", "Test 2: FAILED").