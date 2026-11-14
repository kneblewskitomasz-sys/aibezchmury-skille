---
name: straznik-danych-przed-wysylka
description: "Używaj gdy tekst, dokument albo notatka ma trafić do czatu w chmurze, do zewnętrznego modelu albo do innej firmy. Przed wysłaniem sprawdź PESEL, NIP, REGON, IBAN, numer dowodu, telefon, nazwiska i dane o zdrowiu; przy trafieniu zamaskuj albo nie wysyłaj. Zawiera publiczne sumy kontrolne i pułapki, których sama lista słów nie wychwyci."
license: MIT
---

# Strażnik danych przed wysyłką — procedura

Zasada: **najpierw sprawdź, potem wklej.** Jeden numer w złym miejscu zostaje w historii czatu, w logach i w pamięci usługi, nawet jeśli wiadomość potem usuniesz. Nie da się cofnąć wysłania przez „usuń”.

## Kiedy odpalić
- Wklejasz do czatu w chmurze umowę, fakturę, notatkę ze spotkania, fragment bazy klientów, korespondencję.
- Wysyłasz tekst do zewnętrznego modelu albo do innej firmy: podwykonawcy, kancelarii, księgowości.
- Budujesz funkcję, która wysyła tekst użytkownika do modelu — to jest moment na tę procedurę, nie po wdrożeniu.
- Otrzymałeś dokument od kogoś i nie wiesz, czy są w nim dane osób trzecich.
- Tekst zawiera zdanie o czyimś zdrowiu, nawet bez nazwy choroby.

## Co sprawdzasz

| typ | wzorzec | walidacja | co zrobić z trafieniem |
|---|---|---|---|
| PESEL | 11 cyfr, separatory do usunięcia | suma kontrolna, wagi 1,3,7,9,1,3,7,9,1,3 | zamaskuj cały |
| NIP | 10 cyfr, myślniki i spacje do usunięcia | suma kontrolna, wagi 6,5,7,2,3,4,5,6,7 | zamaskuj cały albo zostaw ostatnie 4 |
| REGON | 9 albo 14 cyfr | suma kontrolna, wagi zależne od długości | zamaskuj cały albo zostaw ostatnie 4 |
| IBAN | `PL` + 26 cyfr, często ze spacjami | reszta z dzielenia przez 97 | zamaskuj środek, zostaw kraj i ostatnie 4 |
| numer dowodu | 3 litery + 6 cyfr | suma kontrolna, litery A=10…Z=35 | zamaskuj cały |
| telefon | 9 cyfr, często z `+48` | normalizacja i kontekst | zamaskuj, zostaw ostatnie 3–4 |
| nazwisko | lista + formy odmienione + kontekst | całe słowa, nie fragmenty | zamaskuj albo zamień na inicjał |
| dane o zdrowiu | słowa i kontekst medyczny | zdanie, nie pojedyncze słowo | zamaskuj całe zdanie albo nie wysyłaj |

## Sumy kontrolne — publiczne algorytmy

### PESEL
- 11 cyfr. Usuń separatory, sprawdź, że zostały same cyfry.
- Wagi pierwszych 10 cyfr: **1, 3, 7, 9, 1, 3, 7, 9, 1, 3**.
- Policz sumę iloczynów, weź resztę z dzielenia przez 10.
- Cyfra kontrolna to `(10 - reszta) mod 10`. Musi równać się 11. cyfrze.
- Miesiąc w dacie bywa przesunięty o 20, 40 albo 80 — to nie błąd, tak zapisuje się inne stulecia.
- Suma kontrolna mówi „to może być PESEL”, nie „to jest ten człowiek”.

### NIP
- 10 cyfr. Usuń myślniki i spacje.
- Wagi pierwszych 9 cyfr: **6, 5, 7, 2, 3, 4, 5, 6, 7**.
- Reszta z dzielenia sumy przez 11. Wynik 10 oznacza numer nieprawidłowy.
- Wynik musi równać się 10. cyfrze.

### REGON
- **9 cyfr:** wagi **8, 9, 2, 3, 4, 5, 6, 7**. Reszta z dzielenia przez 11; wynik 10 zamień na 0; musi równać się 9. cyfrze.
- **14 cyfr:** wagi **2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8** dla pierwszych 13 cyfr. Reszta z dzielenia przez 11; wynik 10 zamień na 0; musi równać się 14. cyfrze. Dodatkowo pierwsze 9 cyfr musi przechodzić sprawdzenie REGON-9.

### IBAN
- Polski IBAN ma **28 znaków**: `PL`, 2 cyfry kontrolne i 24 cyfry (8 cyfr banku + 16 cyfr rachunku).
- Sprawdzenie: przenieś pierwsze 4 znaki na koniec, zamień litery na liczby (A=10, B=11, …, Z=35), a potem licz resztę z dzielenia przez 97 **cyfra po cyfrze**, nie jako liczbę zmiennoprzecinkową.
- Poprawny IBAN daje resztę **1**.
- IBAN innych krajów ma inną długość (od 15 do 34 znaków). Nie zakładaj 28.

### Numer dowodu
- Klasyczny numer: **3 litery + 6 cyfr**.
- Litery zamień na liczby: A=10, B=11, …, Z=35.
- Wagi 9 znaków: **7, 3, 1, 9, 7, 3, 1, 7, 3**.
- Suma iloczynów musi dawać resztę 0 z dzielenia przez 10.
- To sprawdza numer, nie istnienie dokumentu.

### Telefon
- 9 cyfr. Usuń `+48`, `0048`, spacje, myślniki i nawiasy.
- Komórka zaczyna się od 4–8; numer stacjonarny od kodu strefy.
- Ten sam 9-cyfrowy ciąg może być REGON-9 albo numerem faktury. Decyduje kontekst i prefiks, nie sam wzorzec.

### Nazwiska i dane o zdrowiu
- Nazwiska: lista imion i nazwisk, formy odmienione, zdrobnienia; całe słowa, nie fragmenty.
- Kontekst dla nazwiska: „Pan/Pani”, „podpisany”, „reprezentuje”, „w imieniu”, stopka maila, „nr dowodu”.
- Zdrowie: „diagnoza”, „wynik badania”, „recepta”, „zwolnienie”, „dawka”, „tabletka”, „szpital”, „zabieg”, „niepełnosprawność”, nazwy chorób.
- Najczulsze zdania nie zawierają nazwy choroby: „odebrałem wyniki”, „lekarz zwiększył dawkę”, „jestem na zwolnieniu”. Kontekst: osoba + czynność medyczna.

## Co zrobić z trafieniem
1. **Zatrzymaj wysyłkę.** Nie wklejaj „na chwilę, potem usunę”.
2. **Zakwalifikuj:** suma kontrolna plus kontekst. Jeśli nie umiesz zakwalifikować — traktuj jak trafienie.
3. **Zamaskuj albo nie wysyłaj.** Token zamiast wartości: `[PESEL]`, `[NIP]`, `[REGON]`, `[IBAN]`, `[DOWÓD]`, `[TELEFON]`, `[NAZWISKO]`, `[DANE-ZDROWOTNE]`. Jeśli odbiorca potrzebuje końcówki (telefon, rachunek), zostaw ostatnie 4 znaki, resztę zamień.
4. **Mapowanie trzymaj lokalnie.** Jeśli musisz odtworzyć oryginał, trzymaj tabelę „token → wartość” na swojej maszynie, nie w czacie.
5. **Minimum konieczne.** Zapytaj, czy odbiorca naprawdę potrzebuje pełnego numeru. Często wystarczy „PESEL zweryfikowany”, „rachunek w banku X”, ostatnie 4 cyfry.
6. **Jeśli numer jest konieczny do zadania:** użyj modelu lokalnego albo narzędzia na maszynie; wyślij tylko ten fragment, który jest niezbędny, i tylko odbiorcy, który ma podstawę do jego przetwarzania.
7. **Po odpowiedzi nie wklejaj numeru z powrotem.** Sprawdź historię wątku i załączniki; usuń, jeśli platforma pozwala.

Maskowanie:

| typ | co zostawić |
|---|---|
| PESEL | nic |
| NIP, REGON | nic albo ostatnie 4 cyfry |
| IBAN | kraj i ostatnie 4 znaki |
| dowód | nic |
| telefon | ostatnie 3–4 cyfry |
| nazwisko | inicjał, jeśli kontekst wymaga osoby |
| zdrowie | token albo całe zdanie usunięte |

## Pułapki

1. **Imię w środku zwykłego słowa.** „Ala” siedzi w „fala”, „Iga” w „figa”. Wyszukiwanie podciągu bez granic słowa zamienia zwykłe słowo w trafienie. Granice słowa pomagają, ale nie rozwiązują odmiany.
2. **Nazwisko będące rzeczownikiem.** „Lis”, „Wilk”, „Sowa”, „Kowal”, „Baran”, „Kot” to nazwiska i pospolite rzeczowniki. „Lis przebiegł drogę” i „Pan Lis podpisał” mają ten sam ciąg znaków; decyduje kontekst, nie lista.
3. **Suma kontrolna nie jest dowodem.** Część przypadkowych ciągów przechodzi sumę NIP albo REGON. Numer faktury, zamówienia albo data może wyglądać jak identyfikator. Trafienie = kandydat, nie osoba.
4. **Ten sam numer w innym zapisie.** Spacje, myślniki, `+48`, `PL`, nawiasy. Normalizuj przed sprawdzeniem, ale maskuj w oryginale, żeby nie przesunąć znaków.
5. **Nazwisko odmienione i zdrobnienie.** „Kowalski”, „Kowalskiego”, „Kowalskiemu”; „Kasia” dla „Katarzyna”. Lista form podstawowych je przegapi. Rdzeń plus końcówki łapie więcej, ale zwiększa fałszywe trafienia.
6. **Zdrowie bez nazwy choroby.** „Odebrałem wyniki”, „lekarz zmienił dawkę”, „jestem na zwolnieniu” — lista chorób tego nie złapie. Potrzebny kontekst.
7. **Obraz i skan.** Wzorzec widzi tekst, nie zdjęcie recepty ani skan PDF. Jeśli treść jest obrazem, potrzebujesz odczytu obrazu albo nie wysyłasz.
8. **Historia i załączniki.** Tekst w promptcie zamaskowany, a numer w załączniku albo we wcześniejszej wiadomości wątku. Sprawdź cały wątek, nie jedno okno.
9. **Lista nigdy nie jest pełna.** Imiona i nazwiska to zbiór otwarty: nowe nazwiska, obcojęzyczne, zdrobnienia. Lista łapie znane wzorce, nie „wszystkie dane”.

## Dlaczego sama lista słów nie wystarcza

Lista odpowiada na pytanie „czy w tekście jest znane słowo”, a nie „czy w tekście jest dana osoba”. Nazwiska są odmieniane, imiona bywają pospolitymi słowami, dane o zdrowiu są znaczeniowe, a nie leksykalne. Ten sam ciąg cyfr jest numerem faktury albo NIP-em — rozstrzyga kontekst.

**Drugi przebieg małym modelem lokalnym** — na tej samej maszynie, bez wysyłania tekstu — daje ocenę kontekstu: czy „Lis” to nazwisko, czy zwierzę, czy ciąg cyfr jest numerem, a nie kwotą. To sygnał, nie dowód; decyzję podejmuje człowiek.

## Wynik

```
tekst znormalizowany: tak / nie
kandydaci: <typ, liczba, gdzie>
zakwalifikowani: <typ, decyzja: maskuj / nie wysyłaj / zostaw>
zamaskowany tekst: <gdzie sprawdzony>
mapowanie: <lokalnie / brak>
wątek i załączniki: <sprawdzone / nie>
werdykt: WYSYŁAM / NIE WYSYŁAM
```

- „Nie wysyłam” jest pełnoprawnym wynikiem, nie porażką.
- Jeśli nie umiesz zakwalifikować trafienia, werdykt brzmi „nie wysyłam”.

## Czego ten skill nie robi
- Nie jest systemem DLP ani narzędziem zgodności; nie gwarantuje, że wykryje wszystkie dane.
- Nie widzi obrazów, skanów ani dźwięku; nie czyta załączników binarnych.
- Nie zastępuje podstawy prawnej, umowy powierzenia ani oceny, czy wolno wysłać dane.
- Nie szyfruje i nie cofa wysłanej wiadomości.
