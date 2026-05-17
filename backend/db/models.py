from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    telegram_id: str
    platform_id: str
    created_at: datetime
    last_login_at: datetime | None


@dataclass
class AuthCode:
    id: int
    platform_id: str
    code: str
    expires_at: datetime
    is_used: bool