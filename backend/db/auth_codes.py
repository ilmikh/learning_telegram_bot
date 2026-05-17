from backend.db.connection import get_connection
import logging
import backend.logger
from datetime import datetime
from backend.db.models import AuthCode


logger = logging.getLogger(__name__)


def upsert_auth_code(platform_id: str, code: str, expires_at: datetime) -> None:
    """ Создает или обновляет code для пользователя с platform_id. Код работает до expire_at  """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO auth_codes (platform_id, code, expires_at) \
                        VALUES (%s, %s, %s) \
                        ON CONFLICT (platform_id) DO UPDATE SET \
                        code = EXCLUDED.code, \
                        expires_at = EXCLUDED.expires_at, \
                        is_used = FALSE",
                       (platform_id, code, expires_at))
        conn.commit()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    finally:
        if conn:
            conn.close()


def delete_auth_code(platform_id: str) -> None:
    """ Удаляет код для platform_id  """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM auth_codes WHERE platform_id = %s",
                       (platform_id,))
        conn.commit()
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    finally:
        if conn:
            conn.close()


def get_auth_code_by_platform_id(platform_id: str) -> AuthCode | None:
    """ Возвращает код для platform_id """

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, platform_id, code, expires_at, is_used \
                        FROM auth_codes WHERE platform_id = %s",
                       (platform_id,))
        
        row = cursor.fetchone()
        if row is None:
            return None
        
        id, *data = row
        return AuthCode(id, *data)
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        raise
    finally:
        if conn:
            conn.close()