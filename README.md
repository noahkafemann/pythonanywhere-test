# Ideenmanager

Eine kleine Flask-Webanwendung zum Verwalten von Ideen mit Titel und Beschreibung.

## Funktionen

- Ideen hinzufügen (Titel + Beschreibung)
- Alle Ideen übersichtlich anzeigen
- Ideen löschen
- SQLite-Datenbank (lokal, keine Installation nötig)
- Mobilfreundliches, modernes Design (Bootstrap 5)
- Bereit für PythonAnywhere

## Projektstruktur

```
ideenmanager/
├── app.py              # Flask-Anwendung
├── requirements.txt    # Python-Abhängigkeiten
├── .gitignore
├── templates/
│   ├── base.html       # Basis-Layout
│   └── index.html      # Hauptseite
└── static/
    └── style.css       # Eigenes CSS
```

## Lokale Installation

### 1. Repository klonen
```bash
git clone <dein-repo-url>
cd ideenmanager
```

### 2. Virtuelle Umgebung erstellen (empfohlen)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# oder: venv\Scripts\activate  # Windows
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. Anwendung starten
```bash
python app.py
```

Die App läuft nun unter `http://localhost:5000`.

## Deployment auf PythonAnywhere (Schritt-für-Schritt)

Diese Anleitung führt dich durch den kompletten Prozess – von der Anmeldung bis zur laufenden App.

---

### Voraussetzungen

- Ein **PythonAnywhere-Account** (kostenloser "Beginner"-Plan reicht)
- Dein Code liegt in einem **GitHub-Repository** (z. B. `https://github.com/noahkafemann/pythonanywhere-test`)
- Branch: `kilo/short-photon-dga` (oder `main`, falls du gemerged hast)

---

### Schritt 1: Bei PythonAnywhere anmelden & Bash-Konsole öffnen

1. Gehe zu https://www.pythonanywhere.com und melde dich an.
2. Klicke oben auf **Consoles** → **Start a new console** → **Bash** (nicht "Python").
   - Du landest in deinem Home-Verzeichnis: `/home/deinusername`

---

### Schritt 2: Repository klonen

In der Bash-Konsole:

```bash
git clone https://github.com/noahkafemann/pythonanywhere-test.git ideenmanager
cd ideenmanager
git checkout kilo/short-photon-dga
```

> **Hinweis:** Ersetze die URL ggf. durch dein eigenes Repository. Der Ordnername `ideenmanager` ist frei wählbar, wird aber in den folgenden Schritten verwendet.

---

### Schritt 3: Virtual Environment erstellen & Pakete installieren

```bash
# Virtualenv erstellen (Name: ideenmanager)
mkvirtualenv ideenmanager

# Abhängigkeiten installieren
pip install -r requirements.txt
```

**Wichtig:** Nach `mkvirtualenv` sollte links im Prompt `(ideenmanager)` erscheinen. Falls nicht, aktiviere es manuell:
```bash
workon ideenmanager
```

---

### Schritt 4: Web-App anlegen

1. Im PythonAnywhere-Dashboard: Reiter **Web** → **Add a new web app**.
2. Wähle **Manual configuration** (nicht Flask/Django!).
3. Python-Version: **3.10** (oder höher, z. B. 3.11/3.12).
4. Klicke **Next**.

---

### Schritt 5: Web-App-Einstellungen konfigurieren

Nach dem Anlegen siehst du die Konfigurationsseite. Trage folgende Werte ein:

#### Code / Working Directory
- **Source code**: `/home/deinusername/ideenmanager`
- **Working directory**: `/home/deinusername/ideenmanager`

> Ersetze `deinusername` durch deinen tatsächlichen PythonAnywhere-Benutzernamen.

#### WSGI configuration file
Klicke auf den Link **WSGI configuration file** (unter "Code"). Ersetze den **gesamten Inhalt** durch:

```python
import sys
import os

# Pfad zu deinem Projekt
project_path = '/home/deinusername/ideenmanager'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Flask-App importieren
from app import app as application
```

Speichern (Strg+S / "Save") und Tab schließen.

#### Virtualenv
- **Virtualenv**: `/home/deinusername/.virtualenvs/ideenmanager`
  - (Das ist der Standardpfad, den `mkvirtualenv` erstellt.)
  - Klicke auf den grünen Pfeil/Enter, um zu bestätigen.

#### Static files
Scrolle zum Bereich **Static files** und füge einen Eintrag hinzu:
- **URL**: `/static/`
- **Directory**: `/home/deinusername/ideenmanager/static`

Klicke auf **Enter** / das Häkchen zum Bestätigen.

---

### Schritt 6: Datenbank initialisieren (einmalig)

Zurück in der **Bash-Konsole** (mit aktiviertem Virtualenv):

```bash
cd /home/deinusername/ideenmanager
python -c "from app import app, db; app.app_context().push(); db.create_all(); print('DB erstellt')"
```

Erwartete Ausgabe: `DB erstellt` – die Datei `ideen.db` liegt nun im Projektordner.

---

### Schritt 7: Web-App neu laden & testen

1. Im **Web**-Tab: Großer grüner Button **Reload** klicken.
2. Warten bis "Reloaded" erscheint.
3. Deine Domain aufrufen: `https://deinusername.pythonanywhere.com`

Die App sollte jetzt laufen:
- Ideen hinzufügen
- Liste sehen
- Ideen löschen

---

### Schritt 8 (Optional): Eigene Domain / HTTPS

- Im **Web**-Tab kannst du unter "Custom domains" eine eigene Domain eintragen (erfordert kostenpflichtigen Plan).
- HTTPS ist bei `*.pythonanywhere.com` automatisch aktiv.

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| **ImportError: No module named 'flask'** | Virtualenv nicht aktiviert oder falscher Pfad bei "Virtualenv" in Web-Tab. Prüfe: `ls /home/deinusername/.virtualenvs/` |
| **Internal Server Error** | Klicke im Web-Tab auf **Error log** (Link oben rechts). Meist: Pfad in WSGI-Datei falsch oder `app` nicht als `application` exportiert. |
| **Static Files (CSS) laden nicht** | Prüfe Static-Files-Eintrag: URL `/static/` → Directory muss auf `/home/deinusername/ideenmanager/static` zeigen. Reload nicht vergessen. |
| **Datenbankfehler / "table idee doesn't exist"** | Schritt 6 (`db.create_all()`) in der Bash-Konsole mit aktiviertem Virtualenv ausführen. |
| **Änderungen am Code werden nicht angezeigt** | Im Web-Tab **Reload** klicken. PythonAnywhere cached den WSGI-Prozess. |

---

## Updates deployen (spätere Änderungen)

Wenn du Code änderst und pushst:

```bash
# In der Bash-Konsole auf PythonAnywhere:
cd /home/deinusername/ideenmanager
git pull origin kilo/short-photon-dga
# Falls requirements.txt geändert: pip install -r requirements.txt
# Dann im Web-Tab: Reload
```

---

## Datenbank

Die SQLite-Datenbank (`ideen.db`) wird beim ersten Start (Schritt 6) automatisch im Projektverzeichnis erstellt. Sie liegt auf PythonAnywhere unter `/home/deinusername/ideenmanager/ideen.db`.

- **Backup:** Einfach die Datei herunterladen (Files-Tab).
- **Migration:** Bei Schema-Änderungen `db.create_all()` reicht nicht – nutze Flask-Migrate oder lösche die DB neu (nur bei Testdaten).

---

## Entwicklung

```bash
# Lokal mit Debug-Modus
python app.py
```

Läuft auf `http://localhost:5000` mit Auto-Reload bei Code-Änderungen.

---

## Lizenz

MIT