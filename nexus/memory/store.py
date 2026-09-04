import sqlite3


class MemoryStore:
    def __init__(self, path="nexus_memory.db"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY, content TEXT)"
        )

    def save(self, content):
        self.conn.execute(
            "INSERT INTO memories(content) VALUES(?)",
            (content,),
        )
        self.conn.commit()

    def query(self):
        cursor = self.conn.execute("SELECT content FROM memories")
        return [row[0] for row in cursor.fetchall()]
