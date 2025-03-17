#print("hello python")
#text= input("enter your text:")
#character_count=len(text.replace(" ", ""))
#print(f"character_count(excluding spaces)={character_count }")
words=[]
for i in range(1,6):
    word = input(f"Enter word {i}:")
    words.append(word)
print("\nWord Lengths:")
for word in words:
    print(f"'{word}' has {len(word)}characters.")