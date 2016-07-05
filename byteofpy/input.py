## see http://stackoverflow.com/questions/30565525/checking-palindrome-text-with-ignored-punctuation-marks-spaces-and-case

import string

def ignore_punctuation_spaces_case(text):
    return "".join(i.lower() for i in text if i in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = ignore_punctuation_spaces_case(text)
    return text == reverse(text)

something = raw_input("Enter text: ")
if is_palindrome(something):
    print "Yes, it is a plindrome"
else:
    print "No, it is not a palindrome"
