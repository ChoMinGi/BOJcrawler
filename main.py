import requests
import sys
from bs4 import BeautifulSoup


url = 'https://www.acmicpc.net/step'

response = requests.get(url)

step_list = []
num=[]
sub=[]
pc=[]

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find("div", {"class": "table-responsive"})
    body = main.find("tbody")
    links = body.find_all("tr")
    for link in links:
        lnk = link.find("a").attrs['href']
        steps = f"https://www.acmicpc.net{lnk}"
        step_list.append(steps)
# 필요한 링크를 모두 가져왔다.
    need_step = input("필요한 단계를 입력하시오.")
    steps = step_list[int(need_step)-1]
# request를 해오고 이를 BS로 html을 파싱해온다.
    step_response = requests.get(steps)
    if step_response.status_code == 200:
        step_html = step_response.text
        step_soup = BeautifulSoup(step_html, 'html.parser')
        step_main = step_soup.find(
            "div", {"class": "table-responsive"})
        step_name = step_soup.find(
            "div", {"class": "breadcrumbs"}).text
        step_body = step_main.find("tbody")
        pbs = step_body.find_all("tr")
        for pb in pbs[0::2]:
            nums = pb.find("td", {"class": "list_problem_id"}).text
            subs = pb.find("a").text
            num.append(nums)
            sub.append(subs)
            pblink = pb.find("a").attrs['href']
            pbcontent = f"https://www.acmicpc.net{pblink}"
            pbcontent_response = requests.get(pbcontent)
            if pbcontent_response.status_code == 200:
                pbcontent_html = pbcontent_response.text
                pbcontent_soup = BeautifulSoup(pbcontent_html, 'html.parser')
                pbcontent_main = pbcontent_soup.find("div", {"id": "problem-body"})
                pcs = pbcontent_main.find("div",{"class": "problem-text"}).text
                pc.append(pcs)
                
            else:
                print(f'There is no content in {nums}')
                
    else:
        print(f'errorcode: {step_response.status_code} at {steps}step')
    if len(num) == len(sub):
        print('work correctly!')
    else:
        print('something is wrong..')
        
else:
    print(response.status_code)
    

sys.stdout=open(f'output {need_step}.txt','w')
# 블로그 html 출력부
print(f'[백준/python] {step_name} 전체 풀이({need_step}단계)')
print('''
<p data-ke-size="size16">&nbsp;</p>
<!-- 목차 부분 -->
<div class="book-toc">
<p data-ke-size="size16"><i><b><span style="font-family: 'Noto Serif KR';">목차</span></b></i></p>
<ul id="toc" style="list-style-type: disc;" data-ke-list-type="disc"></ul>
</div>
<p data-ke-size="size16">&nbsp;</p>
<p data-ke-size="size16"><br /><br /></p>
<!-- 제목 -->
''')
for i in range(len(num)):
    print(f'<h3 data-ke-size="size23"><b><span style="font-family: \'Noto Serif KR\';">{sub[i]}<b>(#{num[i]})</b></b></h3>')
    print('''
    <!-- Hint 란 -->
    <ul style="list-style-type: disc;" data-ke-list-type="disc">
    <li><b><span style="font-family: 'Noto Serif KR';">Problem</span></b></li>
    </ul>
    ''')
    print(f'<p data-ke-size="size16"><span style="font-family: \'Noto Serif KR\';">{pc[i]}</p>')
    print('''
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    <ul style="list-style-type: disc;" data-ke-list-type="disc">
    
    <li><b><span style="font-family: 'Noto Serif KR';">Hint</span></b></li>
    </ul>

    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">힌트입력 (==)</p>
    <!-- Solution 란 -->
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    <ul style="list-style-type: disc;" data-ke-list-type="disc">
    <li><b><span style="font-family: 'Noto Serif KR';">Solution</span></b></li>
    </ul>
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">을 이용한 풀이</p>

    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    <!-- 코드 삽입란 -->
    <pre class="vim">
        <code>
            code code
        </code>
    </pre>
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">contents 01</p>
    
    <!-- 구분선 -->
    <hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style6" />
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">contents 02</p>
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
    ''')

# 태그 입력을 위한 키워드
print(*sub)

# 다중 크롤링 시에 구분 색적 용도
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")
print("==================================================")

