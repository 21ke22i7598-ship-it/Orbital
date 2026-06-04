import unicodedata

class ProTokenizer:
    def __init__(self):
        # Every basic character (like letters and symbols) has a standard number from 0 to 255
        self.encoder = {i: bytes([i]) for i in range(256)}
        self.decoder = {bytes([i]): i for i in range(256)}
        self.vocab_size = 256
        self.merges = {}

    def train(self, text_corpus: str, target_vocab_size: int):
        """ Trains the tokenizer to find common word chunks, just like Claude or Gemini! """
        raw_bytes = text_corpus.encode("utf-8")
        ids = list(raw_bytes)
        
        num_merges = target_vocab_size - 256
        print(f"Training tokenizer... Learning {num_merges} advanced text patterns.")
        
        for i in range(num_merges):
            stats = {}
            for pair in zip(ids, ids[1:]):
                stats[pair] = stats.get(pair, 0) + 1
            
            if not stats:
                break
                
            # Find the most frequent pattern (like 't' and 'h' constantly next to each other)
            best_pair = max(stats, key=stats.get)
            new_id = 256 + i
            
            # Save this shortcut rule!
            self.merges[best_pair] = new_id
            self.encoder[new_id] = self.encoder[best_pair[0]] + self.encoder[best_pair[1]]
            
            # Group them together across the text
            new_ids = []
            idx = 0
            while idx < len(ids):
                if idx < len(ids) - 1 and (ids[idx], ids[idx+1]) == best_pair:
                    new_ids.append(new_id)
                    idx += 2
                else:
                    new_ids.append(ids[idx])
                    idx += 1
            ids = new_ids
            
        self.vocab_size = target_vocab_size
        print(f"Tokenizer trained! Vocabulary expanded to: {self.vocab_size} rules.")

    def encode(self, text: str) -> list[int]:
        """ Converts text sentences into lists of numbers for the AI core """
        raw_bytes = text.encode("utf-8")
        ids = list(raw_bytes)
        
        while len(ids) >= 2:
            stats = {}
            for pair in zip(ids, ids[1:]):
                stats[pair] = stats.get(pair, 0) + 1
            
            pair_to_merge = min(self.merges, key=lambda p: self.merges.get(p, float('inf')))
            if pair_to_merge not in stats:
                break
                
            new_id = self.merges[pair_to_merge]
            new_ids = []
            idx = 0
            while idx < len(ids):
                if idx < len(ids) - 1 and (ids[idx], ids[idx+1]) == pair_to_merge:
                    new_ids.append(new_id)
                    idx += 2
                else:
                    new_ids.append(ids[idx])
                    idx += 1
            ids = new_ids
        return ids

    def decode(self, ids: list[int]) -> str:
        """ Converts lists of numbers back into human language words """
        byte_fragments = []
        for token_id in ids:
            if token_id in self.encoder:
                byte_fragments.append(self.encoder[token_id])
        return b"".join(byte_fragments).decode("utf-8", errors="replace")


# --- Test Sandbox ---
if __name__ == "__main__":
    print("Testing Custom Tokenizer Engine...")
    
    # Text dataset to teach our tokenizer patterns
    training_data = "artificial intelligence and transformer architectures process token sequences patterns."
    
    tokenizer = ProTokenizer()
    # Teach it to look for 4 main shortcut word patterns
    tokenizer.train(training_data, target_vocab_size=260)
    
    test_sentence = "transformer patterns!"
    encoded = tokenizer.encode(test_sentence)
    decoded = tokenizer.decode(encoded)
    
    print("\n--- RESULTS ---")
    print(f"Original Text: '{test_sentence}'")
    print(f"Encoded Token IDs (Numbers): {encoded}")
    print(f"Decoded Back to Text:        '{decoded}'")
