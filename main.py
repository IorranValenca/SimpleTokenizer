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
        
        def encode(self, text: str) -> List[int]:
            "pega a string transforma em lista de de tokens id. tokens fora do index vao para <UNK> se tiver, senao pula ele " 

            tokens = self._tokenize(text)
            ids= []
            for tok in tokens:  
                if tok in self.token_index:
                    ids.append(self.token_index[tok])
                elif self.unknown_id is not None:
                    ids.append(self.unknown_id)
                
                return ids 