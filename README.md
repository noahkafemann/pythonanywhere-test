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

## Deployment auf PythonAnywhere

### 1. Code hochladen
- Repository auf GitHub pushen
- Auf PythonAnywhere: *Files* → *Clone from GitHub* oder manuell hochladen

### 2. Virtual Environment einrichten
```bash
mkvirtualenv ideenmanager
pip install -r requirements.txt
```

### 3. Web-App konfigurieren
- *Web* → *Add a new web app* → *Manual configuration* → Python 3.10+
- **Source code**: Pfad zum Projektverzeichnis
- **Working directory**: Gleiches Verzeichnis
- **WSGI configuration file**: Bearbeiten auf:

```python
import sys
import os

path = '/home/deinusername/ideenmanager'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

- **Virtualenv**: `/home/deinusername/.virtualenvs/ideenmanager`

### 4. Static Files konfigurieren
- *Static files* → URL: `/static/` → Directory: `/home/deinusername/ideenmanager/static`

### 5. Reload & Testen
- *Reload* klicken
- Deine Domain aufrufen

## Datenbank

Die SQLite-Datenbank (`ideen.db`) wird beim ersten Start automatisch im Projektverzeichnis erstellt. Für PythonAnywhere funktioniert das gleiche – die Datei wird im Working Directory angelegt.

## Entwicklung

```bash
# Debug-Modus (automatisch bei python app.py)
python app.py
```

## Lizenz

MIT