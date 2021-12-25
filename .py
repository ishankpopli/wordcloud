import PIL
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt
import sys, os
os.chdir(sys.path[0])

a= input()

stopwords = STOPWORDS

wc= WordCloud(
    background_color = 'black',
    stopwords = stopwords,
    height = 900,
    width = 500
)
wc.generate(a)
wc.to_file('wordcloud_output.png')

