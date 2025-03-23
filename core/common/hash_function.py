class HashFunction:
    @staticmethod
    def hash_function(string: str) -> int:
        hash = 0
        for i in range(len(string)):
            hash += ord(string[i])
        return hash
    
    @staticmethod
    def reverse_hash_function(hash: int) -> str:
        return chr(hash)