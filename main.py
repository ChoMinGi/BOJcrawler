import requests
import sys
from bs4 import BeautifulSoup
import os
import re


def savewithtext(
    need_step,
    step_name,
    problem_num,
    problem_sub,
    problem_des,
    make_step_dir,
    file_namelist,
):
    problem_sublist = []
    savetext = open(f"output{need_step}.txt", "w")
    # 블로그 html 출력부
    savetext.write(f"[백준/python] {step_name} 전체 풀이({need_step}단계)")
    savetext.write(
        """
    <p data-ke-size="size16">&nbsp;</p>
    <!-- 목차 부분 -->
    <div class="book-toc">
    <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">목차</span></p>
    <ul id="toc" style="list-style-type: disc;" data-ke-list-type="disc"></ul>
    </div>
    <p data-ke-size="size16">&nbsp;</p>
    <p data-ke-size="size16"><br /><br /></p>
    <!-- 제목 -->
    """
    )
    for i in range(len(problem_num)):
        file_name = file_namelist[i]
        make_problem_dir = f"{make_step_dir}/{file_name}"
        if file_name in os.listdir(make_step_dir):
            print("동일 이름을 가진 폴더가 존재합니다.", file_name)
        else:
            os.mkdir(str(make_problem_dir))
        pytext = open(f"{make_problem_dir}/{file_name}.py", "r").read()
        readme = open(f"{make_problem_dir}/README.md", "r").read()
        problem_sublist.append(problem_sub[i])
        savetext.write(
            f'<h3 data-ke-size="size23"><b><span style="font-family: \'Noto Serif KR\';">{problem_sub[i]}<b>(#{problem_num[i]})</b></b></h3>'
        )
        savetext.write(
            """
        <!-- Hint 란 -->
        <ul style="list-style-type: disc;" data-ke-list-type="disc">
        <li><b><span style="font-family: 'Noto Serif KR';">Problem</span></b></li>
        </ul>
        """
        )
        savetext.write(
            f'<p data-ke-size="size16"><span style="font-family: \'Noto Serif KR\';">{problem_des[i]}</p>'
        )
        savetext.write(
            """
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
        """
        )
        savetext.write(f"\n{pytext}")
        savetext.write(
            """
            </code>
        </pre>
        <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
        
        <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">
        
        """
        )
        savetext.write(f"\n{readme}")
        savetext.write(
            """
        </p>
        
        <!-- 구분선 -->
        <hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style6" />
        <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
        <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
        <p data-ke-size="size16"><span style="font-family: 'Noto Serif KR';">&nbsp;</p>
        """
        )

    # 태그 입력을 위한 키워드
    print(*problem_sublist)

    # 다중 크롤링 시에 구분 색적 용도
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")
    savetext.write("==================================================")

    savetext.close()


def urlrequest(url):
    """url header 변형으로 크롤링"""
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    return response


def mkdir(root_path, step_name):
    make_step_dir = f"{root_path}/{step_name}"
    if step_name in os.listdir(root_path):
        print("동일 이름을 가진 폴더가 존재합니다.", step_name)
    else:
        os.mkdir(make_step_dir)
    return make_step_dir


def mkproblemdir(make_step_dir, file_name):
    file_name = re.sub(r"[\/*?<>|]", "MoD", file_name)
    make_problem_dir = f"{make_step_dir}/{file_name}"
    if file_name in os.listdir(make_step_dir):
        print("동일 이름을 가진 폴더가 존재합니다.", file_name)
    else:
        os.mkdir(str(make_problem_dir))
    open(f"{make_problem_dir}/{file_name}.py", "w")
    open(f"{make_problem_dir}/README.md", "w")


root_path = "/home/chomk/Github/BOJ-python"
main_url = "https://www.acmicpc.net"
url = f"{main_url}/step"


# Step 가져오기
step_list = []
# 문제 번호
problem_num = []
# 문제 소제목
problem_sub = []
# 문제 설명
problem_des = []

whole_response = urlrequest(url)
# 응답 코드가 200일시 *정상적으로 가져왔을시에
if whole_response.status_code == 200:
    html = whole_response.text
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("div", {"class": "table-responsive"})
    body = main.find("tbody")
    links = body.find_all("tr")
    for link in links:
        lnk = link.find("a").attrs["href"]
        steps = main_url + lnk
        step_list.append(steps)

    # 필요한 링크를 모두 가져왔다.
    need_step = int(input("필요한 단계를 입력하시오."))
    steps = step_list[int(need_step) - 1]

    # request를 해오고 이를 BS로 html을 파싱해온다.
    step_response = urlrequest(steps)
    if step_response.status_code == 200:
        step_html = step_response.text
        step_soup = BeautifulSoup(step_html, "html.parser")
        step_main = step_soup.find("div", {"class": "table-responsive"})
        step_name = step_soup.find("div", {"class": "breadcrumbs"}).text
        step_body = step_main.find("tbody")
        pbs = step_body.find_all("tr")
        cnt = 1
        # Step 에 해당하는 폴더 생성하기
        make_step_dir = mkdir(root_path, step_name)

        file_namelist = []

        setmode = int(input("블로그 포스팅용 html을 원한다면 1 을 새로운 단계를 가져오려면 0 을 입력하세요"))
        for pb in pbs[0::2]:
            nums = pb.find("td", {"class": "list_problem_id"}).text
            subs = pb.find("a").text
            file_name = f"{str(cnt).zfill(2)}#{nums}_{subs}"
            # 문제별 폴더, 파일(.py, README) 생성하기
            file_namelist.append(file_name)
            if setmode == 0:
                mkproblemdir(make_step_dir, file_name)
            cnt += 1
            problem_num.append(nums)
            problem_sub.append(subs)
            pblink = pb.find("a").attrs["href"]
            pbcontent = main_url + pblink
            pbcontent_response = requests.get(
                pbcontent, headers={"User-Agent": "Mozilla/5.0"}
            )

            if pbcontent_response.status_code == 200:
                pbcontent_html = pbcontent_response.text
                pbcontent_soup = BeautifulSoup(pbcontent_html, "html.parser")
                pbcontent_main = pbcontent_soup.find("div", {"id": "problem-body"})
                pcs = pbcontent_main.find("div", {"class": "problem-text"}).text
                problem_des.append(pcs)

            else:
                print(f"There is no content in {nums}")
    else:
        print(f"errorcode: {step_response.status_code} at {steps}step")
    if len(problem_num) == len(problem_sub):
        print("work correctly!")
    else:
        print("something is wrong..")
else:
    print("파싱 에러", whole_response.status_code)
    raise ConnectionError("크롤링 HTML 가져오지 못하였음")


if setmode == 1:
    savewithtext(
        need_step,
        step_name,
        problem_num,
        problem_sub,
        problem_des,
        make_step_dir,
        file_namelist,
    )
