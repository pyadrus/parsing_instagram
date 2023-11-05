from selenium import webdriver
from loguru import logger
import time
from selenium.webdriver.common.by import By
import instaloader

# https://www.instagram.com/manumendes.rj/

def main():
    post = []  # Создаем пустой список
    with open('post.txt', 'r') as file:  # Открываем файл
        for line in file:
            line = line.strip()  # Удаляем лишние пробелы и символы новой строки в начале и конце строки
            post.append(line)  # Добавляем в список строку

    for url in post:
        browser = webdriver.Firefox()  # Открываем браузер
        browser.get(url)  # Открываем страницу
        time.sleep(10)
        elem = browser.find_element(By.XPATH,
                                    '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')  # Find the search box
        elem.click()
        time.sleep(5)
        elem = browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/span/a')  # Find the search box
        elem.click()
        time.sleep(1)
        get_url = browser.current_url  # Getting current URL
        logger.info(get_url)
        # Создайте объект Instaloader
        L = instaloader.Instaloader()
        # Загрузите профиль Instagram
        profile = instaloader.Profile.from_username(L.context,'manumendes.rj')  # Замените 'username' на имя пользователя Instagram
        # Получите информацию о профиле
        print("Username:", profile.username)
        print("Full Name:", profile.full_name)
        print("Biography:", profile.biography)
        print("Followers:", profile.followers)
        print("Following:", profile.followees)
        print("Posts Count:", profile.mediacount)
        print("External URL:", profile.external_url)
        print("Is Private:", profile.is_private)
        print("Is Verified:", profile.is_verified)
        print("IGTV Count:", profile.igtvcount)


main()
