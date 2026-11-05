---
name: dowod-stanu
description: "Używaj przed napisaniem zdania o STANIE pracy („zrobione”, „wynik gotowy”, „etap ukończony”, „zleciłem, czeka na odbiór”) w dzienniku, raporcie, handoffie albo podsumowaniu dla właściciela, oraz przed zdaniem o STANIE RELACJI z nazwanym człowiekiem („umówiliśmy się”, „potwierdził termin”). Każde takie zdanie wymaga żywego artefaktu, nie tytułu commita, treści zlecenia ani wrażenia z rozmowy."
license: MIT
---

# Dowód stanu — procedura

To nie jest błąd kodu. To błąd narracji: odpowiedź wzięta z rzeczy **sąsiedniej** (zlecenie zamiast wykonania, tytuł commita zamiast diffu, zapowiedź zamiast ustalenia) i podana jako fakt o samym przedmiocie.

## Kiedy odpalić
- Piszesz w dzienniku, raporcie, handoffie albo podsumowaniu zdanie zawierające: „zrobione”, „zleciłem / wynik ma trafić do…”, „etap X ukończony / nie ruszony”, „ktoś skończył / nie zaczął”.
- Audytujesz cudzą pracę na podstawie historii commitów — zanim ogłosisz werdykt.
- Zamykasz zlecenie wysłane do wykonawcy lub subagenta.
- Piszesz do osoby trzeciej zdanie o tym, co ktoś inny ustalił, obiecał albo zaakceptował.

## Trzy nazwane wzorce

### 1. Zlecenie potraktowane jako wykonanie
Licznik zlecenia potwierdza, że **prośba poszła**, nie że **wynik powstał**. Zdanie w czasie przeszłym o pliku, którego nikt nie otworzył, jest zamianą zamiaru na fakt.
**Naprawa:** przed zdaniem o wyniku sprawdź ścieżkę docelową (`ls`, odczyt pliku, uruchomienie). Brak pliku = „zlecone, wynik nie nadszedł”.

### 2. Audyt czytający tytuł commita zamiast diffu
`git log --oneline -- katalog` pokazuje najnowszy komunikat, nie pełną zmianę. Ten sam commit mógł dołożyć coś w katalogu, o czym tytuł milczy.
**Naprawa:** przy pytaniu „co ruszyło plik X” użyj `git log -- X` **oraz** `git show --stat <commit>` na każdym trafieniu. Przy „czy etap jest zrobiony” sprawdź żywy artefakt: uruchomienie, wynik testu, zachowanie na żywo.

### 3. Zapowiedź osoby trzeciej podana jako ustalenie
Ktoś powiedział, że coś **zrobi** („odezwę się”, „przekażę dalej”), a w dokumencie idącym do trzeciej osoby zmienia się to w „umówiliśmy się” albo „X się zgodził”. Dowód dotyczy intencji, nie ustalenia — a te dwie rzeczy różni to, czy druga strona może to zdementować publicznie.
**Naprawa:** bez dosłownego cytatu (mail, notatka) zdanie ma brzmieć jako zapowiedź: „powiedział, że się odezwie”, nie „ustaliliśmy”.

## Zasada ogólna
**Twierdzenie o stanie ma dowód na poziomie tego samego przedmiotu, o którym mówi zdanie — nie sąsiedniego.** „Zleciłem X” nie jest dowodem na „X istnieje”. „Ostatni commit na tej ścieżce wspomina Y” nie jest dowodem na „ostatnia zmiana na tej ścieżce to Y”.

Zadaj sobie pytanie: *czy dowód, na którym stoję, mówi dosłownie o tym, co właśnie twierdzę — czy o czymś obok, co zwykle idzie z tym w parze?*

## Konsekwencje zaniechania
- Priorytet „odczytać wynik”, który nie istniał, blokował pracę przez dobę.
- Polecenie „zaczynaj od etapu 1” poszło na podstawie audytu, który pomylił „niezrobione” z „zrobione, ale tytuł commita mówił o czym innym” — o krok od podwójnej roboty nad działającym kodem.
- Dokument do urzędu twierdził „umówiliśmy się na wrzesień”, gdy rozmówca tylko zapowiedział kontakt — urząd mógł zdementować spotkanie, którego nie było.

## Wynik
Każde zdanie o stanie ma przypisany dowód: plik z treścią, `git show --stat`, wynik uruchomienia albo dosłowny cytat. Zdania bez dowodu przeformułuj na „zlecone / zapowiedziane / nie sprawdzone”.

## Czego ten skill nie robi
Nie zastępuje rzetelnej weryfikacji kodu ani higieny źródła i daty. To czwarta, sąsiednia procedura: rygor zdania o stanie pracy w narracji, nie w kodzie.
