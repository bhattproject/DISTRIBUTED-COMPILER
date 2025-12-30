def validate_sources(files: dict):
    for path, code in files.items():
        if not code.strip():
            raise ValueError(f"Empty file: {path}")
        if "#include" not in code and "main" not in code:
            print(f"Warning: {path} may not be compilable")
