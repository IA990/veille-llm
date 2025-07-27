import os
import requests
from datetime import datetime

OUTPUT_DIR = "data/llm_catalog"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_llm_data():
    # Exemple d'API factice — à adapter selon ta source réelle
    response = requests.get("https://example.com/api/llms")
    if response.status_code != 200:
        print(f"[Erreur] Impossible d'obtenir les données LLM ({response.status_code})")
        return []

    print("[✓] Données récupérées avec succès")
    return response.json()

def create_markdown_file(llm):
    filename = f"{llm['name'].replace(' ', '_').lower()}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {llm['name']}\n\n")
        f.write(f"**Date d'ajout** : {datetime.utcnow().strftime('%Y-%m-%d')}\n\n")
        f.write(f"**Développeur** : {llm['provider']}\n\n")
        f.write(f"**Description** : {llm['description']}\n\n")
        f.write(f"**Site officiel** : [{llm['url']}]({llm['url']})\n")

    print(f"[✓] Fiche créée : {filename}")

def main():
    llms = fetch_llm_data()
    if not llms:
        print("[!] Aucune fiche LLM créée.")
        return

    for llm in llms:
        create_markdown_file(llm)

    print(f"[✓] Terminé — {len(llms)} fiches générées")

if __name__ == "__main__":
    main()
