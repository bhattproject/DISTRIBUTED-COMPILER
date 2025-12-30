import requests
from config import SERVER_URL, TIMEOUT
from exceptions import NetworkError

def submit_compile_job(payload):
    try:
        res = requests.post(
            f"{SERVER_URL}/compile",
            json=payload,
            timeout=TIMEOUT
        )
        return res.json()
    except requests.exceptions.RequestException as e:
        raise NetworkError(str(e))
