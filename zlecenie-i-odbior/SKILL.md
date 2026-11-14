---
name: zlecenie-i-odbior
description: "Używaj gdy zlecasz pracę wykonawcy (agentowi AI, subagentowi, podwykonawcy) albo odbierasz jego wynik. Zlecenie ma z góry zapisaną jedną komendę odbioru i kryterium w liczbach albo słowach; odbiór to uruchomienie tej komendy i jeden wiersz werdyktu, nie czytanie raportu wykonawcy."
license: MIT
---

# Zlecenie i odbiór — jedna kartka

Po co: odbiór zjadał najwięcej czasu, bo opierał się na czytaniu raportu. Raport wykonawcy jest **wsadem**, nie dowodem. Dowodem jest komenda, którą napisałeś, zanim wykonawca zaczął.

## Kiedy odpalić
- Piszesz zlecenie dla wykonawcy: agenta AI, subagenta, osoby, innego modelu.
- Odbierasz wynik i musisz powiedzieć „zielone / czerwone”.
- Zlecenie jest wizualne, mailowe albo dotyczy pliku, który zobaczy człowiek.
- Kolejka zleceń czeka dłużej niż tydzień i nie wiesz, które jeszcze mają odbiorcę.

## 1. Zanim napiszesz treść — napisz ODBIÓR

```
ODBIÓR: <gdzie> · `<jedna komenda>` · <co ma wypisać: liczba albo słowo>
```

- Komenda ma działać **bez czytania czegokolwiek**. Dobra: test, `grep -c`, liczba wierszy, kod wyjścia, rozmiar pliku. Zła: „raport zawiera opis”, „wygląda poprawnie”.
- Nie umiesz napisać komendy → zadanie nie jest gotowe do zlecenia. Rozbij je albo zrób sam.
- **Zadanie wizualne:** zamiast komendy zdanie „na zrzucie widać… / nie widać…”. Zrzut robisz Ty, nie wykonawca.
- **Kod:** test piszesz Ty, przed zleceniem, i ma być czerwony. Wykonawca ma go zazielenić. Wtedy odbiór jest mechaniczny.
- **Rzecz dla człowieka z zewnątrz:** komenda ma pokazać to, co zobaczy człowiek, nie to, co wykonawca napisał o wyniku. Trzy wzory:
  - okno: program uruchomiony tak jak u odbiorcy, z czystej kopii, a komenda czyta to, co wypisało okno;
  - plik: komenda otwiera gotowy plik i liczy to, co odbiorca w nim zobaczy (wiersze, strony, zdjęcia);
  - mail: treść szkicu odczytana z narzędzia pocztowego i porównana z tym, co miało w niej być.
- Zielony test klasy albo funkcji **nie jest** odbiorem rzeczy dla człowieka.

## 2. Nagłówek zlecenia

```
# Zlecenie <id>: <co, jednym zdaniem>
TYP: kod-agent | kod-1strzal | tekst | research | przeglad | obraz
TRUDNOSC: 1–3
WYMAGA_SIECI: true | false
TIMEOUT_MIN: <hojnie>
POTRZEBY: <czego wykonawca naprawdę potrzebuje>
ODBIOR: <jak wyżej>
RAPORT: <ścieżka raportu>
```

Potem, w tej kolejności:
1. **Po co** — dwa zdania, z cytatem zleceniodawcy, jeśli jest.
2. **Do zrobienia** — lista, każdy punkt sprawdzalny.
3. **Granice** — czego nie wolno ruszać i czego nie wolno zrobić (push, wysyłka, publikacja, cudze pliki).
4. **Zgoda na zapis** — dokładne ścieżki, nie katalog „gdzieś w repo”.
5. **Dane cudze** — jedno zdanie: czy w pracy są dane innych osób i czy wolno je wysłać.

## 3. Gdzie leży praca

| praca dotyka | wykonawca |
|---|---|
| powłoki systemowej, ścieżek lokalnych, ustawień maszyny | wykonawca z dostępem do tej maszyny, nie ten, kto ma tylko tekst |
| danych osobowych albo danych klienta | wykonawca lokalny; dane nie opuszczają maszyny |
| kodu, którego zdalna kopia jest starsza niż lokalna | najpierw aktualizacja zdalnej kopii, potem zlecenie |
| czystego tekstu | najtańszy wykonawca, który to udźwignie |

- Jeśli praca jest na Twoim systemie, dopisz to wprost do `POTRZEBY`. Dispatcher, który nie wie, że potrzebna jest Twoja maszyna, wyśle zadanie tam, gdzie go nie ma.
- Uważaj na słowa, które zmieniają trasę. Jeśli w zleceniu napiszesz „dane klienta” albo „prywatne”, dispatcher może skierować pracę na inną maszynę. Gdy chodzi tylko o niezatwierdzone zmiany innych osób, napisz to właśnie tak.

## 4. Start
- Jedna komenda startowa, całe wyjście do pliku. Czytasz z pliku tylko wiersz `wybór:` — wyjście dispatchera bywa kilkaset wierszy i nie ma sensu go wypisywać.
- Najwyżej **dwa** otwarte zlecenia naraz. Trzecie startuje po odbiorze pierwszego. Więcej = nie wiesz, który wynik jest czyj.

## 5. Odbiór — trzy kroki, bez czytania raportu
1. Uruchom komendę z `ODBIÓR`; całe wyjście do pliku.
2. Jeden wiersz werdyktu: `ZIELONY` albo `CZERWONY: <co wypisała komenda>`.
3. Zielony → commit plików wykonawcy i wiersz w planie. Czerwony → **jedna** poprawka tym samym wykonawcą, z wklejonym wyjściem odbioru. Drugi czerwony → zadanie wraca do Ciebie albo do zamknięcia. Nie trzeci raz.

Raport wykonawcy czytasz tylko wtedy, gdy odbiór jest czerwony albo gdy zleceniodawca pyta „dlaczego”.

## 6. Odbiór hurtem
Dla zleceń starszych niż 7 dni bez odbioru: nie odbieraj pojedynczo. Jedno pytanie na pozycję: *czy ktoś dziś czeka na ten wynik?* Nie → status „wygasło bez odbioru” z datą, plik zostaje. Tak → krok 5.

## Dwa nazwane błędy
- **Raport jako dowód.** Wykonawca napisał „gotowe”, więc uznajesz za gotowe. Raport opisuje zamiar i pracę, nie stan artefaktu.
- **Zielony test zamiast rzeczy.** Test klasy jest zielony, a plik, okno albo mail, który zobaczy człowiek, nie został otwarty. To dwa różne przedmioty.

## Wynik
- Każde zlecenie ma `ODBIÓR` zapisany **przed** treścią.
- Każdy odbiór ma plik z pełnym wyjściem komendy i jeden wiersz werdyktu.
- Otwarte są najwyżej dwa zlecenia.
- Czerwony odbiór ma jedną poprawkę i jedno powtórzenie, nie trzy.

## Czego ten skill nie robi
Nie zastępuje procedury dowodu stanu (zdania o stanie w dzienniku) ani pełnego odbioru wizualnego całości. Pilnuje jednej rzeczy: żeby zlecenie i odbiór były mechaniczne.
