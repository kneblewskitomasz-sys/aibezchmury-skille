---
name: kontrakt-zrodla-danych
description: "Higiena PRZED podpięciem nowego zewnętrznego API do kodu: limit zapytań, wymagane nagłówki (Accept, User-Agent, klucz) i klauzula użytku komercyjnego — zanim napiszesz pętlę pobierania albo wystawisz cenę produktowi, który z API korzysta. Używaj przy budowie workera, skryptu pomiarowego lub czujnika odpytującego cudze API cyklicznie, gdy odpowiedź serwera jest niejednoznaczna (403/406/429 mylone z „endpointu nie ma”) oraz gdy istniejący kod z darmowym API zbliża się do pierwszej płatnej transakcji."
license: MIT
---

# Kontrakt źródła danych — procedura

Trzy błędy z jednej rodziny: limit zapytań poznany **po** zbudowaniu czujnika, limit nieopisany w katalogu API i nagłówek `Accept`, którego brak wygląda jak nieistniejący endpoint. Czwarty, inna kategoria: darmowe API z licencją wyłącznie niekomercyjną, wpięte zanim produkt dostał cenę.

**Rate limit i licencja komercyjna to dwa osobne pytania o to samo źródło — sprawdzasz oba.**

## Kiedy odpalić
- Piszesz nowy worker albo skrypt pomiarowy, który będzie odpytował cudze API cyklicznie. Jednorazowe ręczne zapytanie człowieka nie wymaga tej dyscypliny.
- Dostajesz z API kod inny niż 200 i nie wiesz, czy to „nie ma zasobu”, czy „źle pytasz”. 403, 406 i 429 to najczęstsze fałszywe tropy.
- Rozszerzasz istniejący czujnik o nowe źródło. Każde nowe źródło to nowy kontrakt — nie dziedziczy limitu poprzedniego.
- Kod korzystający z darmowego API zbliża się do pierwszej płatnej transakcji (nowy cennik, pierwsza wpłata). Sprawdź zakres komercyjny **przed**, nie po.

## Kroki
1. **Znajdź dokumentację limitu przed pisaniem pętli.** Szukaj strony „rate limit”, „limits”, „terms” dostawcy. Jeśli API ma endpoint diagnostyczny (np. `/rate_limit`), odpytaj go i zapisz liczbę — nie przepisuj z pamięci ani z cudzego artykułu.
2. **Na tej samej stronie sprawdź klauzulę użytku komercyjnego.** „Darmowe” i „wolno sprzedawać wynik” to różne zdania w tej samej umowie. Jeśli kod jest dziś eksperymentem bez ceny, zapisz wprost: „status: niekomercyjne, do sprawdzenia przed cennikiem”. Gdy produkt ma już cenę lub płacącego klienta, decyzję o zakresie licencji podejmuje osoba odpowiedzialna za prawo — nie zgaduj sam.
3. **Sprawdź wymagane nagłówki, nie tylko URL.** `Accept`, `User-Agent`, klucz lub token. Brak właściwego nagłówka bywa nieodróżnialny od nieistniejącego endpointu. Przy odmowie pierwsze, co sprawdzasz, to nagłówki żądania.
4. **Policz własne zużycie wobec limitu.** Ile zapytań na dobę realnie robi worker i jaki jest zapas. Zapisz to, żeby przyszła rozbudowa miała punkt odniesienia.
5. **Zapisz kontrakt w katalogu, nie tylko w kodzie.** Jeden wiersz na źródło: endpoint, kod odpowiedzi zmierzony na żywo z datą, limit, wymagany nagłówek, klauzula komercyjna, do czego służy. Nigdy nie zostawiaj kontraktu wyłącznie w komentarzu.
6. **Współdziel kod, nie wiedzę per worker.** Ogólne mechanizmy (retry, rozróżnienie błędu sieci od kodu HTTP, dopasowanie na granicy słowa) idą do wspólnego modułu. Kontrakt konkretnego źródła jest specyficzny per API i musi być zapisany jawnie przy źródle.

## Przykład wpisu kontraktu
```
źródło:        <nazwa API>
endpoint:      <URL>
limit:         <liczba> / <okno>, zmierzone <data>
nagłówki:      Accept: <...>; User-Agent: <...>; klucz: tak/nie
licencja:      komercyjna / niekomercyjna / wymaga zgody
odpowiedź:     <kod> zmierzony <data>
użycie:        <do czego w produkcie>
zapas:         <nasze zapytania/dobę> przy limicie <...>
```

## Wynik
Dla każdego nowego źródła: limit, nagłówki, klauzula komercyjna, zmierzony kod odpowiedzi i własne zużycie — zapisane przed pierwszą linią pętli. Brak któregokolwiek punktu to bloker przed wdrożeniem, nie notatka na później.

## Czego ten skill nie robi
Nie zastępuje higieny źródła i daty w dokumencie ani weryfikacji kodu, który sam stwierdza stan. To węższa procedura: techniczny kontrakt z zewnętrznym API, zanim napisze się do niego pętlę.
