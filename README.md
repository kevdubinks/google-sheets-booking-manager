# 🏢 Google Sheets Booking Management

**Gestion automatique des réservations de salles de conférence via Google Sheets.**

## 🎯 Pour qui ?
Responsables de réservation dans les salles de conférence, espaces de coworking, centres d'affaires.

## ⚡ Ce que ça fait
- Ajoute des réservations automatiquement dans Google Sheets
- Vérifie la disponibilité des salles en temps réel
- Envoie des alertes quand une réservation arrive à expiration
- Zéro coût (Google Sheets gratuit, API Google gratuite)

## 📦 Installation (5 minutes)

```bash
pip install google-auth google-api-python-client
```

1. Créez un projet sur [Google Cloud Console](https://console.cloud.google.com)
2. Activez l'API Google Sheets
3. Créez un compte de service et téléchargez `credentials.json`
4. Créez un Google Sheet avec un onglet "Reservations"
5. Remplacez `SPREADSHEET_ID` par l'ID de votre Google Sheet

## 🚀 Utilisation

```bash
python booking_manager.py
```

## 📊 Structure du Google Sheet

| Salle | Date début | Date fin | Client | Notes |
|-------|-----------|---------|--------|-------|
| Salle A | 2026-06-15 | 2026-06-16 | Équipe Marketing | Réunion trimestrielle |

## ⚙️ Personnalisation

- Modifiez `BOOKING_RANGE` pour changer la plage de cellules
- Ajustez le paramètre `days` dans `check_upcoming_endings()` pour modifier le délai d'alerte

---

*Généré par Agent IA autonome — Projet d'expérimentation business*
