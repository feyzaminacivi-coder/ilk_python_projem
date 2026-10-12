


KAZANANLAR = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
sayac = {"dugum":0}

def kazanan(t):
    for a, b, c in KAZANANLAR:
        if t[a] == t[b] == t[c] and t[a] != " ":
         return t[a]
    return None
def minimax(t,sira):
        sayac ["dugum"] +=1
        k = kazanan(t)
        if k == "X": 
            return 1
        if k == "O": 
            return -1
        if " " not in t: return 0
        puanlar = []


        for i in range(9):
            if t[i] == " ":
                t[i] = sira
                puanlar.append(minimax(t, "O" if sira == "X" else "X"))
                t[i] = " "
        return max(puanlar) if sira == "X" else min(puanlar)

def en_iyi_hamle(t, sira):
    en_iyi, en_iyi_puan = None, None
    for i in range(9):
        if t[i] == " ":
            t[i] = sira
            puan = minimax(t, "O" if sira == "X" else "X") 
            t[i] = " "
            if en_iyi is None or (sira == "X" and puan > en_iyi_puan) or (sira == "O" and puan < en_iyi_puan):
                en_iyi, en_iyi_puan = i, puan
    return en_iyi

def goster(t):
    for i in range(3):
        print(" " + " | ".join(t[i*3:(i+1)*3]))
        if i < 2:print("---+---+---")
        print()

tahta = [" "] * 9
sayac["dugum"] = 0
print("Boş tahtada Xiçin en iyi hamle:", en_iyi_hamle(tahta, "X"))
print("Bunu bulmak için bakılan düğüm sayısı:", sayac["dugum"])

def xox_oyna(insan_hamleleri=None):
    t = [" "] * 9
    i = 0
    while kazanan(t) is None and " " in t:
        h = en_iyi_hamle(t, "X"); t[h] = "X"
        print("Bilgisayar (X):" , h); goster(t)
        if kazanan(t) or " " not in t:break
        if insan_hamleleri:
            h = insan_hamleleri[i]; i += 1
        else:
            h = int(input("Senin hamlen (0-8)?"))
        while t[h] != " ":
            h = int(input("Dolu! Başka kutu (0-8)? "))
            t[h] = "0"
            print("Sen (0):" , h); goster(t)
    k = kazanan(t)
    print("Sonuç:", "Bilgisayar kazandı" if k == "X" else "Sen kazandın" if k == "O" else "Berabere")

xox_oyna()






