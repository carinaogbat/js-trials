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
    """
    Given a string in snake case, return a string in upper camel case.
    
    >>> string = 'hello_world'
    >>> snake_to_camel(string)
    'HelloWorld'
    
    """

    const =[]

    for word in string.split('_'):
        const.append(word[0].upper())
        const.append(word[1:])

    return "".join(const)


def longest_word_length(words):
    """ 
    Return the length of the longest
     word in the given array of words.
    
    >>> words = ['jellyfish', 'zebra']
    >>> longest_word_length(words)
    9

    """

    longest_word = len(words[0])

    for word in words:
        if longest_word < len(word):
            longest_word = len(word) 

    return longest_word 


def truncate(string):
    """ Truncate repeating characters into one character.

    >>> test_string = 'aaaabbbbcccca'
    >>> truncate(test_string)
    'abca'


    """

    result = [] 

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return "".join(result) 
        



def has_balanced_parens(string):
    """ Return true if all parentheses in a given string are balanced.

    >>> is_balanced = '((This) (is) (good))'
    >>> has_balanced_parens(is_balanced)
    True

    >>> is_not_balanced = '(Oh no!)('
    >>> has_balanced_parens(is_not_balanced)
    False
    
    """
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

    if parens < 0:
        return False

    return parens == 0
    

def compress(string):
    """ Return a compressed version of the given string.
    
    >>> compress('aabbaabb')
    'a2b2a2b2'

    >>> compress('abc')
    'abc'

    >>> compress('Hello, world! Cows go moooo...')
    'Hel2o, world! Cows go mo4.3'

    """
    
    compressed = [] 
    currChar = ''
    CharCount = 0

    for char in string:

        if char != currChar:
            compressed.append(currChar)
            
            if CharCount > 1:
                compressed.append(str(CharCount))
            
            currChar = char
            CharCount = 0
            
        CharCount += 1
                
    compressed.append(currChar)
    if CharCount > 1:
        compressed.append(str(CharCount))

    return "".join(compressed)
 

