import sys
import numpy as np
import re


text = "IdeaWeaver-- a comprehensive CLI tool for AI model training and evaluation?"
tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
tokens = [tok.strip() for tok in tokens if tok.strip()]

all_tokens = sorted(set(tokens))
vocab_size = len(all_tokens)

print(vocab_size)





