A = {"kitap": "book",
    "bilim" : "knowledge",
    "kompyuter" : "computer"}
key = input("Enter the word: ")
if key in A:
    print(key,"-",A[key])
else:
    print("the word isn't in the dictionary")
