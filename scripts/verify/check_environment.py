import importlib

packages = [
    "fastapi",
    "uvicorn",
    "pydantic",
    "pydantic_settings",
    "numpy",
    "pandas",
    "torch",
    "networkx",
    "pennylane",
    "qiskit",
]

print("\nRNAOS Environment Verification\n")

all_ok = True

for package in packages:
    try:
        importlib.import_module(package)
        print(f"[OK] {package}")
    except ImportError:
        print(f"[MISSING] {package}")
        all_ok = False

print("\nVerification Complete.")

if all_ok:
    print("All required packages are installed.")
else:
    print("One or more required packages are missing.")
