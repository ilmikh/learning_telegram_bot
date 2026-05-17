from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    telegram_id: str
    platform_id: str
    created_at: datetime
    last_login_at: datetime | None