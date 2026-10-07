import sys
import numpy as np
import re
from typing import List, Dict, Pattern



class BasicTokenizer:
    def __init__(        self,
        token_index: Dict[str, int],
        split_pattern: Pattern = re.compile(r'([,.:;?_!"\'()]|--|\s)'),
        rejoin_pattern: Pattern = re.compile(r'\s+([,.:;?_!"\'()])')):
        self.token_index = token_index
        self.index_token = {idx: tok for tok, idx in token_index.items()}

    
        self.split_pattern = split_pattern
        self._rejoin_pattern = rejoin_pattern

    def tokenize(self, text: str) -> List[str]:

        "split na pontuacao double dash ou espaço branco e tira elementos vazios"
        raw = self._split_pattern.split(text)
        return [piece.strip() for piece in raw if piece.strip()]
    
    def encoder(self, text: str) -> List[int]:
        "pega a string transforma em lista de de tokens id. tokens fora do index vao para <UNK> se tiver, senao pula ele " 

        tokens = self.tokenize(text)
        ids= []
        for tok in tokens:  
            if tok in self.token_index:
                ids.append(self.token_index[tok])
            elif self.unknown_id is not None:
                ids.append(self.unknown_id)
            
            return ids 
        
    def decode(self, ids: List[int] ) -> str:
        "pega os ids transforma em tokens e dps bota tudo numa string, voltando tokens com espaço (pra ficar legivel), e corrigindo espaço dps da pontuação"

        tokens = [self.index_token[i] for i in ids if i in self.index_token]
        text = "".join(tokens)

        return self._rejoin_pattern.sub(r"\1", text)



text = "IdeaWeaver-- a comprehensive CLI tool for AI model training and evaluation?"
tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
tokens = [tok.strip() for tok in tokens if tok.strip()]

all_tokens  = sorted(set(tokens))               
vocab_size  = len(all_tokens)                  



vocab = {token: idx for idx, token in enumerate(all_tokens)}  


for token, idx in vocab.items():
    print(f"{token}: {idx}")

tokenizer = BasicTokenizer(vocab)

text = "IdeaWeaver-- a comprehensive CLI tool for AI model training and evaluation?"

ids = tokenizer.encoder(text)

decoder_text = tokenizer.decode(ids)

print(decoder_text)


