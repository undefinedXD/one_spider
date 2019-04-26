import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = "one.txt"
with open(filename) as f:
    mytext = f.read()
mytext = " ".join(jieba.cut(mytext))
wordcloud = WordCloud(font_path="STHeiti Medium.ttc").generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()