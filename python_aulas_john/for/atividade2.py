# def anagrams():
#     p1 = input(" Digite a primeira palavra: ")
#     p2 = input(" Digite a segunda palavra: ")    
#     return sorted(p1) == sorted(p2)
# print(anagrams())

def anagrams(p1,p2):       
    return sorted(p1) == sorted(p2)
print(anagrams("tema","mate")) # sorted oraniza as letras aemt = amet
print(anagrams("roma","orma")) # sorted oraniza as letras amor = amor
print(anagrams("tabby","batty")) # sorted oraniza as letras abtty != abbty