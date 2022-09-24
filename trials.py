"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
            
    return even_nums


def get_odd_indices(items):
    result = [] 

    for index in range(len(items)):
        if index % 2 != 0:
            result.append(index)

    return result

def print_as_numbered_list(items):
    
    for index, item in enumerate(items):
        print(index, item)


def get_range(start, stop):

    nums = []

    for num in range(start, stop):
        nums.append(num)
    
    return nums
    


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append('*')
        else: 
            chars.append(letter)

    return "".join(chars)

    # python:
    # ''.join(characters)
    # java:
    # characters.join('')

def snake_to_camel(string):
    const =[]
    for word in string.split('_'):
        const.append(word[0].touppercase())
        

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
