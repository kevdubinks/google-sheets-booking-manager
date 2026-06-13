"""
Google Sheets Booking Management — Gestion des réservations de salles de conférence
Par Agent IA autonome | Optimisé pour responsables de réservation
"""

import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Configuration
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "VOTRE_ID_GOOGLE_SHEETS"  # À remplacer
BOOKING_RANGE = "Reservations!A1:E100"

def get_service():
    """Authentifie et retourne le service Google Sheets."""
    creds = Credentials.from_authorized_user_file("credentials.json", SCOPES)
    return build("sheets", "v4", credentials=creds)

def get_bookings(service):
    """Récupère toutes les réservations."""
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range=BOOKING_RANGE
    ).execute()
    return result.get("values", [])

def add_booking(service, room, start_date, end_date, client="", notes=""):
    """Ajoute une nouvelle réservation."""
    data = [[room, start_date, end_date, client, notes]]
    body = {"values": data}
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID, range="Reservations!A1",
        valueInputOption="RAW", insertDataOption="INSERT_ROWS", body=body
    ).execute()
    print(f"✅ Réservation ajoutée : {room} du {start_date} au {end_date}")

def is_room_available(service, start_date, end_date, room):
    """Vérifie si une salle est disponible sur une période."""
    bookings = get_bookings(service)
    for b in bookings:
        if len(b) >= 3 and b[0] == room:
            if not (end_date <= b[1] or start_date >= b[2]):
                return False
    return True

def check_upcoming_endings(service, days=3):
    """Alerte sur les réservations qui se terminent bientôt."""
    today = datetime.date.today()
    bookings = get_bookings(service)
    for b in bookings:
        if len(b) >= 3:
            room, start, end = b[0], b[1], b[2]
            try:
                end_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()
                days_left = (end_date - today).days
                if 0 <= days_left <= days:
                    print(f"⚠️ Alerte : {room} — réservation terminée dans {days_left} jours ({end})")
            except ValueError:
                continue

# === EXEMPLE D'UTILISATION ===
if __name__ == "__main__":
    service = get_service()
    
    # Ajouter une réservation
    add_booking(service, "Salle A", "2026-06-15", "2026-06-16", "Équipe Marketing")
    
    # Vérifier disponibilité
    if is_room_available(service, "2026-06-15", "2026-06-16", "Salle A"):
        print("✅ Salle A disponible")
    else:
        print("❌ Salle A déjà réservée")
    
    # Vérifier les fins de réservation
    check_upcoming_endings(service, days=3)
