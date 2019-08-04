import os
from profanity_check import predict
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

"""
Returns True if a string contains profanity, else False.  Can accept strings
or arrays of strings.
"""

class Profanity_Checker:
    def __init__(self):
        self.ps = PorterStemmer()
        self.bad_words = None
        if os.path.isfile('bad_words.txt'):
            with open('bad_words.txt', 'r') as file:
                self.bad_words = set(file.read().split("\n"))
                   
    def check_str(self, text): 
        '''
        accepts a string and returns True 
        if the string is profane or False if its all good
        '''
        
        ### Check for proper usage ###
        if type(text) != str:
            raise ValueError("input must be of type string")
        
        if not text:
            return

        #Stem text and check against bad words
        words = word_tokenize(text)
        if self.bad_words:
            for word in words:
                if self.ps.stem(word) in self.bad_words:
                    return True
        
        #Utilize more sophisticated profane checker library
        if predict([text])[0] == 1:
            return True

        return False

    def check_list(self, list_of_strings):
        """
        returns a list of tuples where tuple consists of:
        (original text string, TRUE/FALSE)  TRUE indicates profane
        """
        if type(list_of_strings) != list:
            raise ValueError("Input must be of type list")

        sentences =  [(text, self.check_str(text)) for text in list_of_strings]

        for sentence in sentences:
            print(sentence)
            if sentence[1] == True:
                return True
        return False
