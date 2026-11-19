# NOTICES — Strażnik danych przed wysyłką

Stan odczytu licencji: 2026-11-19. Plik zbiera atrybucje dla skilla `straznik-danych-przed-wysylka` i narzędzi, z którymi bywa używany. Nie jest poradą prawną.

## 1. Ten skill i zestaw testowy

Dotyczy:

- `straznik-danych-przed-wysylka/SKILL.md`;
- `straznik-danych-przed-wysylka/zestaw-testowy/zestaw_d.py`;
- `straznik-danych-przed-wysylka/zestaw-testowy/zestaw-d.json`.

Licencja: MIT, Copyright (c) 2026 aibezchmury.pl — pełny tekst w pliku `LICENSE` w katalogu głównym repozytorium. Przy kopiowaniu zachowaj informację o prawach autorskich i tekst licencji.

## 2. Presidio (opcjonalna zależność)

Pakiet: `presidio-analyzer` (sprawdzana wersja 2.2.358).

- Licencja SPDX: MIT.
- Źródła: https://pypi.org/project/presidio-analyzer/2.2.358/ oraz https://github.com/data-privacy-stack/presidio
- Przy dostarczaniu pakietu razem z rozwiązaniem zachowaj notice i tekst licencji Presidio.

## 3. Zależności Presidio

| pakiet | wersja | SPDX / obowiązek |
|---|---|---|
| phonenumbers | >=8.12,<9.0.0 | Apache-2.0; zachować tekst licencji i ewentualny upstream NOTICE |
| regex | wg resolvera | Apache-2.0 |
| spacy | >=3.4.4,<4.0.0, !=3.7.0 | MIT; tylko jeśli instalator dostarcza pakiet |
| pyyaml | wg resolvera | MIT |
| tldextract | wg resolvera | BSD-3-Clause |
| idna | przechodnia | BSD-3-Clause |
| requests | przechodnia | Apache-2.0 |
| requests-file | przechodnia | Apache-2.0 |
| filelock | przechodnia | Unlicense; zachować upstream notice |
| NumPy i dołączone komponenty | wg resolvera | zachować notices NumPy, OpenBLAS/LAPACK oraz opisane przez wheel libgfortran (GPL-3.0-with-GCC-exception) i libquadmath (LGPL-2.1-or-later) |

Nie używamy modelu językowego spaCy `pl_core_news_*`, więc jego licencja nie dotyczy tej paczki.

## 4. Model lokalny Bielik-Minitron (opcjonalnie)

- GGUF: https://huggingface.co/speakleash/Bielik-Minitron-7B-v3.0-Instruct-GGUF
- Instruct: https://huggingface.co/speakleash/Bielik-Minitron-7B-v3.0-Instruct
- Model bazowy wskazany w karcie: https://huggingface.co/speakleash/Bielik-11B-v3-Base-20250730

Karty oznaczają model GGUF, Instruct i bazę jako Apache-2.0. Przy dystrybucji wag zachowaj odnośniki do kart i tekst Apache-2.0. Warunki modelu: https://bielik.ai/terms/. Karta Instruct opisuje publiczne, kuratorowane dane treningowe, ale nie podaje osobnej licencji każdego zbioru.

Wagi modelu nie są częścią tego repozytorium.

## 5. Runtime lokalny (opcjonalnie)

| runtime | licencja | notice |
|---|---|---|
| Ollama | MIT | https://github.com/ollama/ollama/blob/main/LICENSE |
| llama.cpp | MIT | https://github.com/ggml-org/llama.cpp/blob/master/LICENSE |

Żaden runtime nie jest częścią tego repozytorium.

## 6. Dane testowe i wzorce

`zestaw-d.json` jest syntetyczny: generator `zestaw_d.py` (ziarno 18202) tworzy 40 rekordów z danymi wrażliwymi danej kategorii i 40 czystych. Zestaw nie zawiera danych prawdziwych osób.

Sumy kontrolne NIP, REGON i numeru dowodu to implementacja znanych, publicznych reguł walidacji. Nie rościmy sobie wyłącznych praw do samej matematyki sum kontrolnych.
