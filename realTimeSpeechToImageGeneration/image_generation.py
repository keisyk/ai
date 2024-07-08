from openai import OpenAI

client = OpenAI()

# Generate image prompt using GPT-4
def generate_image_prompt(transcription):
    response = client.chat.completions.create(
        model="text-davinci-004",
        prompt=f"Generate a detailed description for an image based on the following transcription: {transcription}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Generate image using DALL-E
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="256x256",
        quality="standard",
        n=1,
    )
    url = response.data[0].url
    print (url)
    
    return url

# if __name__ == "__main__":
#     # image_prompt = generate_image_prompt("computer")
#     image_url = generate_image("computer")
#     print(image_url)