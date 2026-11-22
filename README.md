# Voyage Japon — informations générales

Données publiques utilisées par l'application familiale **Voyage Japon** : villes, activités, trajets et prix indicatifs des trains,
fêtes et saisons, phrases du traducteur. **Aucune donnée personnelle** (vols, hôtels, dépenses, documents restent sur les téléphones).

L'application télécharge ces fichiers quand elle est en ligne si leur version est plus récente que celle qu'elle contient,
et affiche la liste des changements (« Informations mises à jour »).

## Publier une mise à jour
1. Modifier les données dans `outils/gen_suggestions.py` (ou `outils/gen_phrases.py`).
2. Incrémenter `VERSION`, mettre `VERIFIE` à la date du jour, ajouter une entrée à `CHANGEMENTS`.
3. `python3 outils/publier.py` → régénère `suggestions.json`, `phrases.json` et `version.json`.
4. Commit + push sur `main`.
