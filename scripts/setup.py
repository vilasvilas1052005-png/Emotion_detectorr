import sqlite3
import os


def create_user_table(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password BLOB NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def create_emotion_songs_table(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS emotion_songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT NOT NULL,
            song_title TEXT NOT NULL,
            youtube_url TEXT NOT NULL,
            song_line TEXT
        )
        """
    )
    conn.commit()
    conn.close()


def create_DB_files(db_path: str):
    """
    This checks if the files emotion_songs.sqlite and users.sqlite exist.
    if not it will create the file and then create the tables.
    """
    emotion_db_path = f"{db_path}/emotion_songs.sqlite"
    users_db_path = f"{db_path}/users.sqlite"

    try:
        if not os.path.exists(emotion_db_path):
            open(emotion_db_path, "w").close()  # Create the file if it doesn't exist
            create_emotion_songs_table(db_path)
    except FileNotFoundError:
        os.makedirs(db_path)
        open(emotion_db_path, "w").close()
        create_emotion_songs_table(db_path)
    finally:
        print(f"Emotion songs database is set up at {emotion_db_path}")

    try:
        if not os.path.exists(users_db_path):
            open(users_db_path, "w").close()
            create_user_table(db_path)
    except FileNotFoundError:
        os.makedirs(db_path)
        open(users_db_path, "w").close()
        create_user_table(db_path)
    finally:
        print(f"Users database is set up at {users_db_path}")


def create_env():
    with open(".env", "a") as f:
        f.write("OPENAI_API_KEY='OPEN_AI_APIKEY'\n")

    print(
        ".env file created with placeholder for OPENAI_API_KEY\nPlease update it with your actual API key."
    )


if __name__ == "__main__":
    create_env()
    create_DB_files("DB")
