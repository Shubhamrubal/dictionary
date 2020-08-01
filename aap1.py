import json #importing json module
from difflib import get_close_matches

 # from difflib module we imported a function get_close_matches.
 #What it does is it takes a word as a parameter and a set of (words ,list or string) and finds the word similar to the word given
 #as parameter.


data=json.load(open("data.json"))
#data.json file is first open then load then saved in data variable.

def translate(w): #defining a function translate and giving w as a local parameter.
    w=w.lower() #changing the word into lower case so that the search process is convinient.
    if w in data: # if w word is present in the data variable
        return data[w] #return data[w] : it means take w , search for its meaning in data and return the meaning .
    elif len(get_close_matches(w,data.keys()))>0: #if the get_close_matches function return a list with length greater than zero means it is not a empty list
        yn= input("Did you mean %s instead?? Enter Y if yes and N if no: " %get_close_matches(w,data.keys())[0]) #Ye zero keval get_close_matches ka first match show kar rha,saare nhi.
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return "  ee naahi ba marde ..fir se type kra ho "
        else:
            return "we didn't umderstand your query"
    else:
        return"  ee naahi ba marde ..fir se type kra ho "

word=input("enter word: ")

output=translate(word)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)


'''

>>> "rain" in data
True
>>> "bhapka" in data
False
>>> import difflib
>>> from difflib import SequenceMatcher
>>> Sequencematcher(None,"rainn","rain").ratio()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Sequencematcher' is not defined
>>> SequenceMatcher(None,"rainn","rain").ratio()
0.8888888888888888
>>> SequenceMatcher(None,"rainn","rainn").ratio()
1.0
>>> from difflib import get_close_matches
>>> get_close_matches("rainn",["help","pyramid","rain"])
['rain']
>>> data.keys()
    #displays all the key values
>>> get_close_matches("rainn",data.keys())
['rain', 'train', 'rainy']
>>> get_close_matches("rainn",data.keys(),n=5)
['rain', 'train', 'rainy', 'grain', 'drain']
>>> get_close_matches("rainn",data.keys())[0]
'rain'

'''
