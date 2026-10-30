"""MCP-Server für DIVA: liefert die zuständige HR-Ansprechperson zu einem Thema.
 
Läuft als eigener Prozess und wird vom Notebook über stdio angesprochen.
Wichtig: Auf stdout darf nichts anderes als das MCP-Protokoll stehen, also kein print().
"""
 
from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP("diva")
 
# Beispieldaten – später durch das echte HR-Kontaktverzeichnis ersetzen
HR_CONTACTS = {
    "ferien":      {"name": "Sandra Meier",        "email": "s.meier@firma.ch"},
    "arbeitszeit": {"name": "Sandra Meier",        "email": "s.meier@firma.ch"},
    "lohn_spesen": {"name": "Marco Keller",        "email": "m.keller@firma.ch"},
    "absenzen":    {"name": "Nina Frei",           "email": "n.frei@firma.ch"},
    "kuendigung":  {"name": "Nina Frei",           "email": "n.frei@firma.ch"},
    "verhalten":   {"name": "Vertrauensstelle HR", "email": "vertrauen@firma.ch"},
}
GENERAL_HR = {"name": "HR-Team", "email": "hr@firma.ch"}
 
 
@mcp.tool()
def get_hr_contact(category: str) -> dict:
    """Liefert die zuständige HR-Ansprechperson (Name und E-Mail) zu einem Thema.
 
    Mögliche Themen: ferien, arbeitszeit, lohn_spesen, absenzen (inkl. Krankheit,
    Mutterschaft, Vaterschaft), kuendigung, verhalten (Konflikte, Mobbing, Belästigung).
    Gibt es für ein Thema keinen Eintrag, kommt die allgemeine HR-Adresse zurück
    (found=false). Erfinde nie eine andere Adresse.
    """
    key = category.strip().lower()
    contact = HR_CONTACTS.get(key)
    if contact is None:
        return {"found": False, "category": key, **GENERAL_HR,
                "note": "Für dieses Thema ist keine feste Ansprechperson hinterlegt. Allgemeine HR-Adresse."}
    return {"found": True, "category": key, **contact}
 
 
if __name__ == "__main__":
    mcp.run()
    