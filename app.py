from flask import Flask, render_template, request, jsonify
import subprocess
from ollama import chat
from ollama import ChatResponse

# LLM: Microsoft DialogGPT Medium
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

model_name = ''
model_list = []
messages = []

def get_available_models():
    global model_list
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    model_list = [line.split()[0] for line in result.stdout.splitlines() if line]
    return model_list

app = Flask(__name__)

@app.route("/")
def index():
    get_available_models()
    return render_template('chat.html', models=model_list)

@app.route("/select_model", methods=["POST"])
def select_model():
    """Set the selected model."""
    global model_name, messages
    model_name = request.json.get("model")
    messages = []  # Reset message history when switching models
    return jsonify({"model": model_name})

@app.route("/get", methods = ["GET", "POST"])
def chat_with_model():
    """Handle user messages and get model responses."""
    global model_name, messages
    if not model_name:
        return jsonify({"error": "No model selected"})
    
    user_msg = request.json.get("msg")
    messages.append({'role': 'user', 'content': user_msg})
    
    response = get_chat_response(messages)
    if response:
        messages.append({'role': 'assistant', 'content': response})
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Failed to generate response"})

def get_chat_response(messages):
    # https://huggingface.co/microsoft/DialoGPT-medium
    # Let's chat with the model
    global model_name
    if not model_name:
        return "No model selected."
    
    try:
        response: ChatResponse = chat(model=model_name, messages=messages)
        return response.message.content
    except Exception as e:
        return f"Error: {str(e)}"

    # # Let's chat for 5 lines
    # for step in range(5):
    #     # encode the new user input, add the eos_token and return a tensor in Pytorch
    #     new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

    #     # append the new user input tokens to the chat history
    #     bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    #     # generated a response while limiting the total chat history to 1000 tokens, 
    #     chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    #     # pretty print last ouput tokens from bot
    #     return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

        

if __name__ == '__main__':
    get_available_models()
    app.run(debug=True)

