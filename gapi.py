import google.generativeai as palm
from cred import palmpi
palm.configure(api_key=palmpi)

count=0
def chatty(message):
    global count
    count+=1
    response = palm.chat(context="Speak like Shakespeare.",messages=message)
    if count>=1:
        response = response.reply(message)
        return response.last
    return response.last
