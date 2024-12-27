from flask import Flask, request, jsonify, render_template_string
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>John's AI Chatbot</title>
          </head>
          <body>
            <div class="container">
              <h1>Welcome to John's AI Chatbot!</h1>
              <form action="/chat" method="post">
                <div class="form-group">
                  <label for="context">Context:</label>
                  <textarea id="context" name="context" class="form-control" rows="5"></textarea>
                </div>
                <div class="form-group">
                  <label for="question">Question:</label>
                  <input type="text" id="question" name="question" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Ask</button>
              </form>
            </div>
          </body>
        </html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    context = request.form.get('context', '')
    question = request.form.get('question', '')
    result = chain.invoke({"context": context, "question": question})
    context += f"\nUser: {question}\nAI: {result}"
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>John's AI Chatbot</title>
          </head>
          <body>
            <div class="container">
              <h1>John's AI Chatbot</h1>
              <p><strong>Response:</strong> {{ response }}</p>
              <form action="/chat" method="post">
                <div class="form-group">
                  <label for="context">Context:</label>
                  <textarea id="context" name="context" class="form-control" rows="5">{{ context }}</textarea>
                </div>
                <div class="form-group">
                  <label for="question">Question:</label>
                  <input type="text" id="question" name="question" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Ask</button>
              </form>
            </div>
          </body>
        </html>
    ''', response=result, context=context)

if __name__ == "__main__":
    app.run(debug=True)
