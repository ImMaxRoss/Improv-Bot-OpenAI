from flask import Flask, request, render_template, session
import os
import openai

app = Flask(__name__)

# Set the secret key to enable sessions
app.secret_key = [replace with your secret key]

conversation = []

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = [replace with your own OpenAI api key]

def gpt3_completion(prompt, engine='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['DEL:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

@app.route('/')
def home():
  # Check the client's IP address
  client_ip = request.remote_addr
  if 'client_ip' not in session or session['client_ip'] != client_ip:
      # Reload the app if the IP address has changed
      session['client_ip'] = client_ip
      conversation.clear()
  return render_template('home.html')

@app.route('/send', methods=['POST'])
def send():
  user_input = request.form['user_input']
  conversation.append('USER: %s' % user_input)
  # Convert the conversation list to a string
  conversation_str = '\n'.join(conversation)
  # Replace '<<BLOCK>>' with the conversation string
  prompt = open_file('static/prompt_chat.txt').replace('<<BLOCK>>', conversation_str)
  # Concatenate the strings using the + operator
  prompt = prompt + '\nDEL:'
  response = gpt3_completion(prompt)
  conversation.append('DEL: %s' % response)
  return render_template('home.html', conversation=conversation)

if __name__ == '__main__':
  app.run()
