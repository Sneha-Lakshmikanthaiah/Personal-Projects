
def get_error_type(pred, label):
    # return the type of error: tp,fp,tn,fn
    if(pred == 1 and label == 1):
        return "tp"
    
    elif(pred == 1 and label == 0):
        return "fp"
    
    elif(pred == 0 and label == 1):
        return "fn"
    
    else:
        return "tn"
    

    
    
appos = {

"aren't" : "are not",

"can't" : "cannot",

"couldn't" : "could not",

"didn't" : "did not",

"doesn't" : "does not",

"don't" : "do not",

"hadn't" : "had not",

"hasn't" : "has not",

"haven't" : "have not",

"he'd" : "he would",

"he'll" : "he will",

"he's" : "he is",

"i'd" : "I would",

"i'd" : "I had",

"i'll" : "I will",

"i'm" : "I am",

"isn't" : "is not",

"it's" : "it is",

"it'll":"it will",

"i've" : "I have",

"let's" : "let us",

"mightn't" : "might not",

"mustn't" : "must not",

"shan't" : "shall not",

"she'd" : "she would",

"she'll" : "she will",

"she's" : "she is",

"shouldn't" : "should not",

"that's" : "that is",

"there's" : "there is",

"they'd" : "they would",

"they'll" : "they will",

"they're" : "they are",

"they've" : "they have",

"we'd" : "we would",

"we're" : "we are",

"weren't" : "were not",

"we've" : "we have",

"what'll" : "what will",

"what're" : "what are",

"what's" : "what is",

"what've" : "what have",

"where's" : "where is",

"who'd" : "who would",

"who'll" : "who will",

"who're" : "who are",

"who's" : "who is",

"who've" : "who have",

"won't" : "will not",

"wouldn't" : "would not",

"you'd" : "you would",

"you'll" : "you will",

"you're" : "you are",

"you've" : "you have",

"'re": " are",

"wasn't": "was not",

"we'll":" will",

"didn't": "did not"

}
#Put the code under the classify method here.  Here's some code to start you off
#Original code
#Original code
import nltk
import re
import string
punct = string.punctuation
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
stop.remove('against')
stop.remove('aren\'t')
stop.remove('couldn\'t')
stop.remove('didn\'t')
stop.remove('doesn\'t')
stop.remove('hadn\'t')
stop.remove('hasn\'t')
stop.remove('haven\'t')
stop.remove('mightn\'t')
stop.remove('mustn\'t')
stop.remove('needn\'t')
stop.remove('nor')
stop.remove('shan\'t')
stop.remove('shouldn\'t')
stop.remove('wasn\'t')
stop.remove('weren\'t')
stop.remove('won\'t')
stop.remove('wouldn\'t')
stop.remove('not')
#stop.update(['a', 'able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','by','did','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','may','me','might','my','of','off','on','or','other','our','own','rather','said','say','says','she','should','since','so','than','that','the','their','them','then','there','these','they','this','tis','to','was','us','was','we','were','what','when','where','while','who','whom','why','will','would','yet','you','your','They','Look','Good','A', 'Able','About','Across','After','All','Almost','Also','Am','Among','An','And','Any','Are','As','At','Be','Because','Been','By','Did','Else','Ever','Every','For','From','Get','Got','Had','Has','Have','He','Her','Hers','Him','His','How','However','I','If','In','Into','Is','It','Its','Just','Least','Let','May','Me','Might','My','Of','Off','On','Or','Other','Our','Own','Rather','Said','Say','Says','She','Should','Since','So','Than','That','The','Their','Them','Then','There','These','They','This','Tis','To','Was','Us','Was','We','Were','What','When','Where','While','Who','Whom','Why','Will','Would','Yet','You','Your','!','@','#','"','$','(','.',')'])

from nltk.stem import WordNetLemmatizer
wn = WordNetLemmatizer()
#from textblob import TextBlob 
#import spacy
from nltk import pos_tag,word_tokenize
wn = WordNetLemmatizer()


def classify(text, inqtabs_dict, swn_dict):
    
    #regex = r'[A-Za-z]+' #You'll probably want to update this regular expression
#     comment = text.split()
#     commo = []
#     for i in range(len(comment)):
#         token_comment = word_tokenize(comment[i])
#         tagged_comment = pos_tag(token_comment)
#         for word, tag in tagged_comment:
#             if (tag=='JJS') or (tag=='JJR') or (tag=='JJ') or (tag=='RB') or (tag=='RBR') or (tag=='RBS'):
#                  commo.append(word)
#             else:
#                 continue
            
#     text1 = " ".join(commo)
    for word in text.split():
        if word.lower() in appos:
            text = text.replace(word,appos[word.lower()])
    
    text = "".join(text)
    #Bigram
#     text = text.lower()
#     nltk_tokens = nltk.word_tokenize(text)  
#     bi = list(nltk.bigrams(nltk_tokens))
#     sep = [map(str,l) for l in bi]
#     nl = [(' '.join(s)) for s in sep]
    regex = r'\w(?:[-\w]*\w)?|\w(?:[_\w]*\w)?'
    words = re.findall(regex, text) 
    words = [k.lower() for k in words]
    #words = [word for word in words if word.isalpha()]
    words = [word for word in words if not word.isdigit()]
    words = [i for i in words if i not in stop]
    words = [word for word in words if word not in punct]
    words = [wn.lemmatize(word) for word in words]
    words = [x for x in words if len(x)>2]
    #words = list(set([word for word in words]))
#     words.extend(nl)
    
    
    
    
    positive_words_inqtabs = []
    negative_words_inqtabs = []
    words_matched_inqtabs = []

    positive_words_swn = {}

    negative_words_swn = {}
    words_matched_swn = []
    
    for i,word in enumerate(words):
        if word in inqtabs_dict:
            if ((i-1)>=0) and (words[i-1]=='not'):
                if inqtabs_dict[word] == '1':
                    negative_words_inqtabs.append(word)
                else:
                    positive_words_inqtabs.append(word)
            elif inqtabs_dict[word] == '1':
                positive_words_inqtabs.append(word)
            else:
                negative_words_inqtabs.append(word)
            words_matched_inqtabs.append(word)
       
        if word in swn_dict:
            if ((i-1)>=0) and (words[i-1]=='not'):
                positive_words_swn[word] = swn_dict[word][1]
                negative_words_swn[word] = swn_dict[word][0]
            else:
                positive_words_swn[word] = swn_dict[word][0]
                negative_words_swn[word] = swn_dict[word][1]
           
        if 'not' in positive_words_swn:
            del positive_words_swn['not']
        if 'not' in negative_words_swn:
            del negative_words_swn['not']
        
        positive_words_swn = {k : v for k,v in positive_words_swn.items() if v > 0.65}
        negative_words_swn = {k : v for k,v in negative_words_swn.items() if v > 0.65}

        total_positive = sum(positive_words_swn.values())
        total_negative = sum(negative_words_swn.values())
            
        bad_words = ["bad", "ridiculous","terrible", "horrible", "worse", "worst", "boring", "unfunny", "poor", "shoddy", "horrendous",
                 "waste", 'dominated', 'unsound', 'crap','lousy','corny','sarcasm','ashamed','absurd','show',
    'one',
 'people',
 'never',
 'least',
 'first',
 'got',
 'around',
 'characters',
 'nothing',
 'good',
 'little',
 'going',
 'watching',
 'know',
 'even',
 'much',
 'great',
 'time',
 'movie',
 'made',
 'film',
 'ever',
 'say',
 'could',
 'story',
 'would',
 'bad',
 'really',
 'make',
 "i've",
 'like',
 'two',
 'acting',
 'movie,',
 'see',
 'better',
 'might',
 'think',
 'seen',
 'film,',
 "that's",
 'movie.',
 'character',
 'many',
 'watch',
 'best',
 'get',
 'end',
 "i'm",
 'scenes',
 'way',
 'victor',
 'vargas']
        good_words = ["great","best","wonderfully", "wonderful", "exciting", "enjoy", 'splendid', 'respectable','sensational', 'fantabulous', 'excellent', 'lovely', 'wonderfulness', 'admirability', 'kudos', 'happiness', 'bliss',"beautiful","love","enjoying","favorite",'plot',
 'director',
 'one',
 'first',
 'time',
 'years',
 'bad',
 'well',
 'little',
 'made',
 'movie',
 'never',
 'many',
 'would',
 'make',
 'story',
 'another',
 'think',
 'films',
 'almost',
 'really',
 'also',
 'may',
 'things',
 "there's",
 'work',
 'get',
 'take',
 'something',
 'good',
 'like',
 'say',
 'even',
 'people',
 'man',
 'big',
 'film',
 'scene',
 'part',
 'movie.',
 'much',
 'see',
 'saw',
 'best',
 'back',
 'new',
 'show',
 'love',
 'character',
 'makes',
 'way',
 'two',
 "can't",
 'great',
 'still',
 'life',
 'trying']

        # words = ["bad", "terrible", "horrible", "amazing", "wonderful"]
        # total_negative = 0
        # total_positive = 0

        for i in words:
            if i in bad_words:
                total_negative += 10
            elif i in good_words:
                total_positive += 10

        
    #You'll definitely want to experiment with different ideas for the code below
    if (len(positive_words_inqtabs) - len(negative_words_inqtabs) > 0) and ((total_positive - total_negative) > 0):
        score = 1
    else:
        score = 0

    #Some useful data to help you analyze how the prediction was made
    #You'll probably want to not include these print statements when you copy this code to sentiment.py
#     print("Original text: ", text)
#     print("Words in text: ", words)
#     print("\nScores from Lexicon 1 (Harvard Inquirer)")
#     print("Positive words found: ", len(positive_words_inqtabs), positive_words_inqtabs)
#     print("Negative words found: ", len(negative_words_inqtabs), negative_words_inqtabs)
#     print("\nScores from Lexicon 2 (SentiWordNet)")
#     print("Positive words found: ", len(positive_words_swn), sorted(positive_words_swn.items(), key=lambda x: x[1], reverse=True))
#     print("Total positive sentiment: ", sum(positive_words_swn.values()))
#     print("\nNegative words scores: ", len(negative_words_swn), sorted(negative_words_swn.items(), key=lambda x: x[1], reverse=True))
#     print("Total negative sentiment:", sum(negative_words_swn.values()))
#     print("\nScore: ", score)
    return score

