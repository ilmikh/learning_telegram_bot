from psycopg2 import IntegrityError
from backend.db.connection import get_connection


def create_user(telegram_id: str, platform_id: str) -> bool:
    """ Добавление польвователя в бд
    Успех - True, Исключение - False"""

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (telegram_id, platform_id) VALUES (%s, %s)",
                    (telegram_id, platform_id))
        conn.commit()
        return True
    except IntegrityError:
        return False
    
    finally:
        if conn:
            conn.close()


def get_user_by_platform_id(telegram_id: str, platform_id: str):
    """ Добавление польвователя в бд
    Успех - True, Исключение - False"""

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (telegram_id, platform_id) VALUES (%s, %s)",
                    (telegram_id, platform_id))
        conn.commit()
        return True
    except IntegrityError:
        return False
    
    finally:
        if conn:
            conn.close()