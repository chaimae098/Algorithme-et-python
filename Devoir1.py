import string

def nombremots(texte):
    return len([m for m in texte.split(" ") if m!=""])

def occurencemots(texte):
    d={}
    for mot in texte.split(" "):
        mot = mot.strip(string.punctuation).lower()
        if mot!="":
            d[mot]=d.get(mot,0)+1
    return d

def longueur_moyenne(texte):
    mots=[m for m in texte.split(" ") if m!=""]
    l=[len(m) for m in mots]
    moyenne=sum(l)/len(l)
    d=occurencemots(texte)
    maxOcc=max(d.values())
    motsMax=[k for k,v in d.items() if v==maxOcc]
    return motsMax, maxOcc, moyenne

def palindromes(texte):
  return [mot for mot in texte.split() if mot == mot[::-1] and 
          len(mot) > 1] 

def phrases(texte):
    temp=[]
    ph=""
    for ch in texte:
        ph+=ch
        if ch in ".!?":
            if ph.strip()!="":
                temp.append(ph.strip())
            ph=""
    if ph.strip()!="":
        temp.append(ph.strip())
    return temp

def longueur_phrases(liste):
    return [len(p.split()) for p in liste]

def ponctuation_utilisee(texte):
    return {c for c in texte if c in string.punctuation}

def top_mots(d,n=10):
    return sorted(d.items(), key=lambda x:x[1], reverse=True)[:n]

def moins_utilises(d,n=10):
    return sorted(d.items(), key=lambda x:x[1])[:n]

def vocabulaire_unique(d):
    return set(d.keys())

def patterns_repetitifs(d,min_occ=3):
    return [mot for mot,f in d.items() if f>=min_occ]


with open("texte.txt","r") as f:
    data=f.read()

nb_mots=nombremots(data)
freq=occurencemots(data)
motsMax, maxOcc, moy=longueur_moyenne(data)
pal=palindromes(data)
phr=phrases(data)
long_phr=longueur_phrases(phr)
top10=top_mots(freq)
least10=moins_utilises(freq)
vocab=vocabulaire_unique(freq)
patterns=patterns_repetitifs(freq)
punc=ponctuation_utilisee(data)


print("Nombre de mots :", nb_mots)
print("Fréquence des mots :", freq)
print("Longueur moyenne des mots :", moy)
print("Mots les plus utilisés :", motsMax, "->", maxOcc, "fois")
print("Mots les moins utilisés :", least10)
print("Top 10 mots :", top10)
print("Palindromes :", pal)

print("Nombre de phrases :", len(phr))
print("Longueur des phrases :", long_phr)
print("Types de ponctuation utilisés :", punc)

print("Phrases les plus longues :", sorted(phr, key=lambda p:len(p.split()), reverse=True)[:3])
print("Diversité du vocabulaire :", len(vocab), "mots uniques")
print("Patterns répétitifs :", patterns)
