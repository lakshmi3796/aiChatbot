from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, Message
from .serializer import ConversationSerializer
from django.shortcuts import render
from .utils import generate_reply

def chat_page(request):
    return render(request, "chat/chat.html")

@api_view(["POST"])
def chat_api(request):
    text = request.data.get("message")
    conv_id = request.data.get("conversation_id")
    print(text,conv_id)
    if conv_id:
        conv = Conversation.objects.get(id=conv_id)
    else:
        conv = Conversation.objects.create()
    print(conv)
    # Save user message
    user_msg = Message.objects.create(
        conversation=conv,
        sender="user",
        text=text
    )

    # Generate bot reply
    reply = generate_reply(conv.messages.all())

    bot_msg = Message.objects.create(
        conversation=conv,
        sender="assistant",
        text=reply
    )

    return Response({
        "conversation_id": conv.id,
        "reply": reply
    })
