# client/compiler_executor.py
import subprocess
import tempfile
import os

def compile_code(source_code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f:
        f.write(source_code.encode())
        source_file = f.name

    output_file = source_file.replace(".c", "")

    try:
        result = subprocess.run(
            ["gcc", source_file, "-o", output_file],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return "COMPILE SUCCESS"
        else:
            return result.stderr
    finally:
        os.remove(source_file)
