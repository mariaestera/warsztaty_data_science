import sys
import platform
import psutil
import os

def system_info():
    print("=== System Information ===")
    print(f"Python version : {sys.version.split()[0]}")
    print(f"Platform       : {platform.system()} {platform.release()}")
    print(f"Machine        : {platform.machine()}")
    print(f"Processor      : {platform.processor()}")
    print(f"CPU cores      : {psutil.cpu_count(logical=False)} (physical), {psutil.cpu_count(logical=True)} (logical)")
    print(f"Total RAM      : {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Available RAM  : {round(psutil.virtual_memory().available / (1024**3), 2)} GB")
    print(f"Python path    : {sys.executable}")
    print("Current working directory:", os.getcwd())