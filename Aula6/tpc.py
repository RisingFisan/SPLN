from gensim.models import Word2Vec
from gensim.utils import tokenize, deaccent
import re

try:
    model = Word2Vec.load('word2vec.model')
except:
    files = [
        "star_wars_a_new_hope_(episode_iv).txt",
        "star_wars_attack_of_the_clones_(episode_ii).txt",
        "star_wars_return_of_the_jedi_(episode_vi).txt",
        "star_wars_revenge_of_the_sith_(episode_iii).txt",
        "star_wars_the_empire_strikes_back_(episode_v).txt",
        "star_wars_the_force_awakens_(episode_vii).txt",
        "star_wars_the_phantom_menace_(episode_i).txt"
    ]   

    text = []

    for file in files:
        with open(file) as f:
            for paragraph in f.read().split('\n\n'):
                text.append(deaccent(re.sub(r"""'s|[.:,!?_"'()\[\]{}]|-{2,}""", "", paragraph.strip().lower())).split())

    model = Word2Vec(sentences=text, workers=12, epochs=500)
    model.save('word2vec.model')

print("Palavras mais semelhantes a Luke:")
print(model.wv.most_similar('luke'), end='\n\n')

print("Palavras mais semelhantes a Leia:")
print(model.wv.most_similar('leia'), end='\n\n')

print("Palavras mais semelhantes a Rey:")
print(model.wv.most_similar('rey'), end='\n\n')

print("Han está para Leia tal como Anakin está para:")
# Anakin + Leia - Han
# esperado: Padmé
print(model.wv.most_similar(positive=['anakin','leia'], negative=['han']), end='\n\n')

print("Luke está para Jedi tal como Vader está para:")
# Vader + Jedi - Luke
# esperado: sith
print(model.wv.most_similar(positive=['vader','jedi'], negative=['luke']), end='\n\n')
