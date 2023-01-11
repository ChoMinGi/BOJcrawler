import re
import os

make_step_dir = "/root/Github/BOJ-python/동적 계획법 1"
file_name = "01#24416_알고리즘 수업 - 피보나치 수 1"

def rdproblemdir(make_step_dir,file_name):
    file_name = re.sub(r"[\/*?<>|]","MoD",file_name)
    make_problem_dir = f"{make_step_dir}/{file_name}"
    if file_name in os.listdir(make_step_dir):
        print("동일 이름을 가진 폴더가 존재합니다." , file_name)
    else:
        os.mkdir(str(make_problem_dir))
    pytext = open(f'{make_problem_dir}/{file_name}.py','r')
    readme = open(f'{make_problem_dir}/README.md','r')

    print(pytext.read())
rdproblemdir(make_step_dir,file_name)