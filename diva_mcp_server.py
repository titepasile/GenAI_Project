"""MCP-Server für DIVA: liefert die zuständige HR-Ansprechperson zu einem Thema."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("diva")

# Beispieldaten – später durch echte Zuständigkeiten ersetzen
HR_CONTACTS = {
    "ferien":      {"name": "Sandra Meier", "email": "s.meier@firma.ch"},
    "arbeitszeit": {"name": "Sandra Meier", "email": "s.meier@firma.ch"},
    "lohn_spesen": {"name": "Marco Keller", "email": "m.keller@firma.ch"},
    "absenzen":    {"name": "Nina Frei",    "email": "n.frei@firma.ch"},
    "kuendigung":  {"name": "Nina Frei",    "email": "n.frei@firma.ch"},
    "verhalten":   {"name": "Vertrauensstelle HR", "email": "vertrauen@firma.ch"},
}


@mcp.tool()
def get_hr_contact(category: str) -> str:
    """Liefert die zuständige HR-Ansprechperson (Name und E-Mail) zu einem Thema.

    Mögliche Themen: ferien, arbeitszeit, lohn_spesen, absenzen, kuendigung, verhalten.
    """
    contact = HR_CONTACTS.get(category.strip().lower())
    if contact is None:
        return (f"Für das Thema '{category}' ist keine Ansprechperson hinterlegt. "
                "Allgemeine HR-Adresse: hr@firma.ch")
    return f"Zuständig: {contact['name']} ({contact['email']})"


if __name__ == "__main__":
    mcp.run()  # Kommunikation über stdio, wie beim Dozenten