import re
import string

input_string = input("please enter a sentence: ").strip()
punctuation = f"[{re.escape('.,?:;!-(){}[]')}]+"

clean_string =  re.sub(punctuation, ' ', input_string)

words = clean_string.split()
result = {}

while words:
    key = words[0]
    value = sum(1 for word in words if key.lower() == word.lower())
    words = [word for word in words if key.lower() != word.lower()]    
    result[key] = value

print(result)
          