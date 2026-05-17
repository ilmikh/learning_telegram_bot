from backend.db.auth_codes import delete_auth_code
from backend.db.users import get_user_by_platform_id, update_platform_id


def reset_platform_id(old_platform_id: str, new_platform_id: str) -> None:
    """ Удаляет старый код, обновляет platform_id"""

    user = get_user_by_platform_id(old_platform_id)
    if user is None:
        raise ValueError(f"Пользователь с platform_id {old_platform_id} не найден")
    
    delete_auth_code(old_platform_id)
    update_platform_id(user.telegram_id, new_platform_id)