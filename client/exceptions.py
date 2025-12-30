class ClientError(Exception):
    pass

class ValidationError(ClientError):
    pass

class NetworkError(ClientError):
    pass
