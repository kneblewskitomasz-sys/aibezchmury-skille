---
name: test-skutkow-4-przypadki
description: "Używaj gdy włączasz albo rozszerzasz automat, który blokuje, ponawia, przekierowuje pracę, zmienia status albo wspólny stan. Przed włączeniem sprawdź cztery przypadki: wejście błędne, poprawne, awaria zależności i wycofanie flagą. Opinia modelu nie zastępuje uruchomionego testu."
license: MIT
---

# Test skutków — cztery przypadki

Zasada: **mechanizm, który blokuje, ponawia, przekierowuje pracę albo zmienia wspólny stan, zapowiadasz po ludzku i testujesz na czterech przypadkach, zanim go włączysz.** Opinia modelu — także bardzo dobrego — jest recenzją projektu, nie dowodem skutku.

## Kiedy odpalić
- Włączasz nowy automat: blokadę, kolejkę, ponawianie, przekierowanie, zmianę statusu, wysyłkę, porządek w danych.
- Rozszerzasz istniejący automat o nowy warunek sterowania.
- Naprawiasz odstępstwo od wcześniej ustalonego kontraktu. Wtedy wystarczy starsze źródło i test regresji, ale test skutków nadal jest tańszy niż wiara.
- Ktoś mówi „to proste, wystarczy spojrzeć na kod”. Właśnie wtedy.
- Chroniona rzecz kosztuje właściciela minutę → nie buduj automatu, zrób to ręcznie.

## Zgoda i prototyp
Nowy albo rozszerzony mechanizm **zapowiadasz po ludzku i dostajesz zgodę**, zanim wejdzie na główną ścieżkę. Prototyp w osobnym katalogu budujesz bez pytania. Bez zgody wolno tylko naprawić odstępstwo od wcześniej ustalonego kontraktu: starsze źródło i test regresji, bez nowego warunku sterowania.

## Cztery przypadki

| przypadek | co ma się stać | co konkretnie sprawdzasz |
|---|---|---|
| 1. Wejście błędne | odmowa bez zmiany stanu | puste, zły typ, za duża liczba, brak pola, duplikat, znak specjalny, użytkownik bez uprawnień |
| 2. Wejście poprawne | dokładnie zapowiedziany skutek, raz | typowy przypadek, wartości graniczne, drugie wywołanie, brak skutków ubocznych |
| 3. Awaria zależności | zamknięcie bezpieczne, bez częściowego stanu | brak odpowiedzi, timeout, błąd serwera, brak pliku, brak uprawnień |
| 4. Wycofanie | stare zachowanie wraca | flaga wyłączona, to samo wejście, ten sam wynik, brak śmieci, wycofanie po częściowym działaniu |

### 1. Wejście błędne
Ma **odmówić**, nie zmienić stanu, nie zapisać połowy danych, nie wpaść w pętlę ponowień i wypisać powód. Sprawdź stan przed i po. Sprawdź, że operacja **nie wykonała się** — nie tylko że nie wywaliła programu. Wywołaj dwa razy: drugie wywołanie nie może dopisać duplikatu.

### 2. Wejście poprawne
Ma wykonać dokładnie to, co zapowiedziano, i to raz. Sprawdź efekt w stanie, pliku, kolejce albo logu — nie w deklaracji funkcji. Sprawdź wartości graniczne: zero, maksimum, pusty tekst, najdłuższy dopuszczalny numer. Sprawdź, że nie powstał skutek uboczny, którego nikt nie zapowiadał.

### 3. Awaria zależności
Ma zamknąć się bezpiecznie: bez częściowego stanu, z ograniczoną liczbą ponowień i odstępem, bez nieskończonej pętli, z zachowaną kolejką i alertem. Symuluj awarię **przez zepsucie zależności**, nie przez wyłączenie sprawdzenia. Potem przywróć zależność i sprawdź, czy mechanizm wraca do pracy.

### 4. Wycofanie
Flaga ma przywrócić stare zachowanie. Na tym samym wejściu wynik ma być taki jak przed włączeniem — ten sam plik, ten sam stan, ta sama kolejność. Nowa ścieżka nie może zostawiać śmieci. Sprawdź też wycofanie **po częściowym działaniu**: cofa skutki, nie tylko kod. Dla nowego mechanizmu flaga domyślnie wyłączona.

## Jak to uruchomić
1. Zapisz kontrakt: co mechanizm ma robić w każdym z czterech przypadków, **zanim** napiszesz kod.
2. Uruchom na kopii danych, nie na produkcji.
3. Dla każdego przypadku zapisz: komendę, wejście, oczekiwane, rzeczywiste, datę i godzinę, identyfikator przebiegu.
4. Kolejność: błędne → poprawne → awaria → wycofanie. Po awarii wróć do poprawnego, żeby pokazać, że mechanizm wraca.
5. Test ma być czerwony przed zmianą i zielony po. Jeśli od razu jest zielony, prawdopodobnie nie testuje skutku.
6. Testuj skutek, nie implementację: nie „czy funkcja została wywołana”, tylko „co jest w stanie, pliku, kolejce, logu”.

## Czego opinia modelu nie zastępuje
Recenzja może wskazać dziurę w projekcie, ale nie pokaże, co się stanie po dwóch wywołaniach, przy timeoutcie i po wyłączeniu flagi. „Wygląda dobrze” nie jest wynikiem. Dowodem jest zapis czterech przebiegów.

## Siedem pułapek
1. Test tylko szczęśliwej ścieżki.
2. Test, który mockuje rzecz testowaną i sprawdza własny mock.
3. Ponawianie „przetestowane” tak, że nigdy nie następuje.
4. Wycofanie sprawdzone na pustym stanie.
5. Flaga sprawdzona tylko w stanie „włączona”.
6. Test na produkcji albo na danych, których nie wolno ruszać.
7. „Test” to ręczne kliknięcie bez zapisu — nie ma dowodu.

## Wynik

| przypadek | co uruchomiono | oczekiwane | rzeczywiste | dowód | werdykt |
|---|---|---|---|---|---|
| błędne | | | | | |
| poprawne | | | | | |
| awaria | | | | | |
| wycofanie | | | | | |

- Brak wiersza albo czerwony wiersz → **nie włączaj**.
- Decyzja: `WŁĄCZAM`, `NIE WŁĄCZAM` albo `WŁĄCZAM ZA FLAGĄ`.
- Jeśli „nie włączam”, mechanizm zostaje w prototypie poza główną ścieżką.

## Czego ten skill nie robi
- Nie zastępuje monitoringu, kopii zapasowej ani przeglądu bezpieczeństwa.
- Nie jest zgodą właściciela: zgodę na mechanizm, który blokuje albo zmienia wspólny stan, daje człowiek, nie test.
- Nie dotyczy jednorazowego skryptu, który nic nie zmienia; tam wystarczy zwykły test.
