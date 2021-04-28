# Design a method to find the frequency of occurrences of any given word
# in a book. what if we were running this algorithm multiple times ?


def wordFrequencies(string):
    HashMap = {}
    string = list(string.split())
    for i in string:
        if i in HashMap:
            HashMap[i] += 1
        else:
            HashMap[i] = 1

    return HashMap


if __name__ == "__main__":
    string = "i am vinayak a student at iert vinayak is a nice name"
    print(wordFrequencies(string))
