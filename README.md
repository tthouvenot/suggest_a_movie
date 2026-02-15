# 🎬 Movie & Series Suggester

## 📖 Description

This project is a movie and TV series suggester designed to help you decide what to watch when endless scrolling kills your motivation.

Instead of relying on streaming platform algorithms, this app makes independent and unbiased suggestions based on your own library or selected platforms.
If you keep rejecting suggestions… the app will eventually get annoyed and tell you to figure it out yourself.

## ✨ Features (v0.1 - MVP)

### Core Functionality
- 🎲 **Random Movie Selection** from a user-specified directory.
- 🚀 **Command-Line Interface:**
  - Specify movie directory with `--directory`.
  - Force silent mode with `--silent`.
  - Check version with `--version`.
- 🎭 **Two Modes:**
  - **Silent Mode:** Clean, straightforward suggestions.
  - **Normal Mode:** Sarcastic bot with a theatrical personality.
- ⚠️ **Refusal Counter:** Up to 5 rejections before the bot gives up.
- 📊 **Three Choices:**
  - **Accept:** You've found a movie!
  - **Pass:** Rejects the suggestion (counts towards the limit).
  - **Watched:** Marks the movie as watched (doesn't count as a rejection).
  - Any wrong input will also count as a rejection.

### Bot Personality (Normal Mode)
- Theatrical introduction with typewriter effects.
- Escalating sarcastic responses (4 levels of disappointment).
- Dramatic movie reveal sequence (Oscar parody).
- Existential crisis after 5 rejections.
- Easter eggs and dark humor.

### Technical Features
- ✅ Clean MVC architecture (Model-View-Controller).
- ✅ **Robust Error Handling:** Validates directory existence, type, and permissions.
- ✅ Enum-based state management for clear and predictable states.
- ✅ Refactored code with low cognitive complexity.
- ✅ Docstrings and PEP8 compliant.

## 🎯 Goal

The goal of this project is to build a simple, fun, and honest decision helper:
- No infinite scrolling
- No recommendation bias
- Just “pick something and watch it”
If you refuse too many times, the app assumes you don’t really want to watch anything.

## 🛠 Tech Stack

- Python
- CLI-based (for now)
- Offline-first design
- Extensible for future API integration (TMDb, OMDb, etc.)

## 🚧 Project Status

**Current Version: v0.1 - MVP**

---

## ⚙️ Installation & Usage

### Prerequisites

You need Python 3.7 or higher installed on your system.

#### Installing Python

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ⚠️ **Important:** Check "Add Python to PATH" during installation
4. Verify installation: Open Command Prompt and run:
   ```bash
   python --version
   ```

**macOS:**
1. Option A - Using Homebrew (recommended):
   ```bash
   brew install python3
   ```
2. Option B - Download from [python.org](https://www.python.org/downloads/)
3. Verify installation:
   ```bash
   python3 --version
   ```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

**Linux (Fedora):**
```bash
sudo dnf install python3 python3-pip
python3 --version
```

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd suggest_a_movie
   ```

### Usage

Run the script from the command line. You can specify the movie directory and the interaction mode.

**Basic Usage:**
```bash
# On Windows
python main.py

# On macOS/Linux
python3 main.py
```
If you don't provide any arguments, the script will ask you which mode to use (Normal or Silent) and will search for movies in your home directory.

**Command-Line Arguments:**

| Argument | Short | Description | Default |
|---|---|---|---|
| `--directory` | `-d` | Path to the directory where your movies are stored. | Your home directory |
| `--silent` | `-s` | Run in silent mode (no bot personality). | Interactive prompt |
| `--version` | `-v` | Show the application's version and exit. | N/A |

**Examples:**

*   Run in silent mode with a custom movie directory:
    ```bash
    python3 main.py --silent --directory "/path/to/your/movies"
    ```
*   Run with a custom directory and let the script ask for the mode:
    ```bash
    python3 main.py -d "C:\Users\YourName\Videos\Movies"
    ```
*   Check the version:
    ```bash
    python3 main.py --version
    ```

## 📚 Resources

### 📘 Documentation

- `argparse`: https://docs.python.org/3/library/argparse.html
- `file list` : 
  - https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
  - https://builtin.com/data-science/python-list-files-in-directory
  - https://www.geeksforgeeks.org/python/python-list-files-in-a-directory/
  - https://docs.kanaries.net/fr/topics/Python/python-get-all-files-in-directory
- `Random` : https://docs.python.org/3/library/random.html
- `try...except`: https://docs.python.org/3/tutorial/errors.html

### 🤖 AI Usage (v0.1 Development)

**Claude AI** was used throughout the v0.1 MVC development as:

**Rubber Duck / Consultant:**
- MVC design pattern implementation advice
- Code refactoring strategies
- Python best practices (Enum, error handling)
- Debugging and error identification
- Code quality improvements

**Code Generation:**
- Docstrings and inline comments
- Movie class getters and setters
- Message tuples (nm_refusal_1-4, etc.)
- Helper functions for cognitive complexity reduction
- PEP8 and Flake8 compliance fixes

**Pair Programming:**
- Interactive bug fixing sessions
- Real-time code review and suggestions
- Architecture discussions
- Error handling implementation


---

## 🗺️ Roadmap

### v0.2 - Data Persistence
- [ ] Save watched movies to file
- [ ] Save rejected movies count
- [ ] Track last picked date
- [ ] Prevent suggesting recently watched movies
- [ ] Statistics dashboard

### v0.3 - Metadata & Filtering
- [ ] Extract movie metadata (year, director, actors, duration)
- [ ] Genre filtering
- [ ] Duration filtering
- [ ] Smart filtering based on watch history

### v0.4 - External APIs
- [ ] TMDb API integration
- [ ] OMDb API integration
- [ ] Fetch posters and descriptions
- [ ] Ratings and reviews

### v1.0 - GUI & Advanced Features
- [ ] Graphical user interface
- [ ] Multiple user profiles
- [ ] Streaming platform integration
- [ ] Recommendation algorithm

---

## 📁 Project Structure

```
suggest_a_movie/
├── main.py           # Entry point, mode selection
├── controllers.py    # Business logic, movie selection
├── models.py         # Data models (Movie, Enums)
├── views.py          # Display functions, messages
├── README.md         # Documentation
└── LICENSE           # License file
```

## 🤝 Contribuer

> (Indications succinctes pour contribuer)

## 🧾 Licence

Look at the `LICENSE` file.
