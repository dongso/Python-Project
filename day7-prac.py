from bs4 import BeautifulSoup
import urllib.request as req


#문제1

d=[]


for n in range(1,5000):
    sum=0
    for j in range(len(str(n))):
        sum+=int(str(n)[j])
    sum+=int(n)
    if sum>5000: break
    d.append(sum)

selfN=0
startN=1

d.sort() #d[n]의 결과 오름차순으로 정렬
print(d)
for i in range(len(d)):
    while d[i] > startN: #연산을 통해 얻은 결과중에 startN이 없으면 selfNumber이다.
        selfN+=startN
        startN+=1
    startN=d[i]+1

print(selfN)
#문제2
url="http://naver.com"
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')

getItem=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

index=1
for item in getItem:
    print("%d위"%index, item.string)
    index+=1


