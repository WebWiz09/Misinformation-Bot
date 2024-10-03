
from groq import Groq

client = Groq(
    api_key="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",
)

fact = input("Enter statement for fact checking: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": fact,
        },
        {
            "role": "system",
            "content": """
            Fact check the user input by returning the line you believe is false
            whilst providing factual sources to back up your claims.
            Once you're done, provide an overall percentage of how much of it was fake. 
            Also provide a percentage of your certainty on how correct you are.
            """,
        },
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
