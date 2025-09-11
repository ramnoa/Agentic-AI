import json
from datetime import datetime

class DatabaseChatMemory:
    def __init__(self, user_id, session_id, db_connection):
        self.user_id = user_id
        self.session_id = session_id
        self.db = db_connection

    def save_message(self, role: str, content: str):
        """Save a single message (including system prompt) to the database."""
        self.db.execute("""
            INSERT INTO chat_messages (user_id, session_id, role, content, timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (self.user_id, self.session_id, role, content, datetime.now()))

    def load_conversation(self) -> list:
        """Load the full conversation (including system prompt) in order."""
        result = self.db.execute("""
            SELECT role, content FROM chat_messages
            WHERE user_id = %s AND session_id = %s
            ORDER BY timestamp ASC
        """, (self.user_id, self.session_id))
        return [{"role": row[0], "content": row[1]} for row in result]
