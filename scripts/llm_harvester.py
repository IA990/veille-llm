import os
import requests
from datetime import datetime

OUTPUT_DIR = "data/llm_catalog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEBUG = True
def log(msg):
    if DEBUG:
        print(msg)

def fetch_llm_data():
    try:
        response = requests.get("https://example.com/api/llms")
        if response.status_code != 200:
            log(f"[Erreur] Impossible d'obtenir les données LLM ({response.status_code})")
            return []
        log("[✓] Données récupérées avec succès")
        return response.json()
    except Exception as e:
        log(f"[Erreur] Exception : {e}")
        return []

REQUIRED_KEYS = ["name", "provider", "description", "url"]
def create_markdown_file(llm):
    if not all(key in llm for key in REQUIRED_KEYS):
        log(f"[⚠️] Fiche ignorée — données incomplètes : {llm}")
        return

    filename = f"{llm['name'].replace(' ', '_').lower()}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {llm['name']}\n\n")
        f.write(f"**Date d'ajout** : {datetime.utcnow().strftime('%Y-%m-%d')}\n\n")
        f.write(f"**Développeur** : {llm['provider']}\n\n")
        f.write(f"**Description** : {llm['description']}\n\n")
        f.write(f"**Site officiel** : [{llm['url']}]({llm['url']})\n")

    log(f"[✓] Fiche créée : {filename}")

def main():
    llms = fetch_llm_data()
    if not llms:
        log("[!] Aucune fiche LLM créée.")
        return

    for llm in llms:
        create_markdown_file(llm)

    log(f"[✓] Terminé — {len(llms)} fiches générées")

if __name__ == "__main__":
    main()
