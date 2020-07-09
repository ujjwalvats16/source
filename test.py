import pysrt
import io
import nltk
nltk.download()


subs = pysrt.open('test.srt')
for sub in subs:
    with io.open("output.txt","a",encoding="utf-8")as f1:
        f1.write(sub.text)
        
with open('output.txt', 'r') as read_file:
    data = read_file.read()

tokens = nltk.word_tokenize(data)
text = nltk.Text(tokens)
# 1. de-capitalize
text_nostop = [w.lower() for w in text]

# 2. remove interpunctuation
interp = ['.', ',', '?', '!', ':', ';', '"', "'", ...]
text_nostop = [w for w in text_nostop if w not in interp]

# 3. remove stopwords
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
my_stopwords = ["'s", "n't", '...', "'m", "'re", "'ll","-","(",")","''" ,"``",...]


stopwords = stopwords + my_stopwords
text_nostop = [w for w in text_nostop if w not in stopwords]

fd_nostop = nltk.FreqDist(text_nostop)
with io.open("distribution.txt","w",encoding="utf-8")as f2:
 for w, f in fd_nostop.most_common(1000):
    data_output=w + ':' + str(f)
    f2.write(data_output+"\n")