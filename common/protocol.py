import json

def encode_message(action, data):
    return json.dumps({"action": action, "data": data})

def decode_message(message):
    return json.loads(message)
