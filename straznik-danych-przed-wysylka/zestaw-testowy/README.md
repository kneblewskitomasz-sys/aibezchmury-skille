# Zestaw testowy: dane osobowe w polskich tekstach (zestaw D)

80 krótkich, **zmyślonych** polskich tekstów do sprawdzania, czy narzędzie wykrywa dane osobowe, zanim tekst
opuści komputer. 40 tekstów zawiera dane, 40 nie zawiera.

W tekstach nie ma danych prawdziwych osób. Nazwiska to zwykłe polskie rzeczowniki użyte jako nazwiska
(Brzoza, Chmura, Gajda), adresy prowadzą do nieistniejących miejscowości (np. „Próbkowo”).

## Co jest w środku

| plik | co to |
|---|---|
| `zestaw-d.json` | 80 tekstów; pola: `id`, `rodzaj` (`dane` / `czyste`), `kategorie`, `tekst`, `oczekiwane` (dosłowne fragmenty do wykrycia) |
| `zestaw_d.py` | generator, który odtwarza plik deterministycznie (ziarno 18202) |

Kategorie w tekstach z danymi: nazwisko (14), adres zamieszkania (13), informacja o zdrowiu konkretnej osoby (13).

Teksty czyste są pułapkami, na których mylą się proste listy słów i wiele modeli:

- imię albo nazwisko ukryte w zwykłym słowie, np. „runo”, „korona drzewa”;
- nazwa firmy podobna do nazwiska, np. „Pszczoła Systems”;
- nazwa choroby bez osoby, np. ulotka leku albo katalog.

Nazwiska występują w różnych przypadkach („pani Brzoza … przekazano ją Brzozie”), bo polska odmiana
jest główną trudnością dla narzędzi pisanych pod angielski.

**Suma kontrolna** `zestaw-d.json` (SHA-256):
`002bd67c07fb52742bad5bf0badd5ebc6f17407f40d6fcdae5588bd54c554c72`

Zestaw został zapisany z sumą **przed** pierwszym wywołaniem jakiegokolwiek modelu i nie był używany do
strojenia poleceń.

## Wyniki na tym zestawie (12.11.2026, temperatura 0, dwa przebiegi z identycznym wynikiem)

| wariant | nazwiska | adresy | zdrowie | fałszywe alarmy (na 40 czystych) |
|---|---|---|---|---|
| same wzorce (sumy kontrolne NIP, REGON, IBAN, dowód) | 0 z 14 | 0 z 13 | 0 z 13 | 0 |
| wzorce + Bielik-Minitron-7B-v3.0-Instruct (Q8_0) | 13 z 14 | 12 z 13 | 5 z 13 | 2 |
| wzorce + Qwen3 8B | 10 z 14 | 11 z 13 | 12 z 13 | 18 |

Model działał lokalnie przez Ollamę; mediana czasu odpowiedzi 0,35 s na tekst.

## Czego ten zestaw nie mówi

- Teksty są krótkie i zmyślone. Na prawdziwych dokumentach wynik może być inny.
- To mały zestaw (80 tekstów, jeden autor). Nadaje się do porównania narzędzi i wyłapania regresji,
  nie do ogłaszania ogólnej skuteczności.
- Twarde identyfikatory (PESEL, NIP, REGON, IBAN) sprawdza się sumami kontrolnymi. Do ich testów
  używaj numerów z niepoprawną sumą albo numerów testowych, bo losowy numer z poprawną sumą może
  należeć do prawdziwej osoby. Dlatego tego zestawu nie wypełniamy PESEL-ami.

Licencja: MIT (plik `LICENSE` w katalogu głównym repozytorium).
