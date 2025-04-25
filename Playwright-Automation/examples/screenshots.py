# -*- coding: utf-8 -*-

"""
Пример использования Playwright для создания скриншотов.

Этот скрипт демонстрирует:
- Создание скриншота всей страницы
- Создание скриншота определенного элемента
- Создание скриншота всей страницы с прокруткой
- Эмуляцию разных устройств для скриншотов
"""

from playwright.sync_api import sync_playwright
import time


def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()

    # Открываем сайт
    page.goto("https://www.python.org/")

    # Скриншот всей видимой части страницы
    page.screenshot(path="../screenshots/python_org_viewport.png")

    # Скриншот конкретного элемента
    logo = page.locator(".python-logo")
    logo.screenshot(path="../screenshots/python_logo.png")

    # Скриншот всей страницы с прокруткой
    page.screenshot(path="../screenshots/python_org_full.png", full_page=True)

    # Скриншоты с эмуляцией мобильных устройств
    # Создаем новый контекст с эмуляцией iPhone
    iphone = playwright.devices["iPhone 12"]
    iphone_context = browser.new_context(**iphone)
    iphone_page = iphone_context.new_page()
    iphone_page.goto("https://www.python.org/")
    iphone_page.screenshot(path="../screenshots/python_org_iphone.png")

    # Эмуляция iPad
    ipad = playwright.devices["iPad Pro 11"]
    ipad_context = browser.new_context(**ipad)
    ipad_page = ipad_context.new_page()
    ipad_page.goto("https://www.python.org/")
    ipad_page.screenshot(path="../screenshots/python_org_ipad.png")

    # Закрытие браузера
    browser.close()


with sync_playwright() as playwright:
    run(playwright)