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
# def search_by_genre(cinema:list)->list:
#     lst=[]
#     qidiruv=input(">>>")
#     for kino in cinema:
#         if qidiruv==kino["genre"]:
#             lst.append(kino)
#     print(lst)

# qiymat = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]
# search_by_genre(cinema=qiymat)


# 3-misol
# def merge_unique_ids(a:list,b:list)->list:
#     natija=set(a+b)
#     print(natija)

# merge_unique_ids(a= ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] ,b= ['U1003', 'U1005', 'U1006', 'U1002', 'U1007'])

# 4-misol
def sorted_by_price(products:list)->list:
    
    natija=sorted(products,key=lambda x:int(x[1]),reverse=True)
    for item in natija:
        print(item)


qiymat = [
    ('Olma', '12000', '50'),
    ('Banan', '8000', '100'),
    ('Gilos', '15000', '70'),
    ('Apelsin', '9000', '80'),
    ('Anor', '30000', '20'),
    ('Uzum', '20000', '40'),
    ('Tarvuz', '25000', '15'),
    ('Shaftoli', '18000', '60'),
    ('Qovun', '40000', '25'),
    ('Qulupnay', '35000', '10')
]
sorted_by_price(products=qiymat)

