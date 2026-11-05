---
name: rzetelna-weryfikacja
description: "Higiena kodu, który sam automatycznie stwierdza stan: health-check, status usługi, klasyfikator „czy to X”, grader, warunek startu, watchdog, sprawdzenie gotowości pliku przed użyciem. Osiemnaście nazwanych pułapek cichego fałszywego wyniku (zielony wynik przy braku sprawdzenia, stary log jako dowód, SKIP liczony jako PASS, zły zakres, nieatomowy zapis). Używaj przy pisaniu i przeglądzie takiego kodu oraz przed ogłoszeniem „działa / gotowe / zielone”."
license: MIT
---

# Rzetelna weryfikacja — procedura

Ten skill pilnuje jednej rzeczy: **kod, który sam mówi „OK”, nie może kłamać cicho**. Każda pułapka niżej została nazwana po realnym fałszywym wyniku. Przy przeglądzie kodu zadaj pytanie z każdej sekcji, której kod dotyka.

## Kiedy odpalić
- Piszesz lub recenzujesz health-check, status, watchdog, grader, klasyfikator, warunek startu usługi, sprawdzenie gotowości pliku.
- Ogłaszasz „działa”, „gotowe”, „wszystko zielone” na podstawie kodu, nie na podstawie własnoręcznego użycia.
- Testy są zielone, a produkcja zachowuje się inaczej.

## 1. Dopasowanie fragmentu zamiast granicy słowa lub pola
Podciąg daje fałszywe trafienia w obie strony: „api” wewnątrz „capital” (fałszywy alarm) albo zakazana fraza „jestem człowiekiem” w zdaniu „nie jestem człowiekiem” (fałszywy błąd).
**Sprawdź:** dopasowanie na granicy słowa (`\b`, token, pole strukturalne), a przy zakazanych frazach — przeczenie bezpośrednio przed frazą.

## 2. Dowód bez przypisanego okna czasowego
Stary log bywa brany za dowód obecnego stanu. „Ostatnie N linii” to nie to samo co „linie od zdarzenia, o które pytam”.
**Sprawdź:** trzy stany zawsze rozdzielone — dowód pozytywny w oknie, dowód negatywny w oknie, brak dowodu w oknie. Nie pożyczaj dowodu sprzed granicy zdarzenia.

## 3. Wyścig przy starcie usługi
Usługa startuje przed zależnością (baza, urządzenie, port, biblioteka) i zapisuje fałszywy stan.
**Sprawdź:** jawna zależność startowa (`After`/`Requires`/`ExecStartPre`), a jeśli kolejności nie da się wymusić — retry z odczekaniem i timeoutem, nie jednorazowy strzał.

## 4. Istnienie zamiast treści
Plik istnieje, więc kod uznaje zasób za gotowy — a w środku są puste pola albo szablon.
**Sprawdź:** dwa osobne pytania: (1) czy zasób istnieje, (2) czy ma niepustą, sensowną treść (wypełnione pola, nie same klucze z `null`).

## 5. Cicha podmiana bez trafienia
`replace`, `format`, `sed` lub silnik szablonów nie znajduje wzorca i **nie zgłasza błędu** — dane znikają, wynik wygląda poprawnie.
**Sprawdź:** przed podstawieniem asercja, że wzorzec jest w szablonie; przy braku — głośne ostrzeżenie i wariant awaryjny. Po podstawieniu sprawdź, że wynik **zawiera wstrzykniętą treść**, nie tylko że funkcja się wykonała.

## 6. Pomiar poprawny, doręczenie ciche
Watchdog trafnie diagnozuje problem i zapisuje go do pliku, którego nikt nie otwiera. Pomiar bez kanału doręczenia jest równoważny brakowi pomiaru.
**Sprawdź:** dla każdego alarmu odpowiedz, gdzie wynik faktycznie wyląduje i kto go przeczyta bez pytania. Bierny zapis do pliku nie jest doręczeniem.

## 7. Twierdzenie w tekście mocniejsze niż sprawdzony warunek
Kod generuje zdanie dla człowieka („zobaczysz planetę”, „stała wynosi X”), a sprawdził tylko warunek zastępczy albo policzył dwie liczby osobnymi ścieżkami i nigdy ich nie zestawił.
**Sprawdź:** wypisz dosłowny warunek, który zdanie zakłada, i warunek, który kod naprawdę sprawdził. Przy liczbach, które z definicji muszą się zgadzać — jawna asercja spójności. Przy „ostatnim/najbliższym dopasowaniu” — czy zdarzenie jest unikatowe w oknie.

## 8. SKIP liczony jako PASS
Test pominięty z powodu braku zależności kończy się kodem 0, identycznym jak prawdziwy sukces. Zielony pasek nie odróżnia „sprawdziłem” od „nie sprawdziłem”.
**Sprawdź:** brak zależności w środowisku docelowym to błąd konfiguracji, nie powód do cichego zielonego. Raportuj PASS / FAIL / SKIP osobno, nigdy nie licz SKIP do „wszystko OK”.

## 9. Niecierpliwy timeout
Wywołujący ma limit krótszy niż realny czas zadania i ogłasza awarię, choć zadanie kończy się poprawnie później.
**Sprawdź:** czy limit pochodzi z pomiaru (np. p99 z ostatnich przebiegów), czy ze zgadywania. Przy zadaniach długich — odpytywanie statusu zamiast blokującego czekania. Przekroczenie limitu to „nie zdążyłem sprawdzić”, nie „druga strona nie działa”.

## 10. Metadane deklarują parametr, którego żadna warstwa nie przenosi
Raport mówi „temperature=0, seed=42”, a warstwa pośrednia nie ma pola na `seed` i po cichu go gubi. Wynik wygląda na powtarzalny, ale nie jest.
**Sprawdź:** buduj metadane z tego samego słownika, który realnie idzie w żądanie. Dodaj test kontrolny: bez jawnego parametru wynik **musi** się różnić między powtórzeniami. Brak pola w kontrakcie warstwy pośredniej to błąd kontraktu.

## 11. Warstwa opakowania widzi tylko siebie
Monitoring sprawdza menedżera (systemd, supervisor, hypervisor), który jest zielony, dopóki żyje — niezależnie od tego, co dzieje się w kontenerze lub procesie potomnym.
**Sprawdź:** dwie warstwy jako dwa osobne bezpieczniki: (1) opakowanie żyje, (2) zawartość jest zdrowa (liczba restartów, tempo zdarzeń w dzienniku, healthcheck aplikacji).

## 12. Zapis nieatomowy: kasowanie starych danych przed zbudowaniem nowych
Przerwanie w połowie zostawia magazyn pusty albo uszkodzony. Diagnoza może paść tym samym mechanizmem, który uszkodził dane, więc cisza wygląda jak „jeszcze liczy”.
**Sprawdź:** buduj do magazynu tymczasowego, produkcyjną nazwę przejmuj warunkowo po udanym wyniku i po porównaniu liczby elementów. Długie zadanie odczep od sesji (`setsid`/`nohup`, log do pliku). Sondę „czy magazyn żyje” uruchamiaj w podprocesie — segfault zabija cały interpreter razem z `try/except`.

## 13. Diagnoza trafna, recepta fałszywa
Dwa mechanizmy zarządzają tym samym zasobem bez koordynacji. Alarm mówi „zrestartuj usługę”, ale port trzyma proces startowany poza menedżerem, więc komenda nie może pomóc.
**Sprawdź:** zanim napiszesz skrypt naprawczy, ustal, czy nie tworzysz drugiego właściciela zasobu. Przy każdej gotowej komendzie do wklejenia zapytaj, czy istnieje scenariusz, w którym diagnoza jest trafna, a komenda nic nie zmieni — jeśli tak, zmień treść recepty.

## 14. Weryfikacja producenta zamiast dosięgu konsumenta
Nowy proces żyje i odpowiada lokalnie, ale konsument (inna usługa, urządzenie, klient) nadal wskazuje stary adres albo nie ma drogi sieciowej.
**Sprawdź:** wypisz wszystkich konsumentów ze starymi nazwami/hostami/portami (grep konfiguracji, nie pamięć), przepnij każdego i zweryfikuj **rzeczywistą ścieżką konsumenta**, nie `curl` z boku. „Kontener Up” ≠ „osiągalny”.

## 15. Przyrząd zmierzył pustkę
Proces zakończył się kodem 0, ale zależność (model, usługa, plik danych) nie odpowiadała — wynik jest bezwartościowy, nie „zdany”.
**Sprawdź:** przed zaufaniem wynikowi potwierdź, że zależność realnie działała. Rozdziel dwa kody wyjścia: „brak warunków pomiaru” (nie jest porażką) i „pomiar się odbył, wynik zerowy” (jest porażką).

## 16. Bezpiecznik pilnuje napisu odmowy, nie sytuacji
Dwa kawałki kodu czytają ten sam katalog według różnych reguł; odmowa dotycząca starej wersji danych zostaje odczytana jako odmowa dotycząca bieżącego pomiaru.
**Sprawdź:** zawęź zbiór do tej samej wersji/zestawu, którego dotyczy pomiar (jawny parametr, nie „wszystko w katalogu”), i wypisz w raporcie, ile plików odpadło i dlaczego.

## 17. „?” czyta się jak OK
Strażnik szuka dosłownego napisu w dokumencie; po redakcji nagłówka nie znajduje warunków wejścia i zgłasza „nie sprawdzone” — wizualnie prawie jak „OK”.
**Sprawdź:** kontrola rozpoznaje warianty zapisu, a `?` jest wizualnie i strukturalnie odróżnialny od `OK` (inny symbol, licznik). Przy każdej redakcji dokumentu czytanego przez strażnika sprawdź zaczep przed zapisaniem zmiany.

## 18. Test napisany przez wykonawcę mierzy wykonawcę
Osoba lub model, który naprawia kod, sam pisze testy, na których się rozlicza. Bateria dopasowuje się do jego własnych przykładów, wynik rośnie do 100%, a jakość na niewidzianym materiale stoi.
**Sprawdź:** odbiór idzie na zestawie, którego wykonawca nie widział i nie pisał. Własna bateria to sygnał wewnętrzny („czy w ogóle się uruchamia”), nigdy dowód gotowości dla klienta.

## Wynik — lista kontrolna
- [ ] każde dopasowanie na granicy słowa/pola, przeczenia obsłużone,
- [ ] każdy dowód przypisany do okna zdarzenia,
- [ ] start usługi ma jawną zależność,
- [ ] istnienie i treść sprawdzone osobno,
- [ ] podstawienie szablonu potwierdzone asercją po wyniku,
- [ ] każdy alarm ma odbiorcę, nie tylko plik,
- [ ] tekst dla człowieka nie mocniejszy niż sprawdzony warunek,
- [ ] SKIP nie liczony jako PASS,
- [ ] timeouty zmierzone, nie zgadnięte,
- [ ] parametry obecne w każdej warstwie, metadane z payloadu,
- [ ] monitoring opakowania i zawartości,
- [ ] zapis atomowy, sonda w podprocesie,
- [ ] skrypt naprawczy nie jest drugim właścicielem zasobu,
- [ ] konsument przetestowany własną ścieżką,
- [ ] zależność pomiaru potwierdzona przed wynikiem,
- [ ] bezpiecznik zawężony do właściwej wersji danych,
- [ ] „?” odróżnialne od „OK”,
- [ ] odbiór na zestawie spoza wiedzy wykonawcy.

## Czego ten skill nie robi
Nie zastępuje właściciela domeny (testów, bezpieczeństwa, infrastruktury) — jest mechaniczną listą pytań do kodu, który sam stwierdza stan. Nie obiecuje, że po przejściu listy kod jest poprawny; obiecuje, że nie będzie kłamał cicho w tych osiemnastu miejscach.
