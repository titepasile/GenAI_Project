# DIVA – Digitaler Interner Verwaltungsassistent

Ein Chatbot-Agent für Mitarbeitende, gebaut mit LangGraph in einem Jupyter Notebook, mit Chat-Oberfläche (Gradio).
Das Hauptnotebook ist `diva_agent.ipynb`. Zwei Classifier entscheiden (zuständig? vertraulich?), Tools und ein MCP-Server liefern die Fakten.

---

## Inhalt

- [DIVA – Digitaler Interner Verwaltungsassistent](#diva--digitaler-interner-verwaltungsassistent)
  - [Inhalt](#inhalt)
  - [1. Voraussetzungen](#1-voraussetzungen)
  - [2. Einmaliges Setup](#2-einmaliges-setup)
    - [Schritt 1: Repository klonen](#schritt-1-repository-klonen)
    - [Schritt 2: Terminal in VS Code öffnen](#schritt-2-terminal-in-vs-code-öffnen)
    - [Schritt 3: Virtuelle Umgebung erstellen](#schritt-3-virtuelle-umgebung-erstellen)
    - [Schritt 4: Umgebung aktivieren](#schritt-4-umgebung-aktivieren)
    - [Schritt 5: Pakete installieren](#schritt-5-pakete-installieren)
  - [3. API-Keys einrichten](#3-api-keys-einrichten)
  - [4. Notebook starten](#4-notebook-starten)
  - [5. Täglicher Ablauf](#5-täglicher-ablauf)
  - [6. Zusammenarbeit mit Git](#6-zusammenarbeit-mit-git)
  - [7. Häufige Probleme](#7-häufige-probleme)
  - [Projektstruktur](#projektstruktur)

---

## 1. Voraussetzungen

- **Python 3.13** (alle im Team nutzen dieselbe Version)
- **VS Code** mit den Erweiterungen **Python** und **Jupyter**
- **Git**
- Ein **API-Key für das Modell** (Pflicht). Standard ist das kostenlose `gpt-oss-120b` bei Groq: Key ohne Kreditkarte auf console.groq.com/keys
- Optional: ein kostenloses **LangSmith-Konto** für das Tracing (smith.langchain.com)

Python-Version prüfen:

| System | Befehl |
|---|---|
| Windows | `py --version` |
| Mac | `python3 --version` |

Es sollte `Python 3.13.x` erscheinen.

---

## 2. Einmaliges Setup

Diese Schritte macht jede Person **nur einmal** am Anfang.

### Schritt 1: Repository klonen

Im Terminal (oder VS Code: *Git: Clone*):

```bash
git clone <REPOSITORY-URL>
cd <PROJEKTORDNER>
```

Danach den Ordner in VS Code öffnen (*Datei → Ordner öffnen*).
oder in Bash
```bash
code .
```

### Schritt 2: Terminal in VS Code öffnen

Menü *Terminal → Neues Terminal*. Das Terminal startet im Projektordner.

### Schritt 3: Virtuelle Umgebung erstellen

**Windows:**

```powershell
py -3.13 -m venv .venv
```

**Mac:**

```bash
python3 -m venv .venv
```

Es entsteht ein Ordner `.venv`. Der gehört nur dir und wird **nicht** per Git geteilt.

### Schritt 4: Umgebung aktivieren

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate.bat
```

**Mac:**

```bash
source .venv/bin/activate
```

Wenn es geklappt hat, steht `(.venv)` am Anfang der Terminal-Zeile.

> **Windows-Fehler «Skripts sind deaktiviert»?**
> Einmalig in PowerShell ausführen und danach Schritt 4 wiederholen:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### Schritt 5: Pakete installieren

Mit aktivierter Umgebung `(.venv)`:

```bash
pip install -r requirements.txt
```

Das dauert ein paar Minuten. Danach ist alles installiert.

---

## 3. API-Keys einrichten

API-Keys sind geheim. Sie dürfen **nie** im Code, im Notebook oder in Git landen.

1. Die Datei `.env.example` **kopieren** und die Kopie `.env` nennen:

   **Windows:**
   ```powershell
   copy .env.example .env
   ```

   **Mac:**
   ```bash
   cp .env.example .env
   ```

2. `.env` in VS Code öffnen und die Werte eintragen. Keine Anführungszeichen, keine Leerzeichen um das `=`:

   | Variable | Pflicht? | Wofür |
   |---|---|---|
   | `LLM_API_KEY` | Ja | Zugriff auf das Modell (Groq, Mistral, Gemini oder der Kurs-Proxy). Der alte Name `LITELLM_API_KEY` geht weiterhin |
   | `LLM_MODEL`, `LLM_BASE_URL` | Nein | Nur nötig, um vom Standard (Groq `openai/gpt-oss-120b`) auf ein anderes Modell zu wechseln. Beispiele stehen in `.env.example` |
   | `LANGSMITH_API_KEY` | Nein | Tracing in LangSmith. Ohne Key läuft das Notebook trotzdem. |

3. Speichern. Fertig.

Die Datei `.env` steht in der `.gitignore` und wird deshalb nicht hochgeladen.

Das Notebook liest die Keys automatisch mit `load_dotenv()`. Fehlt der Key, fragt es beim Ausführen danach (Eingabefeld).

Das Notebook hat Standardwerte für Modell und Server-Adresse. Wer wechseln will, ändert nur die `.env`, nicht den Code.

---

## 4. Notebook starten

1. `diva_agent.ipynb` in VS Code öffnen.
2. Oben rechts auf **«Kernel auswählen»** klicken.
3. **«Python-Umgebungen»** wählen, dann den Eintrag mit **`.venv`**.
   Falls VS Code fragt, ob `ipykernel` installiert werden soll: **Ja**.
4. Die Setup-Zellen von oben nach unten ausführen (`Shift + Enter`). Die erste Code-Zelle (`%pip install -r requirements.txt`) installiert die Pakete nochmals in den gewählten Kernel. Das ist gewollt und stellt sicher, dass alle denselben Stand haben.
5. Die Zelle `check_model()` muss dreimal etwas Sinnvolles liefern (Antwort, Tool Calling ✅, Strukturierte Ausgabe ✅). Dann ist alles korrekt eingerichtet.
6. Danach die restlichen Zellen der Reihe nach ausführen.
7. **Chat-Oberfläche:** Die letzte Code-Zelle (`demo.launch(...)`) startet DIVA im Browser (http://127.0.0.1:7860). Beenden mit `demo.close()`.

Bei Änderungen in `.env` muss der Kernel neu gestartet werden (*Restart* oben im Notebook) und die Zellen müssen erneut laufen.

> **Hinweis:** Die Grafik des Graphen wird über das Internet erzeugt. Ohne Internetverbindung gibt das Notebook stattdessen den Mermaid-Text aus, der Rest funktioniert.

---

## 5. Täglicher Ablauf

Bevor du loslegst:

```bash
git pull
```

Falls sich `requirements.txt` geändert hat (steht in der Team-Nachricht oder im Commit):

```bash
pip install -r requirements.txt
```

Ein Neuaufsetzen der `.venv` ist normalerweise **nicht** nötig. VS Code erkennt sie automatisch.

---

## 6. Zusammenarbeit mit Git

**Grundregeln:**

- Immer zuerst `git pull`, dann arbeiten.
- Nicht gleichzeitig im selben Notebook arbeiten, sonst gibt es Konflikte.
- **Vor jedem Commit alle Ausgaben löschen:** Im Notebook oben auf *«Alle Ausgaben löschen»* (Clear All Outputs) klicken. So bleiben die Änderungen klein und übersichtlich.
- Keine Dateien wie `.env` oder `.venv` committen (die `.gitignore` verhindert das).

**Standard-Ablauf zum Speichern der Arbeit:**

```bash
git add .
git commit -m "Kurze Beschreibung der Änderung"
git push
```

**Neues Paket installiert?** Dann `requirements.txt` aktualisieren und dem Team Bescheid geben:

```bash
pip freeze > requirements.txt
```

---

## 7. Häufige Probleme

| Problem | Lösung |
|---|---|
| `ModuleNotFoundError: No module named ...` | Meist falscher Kernel. Oben rechts im Notebook `.venv` wählen. Sonst `pip install -r requirements.txt` ausführen. |
| `(.venv)` steht nicht im Terminal | Umgebung ist nicht aktiviert. Schritt 4 wiederholen. |
| Verbindungstest schlägt fehl (`KeyError: 'LITELLM_API_KEY'` oder Auth-Fehler) | `.env` prüfen: Datei heisst genau `.env`, liegt im Projektordner, Key korrekt, gespeichert. Danach Kernel neu starten. |
| `.venv` erscheint nicht in der Kernel-Liste | VS Code neu laden (`Strg/Cmd + Shift + P` → «Reload Window»). Prüfen, ob `ipykernel` installiert ist: `pip install ipykernel`. |
| Windows: Skripts sind deaktiviert | Siehe Hinweis bei Schritt 4 oder CMD statt PowerShell verwenden. |
| Mac: `python` wird nicht gefunden | Auf dem Mac immer `python3` statt `python` verwenden. |
| Key aus Versehen hochgeladen | **Sofort** beim Anbieter löschen und einen neuen erstellen. Danach Projektverantwortliche informieren. |
| Merge-Konflikt im Notebook | Nicht selbst herumprobieren. Projektverantwortliche fragen. |

---

## Projektstruktur

```
.
├── .venv/                          # lokale Umgebung (nicht in Git)
├── .env                            # echte API-Keys (nicht in Git)
├── .env.example                    # Vorlage für .env
├── .gitignore                      # Dateien, die Git ignoriert
├── diva_agent.ipynb                # Hauptnotebook: Classifier, Tools, Graph, Chat-Oberfläche
├── diva_mcp_server.py              # MCP-Server: liefert die zuständige HR-Ansprechperson
├── docs/                           # Firmendokumente (.md), aktuell erfundene Beispiele
│   ├── personalreglement.md
│   └── merkblatt_austritt.md
├── Projektbeschrieb.md             # Projektbeschrieb
├── README.md                       # diese Anleitung
└── requirements.txt                # benötigte Pakete
```

**Eigene Dokumente verwenden:** Jede `.md`-Datei in `docs/` mit einer Titelzeile (`# Titel`) und Abschnitten (`## Überschrift`) wird automatisch durchsucht. Danach das Notebook neu starten.
