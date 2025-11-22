# 🎓 Hra "Milionář" (Python/Tkinter) - Archiv

> **⚠️ UPOZORNĚNÍ: Archivní projekt**
>
> Toto je záloha staršího školního projektu z dob vysokoškolského studia. Kód je zveřejněn ve stavu "jak je" (as-is) pro účely archivace a reference.
>
> **Projekt není aktivně udržován, nereflektuje současné standardy psaní kódu a nemusí být plně funkční na novějších verzích Pythonu bez úprav.**

## 📝 O projektu

Jednoduchá desktopová implementace vědomostní soutěže na motivy "Chcete být milionářem?". Aplikace je napsána v jazyce **Python** s využitím standardní grafické knihovny **Tkinter**.

Projekt sloužil primárně k procvičení práce s GUI, manipulace s JSON soubory a základní herní logiky.

## ✨ Funkce a vlastnosti

* **Grafické rozhraní:** Vlastní tmavý režim ("Dark/Grey theme").
* **Herní systém:**
    * Načítání náhodných otázek z externího souboru (`otazky.json`).
    * Počítání skóre (zdvojnásobování bodů).
* **Nápovědy:**
    * **50:50**: Odstraní dvě špatné odpovědi.
    * **Nápověda publika**: Vygeneruje a vykreslí graf pravděpodobnosti v novém okně.
* **Scoreboard**: Ukládání jména a skóre nejlepších hráčů do souboru `scoreboard.json`.

## 🛠️ Požadavky a instalace

Ke spuštění je potřeba **Python 3**. Knihovna `tkinter` je obvykle součástí standardní instalace Pythonu.

### Struktura souborů
Pro správné spuštění musí být ve stejném adresáři jako skript umístěny následující soubory:

1.  `main.py` - Hlavní skript hry.
2.  `otazky.json` - Databáze otázek a odpovědí.
3.  `scoreboard.json` - Soubor pro ukládání výsledků.
    * *Tip: Pokud soubor nemáte, vytvořte prázdný soubor s obsahem `[]`.*
4.  `dolar.png` - Ikona aplikace (nutná pro spuštění GUI).

### Spuštění

V příkazovém řádku (terminálu) přejděte do složky projektu a spusťte:

```bash
python main.py

## 📂 Formát dat (otazky.json)

Aplikace načítá otázky ze souboru JSON. Struktura musí vypadat následovně:

```json
[
  {
    "otazka": "Znění otázky?",
    "spravna": "Správná odpověď",
    "vsechny": [
      "Špatná odpověď 1",
      "Špatná odpověď 2",
      "Špatná odpověď 3"
    ]
  },
  {
    "otazka": "Další otázka...",
    "spravna": "...",
    "vsechny": ["...", "...", "..."]
  }
]

## 🐛 Známé problémy / Limitace

- Aplikace vyžaduje existenci souboru `dolar.png`, jinak se nespustí.
- Kód využívá režim `r+` pro otevírání souborů, což znamená, že soubory jako `scoreboard.json` musí existovat před spuštěním.
- Styl kódování odpovídá úrovni začínajícího studenta (mix češtiny a angličtiny v proměnných, globální proměnné).
- Tento repozitář slouží pouze jako osobní záloha.
