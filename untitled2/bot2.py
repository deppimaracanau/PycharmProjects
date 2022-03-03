from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")


# Treino baseado no corpus em português
chatbot.train("chatterbot.corpus.Portuguese.conversations_pt-BR")

# Obtenha uma resposta para uma pergunta
chatbot.get_response("Olá, como você esta hoje?")