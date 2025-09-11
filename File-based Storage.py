from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import FileChatMessageHistory

# Save to a file specific to this user/session
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("chat_history_user123.json"),
    return_messages=True
)

conversation = ConversationChain(llm=llm, memory=memory)
response = conversation.predict(input="What are VAEs?")

# When the user returns, just initialize with the same file
# The conversation history will be automatically loaded
