from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import re

## Text Cleaning:
    # Convert everything to lowercase
    # Remove HTML tags
    # Contraction mapping (see above)
    # Remove (‘s)
    # Remove any text inside the parenthesis ( )
    # Eliminate punctuations and special characters
    # Remove stopwords
    # Remove short words
## TODO probably need to break this into lots of sub-functions and some way to call 
## them together or separately...

def text_cleaner(text):
    newString = text.lower()
    newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub("[\(\[].*?[\)\]]", "", newString)
    newString = re.sub('"','', newString)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])    
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString) 
    tokens = [w for w in newString.split() if not w in stop_words]
    long_words=[]
    for i in tokens:
        if len(i)>=short_word_length:                  #removing short word
            long_words.append(i)   
    return (" ".join(long_words)).strip()


## Basic Text Cleaner
    # just takes lowercase and
    # filters out non-printable characters

def basic_text_cleaner(text):
    text = text.lower()
    printable = set(string.printable)
    text = "".join(list(filter(lambda x: x in printable, text)))
    return text

