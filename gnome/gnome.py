from openai import OpenAI
import base64

client = OpenAI()

# Load the image file and encode to base64
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image('image.png')

# Call api
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Tell me what is the color of the hat in POLISH. Return only color and nothing more."},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

# Print response
print(response.choices[0])