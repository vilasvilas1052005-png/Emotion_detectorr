import sqlite3


def load_all_songs(db_path: str) -> list:
    """
    Loads all songs from the 'emotion_songs' table into a list of dictionaries.
    Args:
        db_path (str): Path to the SQLite database.
    Returns:
        list of dict: Each dict represents a row with column names as keys.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emotion_songs")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        # Assumes columns: id, name, url, desc (adjust if your schema differs)
        data.append({"emotion": row[1], "title": row[2], "url": row[3]})
    conn.close()
    return data


def load_song_to_dict(db_path: str, emotion: str):
    """
    Loads the entire emotion_songs table from SQLite into a list of dictionaries.

    Args:
        db_path (str): Path to the SQLite database.

    Returns:
        list of dict: Each dict represents a row with column names as keys.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # This enables name-based access to columns
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM emotion_songs WHERE emotion = '{str(emotion.lower())}'"
    )
    rows: list = cursor.fetchall()

    # Convert sqlite3.Row objects to dicts
    data: list = [emotion]
    for row in rows:
        _ = list(
            row
        )  # [1, 'happy', 'Happy - Pharrell Williams', 'https://www.youtube.com/watch?v=ZbZSe6N_BXs', "Because I'm happy Clap along if you feel like happiness is the truth"]
        data.append(
            {"name": _[2], "url": _[3], "desc": _[4]}
        )  # Returns [emotion,{name,url,desc},{..,..,..}...]

    conn.close()
    return data
