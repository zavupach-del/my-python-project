import sys
import os

print("Python environment is ready!")
print(f"Python version: {sys.version}")
print(f"Executable: {sys.executable}")
print(f"Current dir: {os.getcwd()}")

#Проверка, что мы внутри .venv
if ".venv" in sys.executable:
    print("✅ Virtual environment is active.")
else:
    print("❌ Virtual environment is NOT active.")