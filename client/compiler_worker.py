import subprocess

class CompilerWorker:
    def __init__(self):
        pass
    
    def compile_code(self, file_path, output_path):
        """Compile C/C++ code using GCC"""
        try:
            result = subprocess.run(
                ["gcc", file_path, "-o", output_path],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return True, result.stdout
            else:
                return False, result.stderr
        except Exception as e:
            return False, str(e)
