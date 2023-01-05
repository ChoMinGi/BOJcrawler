# BOJcrawler
 To reduce the hassle of blog posting
 
 
 포스팅에 사용될 문제나 예제 문제 설명등을 원하는 HTML 서식 형태로 출력
 
 + 여러가지 부가적인(많은) 기능들이 추가 탑재 되었습니다 바로 in Ver 2.0.0 에서!
 
 
# Overview
 fully compatible with tistory
 
 
 Tistory에 맞게 짜여져있다.
 
 You can find what it results in below link
 
 
 아래 링크에서 본 프로젝트의 결과에 대해서 확인이 가능합니다.
 
 https://url.kr/h7egvx
 
[08/14] prettier font [본명조] and spacing between lines


아무튼 예쁘게 만들었습니다.

[10/03] It was printed in the form of a file every time a crawl was requested.


 크롤링 내역이 파일 형태로도 저장되게 하였습니다.

# Module

 requests html
 
 bs4
 
 
# Result preview


**Given the above, the following versioning pattern lends itself well to the BoJcrawling project:**


**본 프로젝트 버전관리 규칙**

_**api.major.patch**_

- **API**: Bumped when Adding or Removing api

  *Examples:* Removing an endpoint, Supporting new website
- **Major**: Bumped when breaking changes are committed to main.py

  *Examples:* Bumping the website structure version, altering the configuration in a non-backward-compatible manner
- **patch**: Bug fixing, Adding little function

  *Examples:* Prettier fonts, Adding blanks

## version 1.0.0


![크롤 결과](https://user-images.githubusercontent.com/81455273/184531679-ead2c0ae-fc84-4148-8e92-12cc740771f0.jpg)


## version 1.1.1
save with txt file


txt 파일 형식으로 저장하게 하였습니다.


+prettier font

It became easier to distinguish and easier to copy to blog.


본 업데이트로 포스팅 시에 복사하기 붙여넣기 하기가 수월해졌습니다.



![image](https://user-images.githubusercontent.com/81455273/194052383-f971feb6-b449-40d5-b604-b85355a21a46.png)

## version 1.2.0
Add subtitle at the top of the resultance file


파일 맨 위에 포스팅의 제목을 규칙에 따라서 출력하게 하였습니다.

It became easier to get title of solution posting on blog.


그래서 블로그 하기가 더 빨라짐ㅎㅎ


![image](https://user-images.githubusercontent.com/81455273/194052795-e4ed4f7c-6aa9-4c1d-a4c9-d59c15786c27.png)


## version 2.0.0
Since the solution was also posted on GitHub, the code was parsed into HTML in the form of code in the blog, and the README file for each folder was in the form of explanation.


이제 깃허브에 풀이와 설명을 적을것이기 때문에 깃에 올린 코드와 README내의 설명을 가져와서 블로그의 HTML 규칙에 맞게 코드 형식을 맞추어서 바로 포스팅 할 수 있게 하였습니다.

Also, the folder by subject is in the following format, create the folder according to the rules and for README files and pools.It also adds the ability to generate py files by itself.


또한 깃허브에 올라갈 폴더도 일정한 형식을 띄고 있기 때문에 이에 맞추어서 파이썬 명령어로 각 문제별 폴더와 .py 파일 README 파일 등도 미리 생성하게 하였습니다.


![image](https://user-images.githubusercontent.com/81455273/210334464-927fa631-5483-4acb-9aaa-69c8c1d1909f.png)


00#00000_문제이름


00#00000_문제이름_문제풀이방식.py


00 - order of each stage


#00000 - number of each problem

![image](https://user-images.githubusercontent.com/81455273/210694335-405aa108-5f30-406d-94a3-72e8900b1e45.png)


So....... It's not a crawler, but a posting macro helper for me. :)
이제는 크롤러가 아니라 나만의,, 포스팅 헬퍼가 되었습니다 :)


+ 추가
https://github.com/ChoMinGi/BOJ-python/commit/b8af02842dcdbd8f45cbdc77a732631365858c5f
위 크롤러의 mkdir, mkproblemdir 을 사용한 결과물
