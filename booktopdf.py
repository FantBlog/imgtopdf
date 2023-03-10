import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

''''''
userID = ''  # 아이디 입력하는곳
userPW = ''  # 비밀번호 입력하는곳
remove = True # 이미지 파일이 pdf생성후 지워지길 바란다면
# remove = False 로 바꿔주세요
''''''


def photo(book_url):
    options = webdriver.ChromeOptions()

    # headless 옵션 설정
    options.add_argument('headless')
    options.add_argument("no-sandbox")

    # 브라우저 윈도우 사이즈
    options.add_argument('window-size=1920x1080')

    # 사람처럼 보이게 하는 옵션들
    options.add_argument("disable-gpu")  # 가속 사용 x
    options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

    # 드라이버 위치 경로 입력
    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

    # url을 이용하여 브라우저로 접속
    driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')

    driver.implicitly_wait(3)

    # 아이디/비밀번호를 입력해준다.
    driver.find_element(By.ID, 'userId').send_keys(userID)
    driver.find_element(By.ID, 'userPwd').send_keys(userPW)
    # elem = driver.find_element('userPwd')

    # 로그인 버튼을 누르기
    # elem.send_keys(Keys.RETURN)
    driver.find_element(By.LINK_TEXT, '로그인').click()

    # 입력받은 교재 링크로 접속
    driver.get(book_url)
    page = driver.find_element(By.CLASS_NAME, 'label-page').text
    max_page = int(list(page.split())[2])
    print(max_page,'개의 이미지')

    title = driver.title
    # print(title)

    img = driver.find_element(By.CLASS_NAME, 'background')
    src = img.get_attribute("src")[:-8]
    # print(src)

    # 폴더 생성
    createFolder(title)

    # 화면 캡처
    for i in range(1, max_page + 1):
        driver.get(f'{src}{i:0>4}.jpg')
        driver.get_screenshot_as_file(f'{title}/capture{i}.png')
        print(f'{i}번째 이미지 다운로드 성공')

    driver.quit()
    return title, max_page


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def pdf(title, max_page):
    path_dir = f'{title}/'

    img_list = []

    img_path = f'{title}/capture1.png'
    im_buf = Image.open(img_path)
    cvt_rgb_0 = im_buf.convert('RGB')

    for i in range(1, max_page + 1):
        print(f'pdf {i}병합 완료')
        img_path = f'{title}/capture{i}.png'
        im_buf = Image.open(img_path)
        cvt_rgb = im_buf.convert('RGB')
        img_list.append(cvt_rgb)

    del img_list[0]
    cvt_rgb_0.save(path_dir + title + '.pdf', save_all=True, append_images=img_list)
    
    if remove:
        for i in range(1, max_page + 1):
            os.remove('/abc/test.text')


def main():
    book_url = input('다운받을 교재 링크를 입력 해주세요 : ')
    # book_url = 'https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2023030212125614400/index.html'
    title, max_page = photo(book_url)
    pdf(title, max_page)


if __name__ == "__main__":
    main()
