import sys
import webbrowser

f = input('$ ')
print("Você buscou pela palavra: {} ".format(f))

googleimage = "https://www.google.com/search?tbm=isch&q={}".format(f)
taoeba = "https://tatoeba.org/en/sentences/search?from=eng&has_audio=&native=&orphans=no&query={}&sort=relevance&sort_reverse=&tags=&to=por&trans_filter=limit&trans_has_audio=&trans_link=&trans_orphan=&trans_to=&trans_unapproved=&trans_user=&unapproved=no&user=".format(f)
wordreference = "https://www.wordreference.com/enpt/{}".format(f)
linguee = "https://www.linguee.com.br/portugues-ingles/search?source=ingles&query={}".format(f)
#forvo = "https://forvo.com/word/{}/#en_usa".format(f)
cambridge = "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/{}".format(f)
michaelis = "https://michaelis.uol.com.br/moderno-ingles/busca/ingles-portugues-moderno/{}".format(f)
reverso = "https://www.reverso.net/tradu%C3%A7%C3%A3o-texto#sl=eng&tl=por&text={}".format(f)
collins = "https://www.collinsdictionary.com/pt/dictionary/english/{}".format(f)
translate = "https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&text={}".format(f)
oxford = "https://www.oxfordlearnersdictionaries.com/us/definition/english/{}".format(f)


#webbrowser.open(forvo,new=2)
webbrowser.open(linguee,new=2)
webbrowser.open(wordreference,new=2)
webbrowser.open(cambridge,new=2)
webbrowser.open(googleimage,new=2)
webbrowser.open(michaelis,new=2)
webbrowser.open(collins,new=2)
webbrowser.open(reverso,new=2)
webbrowser.open(taoeba,new=2)
webbrowser.open(oxford,new=2)
webbrowser.open(translate,new=2)