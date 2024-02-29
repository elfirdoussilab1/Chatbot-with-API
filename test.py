from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
output = generator("Hello man. tell me about yourself !", max_length=200, truncation = True, num_return_sequences=1)
print(output[0]['generated_text'])