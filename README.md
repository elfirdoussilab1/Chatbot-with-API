# Chatbot-with-API
![Binaryhood](Logo/BinaryhoodLogo.png)
Using this code repository, you can interact with your LLMs locally using a graphical interface. All you need is to have Ollama installed on you laptop and some models on it. Enjoy! 

## Installation & Setup

[Install Python] https://www.dataquest.io/blog/installing-python-on-mac/

[Install pip] https://phoenixnap.com/kb/install-pip-mac

[Install ollama] https://ollama.com/

If you have Python & pip installed then check their version in the terminal or command line tools

```
python3 --version
```

```
pip --version
```

## Installing Flask

In your terminal run the requirements.txt file using this pip

```
pip install -r requirements.txt
```

## Downloading models with ollama
To display the models you already have, run in your terminal: 

```
ollama list
```

To download a model, go to ollama's website: [ollama.com](https://ollama.com/), take the exact name of the model you want, and then run:

```
ollama pull <model_name>
```

For example, here is how you can download Gemma-3 4B:

```
ollama pull gemma3:4b
```

# Launching the Chat API
To start chatting with your model, run in your notebook:

```
python3 app.py
```

# Enjoy chatting!