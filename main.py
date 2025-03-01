from flask import Flask, render_template, request
from summarizer import text_summarizer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Example usage
    text = """
"""

    #summary = text_summarizer(text)

    #return summary
    return render_template('index.html')

@app.route('/', methods=['POST'])
def summarize():
    text = request.form['text']
    
    return text_summarizer(text)
app.run(port=5000)
