import torch
import numpy as np # linear algebra
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Config
from transformers import GPT2Tokenizer
import random 

def load_question_joke_model(tokenizer):
    # Loading the model configuration and setting it to the GPT2 standard settings.
    configuration = GPT2Config.from_pretrained('./saved', output_hidden_states=False)

    # Create the instance of the model and set the token size embedding length
    model = GPT2LMHeadModel.from_pretrained("./saved", config=configuration)
    model.resize_token_embeddings(len(tokenizer))
    return model
    
def load_question_tokenizer():
    tokenizer = GPT2Tokenizer.from_pretrained("./saved/",
                                         bos_token='<|startoftext|>', 
                                          eos_token='<|endoftext|>', 
                                          pad_token='<|pad|>')
    return tokenizer


tokenizer=load_question_tokenizer()
model=load_question_joke_model(tokenizer)


#prompt = "hello from the other side"
def what_when_how_joke(prompt):
    ans=[]
    generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
    sample_outputs = model.generate(
                                generated, 
                                do_sample=True,   
                                top_k=50, 
                                max_length = 300,
                                top_p=0.95, 
                                num_return_sequences=3
                                )
    for i, sample_output in enumerate(sample_outputs):
        ans.append(tokenizer.decode(sample_output, skip_special_tokens=True))
    return random.choice(ans)
