import subprocess
import sys
import os

def compile_cpp(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"
    output_path = file_path.replace('.cpp', '.o')
    try:
        result = subprocess.run(
            ['g++', '-c', file_path, '-o', output_path],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return f"Compiled successfully: {output_path}"
        else:
            return f"Compilation error:\n{result.stderr}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dist_compiler.py <source_file>")
    else:
        print(compile_cpp(sys.argv[1]))
