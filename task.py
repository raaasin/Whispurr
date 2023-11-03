from cred import palmpi
import google.generativeai as palm
palm.configure(api_key=palmpi)

model = 'models/text-bison-001'

prompt = """
If you are assigned to do something or a task or a reques reply 'yes' or reply 'no' strictly only in boolean
----------------------------------------------------------
"""
prompt = prompt + "user said:"


def task(message):
    prompt= prompt + message
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
    )   
    return completion.result  