
# **FillMyWeek Automation Script**  

**FillMyWeek** is a Python automation script designed to simplify the process of filling out weekly work hours in Workday. It automates the login process via OKTA and navigates through the required steps to submit weekly time-off hours.  

---

## **Features**  

- Supports multiple environments: **Laptop** and **PC** via flags.  
- Includes error handling and environment validation.  

---

## **Prerequisites**  

1. Python 3.8 or higher.  
2. Google Chrome browser and the **ChromeDriver** installed.  
3. Virtual environment setup with required Python dependencies.  

---

## **Installation**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/fillmyweek.git
   cd fillmyweek
   ```

2. Set up a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Configuration**  

### **Edit Configuration in `res/config.py`:**  
Before running the script, make sure to update the following fields in `res/config.py`:  

```python
# Password for login
password = ""

# Coordinates for clicks on the OKTA login screen
laptop_okta_x = 0  
laptop_okta_y = 0  

# Coordinates for password input clicks
laptop_pas_x = 0  
laptop_pas_y = 0  
station_pas_x = 0  
station_pas_y = 0  
```

---

### **How to Measure Pixel Coordinates on macOS**  

   **Use macOS Screenshot Tool:**
   - Press `Command + Shift + 4`.  
   - Move the crosshair cursor to the desired location.  
   - Note the pixel coordinates shown next to the cursor while dragging.  

---

## **Usage**  

### **Run from Shell Script (Preferred):**  
1. Add the following shell function in your `~/.bashrc` or `~/.zshrc`:  

```bash
function fillmyweek {
  # Navigate to the project directory
  if [[ ! -d "/Users/amitlavi/Repos/github/fillmyweek" ]]; then
    echo "Directory not found! Exiting."
    return 1
  fi
  cd /Users/amitlavi/Repos/github/fillmyweek || return 1

  # Check and activate the virtual environment
  if [[ ! -f "venv/bin/activate" ]]; then
    echo "Virtual environment not found! Exiting."
    return 1
  fi
  source venv/bin/activate

  # Check if main.py exists
  if [[ ! -f "main.py" ]]; then
    echo "main.py not found! Deactivating venv and exiting."
    deactivate
    return 1
  fi

  # Check if a UI flag is passed
  if [[ -z "$1" ]]; then
    echo "Usage: fillmyweek [laptop|pc]"
    deactivate
    return 1
  fi

  # Run the Python script with the provided UI flag
  python main.py -ui "$1"

  # Deactivate the virtual environment
  deactivate
}
```

2. Reload the shell:  
   ```bash
   source ~/.bashrc   # For Bash
   source ~/.zshrc    # For Zsh
   ```

3. Run the script:  
   ```bash
   fillmyweek laptop
   fillmyweek pc
   ```

---

### **Run Directly from Terminal:**  
```bash
python main.py -ui laptop
python main.py -ui pc
```

---

## **Troubleshooting**  

1. **ChromeDriver Version Mismatch:**  
   Ensure your ChromeDriver version matches your Chrome browser version. Update if needed.  
   ```bash
   chromedriver --version
   google-chrome --version
   ```

2. **Environment Issues:**  
   If the virtual environment fails to activate, recreate it:  
   ```bash
   rm -rf venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Pixel Coordinates Are Off:**  
   Re-check the measurements using the **macOS Screenshot Tool** as described above.  

---
