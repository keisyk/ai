from flask import Flask, send_file, render_template, request
from image_generation import generate_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def start_generate_image():
    prompt = request.form['prompt']
    if not prompt:
        return "Empty prompt!"
    
    try:
        image_url = generate_image(prompt)
        return render_template('index.html', image_url=image_url)
    except Exception as e:
        return f"An error occurred while generating the image: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
