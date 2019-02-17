# -*- coding: utf-8 -*-
import random

CONFESSIONS_TEXT = u"""
English,I love you
French,Je t’aime ma chérie
Spanish,Te amo para siempre
German,Ich liebe Dich
Mandarin,我爱你,Wo ai ni
Japanese,愛してる,Aishiteru
Korean,사랑해,Saranghae
Arabic,ٲنَا بحِبَّك,Ana bahebak
Hindi,मैं तुमसे प्यार करता हुँ,Main tumse pyar kartha hoon
Greek,Σ΄αγαπώ,Se agapo
Italian,Ti amo
Russian,Я люблю тебя
Hebrew,אני אוהב אותך,Ani ohev otakh
Cheyenne,Nemehotatse
Tagalog,Mahal kita
Inuktitut,ᓇᒡᓕᒋᕙᒋᑦ,Nagligivaget
Belarus,Я цябе кахаю
Ukranian,Я тебе кохаю
""".strip()


def _confession_by_language():
    result = {}
    for line in CONFESSIONS_TEXT.split(u'\n'):
        language, confession = line.split(u',', 1)
        if ',' in confession:  # transcribtion is available
            confession, transcribtion = confession.split(u',', 1)
            confession = u'%s (sounds like %s)' % (confession, transcribtion)

        result[language] = confession

    return result


def random_confession():
    """Returns a language and a love confession in that language"""
    confessions = _confession_by_language()
    language_of_choice = random.choice(confessions.keys())
    return language_of_choice, confessions[language_of_choice]
