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

    






