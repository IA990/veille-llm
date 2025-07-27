# 🧠 veille-llm

Ce dépôt génère automatiquement des fiches de veille sur les modèles LLM et outils associés.

## 📦 Structure

- `data/llm_catalog/` : fiches Markdown (.md) générées
- `scripts/llm_harvester.py` : pipeline Python de récolte
- `.github/workflows/harvest_llms.yml` : exécution hebdomadaire

## ⚙️ Exécution manuelle

Tu peux lancer la récolte manuellement via l'onglet Actions → `Harvest LLMs and Tools`.

## 🔄 Synchronisation

Les fiches sont injectées dans le profil GitHub (dépôt IA990) via un autre workflow.
