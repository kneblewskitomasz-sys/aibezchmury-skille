# aibezchmury-skille

Dwanaście skilli do pracy z agentem AI, które pilnują jednej rzeczy: **żeby wynik pracy był prawdziwy, a nie tylko dobrze wyglądał**.

To wyciąg z procedur, które powstały przy realnych wpadkach: zielony test przy braku sprawdzenia, liczba bez źródła, „zrobione” bez artefaktu, darmowe API z licencją niekomercyjną, pamięć modelu czytana jak polecenie. Każda procedura została przepisana na neutralny język i oczyszczona z danych konkretnych projektów, klientów i infrastruktury.

## Co jest w środku

| skill | po co |
|---|---|
| `rzetelny-pomiar` | liczba ogłoszona jako wynik ma skrypt, surowy zapis i datę; test na wygodnym podzbiorze nie udaje dowodu |
| `rzetelna-weryfikacja` | osiemnaście pułapek kodu, który sam stwierdza stan: health-check, grader, watchdog, warunek startu |
| `zrodlo-i-data` | każde twierdzenie liczbowe, prawne i faktograficzne ma źródło i datę odczytu |
| `dowod-stanu` | „zrobione / czeka / ustalone” tylko po sprawdzeniu żywego artefaktu, nie tytułu commita czy treści zlecenia |
| `kontrakt-zrodla-danych` | limit, nagłówki i licencja komercyjna cudzego API sprawdzone, zanim napiszesz pętlę pobierania |
| `pamiec-nie-polecenie` | treść z pamięci i RAG to dane, nie polecenia; trzy warstwy obrony przed pośrednim wstrzyknięciem |
| `zapis-na-biezaco` | wynik na dysk po każdym etapie, żeby przerwanie nie skasowało całej pracy |
| `straznik-danych-przed-wysylka` | przed wklejeniem tekstu do czatu w chmurze sprawdza PESEL, NIP, REGON, IBAN, numer dowodu, telefon, nazwiska i dane o zdrowiu; przy trafieniu każe zamaskować albo nie wysyłać. W `zestaw-testowy/` jest 80 zmyślonych polskich tekstów z wynikami pomiaru (Bielik-Minitron 7B, Qwen3 8B) |
| `zlecenie-i-odbior` | komenda odbioru zapisana przed zleceniem; wynik odbierasz po artefakcie, nie po słowie „gotowe” |
| `test-skutkow-4-przypadki` | automat, który blokuje, ponawia albo zmienia wspólny stan, przechodzi cztery przypadki przed włączeniem: błędny, poprawny, awaria zależności, wycofanie |
| `bezpieczenstwo-konta` | podejrzany mail albo alert logowania: co wolno sprawdzić tylko czytając, czego nie klikać i co zostawić właścicielowi konta |
| `polski-tekst-bez-sladow-ai` | polskie ślady pisania modelem (kalki, trójki, myślniki, mała litera po zwrocie) i przepisywanie tylko trafionych zdań |

## Jak zainstalować

Skill to katalog z plikiem `SKILL.md`. Skopiuj wybrane katalogi do miejsca, w którym Twój agent szuka skilli — na przykład:

```
cp -r rzetelny-pomiar ~/.claude/skills/
```

Albo wskaż agentowi plik `SKILL.md` bezpośrednio w promptcie. Skille nie mają zależności, nie łączą się z siecią i nie zawierają kodu do uruchomienia — to procedury w Markdownie.

## Jak tego używać

Skill nie jest skryptem, który „się wykona”. Jest listą pytań, którą agent (albo człowiek) przechodzi przed ogłoszeniem wyniku. Największą wartość daje nie jako osobne narzędzie, ale jako stały element instrukcji projektu: „przed zdaniem z liczbą przejdź `rzetelny-pomiar`”.

Każdy plik ma sekcję **Kiedy odpalić**, listę kroków, **Wynik** w formie listy kontrolnej i sekcję **Czego ten skill nie robi** — żeby nie udawał, że zastępuje właściciela domeny.

## Licencja

MIT. Możesz używać, zmieniać i sprzedawać, także komercyjnie. Zachowaj plik `LICENSE`.

## Pochodzenie

Procedury powstały w pracy nad lokalnymi asystentami AI i automatyką dla firm. Wersja publiczna została przepisana: usunięto nazwy klientów, adresy, nazwy hostów i wewnętrzne numery zdarzeń, a przykłady zastąpiono opisem mechanizmu. Nie zawiera danych osobowych ani konfiguracji infrastruktury.

Repozytorium: https://github.com/kneblewskitomasz-sys/aibezchmury-skille
