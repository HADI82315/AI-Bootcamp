with open("sample_data.txt", mode="r") as file:
    lines =  file.readlines()

for line in lines:
    print(line.strip())