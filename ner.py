from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import io

st = StanfordNERTagger('C:\\nlp_lab\code\external_code\stanford-ner-2017-06-09\classifiers\english.all.3class.distsim.crf.ser.gz',
					   'C:\\nlp_lab\code\external_code\stanford-ner-2017-06-09\stanford-ner.jar',
					   encoding='utf-8')

text = 'Andrew Sullivan Live-Blogging the Crisis in Iran'
# term = 'Sullivan'
# tokenized_text = word_tokenize(text)
# classified_text = st.tag(tokenized_text)
# print(classified_text)

def term_type(text,term):
	tokenized_text = word_tokenize(text)
	classified_text = st.tag(tokenized_text)
	for a in classified_text:
		if (a[0]==term):
			return a[1]
	return None

#POS tagging, needs:
# maxnet ne chunker
#averaged percepetron
#corpora/words
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
#print (ne_chunk(pos_tag(word_tokenize(text))))

input_file = 'C:\DSI\Projects\Ayelet_Sela\Data\\NEDDataHack2017_train.tsv'
f = io.open(input_file, encoding='utf-8')
txt = f.readlines()
d ={}
for t in txt[1:]:
	splited = str.split(t, '\t')
	[index, entity,disambig_term, text, wikipedia_link] = map(lambda x: str.replace(x, '\"', ''), splited)
	term_start = str.split(disambig_term,' ')[0]
#	print (term_start)
	term_ner_type = term_type(text,term_start)
	d[index]=term_ner_type
print (d)
f = io.open(str.replace(input_file,".tsv","_ner_dict.txt"), encoding='utf-8')
f.write(str(d))
f.close()