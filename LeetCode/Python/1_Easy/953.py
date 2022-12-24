# [ LeetCode ] 953. Verifying an Alien Dictionary

def solution(words: list[str], order: str) -> bool:
    order_table: dict[str, int] = {}
    for idx, alphabet in enumerate(order):
        order_table[alphabet] = idx
    
    previous_word: str = words[0]
    for current_word in words[1:]:
        is_same: bool = False
        for prev_letter, curr_letter in zip(previous_word, current_word):
            prev_rank, curr_rank = order_table[prev_letter], order_table[curr_letter]
            if prev_rank < curr_rank:
                is_same = False
                break
            
            elif prev_rank > curr_rank:
                return False
        
            else:
                is_same = True
        
        if is_same and len(previous_word) > len(current_word):
            return False
        
        previous_word = current_word
    
    return True
    
    
def another_solution(words: list[str], order: str) -> bool:
    order_table: dict[str, int] = {
        alphabet: idx for idx, alphabet in enumerate(order)
    }
    
    for curr, next in zip(words, words[1:]):
        if len(curr) > len(next) and curr[:len(next)] == next:
            return False

        else:
            for curr_ch, next_ch in zip(curr, next):
                if curr_ch != next_ch:
                    curr_rnk: int = order_table[curr_ch]
                    next_rnk: int = order_table[next_ch]
                    if curr_rnk < next_rnk:
                        break
                    
                    elif curr_rnk > next_rnk:
                        return False
    
    return True
    
    
if __name__ == "__main__":
    cases: list[dict[str, dict[str, list[str] | str]] | bool] = [
        {
            "input": {
                "words": ["hello", "leetcode"],
                "order": "hlabcdefgijkmnopqrstuvwxyz"
            },
            "output": True
        },
        {
            "input": {
                "words": ["word", "world", "row"],
                "order": "worldabcefghijkmnpqstuvxyz"
            },
            "output": False
        },
        {
            "input": {
                "words": ["apple", "app"],
                "order": "abcdefghijklmnopqrstuvwxyz"
            },
            "output": False
        }                
    ]
    for case in cases:
        assert case["output"] == solution(**case["input"])
        assert case["output"] == another_solution(**case["input"])
    