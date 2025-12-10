#write a function that counts how many times each word appears in a sentence.

def word_count(sentence):
    words = sentence.split()
    count_dict = {}
    for word in words:
        word = word.lower().strip('.,?!"\'')
        if word in count_dict:
            count_dict[word] +=1
        else:
            count_dict[word] =1
    return count_dict
# Example usage:
# sentence = "Hello world! Hello everyone. Welcome to the world of Python."
sentence = input("enter a sentence: ")
result = word_count(sentence)
print(result)