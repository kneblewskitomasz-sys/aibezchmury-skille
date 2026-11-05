---
name: zapis-na-biezaco
description: "Gdy wykonujesz zadanie wieloetapowe albo długie (audyt, budowa modułu, pomiar A/B, praca subagenta w równoległej partii) — zapisuj wynik i wnioski na dysk po każdym znaczącym kroku, nie tylko w końcowej odpowiedzi. Używaj zwłaszcza wtedy, gdy zabraknięcie budżetu sesji może przerwać pracę w połowie. Cel: przerwanie zostawia użyteczną, częściową pracę, a nie nic."
license: MIT
---

# Zapis na bieżąco — procedura

Agent, który pisze wynik dopiero na końcu, traci **wszystko**, jeśli skończy mu się budżet sesji przed dotarciem do odpowiedzi. Agent, który zapisuje po drodze, traci tylko to, czego jeszcze nie zdążył zrobić.

## Kiedy odpalić
- Jesteś subagentem uruchomionym jako część partii kilku równoległych zadań — ryzyko wyczerpania budżetu rośnie z liczbą zadań w kolejce.
- Zadanie ma wyraźne etapy: przeczytaj → zdiagnozuj → zaproponuj → napisz raport; albo zaprojektuj → zaimplementuj → przetestuj → udokumentuj.
- Zadanie jest z natury długie (research, pomiar z wieloma przebiegami, naprawa wielu plików) i nie wiesz z góry, ile kroków zdążysz wykonać.

## Zasada
1. **Po każdym znaczącym etapie zapisz wynik na dysk** — plik roboczy, notatkę, częściowy raport. Format jest nieważny; ważne, żeby istniał i był odczytywalny przez osobę, która przejmie zadanie.
2. **Nazwij plik tak, żeby było jasne, że to wynik częściowy** (`_czesciowy-`, `-W-TOKU` w nazwie albo jawny nagłówek w treści). Inaczej niedokończona praca zostanie pomylona z gotowym rezultatem.
3. **Nie czekaj na „ładne podsumowanie na koniec”.** Surowy plik z trzema z pięciu etapów jest wart więcej niż zero plików, gdy zabraknie budżetu na etap czwarty i piąty.
4. **Przy normalnym zakończeniu** złóż wszystko w jeden spójny raport końcowy. Zapisy pośrednie to siatka bezpieczeństwa, nie zamiennik dobrego podsumowania.

## Wzór nagłówka pliku częściowego
```
# <zadanie> — CZĘŚCIOWY
Data: <data i godzina>
Zrobione: <etapy 1-3>
Niezrobione: <etapy 4-5 i dlaczego>
Pliki wyniku: <ścieżki>
```

## Co to daje w praktyce
W partii pięciu równoległych agentów dwóch padło na limicie sesji w połowie pracy. Obaj zostawili użyteczne wyniki na dysku, bo zapisywali na bieżąco. Gdyby pisali dopiero na końcu, cała ich praca przepadłaby bez śladu — tak jak nocna zmiana, która nie zapisała nic przed utratą zasilania.

## Czego ten skill nie robi
Nie zastępuje weryfikacji kodu ani rzetelnego pomiaru. To osobna rzecz: dyscyplina zapisu w trakcie pracy, żeby przerwanie nie kasowało całości.
