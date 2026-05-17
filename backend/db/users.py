from backend.db.connection import get_connection
from backend.db.models import User
import logging
import backend.logger


logger = logging.getLogger(__name__)


def create_user(telegram_id: str, platform_id: str) -> None:
    """ Добавление пользователя в бд
    Успех - True, Исключение - False"""

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (telegram_id, platform_id) VALUES (%s, %s)",
                    (telegram_id, platform_id))
        conn.commit()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    
    finally:
        if conn:
            conn.close()


def get_user_by_platform_id(platform_id: str) -> User | None:
    """ Ищет пользователя по platform_id и возвращает объект User  """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, telegram_id, platform_id, created_at, last_login_at FROM users \
                       WHERE platform_id = %s",
                    (platform_id,))
        
        row = cursor.fetchone()
        if row is None:
            return None
        
        id, *data = row
        return User(id, *data)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    
    finally:
        if conn:
            conn.close()


def update_last_login(platform_id: str) -> None:
    """ Ищет пользователя по platform_id и обновляет last_login_at  """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET last_login_at = NOW()\
                       WHERE platform_id = %s",
                    (platform_id,))
        conn.commit()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    
    finally:
        if conn:
            conn.close()


def update_platform_id(telegram_id: str, platform_id: str) -> None:
    """ Ищет пользователя по telegram_id и обновляет platform_id """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET platform_id=%s\
                       WHERE telegram_id = %s",
                    (platform_id, telegram_id,))
        conn.commit()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    
    finally:
        if conn:
            conn.close()