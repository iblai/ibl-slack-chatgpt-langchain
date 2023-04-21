from pathlib import Path
from llama_index import GPTSimpleVectorIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from slack_bolt.adapter.django import SlackRequestHandler
from chatbot.slack_listeners import app
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

handler = SlackRequestHandler(app=app)


SimpleCSVReader = download_loader("SimpleCSVReader")

loader = SimpleCSVReader()
documents = loader.load_data(file=Path('./chatbot/fakePhysicianData.csv'))
index = GPTSimpleVectorIndex.from_documents(documents)

tools = [
    Tool(
        name="CSV Index",
        func=lambda q: index.query(q),
        description=f"Useful when you want answer questions about a CSV file.",
    ),
]

llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")
agent_chain = initialize_agent(
    tools, llm, agent="zero-shot-react-description", memory=memory
)


@csrf_exempt
def slack_events_handler(request: HttpRequest):
    return handler.handle(request)


@api_view(("GET",))
def get_answer(request):
    question = request.data.get("question")

    if not question:
        return Response({"error": "Question is required"}, status=400)
    
    output = agent_chain.run(input=question)

    return Response({
        "answer": output,
    })