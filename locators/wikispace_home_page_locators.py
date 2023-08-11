from selenium.webdriver.common.by import By


# locators for the main page of any Wiki space
class WikiSpaceHomePageLocators:
    SPACE_TITLE = (By.XPATH, "//ul[@class='leftSidebarUL']//li[1]//div[@class='text-bold']")
    DEFAULT_PAGE_FOR_SPACE_FIELD_LABEL = (By.XPATH, "/div//label[contains(text(), 'Страница по умолчанию')]")
    FAVORITE_PAGES_AREA_LABEL = (By.XPATH, "//div//li[contains(text(), 'Избранное')]")
    ALL_PAGES_LABEL = (By., "//div//li[contains(text(), 'Страницы')]")
    ANALYTICS_BUTTON = (By.XPATH, "//[@href='/dashboards/analytics']")
    WIKI_BUTTON = (By.XPATH, "/a[@href='/apps/wiki']")
