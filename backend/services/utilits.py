import uuid
import secrets

def generate_platform_id() -> str:
    return str(uuid.uuid4())

def generate_auth_code() -> str:
    return str(secrets.randbelow(1000000)).zfill(6)