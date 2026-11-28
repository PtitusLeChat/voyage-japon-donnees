import json
# Villes : id, nom, japonais, region, lat, lon, ordre, dormir, bases, trajet(h aller), description
V = [
("osaka","Osaka","大阪","Kansai",34.6937,135.5023,10,True,"",0,"Ville gourmande et animée, porte d'entrée par l'aéroport du Kansai."),
("kyoto","Kyoto","京都","Kansai",35.0116,135.7681,20,True,"",0,"Ancienne capitale : temples, jardins et quartiers traditionnels."),
("nara","Nara","奈良","Kansai",34.6851,135.8048,12,False,"kyoto,osaka",0.75,"Daims en liberté et grands temples, idéal en excursion."),
("uji","Uji","宇治","Kansai",34.8844,135.7997,14,False,"kyoto,osaka",0.5,"Ville du thé matcha et du Nintendo Museum."),
("himeji","Himeji","姫路","Kansai",34.8394,134.6939,8,False,"osaka,kyoto,hiroshima",1.0,"Le plus beau château du Japon."),
("hiroshima","Hiroshima","広島","Chugoku",34.3853,132.4553,5,True,"",0,"Ville de la paix et de l'okonomiyaki."),
("miyajima","Miyajima","宮島","Chugoku",34.2960,132.3198,6,False,"hiroshima",0.75,"Île sacrée au torii flottant."),
("naoshima","Naoshima","直島","Setouchi",34.4592,133.9956,7,True,"",0,"Île de l'art contemporain sur la mer intérieure : musées de Tadao Ando, citrouilles de Yayoi Kusama."),
("kanazawa","Kanazawa","金沢","Hokuriku",36.5613,136.6562,30,True,"",0,"Jardins, maisons de thé et feuille d'or."),
("shirakawago","Shirakawa-go","白川郷","Chubu",36.2578,136.9060,32,False,"takayama,kanazawa",1.25,"Village de fermes aux toits de chaume."),
("takayama","Takayama","高山","Chubu",36.1461,137.2522,35,True,"",0,"Vieille ville de montagne en bois."),
("kawaguchiko","Kawaguchiko","河口湖","Mont Fuji",35.5007,138.7690,50,True,"",0,"Lac au pied du mont Fuji."),
("hakone","Hakone","箱根","Kanagawa",35.2324,139.1069,55,True,"",0,"Montagnes, onsen et vues sur le Fuji."),
("kamakura","Kamakura","鎌倉","Kanagawa",35.3192,139.5467,58,False,"tokyo",1.0,"Grand Bouddha et temples en bord de mer."),
("nikko","Nikko","日光","Tochigi",36.7500,139.6000,59,False,"tokyo",2.0,"Sanctuaires dans la forêt et cascades."),
("tokyo","Tokyo","東京","Kanto",35.6762,139.6503,60,True,"",0,"Mégapole : quartiers contrastés, musées immersifs, pop culture."),
("nagoya","Nagoya","名古屋","Aichi",35.1709,136.8815,40,True,"",0,"Grande ville du centre, porte d'entrée du parc Ghibli."),
("nagano","Nagano","長野","Nagano",36.6431,138.1889,45,True,"",0,"Montagnes des Alpes japonaises, temple Zenko-ji et singes des neiges."),
("matsumoto","Matsumoto","松本","Nagano",36.2381,137.9720,43,False,"nagano,takayama",1.0,"Château noir original et vieille ville."),
("kobe","Kobe","神戸","Kansai",34.6901,135.1955,9,False,"osaka,kyoto",0.5,"Port cosmopolite, bœuf de Kobe."),
("koyasan","Koya-san","高野山","Kansai",34.2130,135.5860,11,False,"osaka",2.0,"Montagne sacrée aux 100 temples."),
("yokohama","Yokohama","横浜","Kanagawa",35.4437,139.6380,57,False,"tokyo",0.75,"Port moderne, quartier chinois et musée Cup Noodles."),
("kawagoe","Kawagoe","川越","Saitama",35.9251,139.4858,59,False,"tokyo",0.75,"« Petit Edo » : maisons-entrepôts et ruelle des bonbons."),
("hitachi","Hitachinaka","ひたちなか","Ibaraki",36.3940,140.5340,61,False,"tokyo",1.75,"Parc floral en bord de mer."),
]
# Activités : id, ville, titre, description, categorie, duree, enfant, interieur, lat, lon, reservation, tampon, conseil
A = [
("osaka-dotonbori","osaka","Dotonbori et Namba","Néons, canal et street food (takoyaki, kushikatsu).","QUARTIER",2.5,True,False,34.6687,135.5013,False,False,"Plus spectaculaire à la tombée de la nuit."),
("osaka-chateau","osaka","Château d'Osaka","Donjon-musée et grand parc autour des douves.","MONUMENT",2,True,False,34.6873,135.5262,False,True,""),
("osaka-kaiyukan","osaka","Aquarium Kaiyukan","Un des plus grands aquariums du monde, avec un requin-baleine.","ATTRACTION",3,True,True,34.6545,135.4290,False,False,"Billets en ligne conseillés pour éviter la file."),
("osaka-usj","osaka","Universal Studios Japan","Parc d'attractions avec Super Nintendo World.","ATTRACTION",9,True,False,34.6654,135.4323,True,False,"Super Nintendo World : prévoir un billet daté et un accès à horaire."),
("osaka-shinsekai","osaka","Shinsekai et tour Tsutenkaku","Quartier rétro des années 1920, ambiance populaire.","QUARTIER",2,True,False,34.6525,135.5063,False,False,""),
("osaka-kuromon","osaka","Marché Kuromon","Marché couvert : fruits de mer et en-cas à goûter sur place.","GASTRONOMIE",1.5,True,True,34.6655,135.5068,False,False,"Venir le matin, beaucoup d'étals ferment tôt."),
("osaka-umeda-sky","osaka","Umeda Sky Building","Observatoire en plein air entre deux tours.","VUE",1.5,True,True,34.7053,135.4906,False,False,"Magnifique au coucher du soleil."),
("osaka-cupnoodles","osaka","Musée Cup Noodles (Ikeda)","Créer et décorer son propre pot de nouilles.","MUSEE",2,True,True,34.8197,135.4269,True,False,"À 30 min du centre ; certains ateliers se réservent."),
("osaka-sumiyoshi","osaka","Sanctuaire Sumiyoshi Taisha","Un des plus anciens sanctuaires, pont rouge en arc.","TEMPLE",1.5,True,False,34.6124,135.4930,False,True,""),
("kyoto-fushimi","kyoto","Fushimi Inari","Des milliers de torii orange sur la montagne.","TEMPLE",2.5,True,False,34.9671,135.7727,False,True,"Arriver tôt le matin pour éviter la foule."),
("kyoto-kinkakuji","kyoto","Kinkaku-ji, le Pavillon d'or","Pavillon recouvert de feuille d'or au bord d'un étang.","TEMPLE",1,True,False,35.0394,135.7292,False,True,""),
("kyoto-arashiyama","kyoto","Arashiyama et bambouseraie","Forêt de bambous, pont Togetsukyo et temple Tenryu-ji.","NATURE",3,True,False,35.0170,135.6713,False,True,"La bambouseraie est plus calme avant 8 h."),
("kyoto-monkey","kyoto","Parc aux singes d'Iwatayama","Montée de 20 min pour approcher des macaques et voir Kyoto d'en haut.","NATURE",1.5,True,False,35.0094,135.6773,False,False,"À combiner avec Arashiyama."),
("kyoto-kiyomizu","kyoto","Kiyomizu-dera et Sannenzaka","Temple sur pilotis et ruelles pavées commerçantes.","TEMPLE",2.5,True,False,34.9949,135.7850,False,True,""),
("kyoto-gion","kyoto","Gion, quartier des geishas","Maisons de thé en bois et ruelle Hanamikoji.","QUARTIER",2,False,False,35.0037,135.7750,False,False,"En fin de journée ; ne pas photographier les geiko de près."),
("kyoto-nishiki","kyoto","Marché Nishiki","« La cuisine de Kyoto » : 400 m d'étals couverts.","GASTRONOMIE",1.5,True,True,35.0050,135.7649,False,False,""),
("kyoto-ginkakuji","kyoto","Ginkaku-ji et chemin de la philosophie","Pavillon d'argent, jardin de sable et balade le long d'un canal.","TEMPLE",2.5,False,False,35.0270,135.7982,False,True,""),
("kyoto-kimono","kyoto","Balade en kimono","Location de kimono pour la journée dans le vieux Kyoto.","EXPERIENCE",3,True,False,34.9980,135.7800,True,False,"Réserver la location ; tailles enfant disponibles."),
("kyoto-the","kyoto","Cérémonie du thé","Initiation au rituel du thé matcha.","EXPERIENCE",1,True,True,35.0030,135.7760,True,False,""),
("kyoto-railway","kyoto","Musée du chemin de fer","Shinkansen, locomotives à vapeur et simulateurs.","MUSEE",2.5,True,True,34.9871,135.7427,False,False,"Idéal par temps de pluie."),
("kyoto-manga","kyoto","Musée international du manga","Des milliers de mangas à lire sur place.","MUSEE",2,True,True,35.0117,135.7594,False,False,""),
("kyoto-toei","kyoto","Toei Kyoto Studio Park","Décors de films d'époque, spectacles de ninjas et samouraïs.","ATTRACTION",3,True,False,35.0164,135.7091,False,False,""),
("kyoto-nijo","kyoto","Château de Nijo","Résidence du shogun aux parquets « rossignol » qui chantent.","MONUMENT",1.5,True,True,35.0142,135.7480,False,True,""),
("nara-parc","nara","Parc de Nara et ses daims","Plus de 1 000 daims en liberté qui saluent pour des biscuits.","NATURE",2,True,False,34.6851,135.8430,False,False,"Ranger cartes et papiers : les daims les mangent."),
("nara-todaiji","nara","Todai-ji, le grand Bouddha","Immense statue en bronze dans un gigantesque bâtiment en bois.","TEMPLE",1.5,True,True,34.6890,135.8398,False,True,"Passer dans le trou du pilier porterait chance."),
("nara-kasuga","nara","Kasuga Taisha","Sanctuaire aux milliers de lanternes.","TEMPLE",1,True,False,34.6813,135.8484,False,True,""),
("uji-byodoin","uji","Byodo-in","Le pavillon du Phénix, gravé sur la pièce de 10 yens.","TEMPLE",1.5,True,False,34.8892,135.8077,False,True,""),
("uji-nintendo","uji","Nintendo Museum","Histoire de Nintendo et jeux interactifs géants.","MUSEE",3,True,True,34.8907,135.7843,True,False,"Billets par tirage au sort sur le site officiel, environ 3 mois avant la visite (compte Nintendo requis)."),
("uji-matcha","uji","Dégustation de matcha","Maisons de thé historiques le long de la rivière Uji.","GASTRONOMIE",1,True,True,34.8890,135.8050,False,False,""),
("himeji-chateau","himeji","Château de Himeji","Le « Héron blanc », château original classé à l'UNESCO.","MONUMENT",2.5,True,False,34.8394,134.6939,False,True,"Beaucoup d'escaliers raides à l'intérieur."),
("hiroshima-memorial","hiroshima","Mémorial et musée de la Paix","Parc, dôme de Genbaku et musée sur la bombe atomique.","MUSEE",2.5,False,True,34.3915,132.4536,False,True,"Certaines salles sont éprouvantes : à préparer avec un enfant."),
("hiroshima-okonomiyaki","hiroshima","Okonomimura","Immeuble entier de comptoirs d'okonomiyaki.","GASTRONOMIE",1,True,True,34.3920,132.4610,False,False,""),
("hiroshima-chateau","hiroshima","Château de Hiroshima","Château reconstruit, musée sur les samouraïs.","MONUMENT",1,True,True,34.4027,132.4594,False,True,""),
("miyajima-itsukushima","miyajima","Sanctuaire d'Itsukushima","Le célèbre torii qui semble flotter à marée haute.","TEMPLE",2,True,False,34.2959,132.3199,False,True,"Vérifier les horaires des marées : à marée basse on marche jusqu'au torii."),
("miyajima-misen","miyajima","Mont Misen","Téléphérique et randonnée jusqu'au sommet, vue sur la mer intérieure.","NATURE",3,True,False,34.2794,132.3197,False,True,""),
("naoshima-chichu","naoshima","Chichu Art Museum","Musée enterré de Tadao Ando : Monet, James Turrell, Walter De Maria.","MUSEE",2,True,True,34.4497,133.9908,True,False,"Billet à heure fixe à réserver en ligne ; fermé le lundi (vérifier le calendrier)."),
("naoshima-benesse","naoshima","Benesse House Museum et citrouille jaune","Musée au bord de l'eau et la citrouille de Yayoi Kusama sur le ponton.","MUSEE",2,True,False,34.4540,133.9950,False,False,"Navette gratuite depuis Tsutsuji-so ; fermé certains lundis."),
("naoshima-honmura","naoshima","Art House Project (Honmura)","Maisons du vieux village transformées en œuvres d'art.","QUARTIER",2,True,False,34.4625,134.0095,False,False,"Billet combiné en vente à Honmura ; certaines maisons demandent un créneau."),
("kanazawa-kenrokuen","kanazawa","Jardin Kenroku-en","Un des trois plus beaux jardins du Japon.","NATURE",1.5,True,False,36.5621,136.6627,False,False,""),
("kanazawa-higashi","kanazawa","Higashi Chaya","Quartier de maisons de thé ; glaces à la feuille d'or.","QUARTIER",1.5,True,False,36.5726,136.6667,False,False,""),
("kanazawa-21","kanazawa","Musée d'art du 21e siècle","Art contemporain ludique, dont la célèbre « piscine ».","MUSEE",2,True,True,36.5609,136.6582,False,False,""),
("kanazawa-omicho","kanazawa","Marché Omicho","Marché aux poissons et bols de fruits de mer.","GASTRONOMIE",1,True,True,36.5715,136.6564,False,False,""),
("kanazawa-ninja","kanazawa","Myoryu-ji, le temple des ninjas","Pièges, passages secrets et escaliers cachés.","TEMPLE",1,True,True,36.5544,136.6510,True,True,"Visite guidée uniquement, sur réservation."),
("shirakawago-village","shirakawago","Village de Shirakawa-go","Fermes gassho aux grands toits de chaume, classées UNESCO.","QUARTIER",3,True,False,36.2578,136.9060,False,False,"Bus depuis Takayama ou Kanazawa : réserver le trajet."),
("takayama-sanmachi","takayama","Vieille ville Sanmachi Suji","Rues de maisons marchandes en bois et brasseries de saké.","QUARTIER",2,True,False,36.1410,137.2600,False,False,""),
("takayama-marche","takayama","Marché du matin Miyagawa","Marché le long de la rivière : fruits, pickles, artisanat.","GASTRONOMIE",1,True,False,36.1460,137.2590,False,False,"Le matin uniquement."),
("takayama-hidanosato","takayama","Hida no Sato","Village-musée de maisons traditionnelles de montagne.","MUSEE",2,True,False,36.1340,137.2390,False,False,""),
("hakone-boucle","hakone","Boucle de Hakone","Train de montagne, téléphérique, Owakudani et bateau pirate sur le lac Ashi.","EXPERIENCE",6,True,False,35.2440,139.0210,False,True,"Le Hakone Free Pass couvre la boucle."),
("hakone-openair","hakone","Musée en plein air de Hakone","Sculptures géantes dans un parc, structures à escalader pour les enfants.","MUSEE",2.5,True,False,35.2447,139.0510,False,False,""),
("hakone-onsen","hakone","Bain en onsen","Sources chaudes en ryokan ou bains publics.","EXPERIENCE",2,True,True,35.2330,139.1050,False,False,"Les tatouages peuvent être refusés ; privilégier un bain privatif."),
("kawaguchiko-chureito","kawaguchiko","Pagode Chureito","La vue de carte postale : pagode rouge et mont Fuji.","VUE",2,True,False,35.5013,138.8018,False,True,"Près de 400 marches ; le Fuji est souvent caché en juin."),
("kawaguchiko-lac","kawaguchiko","Tour du lac Kawaguchi","Vélo, téléphérique Kachi Kachi et bords du lac.","NATURE",3,True,False,35.5170,138.7550,False,False,""),
("kawaguchiko-fujiq","kawaguchiko","Fuji-Q Highland","Parc aux montagnes russes records.","ATTRACTION",6,True,False,35.4870,138.7800,False,False,"Vérifier les tailles minimales des attractions."),
("tokyo-sensoji","tokyo","Senso-ji et Nakamise (Asakusa)","Plus ancien temple de Tokyo et allée de boutiques.","TEMPLE",2,True,False,35.7148,139.7967,False,True,""),
("tokyo-shibuya","tokyo","Carrefour de Shibuya et Hachiko","Le passage piéton le plus célèbre du monde.","QUARTIER",1.5,True,False,35.6595,139.7005,False,False,""),
("tokyo-shibuyasky","tokyo","Shibuya Sky","Toit-terrasse vitré à 230 m au-dessus de Shibuya.","VUE",1.5,True,True,35.6584,139.7022,True,False,"Réserver le créneau du coucher de soleil plusieurs semaines avant."),
("tokyo-harajuku","tokyo","Harajuku et sanctuaire Meiji","Rue Takeshita colorée puis forêt du sanctuaire Meiji.","QUARTIER",3,True,False,35.6716,139.7031,False,True,""),
("tokyo-teamlab-planets","tokyo","teamLab Planets (Toyosu)","Musée immersif où l'on marche pieds nus dans l'eau et la lumière.","MUSEE",2,True,True,35.6491,139.7898,True,False,"Ouvert jusqu'à fin 2027 ; billets à horaire."),
("tokyo-teamlab-borderless","tokyo","teamLab Borderless (Azabudai Hills)","Œuvres numériques sans frontières qui se déplacent de salle en salle.","MUSEE",2.5,True,True,35.6604,139.7404,True,False,"Billets à horaire."),
("tokyo-ghibli","tokyo","Musée Ghibli (Mitaka)","L'univers de Miyazaki, court-métrage exclusif.","MUSEE",2.5,True,True,35.6962,139.5704,True,False,"Billets en vente environ un mois avant, partent très vite."),
("tokyo-harrypotter","tokyo","Studio Tour Harry Potter","Décors et costumes des films (Warner Bros. Studio Tour Tokyo).","ATTRACTION",4,True,True,35.7442,139.6466,True,False,"Billets datés à réserver."),
("tokyo-disneysea","tokyo","Tokyo DisneySea","Parc Disney unique au monde, très apprécié des familles.","ATTRACTION",10,True,False,35.6267,139.8851,True,False,"Billet daté à acheter en ligne."),
("tokyo-disneyland","tokyo","Tokyo Disneyland","Le parc Disney classique.","ATTRACTION",10,True,False,35.6329,139.8804,True,False,"Billet daté à acheter en ligne."),
("tokyo-akihabara","tokyo","Akihabara","Jeux vidéo, manga, salles d'arcade.","SHOPPING",2.5,True,True,35.6984,139.7731,False,False,""),
("tokyo-pokemon","tokyo","Pokémon Center Mega Tokyo","La grande boutique Pokémon (Ikebukuro).","SHOPPING",1,True,True,35.7289,139.7193,False,False,""),
("tokyo-tsukiji","tokyo","Marché extérieur de Tsukiji","Sushis, omelette tamagoyaki et brochettes de la mer.","GASTRONOMIE",1.5,True,False,35.6655,139.7707,False,False,"Le matin."),
("tokyo-ueno","tokyo","Parc et zoo d'Ueno","Grand parc, musées et zoo.","NATURE",3,True,False,35.7156,139.7731,False,False,""),
("tokyo-skytree","tokyo","Tokyo Skytree","La plus haute tour du Japon (634 m).","VUE",1.5,True,True,35.7101,139.8107,False,False,""),
("tokyo-odaiba","tokyo","Odaiba","Île artificielle : Gundam géant, front de mer, centres de loisirs.","QUARTIER",3,True,False,35.6247,139.7757,False,False,""),
("tokyo-miraikan","tokyo","Miraikan","Musée des sciences et des robots.","MUSEE",2.5,True,True,35.6190,139.7766,False,False,"Parfait un jour de pluie."),
("tokyo-shinjuku-gyoen","tokyo","Jardin Shinjuku Gyoen","Grand jardin aux styles japonais, anglais et français.","NATURE",1.5,True,False,35.6852,139.7101,False,False,""),
("tokyo-shinjuku-soir","tokyo","Shinjuku le soir","Ruelles d'Omoide Yokocho, néons et tête de Godzilla.","QUARTIER",2,True,False,35.6938,139.6995,False,False,"En début de soirée avec un enfant."),
("tokyo-sumo","tokyo","Entraînement de sumo","Assister à l'entraînement matinal d'une écurie de sumo.","EXPERIENCE",2,True,True,35.6969,139.7932,True,False,"Pas de tournoi à Tokyo en juin : passer par une visite réservée."),
("tokyo-cuisine","tokyo","Cours de cuisine japonaise","Préparer sushis ou bento en famille.","EXPERIENCE",3,True,True,35.6812,139.7671,True,False,""),
("kamakura-daibutsu","kamakura","Grand Bouddha de Kamakura","Bouddha en bronze de 13 m, en plein air.","TEMPLE",1,True,False,35.3169,139.5359,False,True,""),
("kamakura-hasedera","kamakura","Hase-dera","Temple à flanc de colline, célèbre pour ses hortensias en juin.","TEMPLE",1.5,True,False,35.3123,139.5334,False,True,"Pleine floraison des hortensias en juin : affluence."),
("kamakura-enoshima","kamakura","Île d'Enoshima","Île avec grottes, sanctuaires et phare.","NATURE",3,True,False,35.2995,139.4800,False,True,""),
("nikko-toshogu","nikko","Sanctuaire Toshogu","Sanctuaire richement décoré, singes de la sagesse.","TEMPLE",2.5,True,False,36.7580,139.5988,False,True,""),
("nikko-kegon","nikko","Chutes de Kegon et lac Chuzenji","Cascade de 97 m et lac de montagne.","NATURE",3,True,False,36.7383,139.5025,False,False,""),
("nikko-edo","nikko","Edo Wonderland","Village d'époque Edo avec ninjas, samouraïs et spectacles.","ATTRACTION",4,True,False,36.8060,139.7130,False,False,""),
("nagoya-ghibli","nagoya","Parc Ghibli (Nagakute)","Les univers de Totoro, Mononoké, Kiki… dont le Grand Entrepôt.","ATTRACTION",6,True,False,35.1720,137.0870,True,False,"Aucun billet vendu sur place : vente en ligne (Lawson Ticket ou Klook) 2 mois avant, le 10 à 14 h heure japonaise. Pour juin 2027 : le 10 avril 2027. Linimo depuis Fujigaoka."),
("nagoya-scmaglev","nagoya","SCMAGLEV and Railway Park","Musée des trains : Shinkansen, train à sustentation magnétique, simulateurs.","MUSEE",3,True,True,35.0475,136.8513,False,False,"Idéal par temps de pluie."),
("nagoya-legoland","nagoya","Legoland Japan","Parc Lego : attractions et Miniland du Japon en briques.","ATTRACTION",6,True,False,35.0503,136.8434,False,False,"Plutôt pour les moins de 12 ans."),
("nagoya-chateau","nagoya","Château de Nagoya","Château aux dauphins dorés et palais Honmaru.","MONUMENT",1.5,True,False,35.1856,136.8999,False,True,""),
("nagoya-osu","nagoya","Quartier d'Osu","Galeries commerçantes, street food et temple Osu Kannon.","QUARTIER",2,True,False,35.1590,136.9010,False,True,""),
("nagoya-atsuta","nagoya","Atsuta Jingu","Grand sanctuaire dans une forêt de camphriers.","TEMPLE",1,True,False,35.1279,136.9087,False,True,""),
("nagano-zenkoji","nagano","Temple Zenko-ji","Grand temple : passage dans le noir sous l'autel pour trouver la « clé du paradis ».","TEMPLE",2,True,False,36.6617,138.1876,False,True,""),
("nagano-singes","nagano","Singes de Jigokudani","Macaques qui se baignent dans les sources chaudes (présents toute l'année).","NATURE",5,True,False,36.7326,138.4622,False,False,"Bus depuis Nagano puis 30 min de marche en forêt ; en juin les singes vont moins dans l'eau."),
("nagano-togakushi","nagano","Togakushi","Allée de cèdres géants, sanctuaire et musée ninja.","NATURE",5,True,False,36.7413,138.0870,False,True,"Bus depuis la gare de Nagano (~1 h)."),
("matsumoto-chateau","matsumoto","Château de Matsumoto","Un des rares châteaux d'origine, surnommé le « château du corbeau ».","MONUMENT",1.5,True,True,36.2386,137.9689,False,True,""),
("matsumoto-nakamachi","matsumoto","Nakamachi et Nawate","Rues d'entrepôts blancs et allée des grenouilles.","QUARTIER",1.5,True,False,36.2340,137.9710,False,False,""),
("kobe-boeuf","kobe","Déguster le bœuf de Kobe","Teppanyaki de bœuf de Kobe.","GASTRONOMIE",1.5,True,True,34.6913,135.1955,True,False,"Réserver, surtout le soir."),
("kobe-harborland","kobe","Harborland et port de Kobe","Promenade, grande roue et Kobe Port Tower.","QUARTIER",2,True,False,34.6795,135.1850,False,False,""),
("kobe-kitano","kobe","Kitano Ijinkan","Anciennes maisons des marchands étrangers sur la colline.","QUARTIER",2,False,False,34.7000,135.1910,False,False,""),
("kobe-animal","kobe","Kobe Animal Kingdom","Parc animalier couvert : capybaras, oiseaux, kangourous.","ATTRACTION",3,True,True,34.6580,135.2230,False,False,"Parfait un jour de pluie."),
("koyasan-okunoin","koyasan","Cimetière Okunoin","Forêt de cèdres et 200 000 tombes jusqu'au mausolée de Kobo Daishi.","TEMPLE",2,False,False,34.2190,135.6030,False,True,""),
("koyasan-kongobuji","koyasan","Temple Kongobu-ji","Siège du bouddhisme Shingon et grand jardin de pierres.","TEMPLE",1,False,True,34.2130,135.5840,False,True,""),
("yokohama-cupnoodles","yokohama","Musée Cup Noodles de Yokohama","Créer son pot de nouilles et parcourir l'histoire des ramen instantanés.","MUSEE",2,True,True,35.4555,139.6385,False,False,""),
("yokohama-chinatown","yokohama","Quartier chinois de Yokohama","Le plus grand quartier chinois du Japon, brioches à la vapeur.","GASTRONOMIE",2,True,False,35.4423,139.6458,False,False,""),
("yokohama-minatomirai","yokohama","Minato Mirai","Front de mer, grande roue Cosmo World et entrepôts en briques rouges.","QUARTIER",2,True,False,35.4560,139.6380,False,False,""),
("kawagoe-vieille-ville","kawagoe","Vieille ville de Kawagoe","Maisons-entrepôts kurazukuri, tour de la cloche et ruelle des bonbons.","QUARTIER",3,True,False,35.9246,139.4840,False,True,""),
("tokyo-pokemon-cafe","tokyo","Pokémon Café Tokyo","Plats et desserts Pokémon, visite de Pikachu, à côté du Pokémon Center DX (Nihonbashi).","EXPERIENCE",1.5,True,True,35.6810,139.7740,True,False,"Uniquement sur réservation en ligne."),
("osaka-pokemon-cafe","osaka","Pokémon Café Osaka","Café Pokémon au 9e étage du Daimaru Shinsaibashi, avec le Pokémon Center.","EXPERIENCE",1.5,True,True,34.6740,135.5010,True,False,"Uniquement sur réservation en ligne."),
("tokyo-kirby-cafe","tokyo","Kirby Café Tokyo","Café Kirby au pied de la Skytree (Solamachi, 4e étage).","EXPERIENCE",1.5,True,True,35.7100,139.8120,True,False,"Réservation obligatoire : compte et vérification par téléphone à prévoir."),
("hitachi-seaside","hitachi","Parc Hitachi Seaside","Immense parc floral en bord de mer, grande roue et parc d'attractions.","NATURE",4,True,False,36.4038,140.5940,False,False,"En juin : roses, fleurs d'été et kochias encore vertes ; les némophiles bleues fleurissent au printemps."),
]
villes=[dict(id=a,nom=b,nomJaponais=c,region=d,lat=e,lon=f,ordre=g,dormirSurPlace=h,bases=i,trajetH=j,description=k) for a,b,c,d,e,f,g,h,i,j,k in V]
# Terme de recherche de la photo de chaque ville (« Kobe » seul donnait la photo de Kobe Bryant)
PHOTOS_VILLES = {"osaka":"Osaka","kyoto":"Kyoto","nara":"Nara (ville)","uji":"Uji (Kyoto)","himeji":"Château de Himeji",
 "hiroshima":"Hiroshima","miyajima":"Itsukushima-jinja","naoshima":"Naoshima","kanazawa":"Kanazawa","shirakawago":"Shirakawa-gō",
 "takayama":"Takayama (Gifu)","kawaguchiko":"Lac Kawaguchi","hakone":"Hakone","kamakura":"Kamakura","nikko":"Nikkō",
 "tokyo":"Tokyo","nagoya":"Nagoya","nagano":"Nagano (ville)","matsumoto":"Château de Matsumoto","kobe":"Kōbe",
 "koyasan":"Kōya-san","yokohama":"Yokohama","kawagoe":"Kawagoe (Saitama)","hitachi":"Parc maritime national de Hitachi"}
for v in villes: v["photo"] = PHOTOS_VILLES[v["id"]]
ids={v["id"] for v in villes}
acts=[]
for t in A:
    a=dict(zip(["id","villeId","titre","description","categorie","dureeH","enfant","interieur","lat","lon","reservation","tampon","conseil"],t))
    assert a["villeId"] in ids, a
    acts.append(a)
assert len({a["id"] for a in acts})==len(acts)
cats={a["categorie"] for a in acts}; print(cats, len(villes), len(acts))
ACCES = {
 "nara":"Depuis Kyoto : JR Nara Line (~45 min). Depuis Osaka : Kintetsu (~40 min).",
 "uji":"Depuis Kyoto : JR Nara Line jusqu'à Uji (~20 min). Nintendo Museum : Kintetsu jusqu'à Ogura (~20 min).",
 "himeji":"Shinkansen depuis Shin-Osaka (~30 min) ou JR Special Rapid depuis Osaka (~1 h).",
 "miyajima":"JR depuis Hiroshima jusqu'à Miyajimaguchi (~30 min), puis ferry (~10 min).",
 "naoshima":"Shinkansen jusqu'à Okayama, JR Uno Line jusqu'à Uno (~55 min, parfois changement à Chayamachi), puis ferry pour Miyanoura (~20 min, environ toutes les heures).",
 "shirakawago":"Bus Nohi depuis Takayama (~50 min) ou Kanazawa (~1 h 15), à réserver.",
 "kamakura":"JR Yokosuka Line depuis Tokyo (~1 h).",
 "nikko":"Tobu Limited Express depuis Asakusa (~2 h), ou Shinkansen jusqu'à Utsunomiya puis JR Nikko Line.",
 "matsumoto":"Express Shinano depuis Nagano (~50 min) ; bus depuis Takayama (~2 h 30).",
 "kobe":"JR depuis Osaka (~25 min) ou Kyoto (~50 min).",
 "koyasan":"Nankai depuis Namba jusqu'à Gokurakubashi, puis funiculaire et bus (~2 h).",
 "yokohama":"JR ou Tokyu depuis Tokyo / Shibuya (~30-40 min).",
 "kawagoe":"Tobu Tojo Line depuis Ikebukuro (~30 min).",
 "hitachi":"Train jusqu'à Katsuta (~1 h 15 depuis Shinagawa), puis bus jusqu'au parc (~15-20 min).",
}
for v in villes: v["acces"]=ACCES.get(v["id"],"")
ROUTES = [
 ("osaka","kyoto","JR Special Rapid (~30 min) ou Shinkansen depuis Shin-Osaka (~15 min)."),
 ("osaka","tokyo","Shinkansen Nozomi depuis Shin-Osaka (~2 h 30)."),
 ("kyoto","tokyo","Shinkansen Nozomi (~2 h 15)."),
 ("hiroshima","kyoto","Shinkansen (~1 h 40)."),
 ("hiroshima","osaka","Shinkansen jusqu'à Shin-Osaka (~1 h 25)."),
 ("hiroshima","tokyo","Shinkansen (~4 h)."),
 ("kanazawa","kyoto","Thunderbird jusqu'à Tsuruga puis Hokuriku Shinkansen (~2 h 10)."),
 ("kanazawa","osaka","Thunderbird jusqu'à Tsuruga puis Hokuriku Shinkansen (~2 h 40)."),
 ("kanazawa","tokyo","Hokuriku Shinkansen (~2 h 30)."),
 ("kanazawa","nagano","Hokuriku Shinkansen (~1 h)."),
 ("kanazawa","takayama","Bus via Shirakawa-go (~2 h 15), à réserver."),
 ("nagoya","takayama","Express Hida (~2 h 30)."),
 ("kyoto","nagoya","Shinkansen (~35 min)."),
 ("nagoya","osaka","Shinkansen depuis Shin-Osaka (~50 min)."),
 ("nagoya","tokyo","Shinkansen Nozomi (~1 h 40)."),
 ("nagano","nagoya","Express Shinano (~3 h)."),
 ("nagano","tokyo","Hokuriku Shinkansen (~1 h 30)."),
 ("nagano","takayama","Bus jusqu'à Matsumoto puis express Shinano (~3 h 30)."),
 ("hakone","tokyo","Romancecar depuis Shinjuku jusqu'à Hakone-Yumoto (~1 h 30) ou Shinkansen jusqu'à Odawara (~35 min)."),
 ("kawaguchiko","tokyo","Bus express ou train Fuji Excursion depuis Shinjuku (~2 h)."),
 ("hakone","kawaguchiko","Bus via Gotemba (~2 h)."),
 ("hakone","kyoto","Shinkansen Hikari jusqu'à Odawara (~2 h), puis train vers Hakone-Yumoto."),
 ("hakone","osaka","Shinkansen Hikari jusqu'à Odawara (~2 h 15), puis train vers Hakone-Yumoto."),
 ("hakone","nagoya","Shinkansen Hikari jusqu'à Odawara (~1 h 15), puis train vers Hakone-Yumoto."),
 ("kawaguchiko","nagoya","Shinkansen jusqu'à Mishima puis bus (~3 h)."),
]
routes=[dict(a=min(a,b),b=max(a,b),texte=t) for a,b,t in ROUTES]
for r in routes: assert r["a"] in ids and r["b"] in ids, r
AEROPORTS = {
 "KIX":{"osaka":"JR Haruka ou JR Kansai Airport Rapid (🎫 JR Pass ou carte IC ICOCA/Suica) ; ou train Nankai rapi:t vers Namba (🎫 billet Nankai ou carte IC, JR Pass non valable) (~40-50 min).",
        "kyoto":"JR Haruka direct jusqu'à Kyoto (~1 h 20) (🎫 JR Pass, pass ICOCA & Haruka ou carte IC)."},
 "HND":{"tokyo":"Tokyo Monorail (🎫 carte IC ; JR Pass accepté) ou Keikyu (🎫 carte IC) jusqu'au centre (~30 min)."},
}
# Infos à l'arrivée au Japon : retrait des pass et cartes IC, plan de l'aéroport
ARRIVEES = {
 "KIX": {
  "titre": "Retrait du JR Pass et des cartes IC",
  "texte": "Après la douane (1er étage, arrivées internationales), montez au 2e étage du Terminal 1 et traversez la passerelle vers la gare « Kansai-airport Station ». Côté JR (en bleu, pas Nankai en rouge) : guichet JR West « Midori-no-madoguchi » (panneau vert), ouvert de 5 h 30 à 23 h, avec du personnel parlant anglais. Présentez les bons d'échange du JR Pass et les passeports de toute la famille, et indiquez la date de début souhaitée. On y achète aussi le pass « ICOCA & Haruka » (carte IC + train vers Osaka/Kyoto). La carte IC enfant (tarif réduit pour votre fille) s'achète au guichet avec son passeport. Prévoir de la file aux heures d'arrivée des vols.",
  "plan": "https://www.kansai-airport.or.jp/en/map",
  "planPdf": "https://www.kansai-airport.or.jp/sites/default/files/2019-06/MAPen01.pdf"
 }
}

# ---------------------------------------------------------------------------
# Lot 7 : détail des trajets (tronçons) — ligne, gares en japonais, direction, arrêts, durée, JR Pass, prix adulte
# Prix indicatifs 2026 (place réservée, adulte) ; enfant 6-11 ans = moitié. « jr » : oui / non / supplement (Nozomi).
# Un tronçon est décrit dans un sens ; l'appli l'inverse pour le retour.
# ---------------------------------------------------------------------------
def T(m,l,lj,d,dj,a,aj,t,jr,p,n=None,dir=None,dirj=None,dirR=None,dirRj=None,note=""):
    o=dict(m=m,l=l,lj=lj,d=d,dj=dj,a=a,aj=aj,t=t,jr=jr,p=p,note=note)
    if n is not None: o["n"]=n
    o["dir"]=dir or a; o["dirj"]=dirj or aj
    o["dirR"]=dirR or d; o["dirRj"]=dirRj or dj
    return o
SK="shinkansen"; TR="train"; BUS="bus"; BAT="bateau"
NOZOMI_NOTE="Avec le JR Pass : prendre une Hikari (ひかり), sans supplément, ou payer le supplément Nozomi."
TRONCONS = {
 "osaka>kyoto":[T(TR,"JR Special Rapid (Shinkaisoku)","JR 新快速","Osaka","大阪","Kyoto","京都",29,"oui",580,n=2,dir="Kyoto / Maibara",dirj="京都・米原方面",dirR="Osaka / Sannomiya",dirRj="大阪・三ノ宮方面")],
 "osaka>tokyo":[T(SK,"Tokaido Shinkansen Nozomi","東海道新幹線 のぞみ","Shin-Osaka","新大阪","Tokyo","東京",150,"supplement",14720,n=4,note=NOZOMI_NOTE)],
 "kyoto>tokyo":[T(SK,"Tokaido Shinkansen Nozomi","東海道新幹線 のぞみ","Kyoto","京都","Tokyo","東京",135,"supplement",14170,n=3,dirR="Shin-Osaka",dirRj="新大阪",note=NOZOMI_NOTE)],
 "kyoto>hiroshima":[T(SK,"Sanyo Shinkansen Nozomi","山陽新幹線 のぞみ","Kyoto","京都","Hiroshima","広島",96,"supplement",11740,n=3,dir="Hiroshima / Hakata",dirj="広島・博多方面",dirR="Shin-Osaka / Tokyo",dirRj="新大阪・東京方面",note=NOZOMI_NOTE)],
 "osaka>hiroshima":[T(SK,"Sanyo Shinkansen Sakura / Nozomi","山陽新幹線 さくら・のぞみ","Shin-Osaka","新大阪","Hiroshima","広島",85,"oui",10620,n=2,dir="Hiroshima / Hakata",dirj="広島・博多方面",note="La Sakura (さくら) est couverte par le JR Pass ; la Nozomi demande un supplément.")],
 "tokyo>hiroshima":[T(SK,"Tokaido-Sanyo Shinkansen Nozomi","東海道・山陽新幹線 のぞみ","Tokyo","東京","Hiroshima","広島",240,"supplement",19760,n=7,dir="Hiroshima / Hakata",dirj="広島・博多方面",note=NOZOMI_NOTE)],
 "kyoto>kanazawa":[T(TR,"Limited Express Thunderbird","特急サンダーバード","Kyoto","京都","Tsuruga","敦賀",55,"oui",3700,dir="Tsuruga",dirj="敦賀"),
                   T(SK,"Hokuriku Shinkansen Tsurugi / Kagayaki","北陸新幹線 つるぎ・かがやき","Tsuruga","敦賀","Kanazawa","金沢",45,"oui",3900,dir="Kanazawa / Tokyo",dirj="金沢・東京方面",note="Correspondance à Tsuruga : changer de quai (même gare, ~10 min).")],
 "osaka>kanazawa":[T(TR,"Limited Express Thunderbird","特急サンダーバード","Osaka","大阪","Tsuruga","敦賀",80,"oui",5200,dir="Tsuruga",dirj="敦賀"),
                   T(SK,"Hokuriku Shinkansen Tsurugi / Kagayaki","北陸新幹線 つるぎ・かがやき","Tsuruga","敦賀","Kanazawa","金沢",45,"oui",3900,dir="Kanazawa / Tokyo",dirj="金沢・東京方面",note="Correspondance à Tsuruga : changer de quai (même gare, ~10 min).")],
 "tokyo>kanazawa":[T(SK,"Hokuriku Shinkansen Kagayaki","北陸新幹線 かがやき","Tokyo","東京","Kanazawa","金沢",150,"oui",14700,n=4,note="Kagayaki : toutes les places sont réservées.")],
 "nagano>kanazawa":[T(SK,"Hokuriku Shinkansen Kagayaki / Hakutaka","北陸新幹線 かがやき・はくたか","Nagano","長野","Kanazawa","金沢",65,"oui",8970,n=1,dir="Kanazawa / Tsuruga",dirj="金沢・敦賀方面",dirR="Tokyo",dirRj="東京")],
 "kanazawa>takayama":[T(BUS,"Bus Nohi / Hokutetsu (via Shirakawa-go)","濃飛バス・北鉄バス（白川郷経由）","Kanazawa (gare, sortie est)","金沢駅東口","Takayama (Nohi Bus Center)","高山濃飛バスセンター",135,"non",4200,dir="Takayama (via Shirakawa-go)",dirj="高山（白川郷経由）",dirR="Kanazawa (via Shirakawa-go)",dirRj="金沢（白川郷経由）",note="Réservation obligatoire, conseillée plusieurs semaines à l'avance.")],
 "nagoya>takayama":[T(TR,"Limited Express Hida","特急ひだ","Nagoya","名古屋","Takayama","高山",150,"oui",6340,dir="Takayama / Toyama",dirj="高山・富山方面",note="Paysages de montagne : préférez le côté droit en allant vers Takayama.")],
 "kyoto>nagoya":[T(SK,"Tokaido Shinkansen Nozomi","東海道新幹線 のぞみ","Kyoto","京都","Nagoya","名古屋",34,"supplement",5910,n=0,dir="Nagoya / Tokyo",dirj="名古屋・東京方面",dirR="Kyoto / Shin-Osaka",dirRj="京都・新大阪方面",note=NOZOMI_NOTE)],
 "osaka>nagoya":[T(SK,"Tokaido Shinkansen Nozomi","東海道新幹線 のぞみ","Shin-Osaka","新大阪","Nagoya","名古屋",50,"supplement",6680,n=1,dir="Nagoya / Tokyo",dirj="名古屋・東京方面",note=NOZOMI_NOTE)],
 "nagoya>tokyo":[T(SK,"Tokaido Shinkansen Nozomi","東海道新幹線 のぞみ","Nagoya","名古屋","Tokyo","東京",95,"supplement",11300,n=2,dirR="Nagoya / Shin-Osaka",dirRj="名古屋・新大阪方面",note=NOZOMI_NOTE)],
 "nagoya>nagano":[T(TR,"Limited Express Shinano","特急しなの","Nagoya","名古屋","Nagano","長野",180,"oui",7500,dir="Nagano",dirj="長野",note="Belle vue sur la vallée de Kiso.")],
 "tokyo>nagano":[T(SK,"Hokuriku Shinkansen Kagayaki / Hakutaka","北陸新幹線 かがやき・はくたか","Tokyo","東京","Nagano","長野",80,"oui",8340,n=2,dir="Nagano / Kanazawa",dirj="長野・金沢方面")],
 "nagano>takayama":[T(TR,"Limited Express Shinano","特急しなの","Nagano","長野","Matsumoto","松本",50,"oui",2900,dir="Matsumoto / Nagoya",dirj="松本・名古屋方面",dirR="Nagano",dirRj="長野"),
                    T(BUS,"Bus express Alpico / Nohi","高速バス（アルピコ・濃飛）","Matsumoto (Bus Terminal)","松本バスターミナル","Takayama (Nohi Bus Center)","高山濃飛バスセンター",140,"non",3900,note="Réservation conseillée.")],
 "tokyo>hakone":[T(TR,"Odakyu Romancecar","小田急ロマンスカー","Shinjuku","新宿","Hakone-Yumoto","箱根湯本",85,"non",2470,dir="Hakone-Yumoto",dirj="箱根湯本",note="Non couvert par le JR Pass. Le Hakone Free Pass inclut le trajet (sauf supplément Romancecar) et les transports de Hakone.")],
 "tokyo>kawaguchiko":[T(BUS,"Bus express Shinjuku – Kawaguchiko","高速バス 新宿〜河口湖","Shinjuku (Busta Shinjuku)","バスタ新宿","Kawaguchiko (gare)","河口湖駅",110,"non",2200,dir="Kawaguchiko / Fuji-Q",dirj="河口湖・富士急ハイランド",note="Réservation conseillée. Alternative : train Fuji Excursion (富士回遊), JR Pass jusqu'à Otsuki seulement.")],
 "hakone>kawaguchiko":[T(BUS,"Bus via Gotemba","バス（御殿場経由）","Hakone (Sengoku / Togendai)","箱根（仙石・桃源台）","Kawaguchiko (gare)","河口湖駅",120,"non",2500,note="Changement à Gotemba (御殿場) selon les horaires.")],
 "kyoto>hakone":[T(SK,"Tokaido Shinkansen Hikari","東海道新幹線 ひかり","Kyoto","京都","Odawara","小田原",120,"oui",11800,dir="Tokyo",dirj="東京",dirR="Shin-Osaka",dirRj="新大阪"),
                 T(TR,"Hakone Tozan / Odakyu","箱根登山鉄道・小田急線","Odawara","小田原","Hakone-Yumoto","箱根湯本",15,"non",360,dir="Hakone-Yumoto",dirj="箱根湯本")],
 "osaka>hakone":[T(SK,"Tokaido Shinkansen Hikari","東海道新幹線 ひかり","Shin-Osaka","新大阪","Odawara","小田原",135,"oui",12500,dir="Tokyo",dirj="東京"),
                 T(TR,"Hakone Tozan / Odakyu","箱根登山鉄道・小田急線","Odawara","小田原","Hakone-Yumoto","箱根湯本",15,"non",360,dir="Hakone-Yumoto",dirj="箱根湯本")],
 "nagoya>hakone":[T(SK,"Tokaido Shinkansen Hikari","東海道新幹線 ひかり","Nagoya","名古屋","Odawara","小田原",75,"oui",8600,dir="Tokyo",dirj="東京",dirR="Nagoya / Shin-Osaka",dirRj="名古屋・新大阪方面"),
                  T(TR,"Hakone Tozan / Odakyu","箱根登山鉄道・小田急線","Odawara","小田原","Hakone-Yumoto","箱根湯本",15,"non",360,dir="Hakone-Yumoto",dirj="箱根湯本")],
 "nagoya>kawaguchiko":[T(SK,"Tokaido Shinkansen Kodama / Hikari","東海道新幹線 こだま・ひかり","Nagoya","名古屋","Mishima","三島",70,"oui",7600,dir="Tokyo",dirj="東京",dirR="Nagoya / Shin-Osaka",dirRj="名古屋・新大阪方面"),
                       T(BUS,"Bus Mishima – Kawaguchiko","バス 三島〜河口湖","Mishima (gare, sortie nord)","三島駅北口","Kawaguchiko (gare)","河口湖駅",120,"non",2300,note="Réservation conseillée.")],
 "osaka>naoshima":[T(SK,"Sanyo Shinkansen Sakura / Nozomi","山陽新幹線 さくら・のぞみ","Shin-Osaka","新大阪","Okayama","岡山",45,"oui",6000,n=1,dir="Okayama / Hakata",dirj="岡山・博多方面",dirR="Shin-Osaka",dirRj="新大阪",note="Sakura ou Hikari : couvertes par le JR Pass ; Nozomi avec supplément."),T(TR,"JR Uno Line (Seto Ohashi / Uno Minato)","JR 宇野線（宇野みなと線）","Okayama","岡山","Uno","宇野",55,"oui",590,dir="Uno / Chayamachi",dirj="宇野・茶屋町方面",dirR="Okayama",dirRj="岡山",note="Train direct ou changement à Chayamachi (茶屋町) selon l'heure : le Marine Liner va à Chayamachi, puis train local pour Uno."),T(BAT,"Ferry Shikoku Kisen Uno – Miyanoura","四国汽船 宇野〜宮浦","Uno (port, 3 min à pied de la gare)","宇野港","Naoshima (Miyanoura)","直島 宮浦港",20,"non",300,dir="Naoshima (Miyanoura)",dirj="直島（宮浦）",dirR="Uno",dirRj="宇野",note="Environ un ferry par heure : vérifiez l'horaire (Shikoku Kisen) et prévoyez l'attente.")],
 "kyoto>naoshima":[T(SK,"Sanyo Shinkansen Nozomi / Hikari","山陽新幹線 のぞみ・ひかり","Kyoto","京都","Okayama","岡山",65,"supplement",7000,n=2,dir="Okayama / Hakata",dirj="岡山・博多方面",dirR="Kyoto / Tokyo",dirRj="京都・東京方面",note=NOZOMI_NOTE),T(TR,"JR Uno Line (Seto Ohashi / Uno Minato)","JR 宇野線（宇野みなと線）","Okayama","岡山","Uno","宇野",55,"oui",590,dir="Uno / Chayamachi",dirj="宇野・茶屋町方面",dirR="Okayama",dirRj="岡山",note="Train direct ou changement à Chayamachi (茶屋町) selon l'heure : le Marine Liner va à Chayamachi, puis train local pour Uno."),T(BAT,"Ferry Shikoku Kisen Uno – Miyanoura","四国汽船 宇野〜宮浦","Uno (port, 3 min à pied de la gare)","宇野港","Naoshima (Miyanoura)","直島 宮浦港",20,"non",300,dir="Naoshima (Miyanoura)",dirj="直島（宮浦）",dirR="Uno",dirRj="宇野",note="Environ un ferry par heure : vérifiez l'horaire (Shikoku Kisen) et prévoyez l'attente.")],
 "hiroshima>naoshima":[T(SK,"Sanyo Shinkansen Sakura / Nozomi","山陽新幹線 さくら・のぞみ","Hiroshima","広島","Okayama","岡山",36,"oui",6000,n=1,dir="Okayama / Shin-Osaka",dirj="岡山・新大阪方面",dirR="Hiroshima / Hakata",dirRj="広島・博多方面"),T(TR,"JR Uno Line (Seto Ohashi / Uno Minato)","JR 宇野線（宇野みなと線）","Okayama","岡山","Uno","宇野",55,"oui",590,dir="Uno / Chayamachi",dirj="宇野・茶屋町方面",dirR="Okayama",dirRj="岡山",note="Train direct ou changement à Chayamachi (茶屋町) selon l'heure : le Marine Liner va à Chayamachi, puis train local pour Uno."),T(BAT,"Ferry Shikoku Kisen Uno – Miyanoura","四国汽船 宇野〜宮浦","Uno (port, 3 min à pied de la gare)","宇野港","Naoshima (Miyanoura)","直島 宮浦港",20,"non",300,dir="Naoshima (Miyanoura)",dirj="直島（宮浦）",dirR="Uno",dirRj="宇野",note="Environ un ferry par heure : vérifiez l'horaire (Shikoku Kisen) et prévoyez l'attente.")],
 "tokyo>naoshima":[T(SK,"Tokaido-Sanyo Shinkansen Nozomi","東海道・山陽新幹線 のぞみ","Tokyo","東京","Okayama","岡山",195,"supplement",17500,n=5,dir="Okayama / Hakata",dirj="岡山・博多方面",dirR="Tokyo",dirRj="東京",note=NOZOMI_NOTE),T(TR,"JR Uno Line (Seto Ohashi / Uno Minato)","JR 宇野線（宇野みなと線）","Okayama","岡山","Uno","宇野",55,"oui",590,dir="Uno / Chayamachi",dirj="宇野・茶屋町方面",dirR="Okayama",dirRj="岡山",note="Train direct ou changement à Chayamachi (茶屋町) selon l'heure : le Marine Liner va à Chayamachi, puis train local pour Uno."),T(BAT,"Ferry Shikoku Kisen Uno – Miyanoura","四国汽船 宇野〜宮浦","Uno (port, 3 min à pied de la gare)","宇野港","Naoshima (Miyanoura)","直島 宮浦港",20,"non",300,dir="Naoshima (Miyanoura)",dirj="直島（宮浦）",dirR="Uno",dirRj="宇野",note="Environ un ferry par heure : vérifiez l'horaire (Shikoku Kisen) et prévoyez l'attente.")],
 "aeroport:KIX>hiroshima":[T(TR,"Limited Express Haruka","特急はるか","Kansai-Airport","関西空港","Shin-Osaka","新大阪",50,"oui",3300,dir="Kyoto",dirj="京都",dirR="Kansai-Airport",dirRj="関西空港"),T(SK,"Sanyo Shinkansen Sakura / Nozomi","山陽新幹線 さくら・のぞみ","Shin-Osaka","新大阪","Hiroshima","広島",85,"oui",10620,n=2,dir="Hiroshima / Hakata",dirj="広島・博多方面",note="La Sakura (さくら) est couverte par le JR Pass ; la Nozomi demande un supplément.")],
 "aeroport:KIX>naoshima":[T(TR,"Limited Express Haruka","特急はるか","Kansai-Airport","関西空港","Shin-Osaka","新大阪",50,"oui",3300,dir="Kyoto",dirj="京都",dirR="Kansai-Airport",dirRj="関西空港"),T(SK,"Sanyo Shinkansen Sakura / Nozomi","山陽新幹線 さくら・のぞみ","Shin-Osaka","新大阪","Okayama","岡山",45,"oui",6000,n=1,dir="Okayama / Hakata",dirj="岡山・博多方面",dirR="Shin-Osaka",dirRj="新大阪"),T(TR,"JR Uno Line (Seto Ohashi / Uno Minato)","JR 宇野線（宇野みなと線）","Okayama","岡山","Uno","宇野",55,"oui",590,dir="Uno / Chayamachi",dirj="宇野・茶屋町方面",dirR="Okayama",dirRj="岡山",note="Train direct ou changement à Chayamachi (茶屋町) selon l'heure : le Marine Liner va à Chayamachi, puis train local pour Uno."),T(BAT,"Ferry Shikoku Kisen Uno – Miyanoura","四国汽船 宇野〜宮浦","Uno (port, 3 min à pied de la gare)","宇野港","Naoshima (Miyanoura)","直島 宮浦港",20,"non",300,dir="Naoshima (Miyanoura)",dirj="直島（宮浦）",dirR="Uno",dirRj="宇野",note="Environ un ferry par heure : vérifiez l'horaire (Shikoku Kisen) et prévoyez l'attente.")],
 # Aéroports
 "aeroport:KIX>osaka":[T(TR,"JR Kansai Airport Rapid","JR 関空快速","Kansai-Airport","関西空港","Osaka","大阪",70,"oui",1210,dir="Osaka (boucle Osaka Loop)",dirj="大阪環状線方面",dirR="Kansai-Airport",dirRj="関西空港",note="Plus rapide vers Shin-Osaka / Tennoji : Haruka (はるか), ~50 min.")],
 "aeroport:KIX>kyoto":[T(TR,"Limited Express Haruka","特急はるか","Kansai-Airport","関西空港","Kyoto","京都",80,"oui",3590,dir="Kyoto",dirj="京都",dirR="Kansai-Airport",dirRj="関西空港",note="Pass ICOCA & Haruka (tarif étranger) moins cher qu'un billet simple.")],
 "aeroport:HND>tokyo":[T(TR,"Tokyo Monorail","東京モノレール","Haneda T3","羽田空港第3ターミナル","Hamamatsucho","浜松町",15,"oui",520,dir="Hamamatsucho",dirj="浜松町",dirR="Haneda Airport",dirRj="羽田空港"),
                       T(TR,"JR Yamanote","JR 山手線","Hamamatsucho","浜松町","Tokyo","東京",5,"oui",170,dir="Tokyo / Ueno",dirj="東京・上野方面",dirR="Shinagawa",dirRj="品川方面")],
 # Excursions à la journée (depuis la ville-étape)
 "excursion:kyoto>nara":[T(TR,"JR Nara Line (Miyakoji Rapid)","JR奈良線 みやこ路快速","Kyoto","京都","Nara","奈良",45,"oui",760,dir="Nara",dirj="奈良",dirR="Kyoto",dirRj="京都")],
 "excursion:osaka>nara":[T(TR,"JR Yamatoji Rapid","JR 大和路快速","Osaka","大阪","Nara","奈良",50,"oui",820,dir="Nara / Kamo",dirj="奈良・加茂方面",dirR="Osaka (boucle)",dirRj="大阪環状線方面")],
 "excursion:kyoto>uji":[T(TR,"JR Nara Line","JR奈良線","Kyoto","京都","Uji","宇治",20,"oui",250,dir="Nara",dirj="奈良",dirR="Kyoto",dirRj="京都")],
 "excursion:osaka>himeji":[T(TR,"JR Special Rapid (Shinkaisoku)","JR 新快速","Osaka","大阪","Himeji","姫路",62,"oui",1520,dir="Himeji",dirj="姫路方面",dirR="Osaka / Kyoto",dirRj="大阪・京都方面")],
 "excursion:kyoto>himeji":[T(TR,"JR Special Rapid (Shinkaisoku)","JR 新快速","Kyoto","京都","Himeji","姫路",90,"oui",2310,dir="Himeji",dirj="姫路方面",dirR="Kyoto",dirRj="京都方面",note="Plus rapide en Shinkansen (Hikari / Sakura), ~45 min.")],
 "excursion:osaka>kobe":[T(TR,"JR Special Rapid (Shinkaisoku)","JR 新快速","Osaka","大阪","Sannomiya","三ノ宮",21,"oui",420,dir="Kobe / Himeji",dirj="神戸・姫路方面",dirR="Osaka / Kyoto",dirRj="大阪・京都方面")],
 "excursion:osaka>koyasan":[T(TR,"Nankai Koya Line (Limited Express Koya)","南海高野線 特急こうや","Namba","なんば","Gokurakubashi","極楽橋",80,"non",1600,dir="Gokurakubashi",dirj="極楽橋",dirR="Namba",dirRj="なんば"),
                            T(TR,"Koyasan Cable Car","高野山ケーブル","Gokurakubashi","極楽橋","Koyasan","高野山",5,"non",500,note="Puis bus local vers Okunoin / Kongobu-ji (pass Koyasan conseillé).")],
 "excursion:hiroshima>miyajima":[T(TR,"JR Sanyo Line","JR 山陽本線","Hiroshima","広島","Miyajimaguchi","宮島口",27,"oui",420,dir="Iwakuni",dirj="岩国方面",dirR="Hiroshima",dirRj="広島方面"),
                                 T(BAT,"JR Miyajima Ferry","JR西日本宮島フェリー","Miyajimaguchi","宮島口","Miyajima","宮島",10,"oui",200,note="Taxe d'accès à l'île de Miyajima : 100 ¥ par personne.")],
 "excursion:tokyo>kamakura":[T(TR,"JR Yokosuka Line","JR 横須賀線","Tokyo","東京","Kamakura","鎌倉",56,"oui",950,dir="Zushi / Kurihama",dirj="逗子・久里浜方面",dirR="Tokyo / Chiba",dirRj="東京・千葉方面")],
 "excursion:tokyo>yokohama":[T(TR,"JR Tokaido Line","JR 東海道線","Tokyo","東京","Yokohama","横浜",25,"oui",490,dir="Odawara / Atami",dirj="小田原・熱海方面",dirR="Tokyo",dirRj="東京方面")],
 "excursion:tokyo>nikko":[T(SK,"Tohoku Shinkansen Yamabiko","東北新幹線 やまびこ","Tokyo","東京","Utsunomiya","宇都宮",50,"oui",5020,n=2,dir="Sendai",dirj="仙台方面",dirR="Tokyo",dirRj="東京"),
                          T(TR,"JR Nikko Line","JR 日光線","Utsunomiya","宇都宮","Nikko","日光",45,"oui",770,dir="Nikko",dirj="日光",dirR="Utsunomiya",dirRj="宇都宮",note="Sans JR Pass, le train Tobu depuis Asakusa (東武) est moins cher.")],
 "excursion:tokyo>kawagoe":[T(TR,"Tobu Tojo Line","東武東上線","Ikebukuro","池袋","Kawagoe","川越",30,"non",490,dir="Kawagoe / Ogawamachi",dirj="川越・小川町方面",dirR="Ikebukuro",dirRj="池袋",note="Avec le JR Pass : JR Saikyo Line (埼京線) depuis Shinjuku, ~55 min.")],
 "excursion:tokyo>hitachi":[T(TR,"Limited Express Tokiwa","特急ときわ","Ueno","上野","Katsuta","勝田",80,"oui",4000,dir="Katsuta / Takahagi",dirj="勝田・高萩方面",dirR="Ueno / Shinagawa",dirRj="上野・品川方面"),
                            T(BUS,"Bus Ibaraki Kotsu","茨城交通バス","Katsuta (sortie est)","勝田駅東口","Hitachi Seaside Park","ひたち海浜公園",15,"non",400)],
 "excursion:kanazawa>shirakawago":[T(BUS,"Bus Nohi / Hokutetsu","濃飛バス・北鉄バス","Kanazawa (gare, sortie est)","金沢駅東口","Shirakawa-go","白川郷",75,"non",2600,note="Réservation obligatoire.")],
 "excursion:takayama>shirakawago":[T(BUS,"Bus Nohi","濃飛バス","Takayama (Nohi Bus Center)","高山濃飛バスセンター","Shirakawa-go","白川郷",50,"non",2600,note="Réservation obligatoire.")],
 "excursion:nagano>matsumoto":[T(TR,"Limited Express Shinano","特急しなの","Nagano","長野","Matsumoto","松本",50,"oui",2900,dir="Matsumoto / Nagoya",dirj="松本・名古屋方面",dirR="Nagano",dirRj="長野")],
 "excursion:tokyo>hakone":None, "excursion:tokyo>kawaguchiko":None,
}
TRONCONS={k:v for k,v in TRONCONS.items() if v is not None}
for k in TRONCONS:
    a,b=k.split(":")[-1].split(">")
    assert (a in ids or a in ("KIX","HND")) and b in ids, k


# ---------------------------------------------------------------------------
# Lot 7.1 : fêtes, événements et saisons pendant le séjour (11 → 26 juin 2027)
# « sur » : true = date fixe chaque année ; false = date 2027 non publiée (estimée d'après les années précédentes).
# ---------------------------------------------------------------------------
E = lambda id,titre,ville,lieu,debut,fin,type,texte,sur,adresse="": dict(id=id,titre=titre,ville=ville,lieu=lieu,debut=debut,fin=fin,type=type,texte=texte,sur=sur,adresse=adresse)
EVENEMENTS = [
 E("sumiyoshi-otaue","Otaue Shinji, fête du repiquage du riz","osaka","Sumiyoshi Taisha","2027-06-14","2027-06-14","fete",
   "Rite très ancien pour une bonne récolte : danses, chants et repiquage du riz en costumes traditionnels dans la rizière sacrée du sanctuaire. Spectaculaire et gratuit.",True,"住吉大社 大阪市住吉区住吉2-9-89"),
 E("yasaka-15juin","Fête du sanctuaire Yasaka (danses de cour)","kyoto","Yasaka-jinja, Gion","2027-06-15","2027-06-15","fete",
   "Danses de cour de l'époque Heian présentées vers 10 h sur la scène du sanctuaire, au cœur de Gion.",True,"八坂神社 京都市東山区祇園町北側625"),
 E("takekiri","Takekiri Eshiki, cérémonie de la coupe des bambous","kyoto","Kurama-dera","2027-06-20","2027-06-20","fete",
   "Rituel de plus de 1 000 ans : des moines en tenue de guerriers tranchent de gros bambous figurant des serpents, deux équipes s'affrontent en vitesse. À combiner avec Kibune (dîner au-dessus de la rivière).",True,"鞍馬寺 京都市左京区鞍馬本町1074"),
 E("saikusa","Saikusa Matsuri, fête des lys","nara","Isagawa-jinja","2027-06-17","2027-06-17","fete",
   "Procession de prêtresses portant des lys sauvages et de jeunes filles en costume ancien, autour d'un petit sanctuaire proche de la gare de Nara. Date fixe chaque année, à vérifier.",True,"率川神社 奈良市本子守町18"),
 E("yakata","Yakata Matsuri","himeji","Nagakabe-jinja (près du château)","2027-06-22","2027-06-23","fete",
   "Fête de quartier animée avec des centaines de stands de nourriture et de jeux autour du sanctuaire, en soirée. Date fixe chaque année.",True,"長壁神社 姫路市立町"),
 E("sanno","Sanno Matsuri (année « légère »)","tokyo","Hie-jinja, Akasaka","2027-06-07","2027-06-17","fete",
   "Une des trois grandes fêtes d'Edo. En 2027 (année impaire), pas de grand défilé, mais rituels, tambours, danses et passage dans le grand anneau de paille (chinowa) au sanctuaire. Dates 2027 à confirmer.",False,"日枝神社 東京都千代田区永田町2-10-5"),
 E("torigoe","Torigoe Matsuri, défilé de nuit des lanternes","tokyo","Torigoe-jinja, Taito","2027-06-12","2027-06-13","fete",
   "Le plus lourd mikoshi de Tokyo (4 tonnes) porté de nuit, éclairé de lanternes, avec des stands de rue. Habituellement le 2e week-end de juin : dates 2027 à confirmer.",False,"鳥越神社 東京都台東区鳥越2-4-1"),
 E("hakone-ajisai","Train des hortensias de Hakone (de nuit)","hakone","Hakone Tozan, Hakone-Yumoto → Gora","2027-06-12","2027-06-30","saison",
   "Le petit train de montagne serpente entre des milliers d'hortensias éclairés le soir. Train spécial de nuit avec places réservées : réserver dès l'ouverture. Dates 2027 à confirmer (2026 : à partir du 13 juin).",False,"箱根湯本駅"),
 E("kamakura-ajisai","Hortensias de Kamakura (Hase-dera, Meigetsu-in)","kamakura","Hase-dera, Meigetsu-in","2027-06-05","2027-06-25","saison",
   "Les « temples des hortensias » : chemin fleuri avec vue sur la mer à Hase-dera (billet horaire à réserver en pleine saison), escaliers bleus à Meigetsu-in. Y aller tôt le matin.",False,"長谷寺 鎌倉市長谷3-11-2"),
 E("mimurotoji","Jardin des hortensias de Mimuroto-ji","uji","Mimuroto-ji","2027-06-01","2027-07-07","saison",
   "Environ 20 000 hortensias de 50 variétés dans un vallon de temple, près d'Uji. Illuminations certains soirs de week-end.",False,"三室戸寺 宇治市菟道滋賀谷21"),
 E("fujinomori","Fête des hortensias de Fujinomori","kyoto","Fujinomori-jinja (Fushimi)","2027-06-01","2027-06-30","saison",
   "Deux jardins d'hortensias ouverts tout le mois, et le 15 juin une fête avec tambours et danses. À 1 station de Fushimi Inari.",False,"藤森神社 京都市伏見区深草鳥居崎町609"),
 E("hotaru","Lucioles (hotaru)","kyoto","Kibune, Shimogamo, Philosopher's Path","2027-06-05","2027-06-25","saison",
   "Les lucioles dansent au-dessus des ruisseaux à la tombée de la nuit (vers 20 h, soirées chaudes et sans vent). Kibune et le canal du chemin des philosophes sont les plus faciles d'accès.",False),
 E("iris-tokyo","Iris en fleur (Horikiri, Meiji Jingu)","tokyo","Jardin d'iris de Horikiri, jardin intérieur du Meiji Jingu","2027-06-05","2027-06-25","saison",
   "Champs d'iris japonais (hanashobu) en pleine floraison à la mi-juin ; fête des iris à Horikiri avec stands.",False),
 E("ukai-nagara","Pêche au cormoran sur la rivière Nagara","nagoya","Gifu (40 min de Nagoya)","2027-05-11","2027-10-15","spectacle",
   "Tradition de 1 300 ans : de nuit, des pêcheurs en costume guident des cormorans à la lueur de feux, vus depuis des bateaux. Réservation conseillée.",True,"長良川鵜飼 岐阜市湊町"),
 E("kawadoko","Dîners au-dessus de la rivière à Kibune (kawadoko)","kyoto","Kibune","2027-05-01","2027-09-30","saison",
   "Les restaurants installent des plateformes au-dessus de la rivière : on mange au frais, les pieds presque dans l'eau. Réserver.",True),
 E("pas-de-sumo","Pas de tournoi de sumo en juin","tokyo","—","2027-06-11","2027-06-26","info",
   "Les grands tournois ont lieu en mai (Tokyo) et en juillet (Nagoya) : pendant votre séjour, privilégiez une visite de séance d'entraînement (asa-geiko) ou une expérience sumo.",True),
]
for e in EVENEMENTS: assert e["ville"] in ids, e["id"]


# ---------------------------------------------------------------------------
# Lot 9 : climat moyen de juin (normales ≈ 1991-2020, JMA) : [t° max, t° min, humidité %, jours de pluie ≥ 1 mm]
# Utilisé au-delà de l'horizon des prévisions (16 jours).
# ---------------------------------------------------------------------------
CLIMAT_JUIN = {
 "tokyo":[26.5,19.0,75,12], "yokohama":[25.4,19.4,79,12], "kamakura":[25.4,19.4,79,12], "kawagoe":[26.8,18.6,77,12],
 "osaka":[27.8,20.0,69,11], "kyoto":[28.1,19.4,70,12], "uji":[28.0,19.2,71,12], "nara":[27.6,18.6,75,12],
 "kobe":[27.2,20.4,72,11], "himeji":[27.5,19.2,72,11], "hiroshima":[27.0,19.6,76,12], "miyajima":[26.5,19.8,78,12], "naoshima":[27.4,20.2,73,11],
 "nagoya":[27.6,19.6,72,12], "kanazawa":[26.2,18.3,75,11], "shirakawago":[25.5,16.5,80,14], "takayama":[25.6,15.6,79,13],
 "nagano":[26.6,16.6,74,10], "matsumoto":[26.6,16.5,72,11], "hakone":[21.0,15.0,90,14], "kawaguchiko":[24.6,15.4,79,12],
 "nikko":[23.5,15.5,85,14], "koyasan":[22.5,14.5,88,15], "hitachi":[24.0,17.6,85,11],
}
assert set(CLIMAT_JUIN) == ids, ids - set(CLIMAT_JUIN)

# Numéros et contacts utiles (vérifiés le 22/11/2026 : JNTO, diplomatie.gouv.fr)
URGENCES = [
 {"titre":"Police","numero":"110","texte":"Accident, vol, agression. Gratuit, 24 h/24."},
 {"titre":"Ambulance / pompiers","numero":"119","texte":"Urgence médicale ou incendie. Gratuit, 24 h/24 ; interprétariat possible."},
 {"titre":"Japan Visitor Hotline (JNTO)","numero":"050-3816-2787","texte":"Aide aux voyageurs 24 h/24 en anglais : accident, maladie, catastrophe naturelle, renseignements."},
 {"titre":"Ambassade de France (Tokyo)","numero":"+81-3-5798-6000","texte":"Urgence grave, accident, perte de passeport. 4-11-44 Minami-Azabu, Minato-ku, Tokyo."},
 {"titre":"France Consulaire (urgences)","numero":"+33-2-14-69-00-01","texte":"Ligne d'urgence du ministère des Affaires étrangères, joignable depuis l'étranger."},
 {"titre":"Consulat général de France à Kyoto","numero":"","texte":"8 Izumidono-cho, Yoshida, Sakyo-ku, Kyoto. Coordonnées à jour : kyoto.consulfrance.org","site":"https://kyoto.consulfrance.org/"},
 {"titre":"Conseil médical non urgent","numero":"#7119","texte":"Pour savoir s'il faut appeler une ambulance (selon les régions, en japonais)."},
]


# ---------------------------------------------------------------------------
# Lot 9.1 : us et coutumes, escalators, heures de pointe (vérifié le 22/11/2026)
# ---------------------------------------------------------------------------
COUTUMES = [
 {"id":"poubelles","emoji":"🗑️","titre":"Poubelles : il y en a très peu","erreur":True,"texte":
  "Les poubelles publiques sont rares dans la rue, même à Tokyo, Kyoto ou Nara. On garde ses déchets avec soi (prévoir un petit sac par personne) jusqu'à l'hôtel ou une poubelle de konbini, de gare, de toilettes publiques ou à côté des distributeurs (ces dernières sont réservées aux canettes et bouteilles).\n"
  "Le tri est respecté : 燃えるゴミ (moeru gomi, déchets brûlables : papiers, emballages, restes), ペットボトル (bouteilles plastique, sans bouchon ni étiquette si indiqué), かん・びん (canettes et verre). À Nara, ne laissez rien traîner : les daims mangent les sacs plastique."},
 {"id":"pourboire","emoji":"💴","titre":"Pas de pourboire","erreur":True,"texte":
  "Le pourboire ne se pratique pas : le service est compris et laisser de l'argent met souvent le personnel mal à l'aise (il viendra vous le rendre). Un « arigatō gozaimasu » sincère suffit. À la caisse, posez l'argent ou la carte dans le petit plateau prévu plutôt que dans la main."},
 {"id":"saluer","emoji":"🙇","titre":"Dire bonjour et merci","erreur":False,"texte":
  "On se salue par une légère inclinaison de la tête et du buste, sans bise ni accolade (la poignée de main reste rare). Mots utiles : おはようございます ohayō gozaimasu (bonjour, le matin), こんにちは konnichiwa (bonjour), ありがとうございます arigatō gozaimasu (merci), すみません sumimasen (pardon / excusez-moi, aussi pour appeler un serveur). On tend et reçoit un objet ou une carte à deux mains. En entrant dans un magasin, le personnel lance « irasshaimase » : pas besoin de répondre, un sourire ou un signe de tête suffit."},
 {"id":"chaussures","emoji":"👟","titre":"Où enlever ses chaussures","erreur":True,"texte":
  "On se déchausse : dans les maisons, ryokan et certaines auberges, les salles des temples, les restaurants à tatami, certains musées et châteaux (on vous donne un sac pour les porter), les cabines d'essayage. Le signe : une marche à l'entrée (genkan), une rangée de chaussons ou d'étagères à chaussures.\n"
  "Jamais de chaussons sur un tatami : on y marche en chaussettes. Les chaussons spéciaux des toilettes restent dans les toilettes (erreur très fréquente !). Prévoir des chaussures faciles à enlever et des chaussettes sans trou."},
 {"id":"tatouages","emoji":"🐉","titre":"Tatouages","erreur":True,"texte":
  "Les tatouages visibles peuvent être refusés dans les onsen, sento, piscines et salles de sport, et les règles varient d'un établissement à l'autre. Un petit tatouage peut souvent être caché par un patch ou un pansement ; sinon, cherchez les lieux « tattoo-friendly » ou réservez un bain privatif (貸切風呂 kashikiri-buro). Dans la rue, aucun problème."},
 {"id":"onsen","emoji":"♨️","titre":"Bains (onsen) : les règles","erreur":True,"texte":
  "On entre nu (pas de maillot), après s'être lavé et rincé entièrement, assis sur un tabouret aux douches. La petite serviette ne va jamais dans l'eau (on la pose sur la tête ou au bord), les cheveux longs sont attachés, on ne nage pas, on ne fait pas de photos. Les bains sont séparés hommes (男, rideau souvent bleu) / femmes (女, rideau souvent rouge) ; à partir d'environ 7 ans, les enfants vont dans le bain de leur sexe, donc une fille de 11 ans va côté femmes. Buvez de l'eau, et sortez si vous avez la tête qui tourne."},
 {"id":"train","emoji":"🚆","titre":"Dans les trains et le métro","erreur":True,"texte":
  "On parle bas et on ne téléphone pas (téléphone en mode silencieux, « manner mode »). Sac à dos porté devant ou posé dans le filet. On fait la queue aux marques au sol sur le quai et on laisse descendre avant de monter. Les sièges prioritaires (優先席) sont laissés aux personnes âgées, enceintes, handicapées. En semaine le matin, certaines voitures sont réservées aux femmes (女性専用車, marquage rose) : les hommes n'y montent pas.\n"
  "On ne mange pas dans le métro ni les trains de banlieue ; dans le shinkansen et les trains express, c'est normal (ekiben). Shinkansen Tokaido/Sanyo/Kyushu : une valise dont les 3 dimensions dépassent 160 cm demande une place réservée avec espace bagages."},
 {"id":"marcher","emoji":"🍡","titre":"Ne pas manger en marchant","erreur":True,"texte":
  "Manger ou boire en marchant est mal vu, et des rues très touristiques (Asakusa, Kamakura, Nishiki à Kyoto…) demandent de consommer sur place, devant le stand ou dans l'espace prévu. Au konbini, on mange devant le magasin ou au coin repas, puis on jette ses déchets dans leurs poubelles."},
 {"id":"baguettes","emoji":"🥢","titre":"À table","erreur":True,"texte":
  "Ne plantez pas les baguettes debout dans le riz et ne passez pas un aliment de baguettes à baguettes : ces gestes rappellent les funérailles. Posez-les sur le repose-baguettes, ne pointez personne avec. Aspirer bruyamment ses nouilles est normal. Avant de manger : いただきます itadakimasu ; après : ごちそうさまでした gochisōsama deshita. On paie en général à la caisse en sortant, avec le ticket laissé sur la table."},
 {"id":"photos","emoji":"📸","titre":"Photos : Gion, temples, personnes","erreur":True,"texte":
  "À Gion (Kyoto), les photos sont interdites dans les ruelles privées signalées par des panneaux, avec une amende possible ; ne suivez jamais une geiko ou une maiko pour la photographier. Dans beaucoup de temples, les photos sont interdites à l'intérieur des pavillons. On demande avant de photographier quelqu'un de près, et on évite de bloquer une rue ou un passage pour une photo. Drones interdits dans la plupart des lieux touristiques."},
 {"id":"temples","emoji":"⛩️","titre":"Temples et sanctuaires","erreur":False,"texte":
  "À la fontaine (手水舎 chōzuya) : on rince la main gauche, puis la droite, puis on verse un peu d'eau dans sa main pour se rincer la bouche (jamais directement à la louche). Au sanctuaire shinto (torii) : pièce, 2 saluts, 2 claquements de mains, prière, 1 salut. Au temple bouddhiste : on joint les mains en silence, sans claquer. On parle bas et on reste sur les chemins."},
 {"id":"nara","emoji":"🦌","titre":"Les daims de Nara","erreur":False,"texte":
  "On ne leur donne que les biscuits vendus sur place (shika senbei). Ce sont des animaux sauvages : ils peuvent mordre, donner des coups de tête ou pousser, surtout quand on fait semblant de leur donner à manger. Montrez les mains vides quand vous n'avez plus rien, et rangez cartes et papiers."},
 {"id":"especes","emoji":"🏧","titre":"Garder des espèces","erreur":False,"texte":
  "Les cartes sont de plus en plus acceptées, mais beaucoup de petits restaurants, temples, stands et casiers ne prennent que le liquide. Les distributeurs des 7-Eleven et de la Poste japonaise (Japan Post) acceptent les cartes étrangères."},
 {"id":"taxi","emoji":"🚕","titre":"Taxi : la porte s'ouvre toute seule","erreur":True,"texte":
  "La porte arrière gauche s'ouvre et se ferme automatiquement : ne la touchez pas. Montrez l'adresse écrite en japonais (bouton « Montrer en grand » de la fiche hôtel). Pas de pourboire."},
 {"id":"toilettes","emoji":"🚻","titre":"Toilettes","erreur":False,"texte":
  "Le papier toilette va dans la cuvette. Pour tirer la chasse : 流す (nagasu) ou 大 / 小 ; le bouton 止 (tomeru) arrête le jet. Attention au bouton d'appel d'urgence (呼出 yobidashi), souvent rouge."},
 {"id":"bruit","emoji":"🤫","titre":"Discrétion","erreur":False,"texte":
  "On évite de parler fort, de se moucher bruyamment en public (on se mouche discrètement, à l'écart) et de téléphoner dans les lieux fermés. Si vous êtes enrhumé, portez un masque : c'est une marque de politesse."},
 {"id":"fumer","emoji":"🚭","titre":"Fumer dans la rue","erreur":False,"texte":
  "Il est interdit de fumer en marchant dans beaucoup de quartiers de Tokyo, Kyoto ou Osaka ; on fume uniquement dans les espaces fumeurs signalés (喫煙所)."},
]

# Côté où l'on se tient sur les escalators : gauche / droite / immobile (les deux côtés) / variable
ESCALATORS_TEXTES = {
 "gauche":"on se tient à gauche, la droite est laissée à ceux qui marchent (coutume du Kanto et de la plupart des régions)",
 "droite":"on se tient à droite, la gauche est laissée à ceux qui marchent (coutume du Kansai)",
 "kyoto":"coutume du Kansai, on se tient à droite, mais avec les touristes c'est souvent mélangé : faites comme les gens devant vous",
 "immobile":"règlement local : on reste immobile, des deux côtés (on ne marche pas sur les escalators)",
 "aeroport":"les aéroports demandent de rester immobile, des deux côtés",
}
ESCALATORS = {
 "tokyo":"gauche","yokohama":"gauche","kamakura":"gauche","hakone":"gauche","kawaguchiko":"gauche","nikko":"gauche","hitachi":"gauche",
 "kawagoe":"immobile","nagoya":"immobile",
 "osaka":"droite","kobe":"droite","nara":"droite","uji":"droite","himeji":"droite","koyasan":"droite",
 "kyoto":"kyoto",
 "hiroshima":"gauche","miyajima":"gauche","naoshima":"gauche","kanazawa":"gauche","shirakawago":"gauche","takayama":"gauche","nagano":"gauche","matsumoto":"gauche",
}
assert set(ESCALATORS) == ids, ids ^ set(ESCALATORS)
ESCALATORS_GENERAL = ("Escalators : à Tokyo on se tient à gauche, dans le Kansai (Osaka, Kyoto, Nara, Kobe) à droite. "
  "Nagoya et la préfecture de Saitama (Kawagoe) demandent par règlement de rester immobile des deux côtés. "
  "Dans le doute, faites comme les gens devant vous ; avec des valises, restez immobile et tenez la rampe.")

HEURES_POINTE = ("Heures de pointe (jours de semaine) : le matin environ 7 h – 9 h 30, pic vers 8 h – 8 h 30 vers le centre de Tokyo et d'Osaka ; "
  "le soir environ 17 h – 19 h 30. Évitez ces créneaux avec des valises (lignes JR Yamanote, Chuo, Saikyo, Tozai… très chargées à Tokyo). "
  "C'est bien plus calme entre 9 h 30 et 16 h 30, ainsi que le week-end. Le matin en semaine, certaines voitures sont réservées aux femmes (marquage rose).")


# ---------------------------------------------------------------------------
# Lot 10 : plans de transport, envoi de bagages (Hands-Free), tampons (vérifié le 22/11/2026)
# "pdf" = lien direct (téléchargeable dans l'appli) ; "page" = page officielle (si le lien direct change)
# ---------------------------------------------------------------------------
PLANS = [
 {"id":"tokyo-metro-toei-fr","villes":["tokyo"],"titre":"Tokyo : métro (Tokyo Metro + Toei), en français","source":"Toei Transportation",
  "pdf":"https://www.kotsu.metro.tokyo.jp/eng/services/pdf/sub_map_fra.pdf","page":"https://www.kotsu.metro.tokyo.jp/eng/maps/subway/"},
 {"id":"tokyo-metro-en","villes":["tokyo"],"titre":"Tokyo : métro avec numéros de stations (anglais)","source":"Tokyo Metro",
  "pdf":"https://www.tokyometro.jp/station/pdf/202305/202305_number_en.pdf","page":"https://www.tokyometro.jp/en/subwaymap/index.html"},
 {"id":"osaka-reseau","villes":["osaka","kobe","nara"],"titre":"Osaka : tout le réseau (Osaka Metro, JR, lignes privées)","source":"Osaka Convention & Tourism Bureau",
  "pdf":"https://osaka-info.jp/common/img/information/pamphlet/osaka_route_map.pdf","page":"https://osaka-info.jp/en/information/area-map-download/"},
 {"id":"kyoto-navi-1","villes":["kyoto","uji"],"titre":"Kyoto : bus et métro vers les sites (Subway & Bus Navi, recto)","source":"Kyoto City Transportation Bureau",
  "pdf":"https://www2.city.kyoto.lg.jp/kotsu/webguide/files/tikabusnavi/en_tikabusnavi_1.pdf","page":"https://www2.city.kyoto.lg.jp/kotsu/webguide/en/comm/routemap.html"},
 {"id":"kyoto-navi-2","villes":["kyoto","uji"],"titre":"Kyoto : plan complet des bus et du métro (verso)","source":"Kyoto City Transportation Bureau",
  "pdf":"https://www2.city.kyoto.lg.jp/kotsu/webguide/files/tikabusnavi/en_tikabusnavi_2.pdf","page":"https://www2.city.kyoto.lg.jp/kotsu/webguide/en/comm/routemap.html"},
 {"id":"hiroshima-tram","villes":["hiroshima","miyajima"],"titre":"Hiroshima : tramway (Hiroden), anglais","source":"Hiroshima Electric Railway",
  "pdf":"https://www.hiroden.co.jp/train/route-guide/pdf/map-english.pdf","page":"https://www.hiroden.co.jp/en/"},
 {"id":"kansai-jr","villes":["osaka","kyoto","kobe","nara","himeji","uji"],"titre":"Kansai : plans et horaires JR West","source":"JR West",
  "pdf":"","page":"https://www.westjr.co.jp/global/en/timetable/"},
]
assert all(set(p_["villes"]) <= ids for p_ in PLANS)

BAGAGES = {
 "intro":"Au Japon, on envoie facilement ses valises d'un hôtel à l'autre (宅急便 takkyūbin, « TA-Q-BIN » chez Yamato, le chat noir) : on voyage dans le shinkansen avec un simple sac de jour, et la valise arrive en général le lendemain.",
 "etapes":[
  "La veille au soir ou le matin, à la réception de l'hôtel (ou dans un konbini) : demandez « takkyūbin onegaishimasu » et remplissez le bordereau avec l'adresse et le téléphone de l'hôtel suivant, le nom du client et la date d'arrivée.",
  "Livraison en général le lendemain entre grandes villes (souvent l'après-midi ou le soir) : envoyez la valise la veille de votre départ pour la retrouver à l'hôtel suivant le jour de votre arrivée. Sinon, prévoyez une nuit avec le sac de jour.",
  "Pour l'aéroport du retour, envoyez la valise 2 jours avant le vol (comptoir TA-Q-BIN de l'aéroport).",
  "Notez le numéro de suivi (10 ou 12 chiffres, en haut à droite du bordereau) dans l'appli.",
 ],
 "prix":"Repère 2026 : environ 2 500 à 2 700 ¥ par valise standard (taille 160 : longueur + largeur + hauteur ≤ 160 cm, ≤ 25 kg) entre Tokyo et Kyoto/Osaka ; supplément pour l'aéroport. Maximum 200 cm et 30 kg par bagage. Paiement en espèces ou carte selon le lieu.",
 "conseils":[
  "Gardez dans le sac de jour : passeports, médicaments, chargeurs, une tenue et la trousse de toilette pour la nuit sans valise.",
  "Batteries externes, briquets, bombes aérosol et objets dangereux sont interdits dans les envois.",
  "Livraison le jour même possible depuis certains aéroports (Kansai, Haneda) vers les hôtels du centre si l'on dépose la valise le matin.",
  "Shinkansen Tokaido / Sanyo / Kyushu : une valise de plus de 160 cm (3 dimensions) demande une place réservée avec espace bagages ; l'envoi évite ce souci.",
 ],
 "suivi":"https://www.kuronekoyamato.co.jp/en/",
 "phrase_ja":"宅急便で次のホテルに送りたいです。",
 "phrase_fr":"Je voudrais envoyer cette valise à l'hôtel suivant en takkyūbin.",
}

TAMPONS = {
 "intro":"Deux collections à ne pas confondre : les tampons de gares et de sites (gratuits) et les goshuin des temples et sanctuaires (calligraphie sacrée, payante).",
 "gares":"Tampons de gares et de sites (駅スタンプ eki stamp) : gratuits, en libre-service près des portiques, des offices de tourisme, châteaux, musées, belvédères… Encre souvent rouge ou bleue : apportez un carnet à part (ou des cartes) et tamponnez droit, sans appuyer trop longtemps. Les enfants adorent en faire une chasse au trésor.",
 "goshuin":"Goshuin (御朱印) : calligraphie et sceau rouge faits à la main par un moine ou un prêtre, preuve de visite. On prie d'abord, puis on se présente au bureau (納経所 nōkyōsho / 授与所) en tendant son carnet ouvert à la bonne page. Prix habituel : 300 à 500 ¥, parfois plus pour les éditions spéciales ; préparez la monnaie. Il faut un carnet dédié (御朱印帳 goshuinchō, environ 1 000 à 2 500 ¥, vendu dans les grands temples) : n'y mettez jamais de tampons touristiques. Quand il y a foule, on vous donne parfois une feuille déjà écrite (書き置き kakioki) à coller.",
}


# ---------------------------------------------------------------------------
# Lot 10.2 : où trouver les tampons (vérifié le 22/11/2026)
# ---------------------------------------------------------------------------
GOSHUIN = "Goshuin au bureau des amulettes (授与所 juyosho) ou des goshuin (御朱印所 / 納経所 nōkyōsho), en général près du pavillon principal ; bureau ouvert environ de 9 h à 16 h 30 – 17 h."
CHATEAU = "Tampon des « 100 châteaux du Japon » (日本100名城) et souvent un tampon touristique : en général à l'entrée ou au guichet de la visite ; il faut parfois avoir payé l'entrée pour y accéder."
SITE = "Tampon touristique (記念スタンプ) : souvent au guichet, à l'accueil, à la boutique ou à l'office de tourisme le plus proche."
TAMPONS_OU = {
 "osaka-chateau":["chateau",CHATEAU],
 "osaka-sumiyoshi":["goshuin",GOSHUIN],
 "kyoto-fushimi":["goshuin","Goshuin au bureau situé à côté du pavillon principal (本殿 honden), au pied de la montagne, avant les torii ; d'autres petits sanctuaires en proposent en montant. "+SITE+" Gare JR Inari juste en face : tampon de gare."],
 "kyoto-kinkakuji":["goshuin","Goshuin au bureau sur le parcours de visite, vers la sortie (après le Pavillon d'or) ; billet d'entrée nécessaire."],
 "kyoto-arashiyama":["site","Tampons dans les gares de Saga-Arashiyama (JR), d'Arashiyama (Randen, Hankyu) et du train Torokko. Goshuin au temple Tenryū-ji. "+SITE],
 "kyoto-kiyomizu":["goshuin","Plusieurs goshuin possibles selon les pavillons (le temple fait partie de plusieurs pèlerinages) : demandez au bureau principal sur le parcours. Le matin il y a moins de monde."],
 "kyoto-ginkakuji":["goshuin","Goshuin au bureau sur le parcours de visite ; billet d'entrée nécessaire."],
 "kyoto-nijo":["chateau",CHATEAU],
 "nara-todaiji":["goshuin","Goshuin au bureau du Grand Bouddha (Daibutsuden) et dans les pavillons annexes (Nigatsu-dō, Hokke-dō). "+SITE],
 "nara-kasuga":["goshuin",GOSHUIN],
 "uji-byodoin":["goshuin","Goshuin au bureau du temple, dans l'enceinte ; tampon au musée Hōshōkan. "+SITE],
 "himeji-chateau":["chateau",CHATEAU],
 "hiroshima-memorial":["site","Tampon commémoratif au musée de la Paix (hall d'entrée) ; tampons aussi au Dôme et à l'office de tourisme du parc (Rest House)."],
 "hiroshima-chateau":["chateau",CHATEAU],
 "miyajima-itsukushima":["goshuin","Goshuin en général près de la sortie de la galerie du sanctuaire (le parcours se fait dans un seul sens). Tampon au terminal des ferries de Miyajima."],
 "miyajima-misen":["site","Tampons dans les stations du téléphérique (Momijidani, Shishiiwa) ; goshuin au temple Daishō-in au pied du mont."],
 "kanazawa-ninja":["goshuin",GOSHUIN+" Visite guidée sur réservation."],
 "hakone-boucle":["site","Nombreux tampons sur la boucle : gares du Tozan, du funiculaire et du téléphérique (Ōwakudani, Tōgendai), bateaux pirates. Goshuin au sanctuaire de Hakone (torii dans le lac)."],
 "kawaguchiko-chureito":["site","Goshuin au sanctuaire Arakura Fuji Sengen, au pied des escaliers de la pagode. Tampon à la gare de Kawaguchiko et de Shimoyoshida."],
 "tokyo-sensoji":["goshuin","Goshuin au bureau des goshuin dans l'enceinte (file d'attente fréquente en journée) ; le sanctuaire voisin Asakusa-jinja en propose aussi. Tampon à l'office de tourisme d'Asakusa (en face de la porte Kaminarimon)."],
 "tokyo-harajuku":["goshuin","Goshuin au sanctuaire Meiji (Meiji Jingū), au bureau près du pavillon principal ; horaires plus longs en été. Tampon à la gare JR de Harajuku."],
 "kamakura-daibutsu":["goshuin","Goshuin au bureau du temple Kōtoku-in (Grand Bouddha). Tampon à la gare de Hase (Enoden)."],
 "kamakura-hasedera":["goshuin",GOSHUIN],
 "kamakura-enoshima":["site","Goshuin au sanctuaire d'Enoshima ; tampons aux gares d'Enoshima (Enoden) et de Katase-Enoshima (Odakyu)."],
 "nikko-toshogu":["goshuin","Goshuin au bureau du Tōshōgū et dans les sanctuaires voisins (Futarasan, Taiyūin). Tampon à la gare JR et Tōbu de Nikkō."],
 "nagoya-chateau":["chateau",CHATEAU],
 "nagoya-osu":["goshuin","Goshuin au temple Ōsu Kannon, à l'entrée du quartier."],
 "nagoya-atsuta":["goshuin",GOSHUIN],
 "nagano-zenkoji":["goshuin",GOSHUIN+" Tampon à la gare JR de Nagano."],
 "nagano-togakushi":["site","Goshuin aux sanctuaires de Togakushi (Hōkōsha, Chūsha, Okusha)."],
 "matsumoto-chateau":["chateau",CHATEAU],
 "koyasan-okunoin":["goshuin","Goshuin au bureau près du mausolée de Kōbō Daishi (Gobyō), au fond du cimetière."],
 "koyasan-kongobuji":["goshuin",GOSHUIN],
 "kawagoe-vieille-ville":["site","Goshuin au sanctuaire Hikawa et au temple Kita-in ; tampon à l'office de tourisme de la gare de Kawagoe."],
}
assert set(TAMPONS_OU) <= {a["id"] for a in acts}, set(TAMPONS_OU) - {a["id"] for a in acts}

# Gare principale de chaque ville (tampon de gare)
GARE_DEFAUT = "Cherchez une table avec un tampon et un encreur (panneau スタンプ / 駅スタンプ), en général juste à l'extérieur des portiques principaux ou près du guichet JR (みどりの窓口 Midori no madoguchi). Sinon, demandez au guichet."
GARES = {
 "tokyo":["Gare de Tokyo (東京駅)","Sortie Marunouchi Sud (丸の内南口), au rez-de-chaussée, sous la coupole, à gauche en sortant des portiques. Le métro Tokyo Metro propose aussi des tampons commémoratifs dans ses bureaux d'information."],
 "kyoto":["Gare de Kyoto (京都駅)",GARE_DEFAUT],
 "osaka":["Gare d'Osaka / Shin-Osaka (大阪駅・新大阪駅)",GARE_DEFAUT],
 "nara":["Gare JR / Kintetsu de Nara (奈良駅)",GARE_DEFAUT],
 "uji":["Gare JR / Keihan d'Uji (宇治駅)",GARE_DEFAUT],
 "naoshima":["Gare JR d'Uno (宇野駅) et terminal de Miyanoura (海の駅なおしま)","Tampon à la gare d'Uno, puis au terminal des ferries de Miyanoura (« Umi no Eki »), au comptoir d'information."],
 "himeji":["Gare de Himeji (姫路駅)",GARE_DEFAUT],
 "hiroshima":["Gare de Hiroshima (広島駅)",GARE_DEFAUT],
 "miyajima":["Gare de Miyajimaguchi et terminal des ferries (宮島口)",GARE_DEFAUT],
 "kanazawa":["Gare de Kanazawa (金沢駅)",GARE_DEFAUT],
 "shirakawago":["Terminal des bus de Shirakawa-go (白川郷)","Tampon touristique au terminal des bus et à l'office de tourisme du village."],
 "takayama":["Gare de Takayama (高山駅)",GARE_DEFAUT],
 "kawaguchiko":["Gare de Kawaguchiko (河口湖駅)",GARE_DEFAUT],
 "hakone":["Gare de Hakone-Yumoto (箱根湯本駅)",GARE_DEFAUT],
 "kamakura":["Gare de Kamakura (鎌倉駅)",GARE_DEFAUT],
 "nikko":["Gare de Nikkō (日光駅)",GARE_DEFAUT],
 "nagoya":["Gare de Nagoya (名古屋駅)",GARE_DEFAUT],
 "nagano":["Gare de Nagano (長野駅)",GARE_DEFAUT],
 "matsumoto":["Gare de Matsumoto (松本駅)",GARE_DEFAUT],
 "kobe":["Gare de Sannomiya / Shin-Kobe (三ノ宮・新神戸)",GARE_DEFAUT],
 "koyasan":["Gare de Gokurakubashi / téléphérique de Kōya-san (極楽橋・高野山)",GARE_DEFAUT],
 "yokohama":["Gare de Yokohama (横浜駅)",GARE_DEFAUT],
 "kawagoe":["Gare de Kawagoe (川越駅)",GARE_DEFAUT],
 "hitachi":["Gare de Katsuta (勝田駅)",GARE_DEFAUT],
}
assert set(GARES) == ids, ids ^ set(GARES)
TAMPONS["trouver"] = [
 "Repérez les panneaux スタンプ (sutanpu) ou 記念スタンプ (tampon souvenir) ; pour les goshuin : 御朱印 (goshuin).",
 "Gares : en général juste à l'extérieur des portiques principaux ou près du guichet JR ; parfois à l'intérieur, ou gardé derrière le guichet (il suffit de demander).",
 "Sites : guichet, accueil, boutique, sortie du parcours, ou office de tourisme le plus proche.",
 "Goshuin : bureau des amulettes ou des goshuin, souvent près du pavillon principal ; fermé en fin d'après-midi.",
 "Faites d'abord un essai sur une feuille : les tampons anciens marquent parfois peu. Notez le lieu et la date à côté.",
 "Le site stamp.funakiya.com recense les tampons des gares avec leur emplacement (en japonais, avec photos).",
]
TAMPONS["phrases"] = [
 {"ja":"スタンプはどこですか？","fr":"Où est le tampon ? (sutanpu wa doko desu ka)"},
 {"ja":"御朱印をお願いします。","fr":"Un goshuin, s'il vous plaît. (goshuin o onegaishimasu)"},
]
TAMPONS["ou"] = TAMPONS_OU
TAMPONS["gares_villes"] = GARES
TAMPONS["lien"] = "https://stamp.funakiya.com/"

# Règles d'ouverture des réservations (heure du Japon)
RESA = {
 "tokyo-pokemon-cafe": {"type":"JOURS","jours":31,"heure":"18:00","note":"Ouverture environ 1 mois avant à 18 h (heure du Japon), parfois par périodes : vérifier le site officiel."},
 "osaka-pokemon-cafe": {"type":"JOURS","jours":31,"heure":"18:00","note":"Ouverture environ 1 mois avant à 18 h (heure du Japon), parfois par périodes : vérifier le site officiel."},
 "tokyo-kirby-cafe": {"type":"MOIS_JOUR","mois":1,"jour":10,"heure":"18:00","note":"Le 10 du mois précédent (à vérifier) ; créer le compte et valider le téléphone avant."},
 "nagoya-ghibli": {"type":"MOIS_JOUR","mois":2,"jour":10,"heure":"14:00","note":"Lawson Ticket ou Klook (vente internationale)."},
 "tokyo-ghibli": {"type":"MOIS_JOUR","mois":1,"jour":10,"heure":"10:00","note":"Lawson Ticket, vente pour tout le mois suivant."},
 "uji-nintendo": {"type":"TIRAGE","mois":3,"note":"Inscription au tirage au sort pendant le mois indiqué (compte Nintendo)."},
 "tokyo-disneysea": {"type":"MOIS_MEME_JOUR","mois":2,"heure":"14:00","note":"Site ou appli officielle Tokyo Disney Resort, ou Klook."},
 "tokyo-disneyland": {"type":"MOIS_MEME_JOUR","mois":2,"heure":"14:00","note":"Site ou appli officielle Tokyo Disney Resort, ou Klook."},
 "tokyo-shibuyasky": {"type":"JOURS","jours":28,"heure":"00:00","note":"Délai variable selon les sources (2 à 4 semaines) : vérifier sur le site officiel."},
}
for a in acts:
    if a["id"] in RESA: a["resa"]=RESA[a["id"]]
for k in RESA: assert any(a["id"]==k for a in acts), k
for a in acts:
    if a["id"]=="tokyo-sumo": a["heure"]="07:30"
# Manger & sortir / Shopping : id, ville, nom, categorie, description, lat, lon, conseil, activiteId
L = [
("l-tokyo-ramenstreet","tokyo","Tokyo Ramen Street","RAMEN","Huit comptoirs de ramen au sous-sol de la gare de Tokyo.",35.6812,139.7671,"Pratique un jour de trajet en Shinkansen.",""),
("l-tokyo-ichiran","tokyo","Ichiran Shibuya","RAMEN","Ramen tonkotsu servis dans des box individuels.",35.6614,139.7010,"Chaîne présente dans toutes les grandes villes.",""),
("l-tokyo-afuri","tokyo","AFURI Harajuku","RAMEN","Ramen légers au bouillon parfumé au yuzu.",35.6709,139.7062,"",""),
("l-yokohama-ramenmuseum","yokohama","Musée du ramen de Shin-Yokohama","RAMEN","Décor de rue des années 1950 et comptoirs de ramen de tout le Japon.",35.5090,139.6170,"Mini-bols pour goûter plusieurs styles.",""),
("l-tokyo-sushizanmai","tokyo","Sushi Zanmai Tsukiji","SUSHI","Sushis frais près du marché extérieur de Tsukiji.",35.6655,139.7705,"",""),
("l-tokyo-uobei","tokyo","Uobei Shibuya","SUSHI","Sushis commandés sur tablette et livrés par mini-trains express.",35.6590,139.6980,"Très ludique avec un enfant.",""),
("l-tokyo-monja","tokyo","Rue du monjayaki (Tsukishima)","SPECIALITES","Des dizaines de restaurants de monjayaki, la galette de Tokyo qu'on cuit soi-même.",35.6630,139.7820,"",""),
("l-tokyo-pokemoncafe","tokyo","Pokémon Café Tokyo","CAFE_THEME","Café Pokémon à Nihonbashi.",35.6810,139.7740,"Sur réservation.","tokyo-pokemon-cafe"),
("l-tokyo-kirbycafe","tokyo","Kirby Café Tokyo","CAFE_THEME","Café Kirby à Tokyo Skytree Solamachi.",35.7100,139.8120,"Sur réservation.","tokyo-kirby-cafe"),
("l-tokyo-mocha","tokyo","Bar à chats MOCHA","CAFE_ANIMAUX","Chaîne de bars à chats (Shibuya, Harajuku, Ikebukuro, Akihabara…).",35.6600,139.7000,"Vérifier l'âge minimum accepté selon l'établissement.",""),
("l-tokyo-itoya","tokyo","G.Itoya (Ginza)","PAPETERIE","Papeterie mythique sur une douzaine d'étages.",35.6719,139.7671,"",""),
("l-tokyo-loft","tokyo","Loft Shibuya","PAPETERIE","Papeterie, gadgets et cosmétiques.",35.6620,139.6990,"",""),
("l-tokyo-hands","tokyo","Hands Shinjuku","PAPETERIE","Bricolage, papeterie et objets malins.",35.6878,139.7024,"",""),
("l-tokyo-sekaido","tokyo","Sekaido Shinjuku","PAPETERIE","Matériel de dessin et de manga à prix doux.",35.6905,139.7055,"",""),
("l-tokyo-gigo","tokyo","GiGO Akihabara","ARCADE","Salles d'arcade sur plusieurs étages : pinces, rythme, jeux vidéo.",35.6995,139.7710,"",""),
("l-tokyo-taito","tokyo","Taito Station Akihabara","ARCADE","Grande salle d'arcade du quartier électrique.",35.6990,139.7720,"",""),
("l-tokyo-round1","tokyo","Round1 Stadium Ikebukuro","ARCADE","Arcade, bowling et sports en salle (Spo-Cha).",35.7300,139.7140,"",""),
("l-tokyo-gashapon-ikebukuro","tokyo","Gashapon Department Store Ikebukuro","GACHAPON","Environ 3 000 machines à boules surprises (Sunshine City, 3e étage).",35.7289,139.7193,"Monnayeurs sur place : prévoir des pièces de 100 ¥.",""),
("l-tokyo-crossstore","tokyo","Bandai Namco Cross Store Tokyo","GACHAPON","Record mondial de machines à gachapon, à Ikebukuro.",35.7300,139.7170,"",""),
("l-tokyo-gashapon-akiba","tokyo","Gashapon Department Store Akihabara","GACHAPON","Au 4e étage de la salle namco Akihabara.",35.6993,139.7714,"",""),
("l-tokyo-nintendo","tokyo","Nintendo TOKYO","BOUTIQUE_THEME","Boutique officielle Nintendo (Shibuya PARCO, 6e étage).",35.6620,139.6987,"",""),
("l-tokyo-pokemondx","tokyo","Pokémon Center Tokyo DX","BOUTIQUE_THEME","Grande boutique Pokémon à Nihonbashi, à côté du Pokémon Café.",35.6810,139.7740,"",""),
("l-tokyo-characterstreet","tokyo","Character Street (gare de Tokyo)","BOUTIQUE_THEME","Une trentaine de boutiques de personnages, dont Ghibli (Donguri Kyowakoku).",35.6800,139.7680,"",""),
("l-tokyo-kiddyland","tokyo","Kiddy Land Harajuku","BOUTIQUE_THEME","Jouets et personnages sur plusieurs étages.",35.6680,139.7070,"",""),
("l-tokyo-nakano","tokyo","Nakano Broadway","BOUTIQUE_THEME","Galerie de boutiques de manga, figurines et objets de collection.",35.7090,139.6660,"",""),
("l-tokyo-donki","tokyo","Don Quijote Shibuya","SOUVENIRS","Bazar géant ouvert tard : snacks, KitKat, souvenirs.",35.6610,139.6970,"Détaxe sur présentation du passeport.",""),
("l-tokyo-daiso","tokyo","Daiso Harajuku","SOUVENIRS","Boutique à 100 ¥ : petits souvenirs et objets pratiques.",35.6710,139.7040,"",""),
("l-osaka-kinryu","osaka","Kinryu Ramen Dotonbori","RAMEN","Ramen sous le célèbre dragon, ouvert jour et nuit.",34.6687,135.5030,"",""),
("l-osaka-ichiran","osaka","Ichiran Dotonbori","RAMEN","Ramen tonkotsu en box individuels.",34.6688,135.5020,"",""),
("l-osaka-chibo","osaka","Chibo Dotonbori","SPECIALITES","Okonomiyaki cuit devant vous sur plaque chauffante.",34.6688,135.5025,"",""),
("l-osaka-takoyaki","osaka","Takoyaki à Dotonbori","SPECIALITES","Boulettes de poulpe brûlantes, la spécialité d'Osaka.",34.6687,135.5013,"",""),
("l-osaka-pokemoncafe","osaka","Pokémon Café Osaka","CAFE_THEME","Café Pokémon au Daimaru Shinsaibashi.",34.6740,135.5010,"Sur réservation.","osaka-pokemon-cafe"),
("l-osaka-pokemondx","osaka","Pokémon Center Osaka DX","BOUTIQUE_THEME","Grande boutique Pokémon au Daimaru Shinsaibashi.",34.6740,135.5010,"",""),
("l-osaka-nintendo","osaka","Nintendo OSAKA","BOUTIQUE_THEME","Boutique officielle Nintendo (Daimaru Umeda).",34.7020,135.4960,"",""),
("l-osaka-denden","osaka","Den Den Town (Nipponbashi)","BOUTIQUE_THEME","Le quartier geek d'Osaka : jeux vidéo, figurines, arcades.",34.6590,135.5060,"",""),
("l-osaka-round1","osaka","Round1 Sennichimae","ARCADE","Arcade, bowling et karaoké près de Namba.",34.6660,135.5040,"",""),
("l-osaka-loft","osaka","Loft Umeda","PAPETERIE","Papeterie et gadgets.",34.7060,135.4990,"",""),
("l-osaka-donki","osaka","Don Quijote Dotonbori","SOUVENIRS","Bazar géant avec une grande roue sur la façade.",34.6688,135.5034,"",""),
("l-kyoto-ramenkoji","kyoto","Kyoto Ramen Koji","RAMEN","Comptoirs de ramen régionaux au 10e étage de la gare de Kyoto.",34.9858,135.7588,"",""),
("l-kyoto-tsujiri","kyoto","Gion Tsujiri","SPECIALITES","Parfaits et desserts au matcha dans Gion.",35.0036,135.7740,"File d'attente fréquente.",""),
("l-kyoto-nintendo","kyoto","Nintendo KYOTO","BOUTIQUE_THEME","Boutique officielle Nintendo (Takashimaya Kyoto).",35.0036,135.7690,"",""),
("l-kyoto-loft","kyoto","Loft Kyoto","PAPETERIE","Papeterie et gadgets près de Kawaramachi.",35.0040,135.7680,"",""),
("l-nagoya-yabaton","nagoya","Yabaton","SPECIALITES","Le miso-katsu, porc pané à la sauce miso, spécialité de Nagoya.",35.1620,136.9050,"",""),
("l-nagoya-horaiken","nagoya","Atsuta Horaiken","SPECIALITES","Hitsumabushi : anguille grillée sur riz, à déguster de trois façons.",35.1275,136.9080,"Files d'attente : venir tôt.",""),
]
# Idées pour les escales longues (> 2 h), par aéroport
ESCALES = {
 "AMS": {
  "plan": "https://www.schiphol.com/en/airport-maps",
  "idees": [
   {"titre":"Rijksmuseum Schiphol","texte":"Mini-musée gratuit d'art néerlandais, côté embarquement (Holland Boulevard, entre les halls 2 et 3), ouvert 24 h/24.","recherche":"Rijksmuseum Schiphol"},
   {"titre":"Airport Library","texte":"Bibliothèque avec livres, iPads et canapés, juste à côté du musée : parfait pour souffler avec un enfant.","recherche":"Airport Library Schiphol"},
   {"titre":"Goûter néerlandais","texte":"Stroopwafels, poffertjes ou kroketten dans les cafés de Holland Boulevard.","recherche":"Holland Boulevard Schiphol"},
   {"titre":"Voir les avions","texte":"Cherchez un point de vue sur les pistes depuis les grandes baies vitrées des halls.","recherche":""},
   {"titre":"Sortir à Amsterdam (escale de 5 h et plus)","texte":"Arrivant de Marseille (espace Schengen), vous pouvez sortir sans formalité : train jusqu'à Amsterdam Centraal (~15-20 min). Prévoyez d'être revenus à l'aéroport au moins 2 h avant le vol suivant (contrôle des passeports pour le Japon). Avec 6 h 05 d'escale, cela laisse environ 2 h 30 en ville : balade le long des canaux autour de la gare.","recherche":"Amsterdam Centraal"}
  ]
 },
 "CDG": {
  "plan": "https://cdgfacile.com/plans-aeroport-roissy-charlesdegaulle/",
  "idees": [
   {"titre":"Nouveaux noms des terminaux","texte":"Depuis le 16 mars 2027 : arrivée de Tokyo au Terminal 5 (ex-2E), départ pour Marseille au Terminal 6 (ex-2F). Les deux sont voisins et reliés à pied.","recherche":""},
   {"titre":"Passage de la frontière","texte":"En arrivant de Tokyo (hors Schengen), il faut passer la police aux frontières avant le vol pour Marseille : gardez du temps pour cette étape.","recherche":""},
   {"titre":"Aires de jeux et Wi-Fi","texte":"Les terminaux proposent aires de jeux pour enfants, Wi-Fi gratuit, restaurants et boutiques.","recherche":"aire de jeux aéroport Charles de Gaulle terminal 2F"},
   {"titre":"Paris : déconseillé","texte":"Une sortie dans Paris demande au moins 6 à 7 h d'escale : avec 4 h 55, restez à l'aéroport.","recherche":""}
  ]
 },
}
lieux=[dict(id=a,villeId=b,nom=c,categorie=d,description=e,lat=f,lon=g,conseil=h,activiteId=i) for a,b,c,d,e,f,g,h,i in L]
for l in lieux:
    assert l["villeId"] in ids, l
    if l["activiteId"]: assert any(a["id"]==l["activiteId"] for a in acts), l
assert len({l["id"] for l in lieux})==len(lieux)
# Descriptions qui donnent envie + terme de recherche de la photo (outils/accroches.py)
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from accroches import ACCROCHES
for _a in acts:
    if _a["id"] in ACCROCHES:
        # Description courte pour la liste des envies ; description détaillée pour la fiche
        _a["resume"] = _a["description"]
        _a["description"], _a["photo"] = ACCROCHES[_a["id"]]

# ---------------------------------------------------------------------------
# Version, date de vérification et journal des changements (affiché dans l'appli : « Informations mises à jour »)
# À chaque publication : incrémenter VERSION, mettre VERIFIE à la date du jour, ajouter une entrée à CHANGEMENTS.
# ---------------------------------------------------------------------------
VERSION = 18
VERIFIE = "2026-11-28"
CHANGEMENTS = [
 {"version":18,"date":"2026-11-28","textes":[
   "Trajet détaillé aéroport du Kansai → Hiroshima (Haruka puis Shinkansen, ~2 h 45 porte-à-porte).",
 ]},
 {"version":17,"date":"2026-11-28","textes":[
   "Naoshima ajoutée (île de l'art) : trajets détaillés depuis l'aéroport du Kansai, Osaka, Kyoto, Hiroshima et Tokyo, et trois visites.",
   "Durées de trajet porte-à-porte : correspondances et accès aux gares compris, comme sur Google Maps.",
   "Photos des villes corrigées (Kobe affichait une mauvaise photo).",
 ]},
 {"version":16,"date":"2026-11-22","textes":[
   "Tampons : où trouver les tampons de gares, des sites, des châteaux et les goshuin dans chaque ville.",
 ]},
 {"version":15,"date":"2026-11-22","textes":[
   "Sur place : plans de métro et de bus à télécharger (Tokyo, Osaka, Kyoto, Hiroshima).",
   "Sur place : guide de l'envoi de bagages (takkyūbin) et des tampons (gares, goshuin).",
 ]},
 {"version":14,"date":"2026-11-22","textes":[
   "Sur place : nouvelle rubrique « Us et coutumes » (poubelles, pourboire, chaussures, tatouages, onsen, trains…).",
   "Trajets : côté des escalators selon la ville et heures de pointe.",
 ]},
 {"version":13,"date":"2026-11-22","textes":[
   "Météo : climat moyen de juin pour chaque ville (au-delà de 16 jours de prévisions).",
   "Urgences : numéros utiles (110, 119, Japan Visitor Hotline, ambassade de France).",
 ]},
 {"version":12,"date":"2026-11-22","textes":[
   "Liste des envies : description courte pour chaque visite, description détaillée dans la fiche.",
   "Photos des villes et des adresses « Manger & sortir » ajoutées pour la carte et les vignettes.",
 ]},
 {"version":11,"date":"2026-11-22","textes":[
   "Nouvelles descriptions pour les 102 suggestions de visites, et photos des lieux téléchargeables (carte interactive).",
 ]},
 {"version":10,"date":"2026-11-22","textes":[
   "Mise en place de la mise à jour automatique des informations (lieux, trains, fêtes) dès que l'appli est en ligne.",
   "Fêtes et saisons de juin 2027 vérifiées : dates 2027 encore non publiées pour Sanno Matsuri, Torigoe Matsuri et le train des hortensias de Hakone.",
 ]},
]
import os, sys
SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
json.dump({"version":VERSION,"verifie":VERIFIE,"changements":CHANGEMENTS,"villes":villes,"activites":acts,"routes":routes,"aeroports":AEROPORTS,"lieux":lieux,"escales":ESCALES,"arrivees":ARRIVEES,"troncons":TRONCONS,"evenements":EVENEMENTS,"climat_juin":CLIMAT_JUIN,"urgences":URGENCES,"coutumes":COUTUMES,"escalators":{"villes":ESCALATORS,"textes":ESCALATORS_TEXTES,"general":ESCALATORS_GENERAL},"heures_pointe":HEURES_POINTE,"plans":PLANS,"bagages":BAGAGES,"tampons":TAMPONS},open(os.path.join(SORTIE,"suggestions.json"),"w"),ensure_ascii=False,indent=1)
