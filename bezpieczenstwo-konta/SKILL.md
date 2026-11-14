---
name: bezpieczenstwo-konta
description: "Używaj gdy przychodzi podejrzany mail, SMS albo alert logowania, gdy nikt nie inicjował zmiany hasła, albo gdy pojawia się pytanie „czy ktoś się włamał” na konto. Procedura mówi, co wolno sprawdzić tylko czytając, czego nie wolno klikać i czego nie wolno zmieniać bez wyraźnej zgody właściciela konta."
license: MIT
---

# Bezpieczeństwo konta — procedura

To jest procedura na **konto osoby**, nie na kod produktu i nie na dane klienta. Trzy różne rzeczy, trzy różne osoby odpowiedzialne.

## Kiedy odpalić
- Przychodzi mail albo SMS z linkiem „zaloguj się”, którego właściciel nie inicjował.
- Przychodzi alert „nowe logowanie” / „nowe urządzenie” z usługi, której właściciel akurat nie używał.
- Przychodzi prośba o reset hasła, kod weryfikacyjny albo potwierdzenie — bez wcześniejszego działania właściciela.
- Właściciel pyta wprost: „czy ktoś się włamał?”, „czy to bezpieczne?”.

## Co wolno sprawdzić — wyłącznie czytając
1. **Przekazywanie poczty** — czy ktoś dopisał regułę wysyłającą kopię na obcy adres.
2. **POP/IMAP** — czy włączono pobieranie poczty przez zewnętrzną aplikację, której właściciel nie zna.
3. **Filtry i reguły skrzynki** — czy dodano filtr chowający, kasujący albo oznaczający jako przeczytane wiadomości od konkretnego nadawcy. To klasyczna technika ukrywania śladów po przejęciu.
4. **Panel bezpieczeństwa / aktywności konta** — lista logowań z datą, przybliżoną lokalizacją i urządzeniem.
5. **Połączone aplikacje i aktywne sesje** — co ma dostęp do konta i kiedy było ostatnio użyte.
6. **Adres i numer odzyskiwania** — czy nie podmieniono ich na obce.

Czytanie zostawia ślad w logach usługi, ale nie zmienia stanu konta. To jest ta różnica, która pozwala sprawdzić bez ryzyka.

## Czego NIGDY nie wolno zrobić bez wyraźnej zgody właściciela
Klikać linku w podejrzanej wiadomości, otwierać załącznika, wpisywać hasła ani kodu na stronie otwartej z linku, zmieniać hasła, wyłączać albo włączać dwuskładnikowego logowania, kasować wiadomości, wylogowywać aktywnych sesji, blokować nadawcy, odpowiadać nadawcy.

To są **akcje naprawcze**. Decyduje o nich wyłącznie właściciel konta i wykonuje je sam albo na wyraźne polecenie „zrób X”. Przeczytanie sygnału nie jest upoważnieniem do działania na koncie.

## Kolejność pracy
1. **Zabezpiecz dowód, zanim cokolwiek zniknie:** zapisz nagłówki wiadomości, datę, nadawcę i treść linku bez otwierania go.
2. **Sprawdź read-only** punkty z listy wyżej.
3. **Oddziel fakt od wniosku.** „Przyszedł mail z linkiem” to fakt. „Ktoś próbował się włamać” to wniosek, dopóki nie ma śladu w panelu.
4. **Nie domykaj alarmu na siłę** w żadną stronę: ani fałszywe „wszystko gra”, ani „na pewno przejęte”.
5. **Rekomendacja, nie wykonanie.** Najwyżej: „zmień hasło”, „włącz dwuskładnikowe logowanie”, „zignoruj jako phishing bez śladu”. Wykonuje właściciel.

## Nazwany błąd
Alarm wyciągnięty z samych tematów wiadomości w skrzynce. Temat „nowe logowanie” nie jest dowodem logowania. Dopiero panel bezpieczeństwa pokazuje, czy logowanie było, skąd i z jakiego urządzenia. W opisanym przypadku lista logowań nie zawierała obcego wejścia, link nie został kliknięty, a żadne ustawienie konta nie zostało zmienione. Alarm został jawnie skorygowany po dowodzie, nie utrzymany na wyrost.

## Wynik
Dla każdego sygnału:
```
sygnał: <co przyszło>
sprawdzone read-only: <punkty z listy>
znaleziono: <FAKT, nie wniosek>
wniosek: potwierdza / nie potwierdza przejęcia / nie da się rozstrzygnąć
rekomendacja: <jedno zdanie, do wykonania przez właściciela>
```

## Czego ten skill nie robi
Nie zastępuje procedury bezpieczeństwa kodu produktu ani procedury ochrony danych użytkowników. To trzecia, osobna domena: **własne konto właściciela** poza produktem. Nie jest procedurą naprawczą — po ustaleniu faktów decyzję i wykonanie podejmuje właściciel.
