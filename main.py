from flask import Flask, render_template, request, jsonify, after_this_request
import time
import subprocess
import os
import json

output_folder = 'music/'

if os.path.exists("settings.json"):
    with open('settings.json')as f:
        settings = json.load(f)
        output_folder = settings['ouput_folder']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process_data():
    input_data = request.form['input_field']
    # Process the input data here
    subprocess.run(['yt-dlp', input_data, '-x', '--audio-format=mp3'], cwd=output_folder)

    result = f"download complete: {input_data}"
    return result

if __name__ == '__main__':
    app.run(debug=True)
