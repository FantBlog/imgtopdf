# imgtopdf
특정사이트의 이미지를 크롤링 해주는 파이썬 프로젝트

준비물 : 아이디, 비밀번호, 교재 링크, 파이썬이 설치된 PC

# 1. 기본 설정
윈도우 키를 누르고 cmd입력후 엔터

cmd창에 다음 코드를 실행
pip install selenium

cmd창에 다음 코드를 실행
pip install image

cmd창에 다음 코드를 실행 ( 혹시 버전이 맞지 않을경우 )
python.exe -m pip install --upgrade pip

혹시 chromedriver관련 오류가 발생할 경우
chromedriver를 검색 후 본인 chrome의 버전과 맞는 
chromedriver.exe를 다운받아 py파일과 같은 폴더에 넣어주세요

------------------

# 2. 폴더 설정
py를 실행하는 폴더안에 교재 제목의 폴더가 생길 예정입니다.
원하시는 폴더로 미리 옮기세요.

교재topdf.py 파일을 열어서
아이디와 비밀번호 입력하세요.

py파일을 더블클릭하여 실행한 후,
교재 url을 붙여넣고 엔터를 누르세요