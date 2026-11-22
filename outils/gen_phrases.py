import json
P = {
 "Essentiels": [
  ("Bonjour","こんにちは","konnichiwa"),
  ("Merci beaucoup","ありがとうございます","arigatō gozaimasu"),
  ("Excusez-moi (pour appeler ou s'excuser)","すみません","sumimasen"),
  ("Oui / Non","はい / いいえ","hai / iie"),
  ("Je ne comprends pas","わかりません","wakarimasen"),
  ("Parlez-vous anglais ?","英語を話せますか？","eigo o hanasemasu ka ?"),
  ("Pouvez-vous l'écrire, s'il vous plaît ?","書いてもらえますか？","kaite moraemasu ka ?"),
  ("Où sont les toilettes ?","トイレはどこですか？","toire wa doko desu ka ?"),
  ("Nous venons de France","フランスから来ました","furansu kara kimashita"),
  ("Au revoir","さようなら","sayōnara"),
 ],
 "Restaurant": [
  ("Nous sommes trois","三人です","san-nin desu"),
  ("La carte, s'il vous plaît","メニューをお願いします","menyū o onegaishimasu"),
  ("Avez-vous une carte en anglais ?","英語のメニューはありますか？","eigo no menyū wa arimasu ka ?"),
  ("Ceci, s'il vous plaît (en montrant)","これをお願いします","kore o onegaishimasu"),
  ("De l'eau, s'il vous plaît","お水をお願いします","o-mizu o onegaishimasu"),
  ("Pas épicé, s'il vous plaît","辛くしないでください","karaku shinaide kudasai"),
  ("Avez-vous un menu enfant ?","お子様メニューはありますか？","okosama menyū wa arimasu ka ?"),
  ("L'addition, s'il vous plaît","お会計をお願いします","o-kaikei o onegaishimasu"),
  ("Peut-on payer par carte ?","カードで払えますか？","kādo de haraemasu ka ?"),
  ("C'était délicieux, merci (en partant)","ごちそうさまでした","gochisōsama deshita"),
 ],
 "Allergies & santé": [
  ("Je suis allergique à … (montrer l'aliment)","…のアレルギーがあります","… no arerugī ga arimasu"),
  ("Je ne mange pas de viande","肉は食べられません","niku wa taberaremasen"),
  ("Sans porc, s'il vous plaît","豚肉抜きでお願いします","butaniku nuki de onegaishimasu"),
  ("Y a-t-il des fruits de mer dedans ?","魚介類は入っていますか？","gyokairui wa haitte imasu ka ?"),
  ("Où est la pharmacie la plus proche ?","一番近い薬局はどこですか？","ichiban chikai yakkyoku wa doko desu ka ?"),
  ("J'ai mal ici","ここが痛いです","koko ga itai desu"),
 ],
 "Transports": [
  ("Où est la gare ?","駅はどこですか？","eki wa doko desu ka ?"),
  ("Ce train va-t-il à … ?","この電車は…に行きますか？","kono densha wa … ni ikimasu ka ?"),
  ("Quel quai pour … ?","…行きは何番線ですか？","… iki wa nan-bansen desu ka ?"),
  ("Un aller simple pour …, s'il vous plaît","…まで片道一枚お願いします","… made katamichi ichi-mai onegaishimasu"),
  ("Je voudrais réserver des places","席を予約したいです","seki o yoyaku shitai desu"),
  ("Trois places côte à côte, s'il vous plaît","三人並んで座れる席をお願いします","san-nin narande suwareru seki o onegaishimasu"),
  ("Je voudrais recharger ma carte","チャージしたいです","chāji shitai desu"),
  ("À cette adresse, s'il vous plaît (taxi)","この住所までお願いします","kono jūsho made onegaishimasu"),
  ("Arrêtez-vous ici, s'il vous plaît","ここで止めてください","koko de tomete kudasai"),
 ],
 "Hôtel": [
  ("J'ai une réservation au nom de …","…の名前で予約しています","… no namae de yoyaku shite imasu"),
  ("Pouvez-vous garder nos bagages ?","荷物を預かってもらえますか？","nimotsu o azukatte moraemasu ka ?"),
  ("À quelle heure est le petit-déjeuner ?","朝食は何時からですか？","chōshoku wa nan-ji kara desu ka ?"),
  ("Je voudrais envoyer cette valise à … (takkyubin)","このスーツケースを…に送りたいです","kono sūtsukēsu o … ni okuritai desu"),
  ("Quel est le mot de passe du Wi-Fi ?","Wi-Fiのパスワードは何ですか？","wai-fai no pasuwādo wa nan desu ka ?"),
 ],
 "Shopping": [
  ("Combien ça coûte ?","いくらですか？","ikura desu ka ?"),
  ("Est-ce possible en détaxe (tax free) ?","免税できますか？","menzei dekimasu ka ?"),
  ("Je regarde seulement","見ているだけです","mite iru dake desu"),
  ("Avez-vous une autre taille ?","他のサイズはありますか？","hoka no saizu wa arimasu ka ?"),
  ("Un sac, s'il vous plaît","袋をお願いします","fukuro o onegaishimasu"),
 ],
 "Urgences": [
  ("Au secours !","助けて！","tasukete !"),
  ("Appelez une ambulance, s'il vous plaît","救急車を呼んでください","kyūkyūsha o yonde kudasai"),
  ("Appelez la police, s'il vous plaît","警察を呼んでください","keisatsu o yonde kudasai"),
  ("Mon enfant s'est perdu","子供が迷子になりました","kodomo ga maigo ni narimashita"),
  ("J'ai perdu mon passeport","パスポートをなくしました","pasupōto o nakushimashita"),
  ("Où est l'hôpital ?","病院はどこですか？","byōin wa doko desu ka ?"),
 ],
 "Pour les enfants": [
  ("Je m'appelle …","…です","… desu"),
  ("J'ai 11 ans","11歳です","jū-issai desu"),
  ("Je suis perdue, aidez-moi s'il vous plaît","迷子です。助けてください","maigo desu. tasukete kudasai"),
  ("C'est trop mignon !","かわいい！","kawaii !"),
  ("Bonne nuit","おやすみなさい","oyasuminasai"),
 ],
}
out=[{"theme":t,"phrases":[{"fr":a,"ja":b,"romaji":c} for a,b,c in l]} for t,l in P.items()]
import os, sys
SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
json.dump({"version":1,"themes":out},open(os.path.join(SORTIE,'phrases.json'),'w'),ensure_ascii=False,indent=1)
print(sum(len(l) for l in P.values()))
