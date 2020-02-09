import re 
import string

VOWEL_SYMBOLS = {'ٌ', 'ً', 'ٍ', 'ُ', 'َ', 'ِ', 'ْ', 'ٌّ', 'ّ'}
VOWEL_REGEX = re.compile('|'.join(VOWEL_SYMBOLS))
PUNCTUATION_MARKS = ['؟','،','.',':','؛']
PUNCTUATION_MARKS_REGEX = re.compile('[^%s]+' % ''.join(PUNCTUATION_MARKS))
punctuation = '؟،.:؛!'

# clean and preprocessing text 
text = open('text_ar.txt', 'r', encoding='utf-8').read()
text = text.replace("\n", ' ') # replace '\n' by space
text = text.translate(str.maketrans('', '', string.digits)) # remove digits 
text = re.sub(r'[(){}/]', '',text) # remove bracket
text = re.sub(r'http\S+', '', text) # remove url link
text = re.sub(VOWEL_REGEX, '', text) # remove tashakeel
text = re.sub(' +', ' ',text) #remove extra space
text = re.sub(r'\s+([؟.:،؛])', r'\1', text) #remove space before punctuation mark

# this function to keep punctuation and replace each word in text with 'space' 
def output_seq(t):
    t = t.strip().split(' ')
    out = ''
    for i in t:
        mark = PUNCTUATION_MARKS_REGEX.sub('', i)
        if any(mark):
            out+=i[-1]+' '
        else:
            out+='space '
    return out.strip()


# split text into sequances with lenght 10
in_seq = text.strip().split(' ')
n =10
in_sequances = [" ".join(in_seq[i:i+n]) for i in range(0, len(in_seq), n)]


# input file
in_nun_pun = [i.strip().translate(str.maketrans('', '', punctuation)) for i in in_sequances]
with open("input_punctuation.txt", "w") as txt_file:
    for line in in_nun_pun:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line


# output file
out_sequances = [output_seq(i) for i in in_sequances]
with open("output_punctuation.txt", "w") as txt_file:
    for line in out_sequances:
        txt_file.write("".join(line) + "\n") # works with any number of elements in a line