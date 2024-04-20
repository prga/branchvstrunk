import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

dados = pd.read_csv('survey.csv')
words = dados['jobTitle']

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", colormap='winter').generate(' '.join(words))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud_job_title.png')