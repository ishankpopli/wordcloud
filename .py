import PIL
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt
import sys, os
os.chdir(sys.path[0])
text=open('ok.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc= WordCloud(
    background_color = 'black',
    stopwords = stopwords,
    height = 900,
    width = 500
)
wc.generate(text)
wc.to_file('wordcloud_output.png')

