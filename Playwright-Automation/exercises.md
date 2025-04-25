# Практические задания по Playwright

Этот файл содержит упражнения для практики работы с Playwright. Каждое задание построено так, чтобы помочь вам освоить определенный аспект автоматизации браузера.

## Задание 1: Поиск в Google

**Цель:** Написать скрипт, который выполняет поиск в Google и делает скриншот результатов.

**Шаги:**
1. Открыть Google
2. Ввести поисковый запрос "Python для начинающих"
3. Нажать кнопку поиска или клавишу Enter
4. Сделать скриншот результатов

**Подсказки:**
- URL: https://www.google.com
- Поле поиска можно найти по селектору: `input[name="q"]`
- Кнопку поиска можно найти или просто нажать клавишу Enter: `page.press('input[name="q"]', 'Enter')`

**Шаблон решения:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Ваш код здесь
    
    browser.close()
```

## Задание 2: Заполнение простой формы

**Цель:** Заполнить форму на демо-сайте и получить результат.

**Шаги:**
1. Открыть страницу с формой: https://httpbin.org/forms/post
2. Заполнить все поля формы (имя, email, телефон и т.д.)
3. Отправить форму
4. Сделать скриншот страницы с результатами

**Подсказки:**
- Текстовые поля: `input[name="custname"]`, `input[name="custtel"]`, `input[name="custemail"]`
- Выпадающий список: `select[name="size"]`
- Чекбоксы: `input[name="topping"]`
- Кнопка отправки: `button[type="submit"]`

**Шаблон решения:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://httpbin.org/forms/post")
    
    # Заполнение полей
    # ...
    
    # Отправка формы
    # ...
    
    # Ожидание результата и скриншот
    # ...
    
    browser.close()
```

## Задание 3: Сбор данных с веб-сайта

**Цель:** Собрать данные о погоде с веб-сайта.

**Шаги:**
1. Открыть сайт с прогнозом погоды (например, https://www.weather.gov/)
2. Найти элементы, содержащие данные о погоде на ближайшую неделю
3. Извлечь и вывести эти данные (дата, температура, описание)

**Подсказки:**
- Используйте `.inner_text()` для получения текста элемента
- Используйте `.count()` для подсчета количества элементов
- Используйте цикл для обработки нескольких элементов

**Шаблон решения:**
```python
from playwright.sync_api import sync_playwright

def extract_weather_data(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    
    page.goto("https://www.weather.gov/")
    
    # Получение элементов с прогнозом погоды
    # ...
    
    # Извлечение и вывод данных
    # ...
    
    browser.close()

with sync_playwright() as p:
    extract_weather_data(p)
```

## Задание 4: Авторизация на сайте

**Цель:** Написать скрипт, который авторизуется на сайте и сохраняет состояние сессии.

**Шаги:**
1. Открыть страницу авторизации (можно использовать тестовый сайт, например: https://demo.playwright.dev/login)
2. Ввести логин и пароль
3. Нажать кнопку входа
4. Проверить, что авторизация прошла успешно
5. Сохранить состояние сессии в файл
6. Создать второй скрипт, который использует сохраненное состояние

**Подсказки:**
- Для сохранения состояния используйте: `context.storage_state(path="auth.json")`
- Для загрузки состояния: `context = browser.new_context(storage_state="auth.json")`

**Шаблон решения:**
```python
import os
from playwright.sync_api import sync_playwright

def login_and_save_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Код для авторизации
    # ...
    
    # Сохранение состояния
    context.storage_state(path="auth.json")
    
    browser.close()

def use_saved_state(playwright):
    browser = playwright.chromium.launch(headless=False)
    
    # Загрузка сохраненного состояния
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    
    # Проверка авторизации
    # ...
    
    browser.close()

with sync_playwright() as p:
    if not os.path.exists("auth.json"):
        login_and_save_state(p)
    else:
        use_saved_state(p)
```

## Задание 5: Создание скриншотов для разных устройств

**Цель:** Написать скрипт, который создает скриншоты сайта для разных устройств (десктоп, планшет, телефон).

**Шаги:**
1. Открыть веб-сайт (например, ваш любимый новостной сайт)
2. Создать скриншот для десктопа
3. Создать скриншот для iPhone
4. Создать скриншот для iPad
5. Сохранить все скриншоты в отдельные файлы

**Подсказки:**
- Используйте `playwright.devices` для получения предустановленных настроек устройств
- Для каждого устройства создавайте отдельный контекст

**Шаблон решения:**
```python
from playwright.sync_api import sync_playwright

def capture_responsive_screenshots(playwright):
    browser = playwright.chromium.launch()
    
    # URL сайта для скриншотов
    url = "https://www.example.com"
    
    # Скриншот для десктопа
    # ...
    
    # Скриншот для iPhone
    # ...
    
    # Скриншот для iPad
    # ...
    
    browser.close()

with sync_playwright() as p:
    capture_responsive_screenshots(p)
```

---

## Советы по выполнению заданий

1. **Не спешите.** Начните с простых примеров из репозитория, поймите, как они работают.

2. **Используйте отладку.** Добавляйте `page.pause()` для остановки выполнения и изучения страницы.

3. **Подбирайте селекторы.** Если элемент не находится, используйте DevTools (F12) в браузере для поиска правильных селекторов.

4. **Добавляйте ожидания.** Используйте `page.wait_for_selector()` или `page.wait_for_load_state()`, если страница не успевает загрузиться.

5. **Решайте проблемы постепенно.** Если что-то не работает, разбейте задачу на более мелкие части и проверяйте каждую.

Удачи в выполнении заданий!