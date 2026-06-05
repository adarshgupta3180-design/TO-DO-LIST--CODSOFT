# TaskFlow: Professional Python To-Do List Dashboard

TaskFlow is a modern, responsive, and robust desktop To-Do list application built using Python and Tkinter. Engineered with clean Model-View-Controller (MVC) architecture, it serves as a showcase of desktop GUI best practices, interactive layouts, and solid software design principles.

TaskFlow offers a sleek dashboard-style layout, featuring light and dark theme toggling, color-coded priority and category badges, progress tracking, and robust data persistence in JSON with atomic file-saving routines.

---

## Key Features

- **Modern Dashboard UI**: Clean, card-based interface styled with curated slate-based dark and light themes.
- **Dynamic Theme Toggling**: Seamlessly switch between Light Mode and Dark Mode with dynamic widget recoloring.
- **Categorization & Priority Tags**: Organize tasks into categories (Work, Personal, Health, Shopping, etc.) and priority levels (High, Medium, Low) with visual tag pills.
- **Visual Statistics & Progress Bar**: Real-time counter metrics (Total, Completed, Pending tasks) accompanied by a custom, canvas-drawn progress completion bar.
- **Task Sorting & Instant Search**: Filter your view on the fly using the live search bar and sort tasks by due date, priority, or creation date.
- **Modality-Locked Dialogs**: Create or update tasks inside a modal configuration window featuring convenient due-date presets (Today, Tomorrow, Next Week).
- **Atomic JSON Persistence**: Automatic data loading and saving, utilizing atomic file writing (temp file swap) and automatic corrupted database restoration/backup loops.
- **Separated Sections**: Displays pending and completed tasks separately with dynamic headers showing the task counts.
- **Unit Tested Codebase**: Fully covered models and database services using `pytest`.

---

## Folder Structure

The project follows a clean, production-ready directory structure:

```
d:/CODSOFT/
├── README.md                 # Project documentation and run guide
├── requirements.txt          # Third-party dependency configurations (pytest)
├── run.py                    # Root entry point execution script
├── data/
│   ├── tasks.json            # Safe database storage file (created on runtime)
│   └── config.json           # User configuration (theme preference, created on runtime)
├── src/
│   ├── __init__.py
│   ├── main.py               # Configures global ttk styles and boots Tkinter
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py           # Task data model class (properties, serialization, validation)
│   │   └── database.py       # JSON database engine (atomic operations, backups, CRUD, stats)
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── app_controller.py # Coordinator linking models and views (business and sorting logic)
│   └── views/
│       ├── __init__.py
│       ├── main_window.py    # Main window framework layout & custom scroll wrapper
│       ├── sidebar.py        # Left navigation panels, status & tag filters, theme switcher
│       ├── task_card.py      # Custom task card view widget (badges, text strikethroughs)
│       ├── task_dialog.py    # Modality-locked input form for additions/edits
│       ├── stats_panel.py    # Dashboard counters and canvas-drawn progress bar
│       └── themes.py         # Color tokens, typography, and styling configurations
└── tests/
    ├── __init__.py
    └── test_database.py      # Unit test suite verifying CRUD, validation, and database safety
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher is recommended.
- Tkinter is included in standard Windows Python installations. If on Linux, you may need to install it: `sudo apt-get install python3-tk`

### 1. Clone or Copy the Repository
Place the project files in your workspace directory, e.g., `d:/CODSOFT/`.

### 2. Install Dependencies
Initialize a virtual environment (optional but recommended) and install the testing dependencies listed in `requirements.txt`:

```bash
# Optional: Setup virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Unix/macOS

# Install testing packages
pip install -r requirements.txt
```

---

## How to Run the Application

You can start TaskFlow by executing the root `run.py` script:

```bash
python run.py
```

---

## How to Run Tests

Verify code reliability by executing the pytest test suite:

```bash
pytest tests/
```

This runs unit tests covering:
- Task object initialization, validation, and completion flags.
- Task JSON serialization and deserialization.
- Database CRUD actions (saving, reloading, deletion).
- Dashboard statistics computation.
- JSON file corruption detection and backup recovery.

---

## Architecture & Code Quality Highlights

1. **Strict MVC Separation**:
   - The **Model** (`src/models/`) has zero knowledge of the UI. It handles pure data modeling and file storage.
   - The **View** (`src/views/`) has zero knowledge of database logic. It accepts model data directly or configurations and exposes event hook callbacks.
   - The **Controller** (`src/controllers/`) binds them together, handling all routing, updates, filters, and state operations.
2. **Robust File Handling (Atomic Writes)**:
   - Writing directly to a JSON database risks data corruption if the system crashes midway. TaskFlow mitigates this by writing first to a `tasks.json.tmp` file, duplicating the last valid file as `tasks.json.bak`, and then swapping `tasks.json.tmp` with `tasks.json` using `os.replace`.
3. **Advanced Ttk Flat Styles**:
   - Modernized look utilizing the `clam` style theme. Combobox fields and custom scrollbars are styled dynamically using style mapping to match dark and light modes.
4. **Cross-Platform Scrolling**:
   - Supports smooth mouse wheel scrolling binding on Windows, Linux, and macOS.
