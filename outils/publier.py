"""Régénère les fichiers d'informations et l'index version.json (lu par l'appli pour savoir s'il y a du nouveau)."""
import json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.join(ICI, "..")
for g in ("gen_suggestions.py", "gen_phrases.py"):
    subprocess.run([sys.executable, os.path.join(ICI, g), RACINE], check=True)
versions = {f: json.load(open(os.path.join(RACINE, f)))["version"] for f in ("suggestions.json", "phrases.json")}
s = json.load(open(os.path.join(RACINE, "suggestions.json")))
json.dump({"fichiers": list(versions), "versions": versions, "verifie": s["verifie"]},
          open(os.path.join(RACINE, "version.json"), "w"), ensure_ascii=False, indent=1)
print("publié :", versions, "vérifié le", s["verifie"])
