from api_client import submit_compile_job
from cache_manager import get_cached_result, update_cache

def run_compile_job(files):
    final_results = {}

    for path, code in files.items():
        cached = get_cached_result(code)
        if cached:
            final_results[path] = cached
            continue

        response = submit_compile_job({
            "filename": path,
            "code": code
        })

        final_results[path] = response
        update_cache(code, response)

    return final_results
