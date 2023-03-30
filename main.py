import openai
print("*******************************************************************...............CHATGPT.PROGRAMMING TECH................************************************************************************************************************************************************************************************************************")
inputx=input("what information  do you want?:")

openai.api_key = ""


model_engine = "text-davinci-003"
prompt = inputx

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
feedback_text="was it helpful ?"
feedbackx= input(feedback_text)
print("Thanks for ur feedback")