from selenium.webdriver.common.by import By


class HomePageLocators:
    # EXIT button when user login
    exit_loc = (By.XPATH, '//a[@class="quit"]')

    # Hot people
    hot_people_list_loc = (By.XPATH, '//dl[@class="hot-news-text"]')
    hot_people_list_text_loc = (By.XPATH, '//dl[@class="hot-news-text"]//dd')
    loc_lst = (((By.XPATH, '(//dl[@class="hot-news-text"])[1]'), (By.XPATH, '(//dl[@class="hot-news-text"]//dd)[1]')),
               ((By.XPATH, '(//dl[@class="hot-news-text"])[2]'), (By.XPATH, '(//dl[@class="hot-news-text"]//dd)[2]')),
               ((By.XPATH, '(//dl[@class="hot-news-text"])[3]'), (By.XPATH, '(//dl[@class="hot-news-text"]//dd)[3]')),
               ((By.XPATH, '(//dl[@class="hot-news-text"])[4]'), (By.XPATH, '(//dl[@class="hot-news-text"]//dd)[4]')),
               ((By.XPATH, '(//dl[@class="hot-news-text"])[5]'), (By.XPATH, '(//dl[@class="hot-news-text"]//dd)[5]'))
               )


if __name__ == '__main__':
    hpl = HomePageLocators
    for a,b in hpl.loc_lst:
        print(a, b)



