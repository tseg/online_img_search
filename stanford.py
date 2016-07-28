from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from itertools import groupby

class Sanitize_Result:
            
    def capitalize_first_letter(self, bst_guess):
        return ' '.join(word[0].upper() + word[1:] for word in bst_guess.split())
        
    def get_continuous_chunks(self, tagged_sent):
        continuous_chunk = []
        current_chunk = []

        for token, tag in tagged_sent:
            if tag != "O":
                current_chunk.append((token, tag))
            else:
                if current_chunk: # if the current chunk is not empty
                    continuous_chunk.append(current_chunk)
                    current_chunk = []
        if current_chunk:
            continuous_chunk.append(current_chunk)
            
        return continuous_chunk
    
    def sanitize_result(self, text):
        
        
        st = StanfordNERTagger('C:\Python27\stanford_ner\classifiers\english.all.3class.distsim.crf.ser.gz',
                                                   'C:\Python27\stanford_ner\stanford-ner.jar',
                                                   encoding='utf-8')
        tokenized_text = word_tokenize(self.capitalize_first_letter(text))
        classified_text = st.tag(tokenized_text)

        named_entities = self.get_continuous_chunks(classified_text)
        named_entities_str = [" ".join([token for token, tag in ne]) for ne in named_entities]
        named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]


        for tag, chunk in groupby(named_entities_str_tag, lambda x:x[1]):
            if tag == "PERSON":
                #print "%-12s"%tag, " ".join(w for w, t in chunk)
                name = " ".join(w for w, t in chunk)
               
        return name


if __name__ == '__main__':
    sent_result = Sanitize_Result()
    sent_result.sanitize_result('ben goertzel')

