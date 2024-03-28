# pip install openai
from openai import OpenAI

# api key and client
OPENAI_API_KEY='<your_super_secret_openai_api_key>'
client = OpenAI(api_key=OPENAI_API_KEY)

# get response from openai api function
def get_response_from_openai(system, prompt, context):
    response = client.chat.completions.create(
        model='gpt-4-0125-preview', # 'gpt-3.5-turbo' for chat-gpt-3.5
        response_format={'type':'text'},
        messages=[
            {'role':'system', 'content':system},
            {'role':'user', 'content':f'{("\n\nContext:\n").join([prompt, context])}'}
        ]
    )
    ai_reponse = response.choices[0].message.content
    return None if 'None' in ai_reponse else ai_reponse.split('\n')

# example system, prompt, and context parameter strings
system_string = "You are a helpful assistant designed to output only 'None' or a list of strings separated with line breaks"

prompt_string = "List all the names of people provided in the context below. If no names are mentioned, respond with 'None'."

context_string = "Jack and Jill ran up the hill. I do not like green eggs and ham, Sam. But all the king's horses and all the king's men could not put Humpty Dumpty back together."

# example function call
ai_response = get_response_from_openai(system_string, prompt_string, context_string)
print(ai_response)
