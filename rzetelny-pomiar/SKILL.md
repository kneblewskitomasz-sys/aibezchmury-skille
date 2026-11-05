---
name: rzetelny-pomiar
description: "Pilnuje, żeby liczba ogłoszona jako wynik miała skrypt, surowy zapis i datę, a test na wygodnym podzbiorze nie udawał dowodu. Używaj przed zdaniem z wynikiem („X tok/s”, „42/50”, „99% trafności”), przy budowie golden-setu lub fixture'a, przy statystyce liczonej z obszaru lub filtra, przed wdrożeniem zmiany promptu/konfiguracji oraz po każdej zmianie wersji modelu albo środowiska."
license: MIT
---

# Rzetelny pomiar — procedura

Jedno zdanie, które streszcza całość: **jeden przebieg to wrażenie, nie pomiar**, a dobry wynik na złym zbiorze jest gorszy niż brak wyniku, bo brzmi jak dowód.

## Kiedy odpalić
- Zaraz przed napisaniem zdania z liczbą wynikową.
- Przy budowie nowego golden-setu, fixture'a albo zestawu testowego, który ma służyć jako referencja na dłużej.
- Gdy test przechodzi w 100%, a produkcja i tak zawodzi — pierwsze podejrzenie: zestaw nie pokrywa realnych danych.
- Przed wdrożeniem poprawki promptu, konfiguracji albo strażnika (guarda).
- Po podniesieniu wersji modelu, runtime'u, sterownika lub biblioteki inferencji.

## Część 1 — liczba = skrypt + surowy wynik + data
1. Każda liczba w raporcie ma obok: polecenie, które ją wyprodukowało, ścieżkę do surowego pliku wyjściowego (nie tylko przepisane podsumowanie) i datę przebiegu.
2. Niepowtórzony przebieg nazywaj wprost „pojedynczym przebiegiem”, nie „ustalonym faktem”.
3. Zanim zacytujesz liczbę z wcześniejszego materiału — sprawdź, czy nadal ma skrypt, log i datę. Jeśli nie ma, to twierdzenie do ponownego zmierzenia, nie prawda.
4. **Nazwa pliku wyniku musi przetrwać powtórzenie tego samego dnia.** Nazwa z samą datą zostanie nadpisana przez drugi przebieg — dokładnie ten, z którym chcesz porównać pierwszy. Dodaj godzinę, numer serii albo hash parametrów i zapisuj każdy przebieg osobno.

## Część 2 — zestaw testowy musi pokrywać realny rozkład
1. Wypisz, jakie warianty i kategorie istnieją w prawdziwych danych, na których kod będzie pracował — nie tylko te, które było łatwo zebrać.
2. Sprawdź wprost, czy zestaw zawiera przykłady z każdej kategorii, czy tylko z najczęstszej.
3. Test 100% na niereprezentatywnym zbiorze daje fałszywe poczucie bezpieczeństwa. Typowy przypadek: klasyfikator rozróżnia dwie wersje tego samego kodu (np. dwie edycje standardu), a zbiór zawiera wyłącznie starszą wersję.

## Część 3 — zakres pomiaru zgodny z tym, co deklarujesz
1. Zanim ogłosisz statystykę z obszaru lub podzbioru, sprawdź w kodzie, czy liczy się z zakresu, który opisuje tekst — nie z powiększonego zakresu użytego do innego celu (np. bufor dodany tylko do rysowania mapy).
2. Sprawdź maskę lub filtr na najmniejszym i najbardziej skrajnym przypadku. Błąd zakresu bywa niewidoczny na dużym obiekcie i katastrofalny na małym.
3. Gdy jedna zmienna służy dwóm celom (wizualizacja i statystyka), rozdziel je jawnie w kodzie.

## Część 4 — kandydat na zmianę mierzony PRZED wdrożeniem
1. Poprawkę promptu, flagę albo guard zmierz na tym samym przyrządzie, którym mierzysz produkcję: ten sam zestaw, ta sama metryka, to samo ziarno, ten sam przebieg porównawczy.
2. Jeśli kandydat wypada gorzej lub neutralnie — nie wdrażaj. Zapisz wynik jako odrzucony, z liczbami, i cofnij zmianę.
3. Odrzucona, zmierzona hipoteza jest tak samo wartościowym wynikiem jak przyjęta.

## Część 5 — zmiana gruntu unieważnia poprzednie pomiary
1. Gdy zmienia się wersja modelu, runtime'u, sterownika lub biblioteki pod już zmierzonym wynikiem, stary wynik traci ważność z chwilą zmiany.
2. Nie doklejaj starego pomiaru do nowej sytuacji z założeniem „to samo, tylko nowsze”. Oznacz go jako wstępny do czasu powtórki.
3. Przy każdym upgrade wypisz, które ustalone liczby ta zmiana mogła unieważnić.

## Część 6 — ocena zmiany biznesowej wymaga stanu PRZED
1. Zanim ogłosisz „kampania zadziałała / nie zadziałała”, wypisz dwie liczby z porównywalnego okresu: stan przed zmianą i po niej. Sama liczba po zmianie to stan, nie zmiana.
2. Jeśli dane nie mają okresu przed, powiedz to wprost.
3. Przy małej skali bez grupy kontrolnej nie rozdzielisz wpływu kampanii od sezonu — nazwij to ograniczenie, nie przeocz go.

## Część 7 — funkcja wdrożona do promptu ma zmierzony zysk, nie tylko koszt
1. Przy każdej nowej regule w prompcie zapisz datę wdrożenia i zaplanuj sprawdzenie po około tygodniu: czy funkcja wygenerowała jakikolwiek sygnał użycia.
2. Zero sygnału po tym czasie to fakt do zaraportowania, nie milczące „pewnie działa”.
3. Dodana reguła kosztuje punkty jakości nawet wtedy, gdy mieści się w oknie kontekstu — im dłuższy prompt, tym większe rozmycie instrukcji. Mierz to jak każdą inną zmianę (Część 4).

## Część 8 — narzędzie agregujące jest częścią przyrządu
1. Skrypt, który uśrednia lub rankuje wiele przebiegów, może po cichu zmieszać epoki: inny rozmiar zestawu, przeformułowane pytania, nowa wersja.
2. Zanim zaufasz podsumowaniu, sprawdź, czy grupuje przebiegi po przedmiocie **i** wersji przyrządu.
3. Uśrednianie przez granicę wersji daje liczbę, która nie odpowiada żadnemu realnemu przebiegowi.

## Wynik — lista kontrolna przed ogłoszeniem liczby
- [ ] liczba → skrypt → surowy plik (nazwa odporna na nadpisanie) → data,
- [ ] pojedynczy czy powtórzony przebieg,
- [ ] kategoria realnych danych → pokryta w zestawie? tak/nie,
- [ ] zakres w kodzie == zakres w tekście (sprawdzone na najmniejszym przypadku),
- [ ] kandydat zmierzony przed wdrożeniem → lepszy/gorszy/neutralny → wdrożony czy odrzucony,
- [ ] po zmianie wersji modelu/runtime'u: które wyniki powtórzone,
- [ ] przy ocenie kampanii: stan przed i po wypisane jawnie,
- [ ] przy narzędziu agregującym: grupowanie po (przedmiot, wersja przyrządu).

Brak któregokolwiek punktu to bloker przed ogłoszeniem wyniku jako faktu — nie kosmetyka.

## Czego ten skill nie robi
Nie zastępuje właściciela domeny (np. osoby od testów kodu albo od marketingu). To węższa, mechaniczna procedura, którą każdy z nich stosuje przy raportowaniu wyniku.
