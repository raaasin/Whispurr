import google.generativeai as palm
from cred import palmpi
from cred import palmpi
palm.configure(api_key=palmpi)


contexts="You are a chatbot replying in place for Nisar Ahmed your master, reply short and make it sweet and tell them that you are replying inplace of your master, remember make it short. here is some context about Nisar"""
    

def chatty(message,palm=palm, contexts=contexts,response=None):
    if response is None:
        response = palm.chat(context=contexts, messages=message)
    else:
        response = response.reply(message)

    return response.last
