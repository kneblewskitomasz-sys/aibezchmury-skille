---
name: polski-tekst-bez-sladow-ai
description: "Używaj gdy polski tekst idzie do człowieka spoza zespołu: mail, oferta, post, wiadomość prywatna, wniosek, zgłoszenie, odpowiedź na reklamację. Znajduje ślady pisania modelem (sztampy, kalki z angielskiego, trójki, myślniki, formatowanie markdown, mała litera po zwrocie) i każe przepisać tylko trafione zdania, bez zmiany treści, cen, terminów i zobowiązań."
license: MIT
---

# Polski tekst bez śladów AI — procedura

Zasada: **najpierw zmierz, potem poprawiaj tylko trafione zdania.** Przepisanie całego tekstu „na świeżo” razem ze śladami zmienia fakty, ceny i zobowiązania. Ten skill działa na samej kartce — nie potrzebuje skryptu, modelu ani połączenia z siecią.

## Kiedy odpalić
- Przed **każdym** tekstem, który idzie do człowieka spoza zespołu: mail do klienta, oferta, post w mediach społecznościowych, wiadomość prywatna, wniosek do urzędu, zgłoszenie błędu, odpowiedź na reklamację.
- Gdy tekst powstał z pomocą modelu albo powstał przez przepisanie starszego tekstu.
- Gdy odbiorca ma wrażenie, że „to pisze robot”, a Ty nie umiesz wskazać dlaczego.

Nie używaj do notatek wewnętrznych, raportów dla siebie ani dokumentacji technicznej, która zostaje w zespole.

## Krok 1 — zmierz

Przejdź tekst zdanie po zdaniu i zaznacz trafienia. Dwie kategorie:

### Twarde — jedno trafienie wystarcza do ALARMU
Twarde to konstrukcja, której człowiek piszący do **konkretnego** odbiorcy zwykle nie używa:

- mała litera po zwrocie grzecznościowym: „Szanowny Panie, dziękuję…” (ma być „Dziękuję”);
- „mam nadzieję, że ta wiadomość zastaje Pana w dobrym zdrowiu” i podobne otwarcia;
- „w dzisiejszym dynamicznym świecie”, „w dobie cyfrowej transformacji”;
- „warto podkreślić, że…”, „kluczowe jest, aby…”, „należy zaznaczyć, że…”;
- „dedykowane rozwiązanie”, „szyte na miarę”, „kompleksowe rozwiązanie”, „innowacyjne podejście”, „holistyczne podejście”, „synergia”;
- „adresujemy wyzwania”, „odpowiadamy na potrzeby współczesnego biznesu”;
- „podsumowując”, „reasumując”, „na koniec dnia” jako wypełniacz;
- „jako model językowy”, „jako AI”.

### Miękkie — ALARM przy zagęszczeniu
Miękkie to rzeczy, których ludzie uczciwie używają, ale w nadmiarze zdradzają szablon:

- myślnik ` — ` łączący zdania w miejscu przecinka, kropki albo dwukropka;
- trójki równoległe: „szybko, sprawnie i bezpiecznie”;
- „zarówno…, jak i…”, „nie tylko…, ale także…”;
- „warto zauważyć”, „należy pamiętać”, „w praktyce”, „w istocie”;
- nadmiar przymiotników: „wyjątkowy, unikalny, skuteczny”;
- „w ramach”, „w kontekście”, „podejmować działania”, „optymalizować” jako wypełniacze;
- angielskie cudzysłowy zamiast polskich „…”;
- emoji, pogrubienia, nagłówki `##`, listy z `-` w mailu.

**Próg miękki:** 3 trafienia na 100 słów. Przy 200 słowach próg to 6, przy 100 — 3. Policz słowa, nie „na oko”.

**Formatowanie w mailu** liczy się jako osobna kategoria: raportuj je, ale i tak usuń **całe** formatowanie markdown, nie tylko trafione fragmenty. Mail ma wyglądać jak list od osoby, nie jak post.

## Krok 2 — przepisz TYLKO trafione zdania

1. Popraw **wyłącznie zdania z trafieniami**. Nie zmieniaj układu, nie skracaj całego tekstu, nie „ulepszaj” zdań, których nie oznaczyłeś.
2. **Nie zmieniaj treści:** nazw, liczb, cen, terminów, obietnic, zobowiązań, zakresu, warunków. Ślad usuwasz, fakt zostaje.
3. Nie dodawaj nowych twierdzeń, których w tekście nie było.
4. Nie usuwaj zastrzeżeń i ograniczeń, nawet jeśli brzmią niezgrabnie.

Najczęstsze zamiany:

| ślad | zamiana |
|---|---|
| „Warto podkreślić, że X” | „X” — usuń zapowiedź, podaj fakt |
| „Kluczowe jest, aby X” | „X” |
| „Dedykowane rozwiązanie” | „rozwiązanie dla <kogo>” albo „zrobione pod <co>” |
| „Adresujemy wyzwania” | „rozwiązujemy problem <jaki>” |
| „W dzisiejszym dynamicznym świecie…” | usuń, zacznij od faktu |
| „Mam nadzieję, że ta wiadomość zastaje…” | „Dzień dobry, piszę w sprawie…” |
| myślnik ` — ` | przecinek, kropka albo dwukropek |
| mała litera po „Szanowny Panie,” | wielka litera na początku zdania |
| „Podsumowując” | usuń, postaw wniosek |
| „Kompleksowe rozwiązanie” | co konkretnie robi |

W mailu dodatkowo: usuń nagłówki, pogrubienia, emoji i angielskie cudzysłowy; zostaw zwykłe akapity i polskie cudzysłowy „…”.

## Krok 3 — zmierz ponownie

Przeczytaj poprawiony tekst i porównaj **z wzrokiem, nie z pamięci**:
- czy każda cena, kwota i data została ta sama,
- czy nie zniknęło żadne zobowiązanie ani zastrzeżenie,
- czy nie pojawiło się nowe twierdzenie, którego nie było,
- czy po zwrocie grzecznościowym jest wielka litera,
- czy w mailu nie zostało formatowanie markdown.

Jeśli nadal jest ALARM, popraw kolejne trafione zdanie. **Nie podnoś progu** i nie wyłączaj wzorca, żeby „przeszło”.

## Przykład przed i po

**Przed (ALARM):**
> Szanowny Panie, w dzisiejszym dynamicznym świecie warto podkreślić, że nasze dedykowane rozwiązanie kompleksowo adresuje wyzwania, przed którymi stoją firmy — nie tylko w obszarze sprzedaży, ale także w marketingu.

**Po (OK):**
> Dzień dobry, przygotowaliśmy rozwiązanie dla firm, które chcą uporządkować sprzedaż i marketing.

Zmieniły się tylko trafione zdania. Nie doszła żadna cena, termin ani obietnica.

## Wynik
- 0 trafień twardych.
- Mniej niż 3 trafienia miękkie na 100 słów.
- 0 formatowania markdown w mailu.
- Wszystkie ceny, daty, terminy i zobowiązania bez zmian.
- Żadne nowe twierdzenie nie weszło.

## Czego ten skill nie robi
- Nie gwarantuje, że tekst przejdzie detektor AI. Detektory flagują też teksty pisane przez ludzi; to nie jest miara człowieczeństwa.
- Nie usuwa tonu ani rejestru — tylko konstrukcje z listy.
- Nie działa dla tekstów angielskich; wzorce są polskie.
- Nie sprawdza prawdziwości faktów — od tego jest osobna procedura źródła i daty.
- Nie wysyła tekstu nigdzie: to kartka do przejścia ręcznie.
