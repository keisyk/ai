from openai import OpenAI

# list to keep the content during conversation
conversationList = [
    {"role": "system", "content": "You are a assistant."},
]

client = OpenAI()

def callApiAndGetResponse(userPrompt, conversationList):
    conversationList.append({"role": "user", "content": userPrompt})

    # call api
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversationList,
        max_tokens=300
    )

    print(response)

    # get response content
    responseContent = response.choices[0]['message']['content']
    conversationList.append({"role": "assistant", "content": responseContent})

    return responseContent

if __name__ == "__main__":
    while True:
        userInput = input()

        if userInput.lower() == 'q':
            break

        response = callApiAndGetResponse(userInput, conversationList)
        print(response)
