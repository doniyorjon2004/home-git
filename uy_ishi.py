# 1-misol
# def majority(lst:list)->int:
#     if not lst:
#         print(-1)
#     else: 
#         dct={}
#         for son in lst:
#             if son not in dct:
#                 dct[son]=1
#             else:
#                 dct[son]+=1
#         natija=max(dct.items(),key=lambda x:x[1])
#         print(natija)


# majority(lst=list(map(int, input("Sonlarni kiriting: ").split())))


# 2-misol
def search_by_genre(cinema:list)->list:
    lst=[]
    qidiruv=input(">>>")
    for kino in cinema:
        if qidiruv==kino["genre"]:
            lst.append(kino)
    print(lst)

qiymat = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]
search_by_genre(cinema=qiymat)
