text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("banananananan".count("n"))
print("baabajsbaabba".index("aj"))
print("banabanababaa".replace("ana", "XYXYX"))

sentence = "Hello, kind-sir; how many! I be of service today?"
print(sentence.replace(",", "").replace(";", "").replace("!", "").replace("?", ""))

punctuation = ".,;!?"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("this is a sentence and I want the words".split(" "))

text = "Bob goes to school. Bob sleeps with his friend. Bob support Biden. Bob usually goest to school naked"
print(text.find("Bob"))
print(text.rfind("Bob"))

i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1


