import requests
from bs4 import BeautifulSoup

url = 'https://www.acmicpc.net/step'

response = requests.get(url)

step_list = []

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
        step_body = step_main.find("tbody")
        pbs = step_body.find_all("tr")
        for pb in pbs[0::2]:
            nums = pb.find("td", {"class": "list_problem_id"}).text
            subs = pb.find("a").text
            print(nums, subs)
    else:
        print(f'errorcode: {step_response.status_code} at {steps}step')

else:
    print(response.status_code)
