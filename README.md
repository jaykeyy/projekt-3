Volební skraper

O co jde v projektu?

Tento skript umožňuje získat výsledky parlamentních voleb z roku 2017 pro konkrétní okres z této webové stránky (https://cs.wikipedia.org/wiki/Volby_do_Poslaneck%C3%A9_sn%C4%9Bmovny_Parlamentu_%C4%8Cesk%C3%A9_republiky_2017) (vyberte si okres ve sloupci Výběr obce) a uložit je do CSV souboru.

Jak na to?

Před spuštěním projektu si nainstalujte potřebné knihovny uvedené v souboru requirements.txt. Skript spustite z příkazového řádku pomocí následujícího přikazu:

python volby17_RK.py <odkaz_uzemniho_celku> <vystupni_soubor>
Výstupem bude soubor .csv s výsledky voleb pro daný okres.

Jak to vypadá v praxi?

Například pro okres Cheb:

Odkaz -> [neplatná webová adresa bola odstránená]
Název výstupního souboru -> cheb_volby17.csv
Popis projektu

Projekt Volební skraper je skript v jazyce Python, který umožňuje automaticky stahovat výsledky parlamentních voleb z roku 2017 z webové stránky https://cs.wikipedia.org/wiki/Volby_do_Poslaneck%C3%A9_sn%C4%9Bmovny_Parlamentu_%C4%8Cesk%C3%A9_republiky_2017. Skript stahuje data pro konkrétní okres a ukládá je do souboru CSV.

Funkce skriptu

Stahuje výsledky parlamentních voleb z roku 2017 z webové stránky https://cs.wikipedia.org/wiki/Volby_do_Poslaneck%C3%A9_sn%C4%9Bmovny_Parlamentu_%C4%8Cesk%C3%A9_republiky_2017.
Umožňuje vybrat si okres, pro který chcete stáhnout data.
Ukládá data do souboru CSV.
Požadavky

Pro spuštění skriptu je nutné mít nainstalované knihovny uvedené v souboru requirements.txt. Knihovny si můžete nainstalovat pomocí příkazu pip install -r requirements.txt.

Spuštění skriptu

Skript spustíte z příkazového řádku pomocí následujícího přikazu:

python volby17_RK.py <odkaz_uzemniho_celku> <vystupni_soubor>
Kde:

<odkaz_uzemniho_celku> je odkaz na webovou stránku s výsledky voleb pro daný okres.
<vystupni_soubor> je název souboru CSV, do kterého budou data uložena.
Příklad spuštění

Pro okres Cheb spusťte skript následujícím příkazem:

python volby17_RK.py https://cs.wikipedia.org/wiki/Volby_do_Poslaneck%C3%A9_sn%C4%9Bmovny_Parlamentu_%C4%8Cesk%C3%A9_republiky_2017(https://cs.wikipedia.org/wiki/Volby_do_Poslaneck%C3%A9_sn%C4%9Bmovny_Parlamentu_%C4%8Cesk%C3%A9_republiky_2017)&xkraj=5&xnumnuts=4101 cheb_volby17.csv
Tento příkaz stáhne výsledky voleb pro okres Cheb a uloží je do souboru cheb_volby17.csv.

Výstup

Výstupem skriptu je soubor CSV s výsledky voleb pro daný okres. Soubor obsahuje následující sloupce:

Název obce
Počet voličů
Počet platných hlasů
Počet hlasů pro jednotlivé strany
Použití

Skript lze použít k získání dat o výsledcích parlamentních voleb z roku 2017 pro libovolný okres v České republice. Data lze dále zpracovávat a analyzovat pomocí různých nástrojů.

Poznámky

Skript je určen pro výzkumné a vzdělávací účely.
Skript není určen pro komerční použití.
Skript je distribuován pod licencí GPLv3.
