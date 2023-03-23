# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prueba_50_key.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/22 20:56:29 by dacortes          #+#    #+#              #
#    Updated: 2023/03/22 21:14:47 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''.................................. libraries .............................'''

from termcolor import colored #print colors
from tqdm import tqdm #bar
import pandas as pd #table json
import json #open close
import spacy #
import numpy as np
from sentence_transformers import SentenceTransformer #analyze

'''................................ Funtions ................................'''

###...............................  Open.json ...............................###

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return  (data)

###...............................  Push_dic ................................###

def push_dic_dic(dic, id_article, id_video, score):
    if id_article not in dic:
        dic[id_article] = {}
    if id_video not in dic[id_article]:
        dic[id_article][id_video] = {}
    dic[id_article][id_video].update({'score': score})


def push_dic(dic, id_article):
    dic[id_article] = {}
###...............................  extract_keyw ............................###

def search_keywords(text):
    article = text
    article = text.lower()
    doc = nlp(article)
    num_keywords = 50
    keywords = []
    for token in doc:
        if not token.is_stop and token.pos_ in ['PRON','ADJ', 'PROPN','NOUN']:
            keywords.append(token.lemma_)
            if len (keywords) == num_keywords:
                break
    return (keywords)

###...............................  Analyze_all .............................###

def score(df, article):
    scores = []
    i = 0
    while i < len(in_video):
        tmp_video = ' '.join(search_keywords(df['text'][i]))
        video = ' '.join(df['keywords'][i]) + tmp_video
        m_video = model.encode(video)
        m_article = model.encode(article)
        res = np.dot(m_article, m_video)/(np.linalg.norm(m_article)*np.linalg.norm(m_video))
        scores.append((res, i, df_video.index[i]))
        i += 1
    scores.sort(reverse=True)
    return (scores)

def analyze(df_video):
    i = 0
    num = 1
    tittle = colored("Analisis", attrs=["bold"])
    print(colored(f"\n\t\t\t{tittle}", "blue"))
    pbar = tqdm(total=len(in_article))
    while i < len(in_article):
        tmp_article = ' '.join(search_keywords(df_article['text'][in_article[i]]))
        article = df_article['title'][i] + ' '.join(df_article['keywords'][i]) + tmp_article
        scores = score(df_video, article)
        v1 = round((scores[0][0] * 10), 1)
        id1 = scores[0][1]
        v2 = round((scores[1][0] * 10), 1)
        id2 = scores[1][1]
        push_dic(dic_outut, in_article[i])
        push_dic_dic(dic_outut, in_article[i], in_video[id1], str(v1))
        push_dic_dic(dic_outut, in_article[i], in_video[id2], str(v2))
        i += 1
        num += 1
        pbar.update(1)
    pbar.close()
    print(colored("\t\t\tAnalisis finalizado","green"))

'''.................................. Vars ..................................'''

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
nlp = spacy.load('es_core_news_md')

'''.................................. Main ..................................'''

if __name__ == "__main__":
###............................... Read.json ................................###
    df_video = read_json('videos.json')
    df_article = read_json('articles.json')
    df_video = pd.DataFrame.from_dict(df_video, orient='index')
    df_article = pd.DataFrame.from_dict(df_article, orient='index')
###............................... Index.json ...............................###
    dic_outut = {}
    in_video = df_video.index
    in_article = df_article.index
    print(colored(f"\nla cantidad de articulos para analizar es:", "blue") +
          f" {df_article.shape[0]}")
    print(colored(f"videos con los que se pueden relacionar:", "blue") +
          f" {df_video.shape[0]}")
###............................... Score ....................................###
    analyze(df_video)
    with open('data1.json', 'w') as file:
        json.dump(dic_outut, file, indent=2)