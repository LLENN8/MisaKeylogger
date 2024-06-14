# MisaKeylogger

MisaKeylogger is a Python program that logs keyboard inputs, monitors active windows, and tracks clipboard changes. It is designed for educational and research purposes only. Please use it responsibly and in compliance with applicable laws and regulations.

## Features

- Logs keyboard inputs, including key presses and releases.
- Monitors changes in the active window and logs window titles.
- Tracks clipboard changes and logs copied text.
- Saves logs to session-specific folders with timestamps.
- Gathers device information including OS details, CPU specs, RAM, storage, and IP addresses.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/MisaKeylogger.git
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
os: Windows 10
node: DESKTOP-123456
version: 10.0.19042
machine: AMD64
processor: Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
cpu_count: 8
cpu_freq: 3.60
ram: 15.78
Storage:
  Device: C:
  Mountpoint: C:\
  Filesystem: NTFS
  Total: 237.69 GB
  Used: 120.45 GB
  Free: 117.24 GB
local_ip: 192.168.1.2
public_ip: 203.0.113.1

[2024-06-15 13:45:02] Active Window: Mozilla Firefox
 - This is a sample sentence.
[2024-06-15 13:45:05] Active Window: Visual Studio Code
```

**clipboard_20240615_134500.txt:**

```
### Clipboard Log - Session Start ###
Date: 2024-06-15

[2024-06-15 13:45:03] Clipboard Content: This is a sample text copied from a webpage.
```

## Disclaimer

The author of this software is not responsible for any misuse, damage, or legal implications resulting from the use of this program. **MisaKeylogger is provided for educational and research purposes only**. It is the responsibility of the user to comply with all applicable laws and regulations governing the use of such software.

## License

This project is licensed under the [MIT License](LICENSE).
```
