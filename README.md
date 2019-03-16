Michal Kabáč, dokumentácia k 2. zadaniu

Problém 3.​ Pre riešenie problému Eulerovho koňa existuje veľmi dobrá a pritom jednoduchá
heuristika, skúste na ňu prísť sami. Ak sa vám to do týždňa nepodarí, pohľadajte na
dostupných informačných zdrojoch heuristiku (z roku 1823!), prípadne konzultujte na
najbližšom cvičení cvičiaceho. Implementujte túto heuristiku do algoritmu prehľadávania
stromu do hĺbky a pre šachovnicu 8x8 nájdite pre 10 rôznych východzích bodov jedno (prvé)
správne riešenie (pre každý východzí bod). Algoritmus s heuristikou treba navrhnúť a
implementovať tak, aby bol spustiteľný aj pre šachovnice iných rozmerov než 8x8. Treba
pritom zohľadniť upozornenie v​ ​ Poznámke 1​ . Je preto odporúčané otestovať
implementovaný algoritmus aj na šachovnici rozmerov 7x7, 9x9, prípadne 20x20 (máme
úspešne odskúšaný aj rozmer 255x255) a prípadné zistené rozdiely v úspešnosti heuristiky
analyzovať a diskutovať.

Stručný opis riešenia:
Zo vstupu sa načíta hodnota - veľkosť mapy. Táto mapa sa postupne prehľadáva, začíname
na indexe 0. V mojom zadaní som použil heuristiku, ktorá dopredu ohodnotí každé políčko
na ktoré sa viem dostať z aktuálnej pozície. Toto ohodnotenie funguje na základe toho,
koľko pohybov viem vykonať z daného políčka. Všetky tieto ohodnotenia si vložím do min
haldy. Následne ich postupne vložím do aktuálneho poľa a pole vložím do stacku(vloženie
celého poľa do stacku mi zabezpečí, že na nejaké políčko nevstúpim 2x z rovnakej pozície,
zároveň mi pole slúži aj ako postupnosť vykonaných krokov). Ako ďalšie políčko z ktorého
budem prehľadávať vyberiem to ktoré má najmenšie ohodnotenie z minhaldy. Index tohto
políčka si poznačím v jednorozmernom poli aby som vedel že políčko už mám navštívené.
Takto pokračujem až kým nemám minimum v poli = 1. Heuristika funguje veľmi optimálne,
nakoľko nájde cestu takmer vždy na prvý pokus. Pri vypnutí heuristiky nájdenie výsledku
trvalo niekoľko krát dlhšie.

Reprezentáciu pohybu kona som si ukladal do jednorozmerného poľa. Pri spustení
programu sa toto jednorozmerné pole alokuje na rozmer n x n pričom je naplnené samými
nulami. Na index v poli si následne ukladám poradie, v ktorom kôň políčko navštívil. Akcie
mám reprezentované pomocou 8 funkcii. Tieto funkcie reprezentujú pohyb koňa - (dva hore
jeden doľava, dva hore jeden doprava....). Prehľadávanie stavového priestoru prebieha
dovtedy, kým bude v reprezentácii pohybu koňa ako minimum 0. (prvý krok mám
ohodnotený 1 a posledný má hodnotu n x n, takže keď bude min 1 celý stavový priestor
bude prehľadaný) Zároveň prehľadávanie prebieha, pokiaľ nie je stack prázdny. Počas
prehľadávania som musel kontrolovať či kôň nevystúpi z mapi(kontroloval som to prepisom
súradníc jednorozmerného poľa do dvojrozmerného).Stavový priestor som prehľadával
prehľadávaním do hĺbky.

Pri testovaní som postupoval nasledovne: malé vstupy (mapa 5 x 5, 6 x 6) som skontroloval
ručne. Zistil som že algoritmus funguje správne. Potom som napísal vlastné testy, ktorými
som neskôr kontroloval výstupy. Testy kontrolujú, či výsledné pole je dostatočne dlhé
vzhľadom na vstup, ďalej kontrolujem či sa tam každé číslo nachádza práve raz a či súčet
prvkov v poli sa rovná súčtu prvkov v rozmere mapy (od 1 po n x n). Následne výstup
skontrolujem tak, Že prebehnem pole od začiatku do konca (podľa pohybov koňa). Ak sadostanem do 1 tak výstup je správny. Ďalej som testoval aj jednotlivé menšie funkcie či
dávajú správne výstupy. Po spustení programu sa výstupné hodnoty uložia do súboru
inputs, následne sú skontrolované testami. V niektorých výstupoch som schválne urobil
chybu, avšak moje testy to odhalili. Nepodarilo sa mi nájsť žiadny nekorektný vstup, ktorý by
prešiel cez testy.

Moje riešenie je podľa mňa optimálne. Skúšal som ho aj na väčších vstupoch ako vyplýva zo
zadania (dokázal nájsť riešenia aj na mape 100 x 100 a 500 x 500). Výhoda v mojom
algoritme určite spočíva v navrhnutej heuristike, ktorá riešenie nájde skoro vždy na prvýkrát.
Vtedy je časová zložitosť O(N). Kód som sa pokúšal čo najviac optymalizovať, ale brzdili ma
moje skúsenosti s Pythonom, nakoľko je to môj prvý program v pythone. Program je
organizovaný do funkcií, takže aj jeho rozšíriteľnosť by mala byť bezproblémová. Nevýhody,
som v mojom algoritme nepostrehol. Program je spustiteľný v ktoromkoľvek prostredí, kde
sú dostupné python knižnice ktoré používam v mojom programe a je možné skompilovať
python kód.

Program som testoval pre dĺžky do max 500 x 500. Čím bol vstup väčší, tým dlhšie trvalo
zbehnutie programu. Tak isto bolo treba aj viac pamäte. Dĺžka behu programu sa odvíja aj
od toho, či z danej štartovnej pozície sa šachovnica dala prejsť. Napr pri veľkosti mapy 5
existuje riesenie iba z párnych pozícii. Preto keď skúšal nepárnu pozíciu, beh programu
závisel od počtu krokov, koľko sa má vykonať a ak nenájde riešenie tak dosiahnutie
cieľového stavu prehlási za nemožné. Prípadne mohol skončiť aj skôr ak už prehľadal celý
stavový priestor.