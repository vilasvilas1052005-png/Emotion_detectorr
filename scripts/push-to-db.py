import sqlite3


def delete_table(db_path: str, table_name: str):
    """
    Deletes a table from the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to be deleted.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()


def create_db_and_insert(json_data, db_path):
    """
    Create SQLite DB, table, and insert JSON data.

    Args:
        json_data (list): List of dictionaries with emotion-song info.
        db_path (str): Path to the SQLite database file.
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Create table for emotion songs
    cur.execute("""
        CREATE TABLE IF NOT EXISTS emotion_songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT NOT NULL,
            song_title TEXT NOT NULL,
            youtube_url TEXT NOT NULL,
            song_line TEXT NOT NULL
        )
    """)

    # Prepare list of tuples for bulk insert
    records = [
        (item["emotion"], item["song_title"], item["youtube_url"], item["song_line"])
        for item in json_data
    ]

    # Bulk insert all records
    cur.executemany(
        """
        INSERT INTO emotion_songs (emotion, song_title, youtube_url, song_line)
        VALUES (?, ?, ?, ?)
    """,
        records,
    )

    conn.commit()
    conn.close()


# Example Usage:

json_data = [
    {
        "emotion": "happy",
        "song_title": "Happy - Pharrell Williams",
        "youtube_url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "song_line": "Because I'm happy Clap along if you feel like happiness is the truth",
    },
    {
        "emotion": "happy",
        "song_title": "Can't Stop the Feeling! - Justin Timberlake",
        "youtube_url": "https://www.youtube.com/watch?v=ru0K8uYEZWw",
        "song_line": "I got that sunshine in my pocket, got that good song in my feet",
    },
    {
        "emotion": "happy",
        "song_title": "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "youtube_url": "https://www.youtube.com/watch?v=OPf0YbXqDm0",
        "song_line": "Don't believe me just watch",
    },
    {
        "emotion": "happy",
        "song_title": "Good Vibrations - The Beach Boys",
        "youtube_url": "https://www.youtube.com/watch?v=UtrLgxQx7Yw",
        "song_line": "I'm picking up good vibrations",
    },
    {
        "emotion": "happy",
        "song_title": "Walking on Sunshine - Katrina & The Waves",
        "youtube_url": "https://www.youtube.com/watch?v=iPUmE-tne5U",
        "song_line": "I'm walking on sunshine, whoa",
    },
    {
        "emotion": "happy",
        "song_title": "Best Day of My Life - American Authors",
        "youtube_url": "https://www.youtube.com/watch?v=Y66j_BUCBMY",
        "song_line": "This is gonna be the best day of my life",
    },
    {
        "emotion": "sad",
        "song_title": "Someone Like You - Adele",
        "youtube_url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
        "song_line": "Never mind I'll find someone like you",
    },
    {
        "emotion": "sad",
        "song_title": "Fix You - Coldplay",
        "youtube_url": "https://www.youtube.com/watch?v=k4V3Mo61fJM",
        "song_line": "Lights will guide you home and ignite your bones",
    },
    {
        "emotion": "sad",
        "song_title": "Hurt - Johnny Cash",
        "youtube_url": "https://www.youtube.com/watch?v=8AHCfZTRGiI",
        "song_line": "I hurt myself today to see if I still feel",
    },
    {
        "emotion": "sad",
        "song_title": "Everybody Hurts - R.E.M.",
        "youtube_url": "https://www.youtube.com/watch?v=ijZRCIrTgQc",
        "song_line": "When your day is long and the night, the night is yours alone",
    },
    {
        "emotion": "sad",
        "song_title": "The Night We Met - Lord Huron",
        "youtube_url": "https://www.youtube.com/watch?v=KtlgYxa6BMU",
        "song_line": "I had all and then most of you, some and now none of you",
    },
    {
        "emotion": "angry",
        "song_title": "Break Stuff - Limp Bizkit",
        "youtube_url": "https://www.youtube.com/watch?v=ZpUYjpKg9KY",
        "song_line": "It's just one of those days where you don't wanna wake up",
    },
    {
        "emotion": "angry",
        "song_title": "Killing in the Name - Rage Against The Machine",
        "youtube_url": "https://www.youtube.com/watch?v=bWXazVhlyxQ",
        "song_line": "Some of those that work forces, are the same that burn crosses",
    },
    {
        "emotion": "angry",
        "song_title": "You Oughta Know - Alanis Morissette",
        "youtube_url": "https://www.youtube.com/watch?v=NPcyTyilmYY",
        "song_line": "And every time I scratch my nails down someone else's back",
    },
    {
        "emotion": "angry",
        "song_title": "Du Hast - Rammstein",
        "youtube_url": "https://www.youtube.com/watch?v=W3q8Od5qJio",
        "song_line": "Du hast mich gefragt, du hast mich gefragt",
    },
    {
        "emotion": "angry",
        "song_title": "Fighter - Christina Aguilera",
        "youtube_url": "https://www.youtube.com/watch?v=PstrAfoMKlc",
        "song_line": "Made me learn a little bit stronger",
    },
    {
        "emotion": "surprise",
        "song_title": "Surprise Yourself - Jack Garratt",
        "youtube_url": "https://www.youtube.com/watch?v=nyEbB0YijZQ",
        "song_line": "I wanna surprise myself",
    },
    {
        "emotion": "surprise",
        "song_title": "What a Wonderful World - Louis Armstrong",
        "youtube_url": "https://www.youtube.com/watch?v=CWzrABouyeE",
        "song_line": "I see trees of green, red roses too",
    },
    {
        "emotion": "surprise",
        "song_title": "Bohemian Like You - The Dandy Warhols",
        "youtube_url": "https://www.youtube.com/watch?v=eda1w-BPx6I",
        "song_line": "I've got a girlfriend and I love her, yeah yeah",
    },
    {
        "emotion": "surprise",
        "song_title": "Closer to the Edge - 30 Seconds to Mars",
        "youtube_url": "https://www.youtube.com/watch?v=I_izvAbhExY",
        "song_line": "We live, we love, we lie",
    },
    {
        "emotion": "surprise",
        "song_title": "Here Comes the Sun - The Beatles",
        "youtube_url": "https://www.youtube.com/watch?v=KQetemT1sWc",
        "song_line": "Here comes the sun, and I say it's all right",
    },
    {
        "emotion": "disgust",
        "song_title": "Creep - Radiohead",
        "youtube_url": "https://www.youtube.com/watch?v=XFkzRNyygfk",
        "song_line": "I'm a creep, I'm a weirdo",
    },
    {
        "emotion": "disgust",
        "song_title": "Toxic - Britney Spears",
        "youtube_url": "https://www.youtube.com/watch?v=LOZuxwVk7TU",
        "song_line": "With a taste of your lips I'm on a ride",
    },
    {
        "emotion": "disgust",
        "song_title": "Bad Guy - Billie Eilish",
        "youtube_url": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
        "song_line": "So you're a tough guy, like it really rough guy",
    },
    {
        "emotion": "disgust",
        "song_title": "Smells Like Teen Spirit - Nirvana",
        "youtube_url": "https://www.youtube.com/watch?v=hTWKbfoikeg",
        "song_line": "With the lights out, it's less dangerous",
    },
    {
        "emotion": "disgust",
        "song_title": "Ran - Aimee Mann",
        "youtube_url": "https://www.youtube.com/watch?v=7BUoIejdwmg",
        "song_line": "But I don't want to go",
    },
    {
        "emotion": "fear",
        "song_title": "Thriller - Michael Jackson",
        "youtube_url": "https://www.youtube.com/watch?v=sOnqjkJTMaA",
        "song_line": "'Cause this is thriller, thriller night",
    },
    {
        "emotion": "fear",
        "song_title": "Disturbia - Rihanna",
        "youtube_url": "https://www.youtube.com/watch?v=E1mU6h4Xdxc",
        "song_line": "Bum-bum-be-dum, bum-bum-be-dum, be-dum, be-dum",
    },
    {
        "emotion": "fear",
        "song_title": "Fear of the Dark - Iron Maiden",
        "youtube_url": "https://www.youtube.com/watch?v=J0S91fXfHfI",
        "song_line": "Have you run your fingers down the wall",
    },
    {
        "emotion": "fear",
        "song_title": "Somebody's Watching Me - Rockwell",
        "youtube_url": "https://www.youtube.com/watch?v=LU6mTEomtHk",
        "song_line": "I'm just an average man with an average life",
    },
    {
        "emotion": "fear",
        "song_title": "Creep - Radiohead",
        "youtube_url": "https://www.youtube.com/watch?v=XFkzRNyygfk",
        "song_line": "I'm a creep, I'm a weirdo",
    },
    {
        "emotion": "neutral",
        "song_title": "Let It Be - The Beatles",
        "youtube_url": "https://www.youtube.com/watch?v=QDYfEBY9NM4",
        "song_line": "And when the broken-hearted people living in the world agree, there will be an answer, let it be",
    },
    {
        "emotion": "neutral",
        "song_title": "Everybody's Got to Learn Sometime - The Korgis",
        "youtube_url": "https://www.youtube.com/watch?v=oFRPc9vxmvo",
        "song_line": "Change your heart, look around you",
    },
    {
        "emotion": "neutral",
        "song_title": "Stand by Me - Ben E. King",
        "youtube_url": "https://www.youtube.com/watch?v=hwZNL7QVJjE",
        "song_line": "No, I won't be afraid, oh, I won't be afraid",
    },
    {
        "emotion": "neutral",
        "song_title": "Waiting on the World to Change - John Mayer",
        "youtube_url": "https://www.youtube.com/watch?v=wRLWHKOl5PA",
        "song_line": "It's hard to beat the system when we're standing at a distance",
    },
    {
        "emotion": "neutral",
        "song_title": "Breathe Me - Sia",
        "youtube_url": "https://www.youtube.com/watch?v=SFGvmrJ5rjM",
        "song_line": "Help, I have done it again",
    },
]


if __name__ == "__main__":
    delete_table("DB/emotion_songs.sqlite", "emotion_songs")
    create_db_and_insert(json_data, "DB/emotion_songs.sqlite")
