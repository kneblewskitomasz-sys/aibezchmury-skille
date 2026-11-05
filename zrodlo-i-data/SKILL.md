---
name: zrodlo-i-data
description: "Higiena „twierdzenie ↔ źródło ↔ data odczytu” w dokumencie, który idzie do klienta, urzędu lub opinii publicznej, oraz przy przyjmowaniu nowych twierdzeń do zespołu (zrzuty ekranu, posty, newslettery). Wypisuje każde zdanie z liczbą, datą, ceną, przepisem i nazwą własną, sprawdza źródło i datę odczytu, oddziela fakt potwierdzony od niepotwierdzalnego. Używaj przed wysyłką oferty, briefingu, raportu, posta oraz przed zapisaniem faktu z social mediów do planu lub watchlisty."
license: MIT
---

# Źródło i data — procedura

Zasada: **liczby, daty, nazwy i przepisy podajesz ze źródłem i datą odczytu albo nie podajesz ich wcale.** Ten skill zamienia zasadę w listę kroków.

## Kiedy odpalić
- Dokument idzie na zewnątrz (klient, urząd, publiczny post) i zawiera choć jedną liczbę, datę lub przepis.
- Dokument jest wewnętrzny, ale ktoś fizycznie na jego podstawie działa — jedzie, płaci, kupuje. Skutek błędu jest identyczny jak przy dokumencie zewnętrznym.
- Fakt jest kopiowany z wcześniejszego materiału, a nie z pierwotnego źródła — to najczęstsze miejsce utrwalenia błędu.
- Ktoś wkleja zrzuty ekranu lub posty z mediów społecznościowych jako podstawę decyzji.

## Kroki
1. **Wypisz osobno** każde zdanie zawierające: liczbę, datę, nazwę przepisu lub ustawy, cenę, nazwę własną firmy lub instytucji, lokalizację lub adres.
2. **Dla każdego zapytaj:** czy ma źródło (URL, dokument, API) **oraz** datę odczytu obok siebie — w dokumencie albo w notatce roboczej. Jeśli nie, oznacz „do weryfikacji” i nie traktuj dokumentu jako gotowego.
3. **Fakt prawny lub regulacyjny** weryfikuje osoba odpowiedzialna za prawo w zespole — nie zgaduj treści przepisu, nawet gdy wygląda znajomo.
4. **Fakt skopiowany z własnego wcześniejszego pliku** jest surowym twierdzeniem do ponownego sprawdzenia, nie ustaloną prawdą. Sprawdź datę pliku źródłowego; fakt prawny starszy niż kilka dni zweryfikuj od nowa.
5. **Lokalizacja konkretnego klienta** (miejscowość, dzielnica, numer działki) to tak samo źródłowalny fakt jak cena — sprawdź w rejestrze lub geoportalu, nie w pamięci rozmowy.
6. **Wynik:** lista twierdzeń bez źródła i daty to blokery przed wysyłką, nie kosmetyka. Mają wagę literówki w cenie.

## Twierdzenia wchodzące ze zrzutów ekranu
1. Zrzut ekranu **nie jest źródłem** — jest wskazówką, gdzie szukać. Dla każdego konkretnego twierdzenia (liczba, data wydania, nazwa funkcji, wynik benchmarku) znajdź pierwotne źródło: repozytorium, ogłoszenie producenta, oficjalną dokumentację.
2. Trzy możliwe losy twierdzenia:
   - **potwierdzone u źródła** — cytuj z URL i datą, wolno na nim budować plan,
   - **niepotwierdzalne teraz** — źródło nie istnieje, jest za logowaniem albo autor nie podaje dowodu; odrzuć, nawet jeśli brzmi wiarygodnie,
   - **istnieje, ale treść niezweryfikowana** — narzędzie istnieje, ale konkretna zaleta ze zrzutu wymaga osobnego sprawdzenia.
3. Twierdzenie potwierdzone co do istnienia nie jest potwierdzone co do mechanizmu. Sprawdź też, czy sposób działania nie łamie regulaminu serwisu albo prawa.

## Dwa nazwane błędy, które ten skill ma wyłapywać
- **Stary fakt przepisany bez odświeżenia.** Briefing powtórzył z materiału sprzed tygodnia termin wejścia obowiązku prawnego; termin w międzyczasie się zmienił. Błąd nie był zmyśleniem — był kopią. Wyłapały go dopiero dwie niezależne kontrole po napisaniu.
- **Lokalizacja z pamięci zamiast z rejestru.** Materiał podał miejscowość „z pamięci sesji”, a faktyczna działka leżała w innym powiecie. Fakt geograficzny o kliencie został potraktowany jak wiedza ogólna, choć jest tak samo źródłowalny jak cena.

## Wynik
Tabela: twierdzenie → źródło (URL/dokument) → data odczytu → status (potwierdzone / do weryfikacji / odrzucone). Każdy wiersz „do weryfikacji” blokuje wysyłkę.

## Czego ten skill nie robi
Nie zastępuje prawnika ani pełnej kontroli jakości dokumentu. To węższa, mechaniczna procedura wyłapywania **braku źródła i daty**, którą stosuje każdy, kto pisze dokument zewnętrzny, zanim przekaże go do pełnej redakcji.
