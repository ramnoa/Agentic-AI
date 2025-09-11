from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import SQLChatMessageHistory

# Save to SQLite database
memory = ConversationBufferMemory(
    chat_memory=SQLChatMessageHistory(
        session_id="user123_session456",
        connection_string="sqlite:///chat_history.db"
    ),
    return_messages=True
)

conversation = ConversationChain(llm=llm, memory=memory)
