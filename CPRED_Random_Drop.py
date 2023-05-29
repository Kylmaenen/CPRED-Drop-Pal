import random
import pprint


#CONSTANTS

FIRSTNAME = [
    "Lindsey" , "Athena" , "Shyann" , "Malik" , "Shae" , "Dalia" , "Reese" , "Christine" , "Dominik" , "Gregory" , "Dyllan", "John" ,
    "Maximus" , "Camron" , "Anyssa" , "Maximiliano" , "Noemi" , "Brandon" , "Kassidy" , "Toshiro" , "Ayden" , "Aniya" , "Rena" , "Marvin" ,
    "Owen" , "Jaiden" , "Gordon" , "Mindy" , "Laurel" , "Grayson" , "Keenan" , "Gunnar" , "Keelan" , "Sydni" , "Matsuda" , "Hernan" , "Tayler" ,
    "Kaylie" , "Blaine" , "Braxton" , "Keira" , "Ayana" , "Aileen" , "Dayna" , "Karah" , "Lena" , "Ezekiel" , "Katelin" , "Kaiden" , "Tobias" ,
    "Jorgen" , "Goethe" , "Mario" , "Claudio" , "Toshi" , "Joey" , "Maria" , "Sax" , "Valerie" , "Wakisaka" ,  "Joji" , "Nobira" , "Morishige" ,
    "Iida" , "Johanne" , "Esmeralda" , "Concita" , "Nagase" , "Misaki" , "Sakura" , "Tsuki" , "Hanako" , "Tomiko" , "Ramiro", "Nagase" , "Isaac" ,
    "Alejandro" , "Mateo" , "Juan" , "Pablo" , "Ximena" , "Gabriele" , "Sara" , "Andrea" , "Enrico" , "Luciano" , "Mercedes" , "Johnny" , "Hardcore" ,
    "Blake" , "Vasilii" , "Artyom" , "Vanya" , "Viktor" , "Ivan" , "Raji" , "Rashid" , "Sued" , "Samir" , "Said" , "Imar" , "Habib" , "Aicha" , "Jane"
    "Maurice" , "Hana" , "Carl" , "Panam" , "Simon" , "Xander" , "Alex" , "Hideki" , "Kuroi" , "Myosaki" , "Jean" , "Petrov" , "Yuan" , "Shaoran" ,
    "Zao" , "Frankie" , "Akame" , "Maylin" , "Mei" , "Sharon" , "Ana" , "Anastasia" , "Fosco" , "Fosca" , "Lin" , "Rebecca" , "Judy" , "Yamir" , "Alisha" 
]

LASTNAME = [
    "Wiater" , "Matches" , "James" , "Donaldson" , "Gill" , "Hamilton" , "McCoy" , "Young" , "Tait" , "Griffin" , "Gardner" , "Garza" , "Gibson" , "Ford" ,
    "Graham" , "Molina" , "Swan" , "Johnson" , "Doe" , "Wolf" , "McGuire" , "Hughes" , "Pilar" , "Carrillo" , "Jimenez" , "Schwartz" , "Schultz" , "Curtis" ,
    "Burton" , "Sato" , "Suzuki" , "Takahashi" , "Tanaka" , "Shibata" , "Maruyama" , "Murata" , "Hirano" , "Lee" , "Wong" , "Yang" , "Chow" , "Son" , "Lopez" , 
    "Garcia" , "Morales" , "Hernandez" , "Pérez" , "De Leòn" , "Rodriguez" , "Alpizar" , "Ivanov" , "Petrovich" , "Sidorov" , "Smirnoff" , "Fedorov" , "Obolensky" ,
    "Chopra" , "Das" , "Deshmukh" , "Gupta" , "Iyer" , "Khan" , "Khatri" , "Patel" , "Popescu" , "Matei" , "Mihai" , "Dumitru" , "Sandu" , "Müller" , "Fischer" , 
    "Wagner" , "Becker" , "Weber" , "Schneider" , "Schmidt" , "Esposito" , "Campolo" , "Frati" , "De Santis" , "Rossi" , "Abara" , "Achebe" , "Adegoke" , "Adisa" ,
    "Mohamed" , "Alì" , "Ahmed" , "Yusuf" , "Issa" , "De Liagre" , "Abadie" , "Bastien" , "Beaubois" , "Beauregard" , "Blanc" , "Charlet" , "Geun" , "Cheon" , "Il-Sam" ,
    "Jong" , "Russell" , "Iosua" , "Kahale" , "Mahoe" , "Kelekolio" , "Kylmänen" , "Tenkula" , "Aalto" , "Andersson" , "Karlsson" , "Welles" , "Goseyun" , "Altaha" , 
    "Shanta" , "Tessay" , "Acoutsina" , "Aariak" , "Nutarak" , "Fox" , "Firebolt" , "Thunder" , "Beastrider" , "Doom" , "Beowulf" , "Montenegro" , "Zazzinga" ,
    "Rapagnetta" , "Pagliacci" , "Rorschach" , "Caccamo" , "Cazzaniga" , "Gold" , "Torini" , "Ghosts" , "Mistrali" , "Peroni" , "Pelagatti" , "Aschenez" , "Black"
]

MELEE = [
	"Nessuna" ,
    "Coltello da combattimento (Leggera) 1d6/CF2, Occultabile" ,
	"Tomahawk (Leggera) 1d6/CF2, Occultabile" ,
	"Rasoio (Leggera) 1d6/CF2, Occultabile" ,
	"Mazza da baseball (Media) 2d6/CF2, Non Occultabile" ,
	"Piede di porco (Media) 2d6/CF2, Non Occultabile" ,
	"Machete (Media) 2d6/CF2, Non Occultabile" ,
	"Tubo di piombo (Pesante) 3d6/CF2, Non Occultabile" ,
	"Spada (Pesante) 3d6/CF2, Non Occultabile",
	"Randello chiodato (Pesante) 3d6/CF2, Non Occultabile" ,
	"Motosega (Molto pesante) 4d6/CF1, Non Occultabile",
	"Martello da demolizione (Molto pesante) 4d6/CF1, Non Occultabile" ,
	"Naginata (Molto pesante) 4d6/CF1, Non Occultabile"
]

WEAPONS = [
    "Nessuna" ,
    "Mezz'arco Arasaka Arms (Standard) 3d6/CF1, Non Occultabile" ,
    "Arco Composito Eagletech Tomcat (Eccellente) 4d6/CF1, Non Occultabile" ,
    "Balestra Eagletech Handbow (Standard) 2d6/CF1, Non Occultabile" ,
    "Balestra Eagletech Stryker (Eccellente) 4d6/CF1, Non Occultabile" ,
    "Pistola M. Arasaka WSA Autopistol (Standard) 2d6/CF2, 16 Colpi, Occultabile" ,
    "Pistola M. Beretta M97P (Eccellente) 2d6/CF2, 18 Colpi, Occultabile" ,
    "Pistola M. BudgetArms C-41 (Standard) 2d6/CF2, 16 Colpi, Occultabile" ,
    "Pistola M. Dai Lung Streetmaster (Scadente) 2d6/CF2, 16 Colpi, Occultabile" ,
    "Pistola P. BudgetArms Auto-3 (Scadente) 3d6/CF2, 8 Colpi, Occultabile (10% possibilità che esploda-2d6)" ,
    "Pistola P. Dai Lung Magnum (Scadente) 3d6/CF2, 8 Colpi, Occultabile (60& possibilità che esploda-2d6)" ,
    "Pistola P. Mustang Arms Mark III (Standard) 3d6/CF2, 20 Colpi, Occultabile" ,
    "Pistola P. Nova Model 338 Citygun (Eccellente) 3d6/CF2, 8 Colpi, Occultabile" ,
    "Pistola M.P. Ameritech Magnum (Eccellente, Smartgun) 4d6/CF1, 6 Colpi, Non Occultabile" ,
    "Pistola M.P. Armalite-44 (Standard) 4d6/CF1, 8 Colpi, Non Occultabile" ,
    "Mitra L. Federated Arms Tech-Assault (Standard) 2d6/CF1, 30 Colpi, Occultabile" ,
    "Mitra L. Heckler&Koch MPK-9 (Standard) 2d6/CF1, 50 Colpi, Occultabile" ,
    "Mitra L. Uzi Miniauto 9 (Standard) 2d6/CF1, 30 Colpi, Occultabile" ,
    "Mitra L. Setsuko-Arasaka PMS (Eccellente, Smartgun) 3d6/CF1, 40 Colpi, Occultabile" ,
    "Mitra M. Arasaka WMA Minami 10 (Eccellente) 2d6/CF1, 40 Colpi, Occultabile" ,
    "Mitra M. Beretta 1010 (Eccellente) 2d6/CF1, 30 Colpi, Occultabile" ,
    "Mitra M. Militech 10 (Standard) 2d6/CF1, 30 Colpi, Occultabile" ,
    "Mitra P. CCMMC Tuzi-7 (Standard) 3d6/CF1, 30 Colpi, Non Occultabile" ,
    "Mitra P. Beretta PM 36 (Standard) 3d6/CF1, 30 Colpi, Non Occultabile" ,
    "Shotgun Constitution Arms Hurricane (Eccellente) 5d6/CF1, 40 Colpi, Non Occultabile" ,
    "Shotgun Arasaka WCAA Rapid Assault Shot 12 (Standard) 5d6/CF1, 20 Colpi, Non Occultabile" ,
    "Shotgun Franchi SPAS-102 (Standard) 5d6/CF1, 8 Colpi, Non Occultabile" ,
    "Shotgun Militech Bulldog (Eccellente) 5d6/CF1, 20 Colpi, Non Occultabile" ,
    "Shotgun Stovolboy 12 MAG (Standard) 5d6/CF1, 20 Colpi, Non Occultabile" ,
    "Shotgun Canne Mozze (Standard) 5d6/CF1, 2/6 Colpi, Non Occultabile" , 
    "F.A. AKR-20 (Standard) 5d6/CF1, 30 Colpi, Non Occultabile" ,
    "F.A. Arasaka WAA Bullpup (Eccellente) 5d6+1/CF1, 30 Colpi, Non Occultabile" ,
    "F.A. Chadran Arms Jungle Reaper (Eccellente) 5d6+1/CF1, 60 Colpi, Lanciagranate 6 Colpi, Non Occultabile" ,
    "F.A. FN-RAL (Standard) 5d6/CF1, 30 Colpi, Non Occultabile" ,
    "F.A. Militech M-31A1 (Standard) 5d6/CF1, 150 Colpi, Lanciagranate CF2 4 Colpi, Non Occultabile" ,
    "F.A. BudgetArms Kiddo47 (Scadente) 5d6, 30 Colpi, Non Occultabile" ,
    "Lanciagranate BudgetArms FRO (Scadente) CF1, 1 Colpo, Non occultabile" ,
    "Lanciagranate Heckler&Koch MGL-4 (Eccellente) CF1, 8 Colpi, Non Occultabile" ,
    "Lanciagranate Constitution Arms M-212 (Eccellente) CF2 (CF1 Se Cambi tipo di Granata) 8 Colpi, Non Occultabile" ,
    "Lanciagranate Militech Cowboy U-55 (Standard) CF3, 12 Colpi, Non Occultabile" ,
    "Lanciamissili CCMMC MSH-85 (Scadente) 8d6/CF1, 1 Colpo, Non Occultabile" ,
    "Lanciamissili Militech RPG-B (Eccellente) 8d6/CF1, 1 Colpo, Non Occultabile" ,
    "F.P. Arasaka WSSA (Eccellente, Smartgun) 5d6/CF1, 40 Colpi, Non Occultabile" ,
    "F.P. Remington 950 (Eccellente) 5d6/CF1, 6 Colpi, Non Occultabile" ,
    "F.P. Stolvoboy Oktober (Eccellente) 5d6/CF1, 30 Colpi, Non Occultabile" ,
]

AMMO = [
    "Nessuna" ,
    "Munizioni Base (Eccetto Missili/Granate)" ,
    "Munizioni Biotossina (Frecce/Granate)" ,
    "Munizioni a Espansione (Frecce/Proiettili/Slug)" ,
    "Munizioni Avvelenate (Frecce/Granate)" ,
    "Munizioni EMP (Granate)" ,
    "Munizioni Flashbang (Granate)" ,
    "Munizioni Fumogene (Granate)" ,
    "Munizioni Incendiarie (Cartucce a Pallini/Frecce/Granate/Proiettili/Slug)" ,
    "Munizioni in Gomma (Frecce/Proiettili/Slug)" ,
    "Munizioni Lacrimogene (Granate)" ,
    "Munizioni Perforanti (Eccetto Cartucce a Pallini)" ,
    "Munizioni Smart (Frecce/Proiettili/Razzi/Slug)" ,
    "Munizioni Soporifere (Frecce e Granate)"
]

GENERIC_EQUIP = [
    "Niente" ,
    "Amplificatore Tascabile" ,
    "Barretta Alimentare" ,
    "Bengala" ,
    "Binocolo" ,
    "Borsone" ,
    "CarePak Personale" ,
    "Cellulare Usa-e-Getta" ,
    "Chip di Memoria" ,
    "Codificatore/Decodificatore" ,
    "Computer" ,
    "Comunicatore Radio" ,
    "Corda (60m)" ,
    "Fiala di Biotossina" ,
    "Fiala di Veleno" ,
    "Geolocalizzatore" ,
    "Letto Gonfiabile e Sacco a Pelo" ,
    "Manette" ,
    "Nastro Isolante" ,
    "Occhiali Intelligenti" ,
    "Pacchetto di Kibble" ,
    "Pistola con Rampino" ,
    "Protezione Auricolare Autolivellante" ,
    "Radio/Lettore Musicale" ,
    "Razione Militare" ,
    "Registratore Audio" ,
    "Respiratore Anti-Smog" ,
    "Rilevatore di Cimici" ,
    "Rilevatore Radar" ,
    "Set di Grimaldelli" ,
    "Tenda ed Equipaggiamento da Campeggio" ,
    "Torcia Chimica" ,
    "Torcia Elettrica" ,
    "Tuta Antiradiazioni" ,
    "Vernice Fosforescente" ,
    "Videocamera" ,
    "Scudo Balistico" ,
]

DRUGS = [
    "Nessuna" ,
    "Berserker" ,
    "Synthcoke" ,
    "Boost" ,
    "Black Lace" ,
    "Timewarp" ,
    "Sixgun" ,
    "Emerald City" ,
    "Prime Time" ,
    "Smash" ,
    "Piranha Smash" ,
    "Blue Glass"
]

PERSONAL = [
    "Niente" ,
    "Coltellino Svizzero" ,
    "Accendino" ,
    "Sigarette" ,
    "Fiche da Poker" ,
    "Sigaro" ,
    "Disegno da Bambino" ,
    "Fazzoletti" ,
    "Anello di Fidanzamento" ,
    "Anello Nuziale" ,
    "Profilattici" ,
    "Visore Braindance" ,
    "Orecchino di Plastica" ,
    "Orecchino d'Argento" ,
    "Orecchino d'Oro" ,
    "Rosario" ,
    "Biglietto della Metro" ,
    "Sigaretta Elettronica" ,
    "Liquido per Sigaretta Elettronica" ,
    "Specchio" ,
    "Dadi a Sei Facce" ,
    "Fiaschetta d'Alcool" ,
    "Armonica" ,
    "Gift Card per Vendit" ,
    "Carte da Gioco" ,
    "Carte di Elflines" ,
    "Miniatura per GDR" ,
    "Pacchetto di Mentine" ,
    "Pezzo di Stoffa Profumato" ,
    "Penna" ,
    "Collana" ,
    "Braindance" ,
    "XBD" , 
    "Filo Interdentale" ,
    "Occhiali Smart" ,
    "Spilla NUSA" ,
    "Biscotto della Fortuna" ,
    "Pacchetto di fiammiferi" ,
    "Biglia" ,
    "Vecchia moneta" ,
    "Fazzoletto Scarabocchiato" ,
    "Gratta-E-Vinci" ,
    "Plettro" ,
    "Latta di Tabacco da fiuto" ,
    "Tabacco da Masticare" ,
    "Tabacco, Cartine e Filtrini" ,
    "Foto di Famiglia" ,
    "Spoletta" ,
    "Fiala di Cianuro" 
]


#DEFINITIONS

mook = {}


def assign_ID():
    random_id = random.choice(FIRSTNAME)+" "+random.choice(LASTNAME)
    mook["ID"] = random_id

def assign_eddies():
    eddies = random.randint(10,500)
    mook["EDDIE"] = eddies

def assign_weapons():
    random_melee = random.choice(MELEE)
    random_weapon_1 = random.choice(WEAPONS)
    random_weapon_2 = random.choice(WEAPONS)
    mook["MELEE"] = random_melee
    mook["ARMA 1"] = random_weapon_1
    mook["ARMA 2"] = random_weapon_2


def assign_ammo():
    random_ammo_1 = random.choice(AMMO)+" "+str(random.randint(1,20))
    random_ammo_2 = random.choice(AMMO)+" "+str(random.randint(1,20))
    mook["MUNIZIONI"] = ([random_ammo_1 , random_ammo_2])


def assign_equip():
    equip_1 = random.choice(GENERIC_EQUIP)
    equip_2 = random.choice(GENERIC_EQUIP)
    equip_3 = random.choice(GENERIC_EQUIP)
    mook["EQUIPAGGIAMENTO"] = ([equip_1 , equip_2 , equip_3])


def assign_drugs():
    drugs = random.choice(DRUGS)
    mook["DROGHE"] = drugs


def assign_personal():
    personal = random.choice(PERSONAL)
    mook["EFFETTI PERSONALI"] = personal

def print_mook_drop():
    pp = pprint.PrettyPrinter(depth=5, width=100, sort_dicts=False)
    pp.pprint(mook)

print("GENERATORE DI GENTE DA DEPREDARE COME I BASTARDI CHE SIETE")

while True:
    mooks = int(input("Numero di booster da depredare: "))
    i = 1
    while i <= mooks :
        i = i+1
        print("/////////////////////////")
        assign_ID()
        assign_eddies()
        assign_weapons()
        assign_ammo()
        assign_equip()
        assign_drugs()
        assign_personal()
        print_mook_drop()
        print("/////////////////////////")
        mook.clear()