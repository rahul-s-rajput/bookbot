from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    a = {}
    for i in text:
        if i.isalpha():
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
    counter = Counter(a)
    sorted_dict = dict(counter.most_common())
    return sorted_dict

def main():
    file_name = 'books/frankenstein.txt'
    with open(file_name, 'r') as file:
        data = file.read()
        print(f'--- Begin report of {file_name} ---')
        print(f'{count_words(data)} words found in the document\n')
        letter_count = count_chars(data)
        for letter, count in letter_count.items():
            print(f"The '{letter}' character was found {count} times")

        print('--- End report ---')

main()