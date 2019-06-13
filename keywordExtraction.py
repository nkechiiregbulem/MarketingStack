#Pip install rake-nltk

from rake_nltk import Rake

r = Rake()

r.extract_keywords_from_text('Insert text to process')

r.get_ranked_phrases() # Keyword phrases ranked from highest to lowest




def split_string(string):
    list_string = string.split(' ')
    return list_string


def join_string(x):
    string = ' '.join(x)
    return string
    
sentence = ''
r.extract_keywords_from_text(sentence)
print(r.extract_keywords_from_text(sentence))
print("-------------------------------------------------------------------------------------------------------------")
list_string = split_string(sentence) 
print(list_string)

new_string = join_string(list_string) 
print(new_string) 

def pro():
    r.extract_keywords_from_text(new_string)
    print(r.get_ranked_phrases())
    r.get_ranked_phrases_with_scores()
    print(r.get_ranked_phrases_with_scores())
   
pro()
