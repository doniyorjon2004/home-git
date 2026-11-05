# 1-misol
def majority(lst:list)->int:
    if not lst:
        print(-1)
    else: 
        dct={}
        for son in lst:
            if son not in dct:
                dct[son]=1
            else:
                dct[son]+=1
        natija=max(dct.items(),key=lambda x:x[1])
        print(natija)


majority(lst=list(map(int, input("Sonlarni kiriting: ").split())))