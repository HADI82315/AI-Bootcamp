string = input("please enter an string: ").replace(' ', '').lower()
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counts = 0
for char in string:
    if char in vowels:
        vowel_counts += 1
        
print(vowel_counts)
