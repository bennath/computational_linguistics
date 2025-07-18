from wordDic import wordPos,WordMean
from databaseAccess import DatabaseAccess
import re


class TranslatorCore:


    def preprocess(self,phrase):
        #print(wordPos)
        #print(WordMean)
        'Salle à manger, banane plantain, salle de bain'
        phrase = phrase.lower()
        token = phrase.split()
        outtoken = []
        iterToken = iter(token)
        #if iterToken.__next__()
        for i in range(len(token)):
            try:
                if token[i] == "salle" and token[i+1] == "de" and token[i+2] == "manger":
                    word = token[i]+" "+token[i+1]+" "+token[i+2]
                    token[i] = word
                    token.remove("de")
                    token.remove("manger")
                elif token[i] == "banane" and token[i+1] == "plantain":
                    word = token[i]+" "+token[i+1]
                    token[i] = word
                    token.remove("plantain")
                elif token[i] == "salle" and token[i+1] == "de" and token[i+2] == "bain":
                    word = token[i]+" "+token[i+1]+" "+token[i+2]
                    token[i] = word
                    token.remove("de")
                    token.remove("bain")
                elif token[i] == "du" and token[i + 1] == "vent":
                    word = token[i] + " " + token[i + 1]
                    token[i] = word
                    #token.remove("du")
                    token.remove("vent")
                elif token[i] == "les" and token[i + 1] == "enfants":
                    word = token[i] + " " + token[i + 1]
                    token[i] = word
                    #token.remove("les")
                    token.remove("enfants")
                elif token[i] == "au" and token[i + 1] == "feu":
                    word = token[i] + " " + token[i + 1]
                    token[i] = word
                    #token.remove("au")
                    token.remove("feu")
                elif token[i] == "du" and token[i + 1] == "riz":
                    word = token[i] + " " + token[i + 1]
                    token[i] = word
                    #token.remove("du")
                    token.remove("riz")
                elif token[i] == "la" and token[i + 1] == "télé":
                    word = token[i] + " " + token[i + 1]
                    token[i] = word
                    #token.remove("je")
                    token.remove("télé")
            except IndexError:
                print("Thanks")
        try:
            if re.match("^j'",token[0]):
                temp = token[0].split("'")
                token[0] = "j'"
                token.insert(1,temp[1])
            elif re.match("^l'",token[0]):
                temp = token[0].split("'")
                token[0] = "l'"
                token.insert(1,temp[1])
        except IndexError:
            print("pretty thanks")


        for i in range(len(token)):
            print(i,len(token))
            if wordPos[token[i]] == 'V':
                for j in token[i:]:
                    try:
                        if (wordPos[j] == 'D' and (j == 'le' or j == 'la' or j == 'au' or j == "l'" or j == 'les' or j == 'du' or j == 'de' or j == 'des')):
                            print(token[token[i:].index(j)+i])
                            del token[token[i:].index(j)+i]
                            print(token)
                    except IndexError:
                        print("end reached")
                break
        return token



    def transwordForWord(self,phrase):
        phrase = phrase.lower()
        phraseToken = phrase.split()
        out = ""
        for i in phraseToken:
            out = out + " " + WordMean[i]
        return out
    def furthersplit(self,phrase):
        phrase = phrase.lower()
        phrasetoken = phrase.split()
        poslist = []
        for i in phrasetoken:
            poslist.append(wordPos[i])
        for word,pos in wordPos.items():
            if pos == 'conj':
                conjword = word
        totalout = ""
        if conjword in phrasetoken:
            phraseToken1 = phrasetoken[slice(phrasetoken.index(conjword))]
            phraseToken2 = phrasetoken[phrasetoken.index(conjword) + 1:len(phrase)]
            print(phraseToken1,phraseToken2)
            totalout = totalout + self.translate(phraseToken1) + ' '+ self.translate([conjword]) + ' '+self.translate(phraseToken2)
        else:
            totalout = totalout + self.translate(phrasetoken)
        return totalout

    def translate(self,phrase):
        #phrase = phrase.lower()
        phraseToken = phrase
        for i in phraseToken:
            print(i, wordPos[i])
        j = 0
        out = ""
        for i in range(len(phraseToken)):
            if len(phraseToken) == 6:
                if wordPos[phraseToken[i]] == "D"  and wordPos[phraseToken[i+1]] == "N" and wordPos[phraseToken[i+2]] == "V" and wordPos[phraseToken[i+3]] == "Adv" and wordPos[phraseToken[i + 4]] == "P" and wordPos[phraseToken[i + 5]] == "N":
                    
                    phraseToken[i],phraseToken[i+1] = phraseToken[i+1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out+" "+WordMean[phraseToken[j]]
                        j+=1
                    return out

                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "N" and wordPos[phraseToken[i + 3]] == "P" and wordPos[phraseToken[i + 4]] == "Ppr" and wordPos[phraseToken[i + 5]] == "N":

                    phraseToken[i + 4], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "D"  and wordPos[phraseToken[i+1]] == "N" and wordPos[phraseToken[i+2]] == "V" and wordPos[phraseToken[i+3]] == "P" and wordPos[phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":

                    phraseToken[i],phraseToken[i+1],phraseToken[i+4],phraseToken[i+5] = phraseToken[i+1],phraseToken[i],phraseToken[i+5],phraseToken[i+4]
                    while j < len(phraseToken):
                        out = out+" "+WordMean[phraseToken[j]]
                        j+=1
                    return out

                    '''elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "P" and wordPos[phraseToken[i + 3]] == "Ppr" and wordPos[phraseToken[i + 4]] == "N" and wordPos[phraseToken[i + 5]] == "N":
                    
                    #phraseToken[i + 2], phraseToken[i + 6], phraseToken[i+4], phraseToken[i+5] = phraseToken[i + 6], phraseToken[i + 2], phraseToken[i+5], phraseToken[i+4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Ppr" and wordPos[phraseToken[i + 1]] == "Adj" and wordPos[
                    phraseToken[i + 2]] == "N" and wordPos[phraseToken[i + 3]] == "V" and wordPos[
                    phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":
                    phraseToken[i],phraseToken[i + 1], phraseToken[i + 4], phraseToken[i + 5] =  phraseToken[i + 1], phraseToken[i], phraseToken[i + 5], phraseToken[i + 4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Ppr" and wordPos[phraseToken[i + 1]] == "N" and wordPos[
                    phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "P" and wordPos[
                    phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":
                    
                    phraseToken[i], phraseToken[i + 1],phraseToken[i + 4], phraseToken[i + 5] = phraseToken[i + 1], phraseToken[i],phraseToken[i + 5], phraseToken[i + 4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out



                elif wordPos[phraseToken[i]] == "Ppr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "D" and wordPos[phraseToken[i + 3]] == "N" and wordPos[
                    phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":

                    #phraseToken[i + 3], phraseToken[i + 4], phraseToken[i + 5] = phraseToken[i + 4], phraseToken[i + 5], phraseToken[i + 3]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "Adj" and wordPos[phraseToken[i + 3]] == "P" and wordPos[
                    phraseToken[i + 4]] == "Ppr" and wordPos[phraseToken[i + 5]] == "N":

                    #phraseToken[i + 1], phraseToken[i + 2], phraseToken[i + 3], phraseToken[i + 4], phraseToken[i + 5],  phraseToken[i + 6] = phraseToken[i + 6], phraseToken[i + 1], phraseToken[i + 2], phraseToken[i + 4], phraseToken[i + 5], phraseToken[i + 3]

                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "Adv" and wordPos[phraseToken[i + 3]] == "P" and wordPos[
                    phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":
                    
                    #phraseToken[i + 2], phraseToken[i + 6] = phraseToken[i + 6], phraseToken[i + 2]
                    phraseToken[i + 4], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "N" and wordPos[phraseToken[i + 3]] == "P" and wordPos[
                    phraseToken[i + 4]] == "D" and wordPos[phraseToken[i + 5]] == "N":

                    #phraseToken[i + 2], phraseToken[i + 6] = phraseToken[i + 6], phraseToken[i + 2]
                    phraseToken[i + 4], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 4]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out'''

                else: raise RuleNotImplemented("Rule Not Implemented")

            elif len(phraseToken) == 5:
                if wordPos[phraseToken[i]] == "D" and wordPos[phraseToken[i + 1]] == "N" and wordPos[phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "P" and wordPos[phraseToken[i + 4]] == "N":
                    
                    phraseToken[i ], phraseToken[i + 1] = phraseToken[i + 1], phraseToken[i]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Ppr" and wordPos[phraseToken[i + 1]] == "N" and wordPos[phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "P" and wordPos[phraseToken[i + 4]] == "N":
                    
                    #phraseToken[i + 1], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 1]
                    phraseToken[i], phraseToken[i + 1] = phraseToken[i + 1], phraseToken[i]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "Adv" and wordPos[phraseToken[i + 3]] == "P" and wordPos[
                    phraseToken[i + 4]] == "Ppr":

                    # phraseToken[i + 2], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "P" and wordPos[phraseToken[i + 3]] == "Ppr" and wordPos[phraseToken[i + 4]] == "N":

                    phraseToken[i + 3], phraseToken[i + 4] = phraseToken[i + 4], phraseToken[i + 3]
                    #phraseToken.insert(i + 3, "ní")
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "Adv" and wordPos[phraseToken[i + 3]] == "P" and wordPos[phraseToken[i + 4]] == "N":
                    #phraseToken.remove(phraseToken[i + 3])
                    #phraseToken[i + 2], phraseToken[i + 1] = phraseToken[i + 1], phraseToken[i + 2]
                    #phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "N" and wordPos[phraseToken[i + 3]] == "P" and wordPos[phraseToken[i + 4]] == "N":
                    #phraseToken.remove(phraseToken[i + 3])
                    #phraseToken[i + 1], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 1]
                    #phraseToken[i + 3], phraseToken[i + 4] = phraseToken[i + 4], phraseToken[i + 3]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "P" and wordPos[phraseToken[i + 3]] == "Ppr" and wordPos[phraseToken[i + 4]] == "N":
                    
                    phraseToken[i + 3], phraseToken[i + 4] = phraseToken[i + 4], phraseToken[i + 3]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "Ppr" and wordPos[phraseToken[i + 3]] == "D" and wordPos[
                             phraseToken[i + 4]] == "N":

                    # phraseToken[i + 1], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 1]
                    phraseToken[i + 3], phraseToken[i + 4] = phraseToken[i + 4], phraseToken[i + 3]
                    phraseToken.insert(i + 3, "ní")
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out




                    '''
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "V" and wordPos[phraseToken[i + 2]] == "D" and wordPos[phraseToken[i + 3]] == "N" and wordPos[phraseToken[i + 4]] == "N":
                    #phraseToken.remove(phraseToken[i + 3])
                    #phraseToken[i + 1], phraseToken[i + 5] = phraseToken[i + 5], phraseToken[i + 1]
                    phraseToken[i + 3], phraseToken[i + 2] = phraseToken[i + 2], phraseToken[i + 3]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out'''

                else:
                    raise RuleNotImplemented("Rule Not Implemented")

            elif len(phraseToken)  == 4:
                if wordPos[phraseToken[i]] == "D" and wordPos[phraseToken[i + 1]] == "N" and wordPos[
                    phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "N":

                    phraseToken[i+1], phraseToken[i] = phraseToken[i], phraseToken[i+1]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "Ppr" and wordPos[phraseToken[i + 1]] == "N" and wordPos[
                    phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "N":

                    phraseToken[i+1], phraseToken[i] = phraseToken[i], phraseToken[i+1]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i+1]] == "V" and wordPos[phraseToken[i+2]] == "D" and wordPos[phraseToken[i+3]] == "N":
                    
                    phraseToken[i+2],phraseToken[i+3] = phraseToken[i+3],phraseToken[i+2]
                    while j < len(phraseToken):
                        out = out+" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "Ppr" and wordPos[phraseToken[i + 3]] == "N":

                    phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    #phraseToken.insert(i + 2, "ní")
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i + 1]] == "V" and wordPos[
                    phraseToken[i + 2]] == "P" and wordPos[phraseToken[i + 3]] == "N":

                    # phraseToken[i+2], phraseToken[i+4] = phraseToken[i+4], phraseToken[i+2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]]=="N" and wordPos[phraseToken[i+1]]=="V" and wordPos[phraseToken[i+2]]=="P" and wordPos[phraseToken[i+3]]=="Ppr":
                    
                    #phraseToken[i+2], phraseToken[i+4] = phraseToken[i+4], phraseToken[i+2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out

                elif wordPos[phraseToken[i]]=="Pr" and wordPos[phraseToken[i+1]]=="V" and wordPos[phraseToken[i+2]]=="D" and wordPos[phraseToken[i+3]]=="N":
                    
                    phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i + 1]] == "Ppr" and wordPos[
                    phraseToken[i + 2]] == "V" and wordPos[phraseToken[i + 3]] == "N":

                    #phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]]=="Pr" and wordPos[phraseToken[i+1]]=="V" and wordPos[phraseToken[i+2]]=="Ppr" and wordPos[phraseToken[i+3]]=="N":
                    
                    phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out
                elif wordPos[phraseToken[i]]=="Pr" and wordPos[phraseToken[i+1]]=="V" and wordPos[phraseToken[i+2]]=="P" and wordPos[phraseToken[i+3]]=="N":
                    
                    #phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 2]
                    while j < len(phraseToken):
                        out = out + " " + WordMean[phraseToken[j]]
                        j += 1
                    return out



                else:
                    raise RuleNotImplemented("Rule Not Implemented")

            elif len(phraseToken) == 3:
                #print("True1")
                if wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i+1]] == "V" and wordPos[phraseToken[i+2]] == "N":
                    #phraseToken[i],phraseToken[i+1],phraseToken[i+2] = phraseToken[i+2],phraseToken[i+1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i+1]] == "V" and wordPos[phraseToken[i+2]] == "N":
                    #phraseToken[i],phraseToken[i+1],phraseToken[i+2] = phraseToken[i+2],phraseToken[i+1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                else:
                    raise RuleNotImplemented("Rule Not Implemented")
            elif  len(phraseToken) == 2:
                #print("True2")
                if wordPos[phraseToken[i]] == "Adj" and wordPos[phraseToken[i+1]] == "N":
                    phraseToken[i], phraseToken[i + 1] =  phraseToken[i + 1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                elif wordPos[phraseToken[i]] == "Pr" and wordPos[phraseToken[i+1]] == "V":
                    #phraseToken[i], phraseToken[i + 1] =  phraseToken[i + 1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                elif wordPos[phraseToken[i]] == "N" and wordPos[phraseToken[i+1]] == "V":
                    #phraseToken[i], phraseToken[i + 1] =  phraseToken[i + 1],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
                else:
                    raise RuleNotImplemented("Rule Not Implemented")
            elif len(phraseToken) > 3:
                #print("True3")
                if wordPos[phraseToken[i]] == "Det" and wordPos[phraseToken[i + 1]] == "Adj" and wordPos[phraseToken[i + 2]] == "Adj" and wordPos[
                    phraseToken[i + 3]] == "N":
                    phraseToken[i], phraseToken[i + 1], phraseToken[i + 2], phraseToken[i + 3] = phraseToken[i + 3], phraseToken[i + 1], phraseToken[i + 2],phraseToken[i]
                    while j < len(phraseToken):
                        out = out +" "+WordMean[phraseToken[j]]
                        j+=1
                    return out
            elif len(phraseToken) == 1:
                out = out +WordMean[phraseToken[0]]
                return out
    def databaseword(self):
        return WordMean.keys()

class RuleNotImplemented(RuntimeError):
    def __init__(self,arg):
        self.args = arg

if __name__ == "__main__":
    tran = TranslatorCore()
    #phrase = ['Aisha','and','Tobi','cooked','the','rice']
    #tran.furthersplit(phrase)
    #print(tran.preprocess("Mes vêtements sont dans la chambre"))
    #print(tran.preprocess("j'ouvre la porte de ma chambre"))
    #print(tran.translate(tran.preprocess("ma jeune sœur balaie la maison")).strip())
    #print(tran.translate(tran.preprocess("Nikẹ lit un journal")).strip())
    #print(phrase[phrase.index("and")+1:len(phrase)])
    file = open('inputtext.txt','r')
    outputfile = open('outputtext','w')
    texts = file.readlines()
    for text in texts:
        print(text+" --> "+tran.translate(tran.preprocess(text)))
        outputfile.write(text.strip()+" --> "+tran.translate(tran.preprocess(text))+"\n")
    #unfoundword = []
    '''databasewords = tran.databaseword()
    for text in texts:
        wordlist = tran.preprocess(text)
        for word in wordlist:
            if word not in databasewords:
                if word not in unfoundword:
                    unfoundword.append(word)

    print(len(unfoundword),unfoundword)'''


