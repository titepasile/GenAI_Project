# Swiss Agent (LangGraph)

Ein Chatbot-Agent, der mit LangGraph in einem Jupyter Notebook gebaut wird.
Das Hauptnotebook ist `05_swiss_agent_langgraph.ipynb`.

---

## Inhalt

- [Swiss Agent (LangGraph)](#swiss-agent-langgraph)
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
- Ein **LiteLLM-API-Key** (Pflicht, wird vom Projektverantwortlichen bereitgestellt)
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
   | `LITELLM_API_KEY` | Ja | Zugriff auf das Modell über den LiteLLM-Proxy |
   | `LANGSMITH_API_KEY` | Nein | Tracing in LangSmith. Ohne Key läuft das Notebook trotzdem. |

3. Speichern. Fertig.

Die Datei `.env` steht in der `.gitignore` und wird deshalb nicht hochgeladen.

Das Notebook liest die Keys automatisch mit `load_dotenv()`. Fehlt `LITELLM_API_KEY`, fragt es beim Ausführen danach (Eingabefeld).

Modellname und Server-Adresse (`LLM_MODEL`, `LLM_BASE_URL`) stehen direkt im Notebook und müssen nicht in die `.env`.

---

## 4. Notebook starten

1. `05_swiss_agent_langgraph.ipynb` in VS Code öffnen.
2. Oben rechts auf **«Kernel auswählen»** klicken.
3. **«Python-Umgebungen»** wählen, dann den Eintrag mit **`.venv`**.
   Falls VS Code fragt, ob `ipykernel` installiert werden soll: **Ja**.
4. Die Setup-Zellen von oben nach unten ausführen (`Shift + Enter`). Die erste Code-Zelle (`%pip install -r requirements.txt`) installiert die Pakete nochmals in den gewählten Kernel. Das ist gewollt und stellt sicher, dass alle denselben Stand haben.
5. Die Verbindungstest-Zelle (`llm.invoke("Antworte mit einem Wort: bereit?")`) muss eine Antwort liefern. Dann ist alles korrekt eingerichtet.
6. Danach die restlichen Zellen der Reihe nach ausführen.

Bei Änderungen in `.env` muss der Kernel neu gestartet werden (*Restart* oben im Notebook) und die Zellen müssen erneut laufen.

> **Hinweis:** Die Grafik des Graphen (Schritt 8) wird über das Internet erzeugt. Ohne Internetverbindung fehlt sie, der Rest funktioniert.

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
├── 05_swiss_agent_langgraph.ipynb  # Hauptnotebook
├── README.md                       # diese Anleitung
└── requirements.txt                # benötigte Pakete
```
