# MisaKeylogger

MisaKeylogger is a Python program that logs keyboard inputs, monitors active windows, and tracks clipboard changes. It is designed for educational purposes only.

## Features

- Logs keyboard inputs, including key presses and releases.
- Monitors changes in the active window and logs window titles.
- Tracks clipboard changes and logs copied text.
- Saves logs to session-specific folders with timestamps.
- Gathers device information including OS details, CPU specs, RAM, storage, and IP addresses.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/llenn8/MisaKeylogger.git
   ```

2. Navigate to the project directory:

   ```bash
   cd MisaKeylogger
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:

   ```bash
   python keylogger.py
   ```

2. program started to logging activity...

## Output Example

### Folder Structure

```
MisaKeylogger
│   keylogger.py
│   README.md
│   requirements.txt
└───session_20240615_134500
    │   keylog_20240615_134500.txt
    │   clipboard_20240615_134500.txt
```

### Sample Log Files

**keylog_20240615_134500.txt:**

```
### Device Information ###
User: user123
os: Windows 11
node: DESKTOP-123456
version: 12.0.19042
machine: AMD64
processor: Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
cpu_count: 8
cpu_freq: 3.60
ram: 15.78
Storage:
  Device: C:
  Mountpoint: C:\
  Filesystem: NTFS
  Total: 100 GB
  Used: 120.45 GB
  Free: 117.24 GB
local_ip: 182.123.4.5
public_ip: 123.0.456.1

[2024-06-15 13:45:02] Active Window: Mozilla Firefox
 - This is a sample sentence.
 - This is a new lins.
[2024-06-15 13:45:05] Active Window: Visual Studio Code
```

**clipboard_20240615_134500.txt:**

```
### Clipboard Log - Session Start ###
Date: 2024-06-15

[2024-06-15 13:45:03] Clipboard Content: This is a sample text copied from a webpage.
```

## Disclaimer

The author of this software is not responsible for any misuse, damage, or legal implications resulting from the use of this program. **MisaKeylogger is provided for educational purposes only**.

## License

This project is licensed under the [MIT License](LICENSE).
