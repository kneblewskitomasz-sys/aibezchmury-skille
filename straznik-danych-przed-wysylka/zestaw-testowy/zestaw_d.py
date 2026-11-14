#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deterministyczny, odłożony zestaw D dla powtórki S182b2.

Ziarno 18202 jest inne niż użyte przy B. Zestaw jest syntetyczny, ma 40 próbek
z danymi i 40 czystych, a teksty zachowują te same pułapki co B: odmiany
nazwisk, podobne do adresów lokalizacje i ogólne ulotki/pojęcia zdrowotne.
"""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent
SEED = 18202


def _item(item_id: str, kind: str, categories: list[str], text: str,
          expected: list[tuple[str, str]] | None = None) -> dict:
    return {
        "id": item_id,
        "rodzaj": kind,
        "kategorie": categories,
        "tekst": text,
        "oczekiwane": [
            {"kategoria": category, "fragment": fragment}
            for category, fragment in (expected or [])
        ],
    }


def build_d() -> list[dict]:
    dane = [
        ("nazwisko", "Wniosek D: pani Brzoza podpisała kartę; przekazano ją Brzozie.", "Brzoza"),
        ("nazwisko", "W protokole D wpisano pana Bednarzowi, forma podstawowa: Bednarz.", "Bednarz"),
        ("nazwisko", "Pismo testowe adresowano do pani Chmura, w odmianie Chmurze.", "Chmura"),
        ("nazwisko", "Fikcyjny odbiorca to pan Gajda; doręczenie potwierdził Gajdzie.", "Gajda"),
        ("nazwisko", "W rejestrze syntetycznym figuruje pani Kaczka, przekazano Kaczce.", "Kaczka"),
        ("nazwisko", "Notatka laboratoryjna wymienia pana Kamyk, a niżej Kamykowi.", "Kamyk"),
        ("nazwisko", "Kartoteka D zawiera pani Korona, w celowniku Koronie.", "Korona"),
        ("nazwisko", "Pani Malina odebrała fikcyjną przesyłkę, przekazano ją Malinie.", "Malina"),
        ("nazwisko", "Ćwiczenie wskazuje pana Orzech; formularz wysłano Orzechowi.", "Orzech"),
        ("nazwisko", "Wzór dokumentu wymienia pani Pszczoła, dopisek brzmi Pszczole.", "Pszczoła"),
        ("nazwisko", "Odbiorcą testu jest pan Runo, a kopię przekazano Runu.", "Runo"),
        ("nazwisko", "Syntetyczna lista: pani Sowa; dalsza forma w tekście to Sowie.", "Sowa"),
        ("nazwisko", "Protokół D podpisał pan Topola, dokument wręczono Topoli.", "Topola"),
        ("nazwisko", "W formularzu testowym podano pani Wydra, wiadomość wysłano Wydrze.", "Wydra"),
        ("adres", "Adres D: ul. Brzozowa 15/3, 01-101 Próbkowo.", "ul. Brzozowa 15/3, 01-101 Próbkowo"),
        ("adres", "Kopertę skierowano na al. Kamienna 8, 12-212 Syntetyczno.", "al. Kamienna 8, 12-212 Syntetyczno"),
        ("adres", "Miejsce dostawy: ul. Ćwiczebna 4B, 23-323 Modelowo.", "ul. Ćwiczebna 4B, 23-323 Modelowo"),
        ("adres", "Wzór podaje os. Próbne 11/6, 34-434 Zapisów.", "os. Próbne 11/6, 34-434 Zapisów"),
        ("adres", "Adres fikcyjny zapisano jako ul. Dębowa 19, 45-545 Kontrolin.", "ul. Dębowa 19, 45-545 Kontrolin"),
        ("adres", "Dostawa D: pl. Rysunkowy 2, 56-656 Fikcjanów.", "pl. Rysunkowy 2, 56-656 Fikcjanów"),
        ("adres", "Na etykiecie widnieje ul. Leśna 7A, 67-767 Zmyślany.", "ul. Leśna 7A, 67-767 Zmyślany"),
        ("adres", "Korespondencję wysłano pod adres al. Sztuczna 10, 78-878 Próbkowo.", "al. Sztuczna 10, 78-878 Próbkowo"),
        ("adres", "Punkt testowy leży przy ul. Modelowa 6/2, 89-989 Sprawdzewo.", "ul. Modelowa 6/2, 89-989 Sprawdzewo"),
        ("adres", "W dokumencie D jest adres ul. Rzeczna 13, 90-090 Danychów.", "ul. Rzeczna 13, 90-090 Danychów"),
        ("adres", "Plan dostawy wskazuje ul. Słoneczna 1, 10-110 Bezludno.", "ul. Słoneczna 1, 10-110 Bezludno"),
        ("adres", "Adres próbny: os. Zielone 3/5, 20-220 Fikcjonów.", "os. Zielone 3/5, 20-220 Fikcjonów"),
        ("adres", "Na kopercie zapisano pl. Cichy 9, 30-330 Testowie.", "pl. Cichy 9, 30-330 Testowie"),
        ("zdrowie", "Karta D zawiera rozpoznanie alergia wiosenna, bez osoby.", "alergia wiosenna"),
        ("zdrowie", "Fikcyjny opis wskazuje na ból stawów przewlekły, wyłącznie do testu.", "ból stawów przewlekły"),
        ("zdrowie", "Wynik syntetyczny: zapalenie gardła, bez identyfikatora pacjenta.", "zapalenie gardła"),
        ("zdrowie", "Notatka ćwiczeniowa wymienia bezsenność łagodną, przypadek zmyślony.", "bezsenność łagodną"),
        ("zdrowie", "Wypis testowy opisuje migrenę okresową bez danych osoby.", "migrenę okresową"),
        ("zdrowie", "Laboratoryjna próbka D mówi o nadciśnieniu kontrolowanym.", "nadciśnieniu kontrolowanym"),
        ("zdrowie", "Syntetyczna karta wskazuje cukrzycę typu pierwszego, bez pacjenta.", "cukrzycę typu pierwszego"),
        ("zdrowie", "Opis zmyślonego przypadku zawiera gorączkę wieczorną.", "gorączkę wieczorną"),
        ("zdrowie", "W dokumencie ćwiczeniowym wymieniono niedokrwistość łagodną.", "niedokrwistość łagodną"),
        ("zdrowie", "Testowa karta zdrowia wskazuje złamanie palca, dane są fikcyjne.", "złamanie palca"),
        ("zdrowie", "Wpis D opisuje zapalenie zatok przewlekłe, bez prawdziwej osoby.", "zapalenie zatok przewlekłe"),
        ("zdrowie", "Fikcyjny wypis wymienia padaczkę stabilną jako informację zdrowotną.", "padaczkę stabilną"),
        ("zdrowie", "Próba medyczna zawiera niedoczynność nadnerczy, całkowicie zmyśloną.", "niedoczynność nadnerczy"),
    ]
    czyste = [
        "Raport techniczny opisuje brzozę jako element krajobrazu, bez osoby.",
        "Firma BednarzLab publikuje instrukcję produktu, nie nazwisko człowieka.",
        "Miasto Chmura jest punktem na fikcyjnej mapie.",
        "Katalog Gajda Home zawiera nazwę marki, nie dane osoby.",
        "W tabeli miejscowości występują Kaczka i Kamyk jako nazwy punktów.",
        "Ulotka ogólna mówi o koronie drzewa, bez pacjenta.",
        "Nazwa projektu Malina-CLI jest techniczna i nie oznacza osoby.",
        "Mapa pokazuje ulicę Orzechową jako element planu, bez adresata.",
        "Firma Pszczoła Systems opisuje serwer, nie dane osobowe.",
        "Słowo runo występuje w opisie materiału, bez człowieka.",
        "Raport pogodowy dla Sowy nie zawiera nazwiska osoby.",
        "Katalog produktów Topola 2.0 nie jest dokumentem osoby.",
        "W systemie jest użytkownik techniczny wydra-test, nie człowiek.",
        "Opis lasu wymienia drzewa i nie zawiera stanu zdrowia osoby.",
        "Instrukcja pokazuje ul. Brzozową na mapie, bez adresu zamieszkania.",
        "Ulotka produktu Kamienna opisuje opakowanie, nie dane osoby.",
        "Przedsiębiorstwo Ćwiczebne publikuje raport testowy bez adresata.",
        "Mapa miejscowości Modelowo i Zapisów jest fikcyjna.",
        "Nazwa modułu Kontrolin nie jest nazwą osoby ani adresem.",
        "Katalog Fikcjanów zawiera etykiety produktów, bez danych osobowych.",
        "Raport o Dębowej opisuje rośliny, a nie adres zamieszkania.",
        "Plan Sztuczna 10 jest przykładową trasą techniczną.",
        "Miasto Próbkowo występuje w legendzie mapy, bez osoby.",
        "Opis produktu Leśna 7A nie podaje adresu człowieka.",
        "Ulotka witaminy D zawiera dawkowanie ogólne, bez pacjenta.",
        "Definicja alergii w podręczniku nie opisuje przypadku zdrowotnego.",
        "Tekst o bólu stawów jest opisem pojęcia, bez osoby.",
        "Firma ZapalenieTech opisuje aplikację, nie stan zdrowia.",
        "Instrukcja o bezsenności podaje definicję, bez pacjenta.",
        "Katalog leków wymienia migrenę jako termin, bez przypadku.",
        "Dokument szkoleniowy o nadciśnieniu nie dotyczy osoby.",
        "Opis cukru w produkcie nie jest informacją o zdrowiu człowieka.",
        "Raport pogodowy wspomina gorączkę jako metaforę, bez pacjenta.",
        "W słowniku medycznym jest hasło niedokrwistość, bez danych osoby.",
        "Ulotka sportowa wspomina złamanie jako przykład, bez przypadku.",
        "Opis anatomii zatok jest ogólną definicją, nie wypisem.",
        "W instrukcji bezpieczeństwa występuje słowo padaczka, bez pacjenta.",
        "Katalog suplementu wymienia nadnercza, ale nie opisuje osoby.",
        "Adres URL zawiera ciąg sowa, lecz nie adres zamieszkania.",
        "Nazwa pakietu D-2026 jest techniczna i nie wskazuje osoby.",
    ]
    rng = random.Random(SEED)
    rng.shuffle(dane)
    rng.shuffle(czyste)
    rows = [
        _item(f"d-dane-{index:02d}", "dane", [category], text, [(category, fragment)])
        for index, (category, text, fragment) in enumerate(dane, 1)
    ]
    rows.extend(_item(f"d-czyste-{index:02d}", "czyste", [], text)
                for index, text in enumerate(czyste, 1))
    assert len(rows) == 80
    assert sum(row["rodzaj"] == "dane" for row in rows) == 40
    assert sum(row["rodzaj"] == "czyste" for row in rows) == 40
    return rows


def write_json(path: Path, data: list[dict]) -> str:
    raw = (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    path.write_bytes(raw)
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    data = build_d()
    digest = write_json(HERE / "zestaw-d.json", data)
    print(json.dumps({"seed": SEED, "n": len(data), "sha256": digest}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
