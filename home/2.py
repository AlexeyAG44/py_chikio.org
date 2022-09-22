import pickle

FILENAME = "C://data.bin"

with open(FILENAME, "rb") as file:
    a = pickle.load(file)
    print(a)
