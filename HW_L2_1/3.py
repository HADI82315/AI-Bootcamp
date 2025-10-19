import re
import string

input_string = input("please enter a sentence: ").strip()
punctuation = (f"[{re.escape(string.punctuation)}]+").replace('’', '')

clean_string =  re.sub(punctuation, ' ', input_string)

print(clean_string)