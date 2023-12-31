import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0,
)
print(chat([HumanMessage(content="Write me a song about sparkling water.")]))
