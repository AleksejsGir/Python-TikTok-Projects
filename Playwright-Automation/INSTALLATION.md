# Установка и запуск проекта

В этом руководстве подробно описан процесс установки и запуска проекта Playwright-Automation. Даже если вы никогда раньше не устанавливали Python или не работали с командной строкой, вы сможете легко следовать этим инструкциям.

## Шаг 1: Установка Python

### Windows
1. Скачайте установщик Python с [официального сайта](https://www.python.org/downloads/)
2. Запустите установщик и **обязательно отметьте галочку "Add Python to PATH"**

   ![Отметьте галочку Add Python to PATH](https://docs.python.org/3/_images/win_installer.png)

3. Нажмите "Install Now"
4. Дождитесь завершения установки и закройте установщик

### macOS
1. Скачайте установщик Python для Mac с [официального сайта](https://www.python.org/downloads/)
2. Запустите установщик и следуйте инструкциям
3. Или установите через Terminal с помощью Homebrew:
   ```
   brew install python
   ```

### Linux
В большинстве дистрибутивов Python уже установлен. Если нет, используйте:

Ubuntu/Debian:
```
sudo apt update
sudo apt install python3 python3-pip
```

### Проверка установки Python

После установки откройте командную строку (Terminal на Mac/Linux или Command Prompt на Windows) и введите:
```
python --version
```

Вы должны увидеть версию Python (например, `Python 3.9.5`). Если вместо этого появляется ошибка, проверьте, правильно ли установлен Python и добавлен ли он в PATH.

## Шаг 2: Скачивание проекта

### Вариант 1: Через Git (рекомендуется)
1. Установите Git с [официального сайта](https://git-scm.com/downloads)
2. Откройте командную строку или терминал
3. Выполните команду:
   ```
   git clone https://github.com/AleksejGir/Python-TikTok-Projects.git
   cd Python-TikTok-Projects
   ```

### Вариант 2: Скачивание ZIP-архива
1. Перейдите на страницу репозитория: https://github.com/AleksejGir/Python-TikTok-Projects
2. Нажмите на зеленую кнопку "Code"
   
   ![Кнопка Code на GitHub](https://docs.github.com/assets/images/help/repository/code-button.png)

3. Выберите "Download ZIP"
   
   ![Скачивание ZIP-архива](https://docs.github.com/assets/images/help/repository/download-code-button.png)

4. Распакуйте архив в удобное место на компьютере
5. Откройте командную строку или терминал и перейдите в распакованную папку:
   ```
   cd путь/к/папке/Python-TikTok-Projects
   ```

## Шаг 3: Установка зависимостей

### Открытие командной строки (если еще не открыта)

#### Windows
1. Нажмите Win+R
2. Введите `cmd` и нажмите Enter

#### macOS
1. Откройте Finder
2. Перейдите в Applications → Utilities
3. Запустите Terminal

#### Linux
1. Используйте сочетание клавиш Ctrl+Alt+T в большинстве дистрибутивов

### Установка Playwright и зависимостей

1. Перейдите в папку проекта:
   ```
   cd Python-TikTok-Projects/Playwright-Automation
   ```

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
   
   Если у вас возникла ошибка "pip не является внутренней или внешней командой", попробуйте:
   ```
   python -m pip install -r requirements.txt
   ```

3. Установите браузеры для Playwright:
   ```
   playwright install
   ```
   
   Или, если возникла ошибка:
   ```
   python -m playwright install
   ```

4. Дождитесь завершения установки. Playwright скачает и установит необходимые браузеры (Chrome, Firefox, WebKit).

## Шаг 4: Запуск примеров

1. Перейдите в папку с примерами:
   ```
   cd examples
   ```

2. Запустите самый простой пример для начинающих:
   ```
   python super_simple_example.py
   ```

3. После успешного запуска вы увидите, как открывается браузер, переходит на сайт и делает скриншот:
   
   ![Пример работы скрипта](../screenshots/example_screenshot.png)

4. Затем вы можете запустить другие примеры:
   ```
   python basic_example.py
   python form_filling.py
   python screenshots.py
   ```

## Возможные проблемы и их решения

### "pip не является внутренней или внешней командой"
**Проблема:** Система не может найти команду pip.

**Решение:**
1. Убедитесь, что Python добавлен в PATH при установке
2. Попробуйте использовать `python -m pip` вместо просто `pip`
3. Перезапустите командную строку или компьютер после установки Python

### "ImportError: No module named playwright"
**Проблема:** Не установлена библиотека Playwright.

**Решение:**
1. Убедитесь, что вы правильно установили зависимости:
   ```
   python -m pip install -r requirements.txt
   ```
2. Проверьте, что установка прошла без ошибок

### "Ошибка при запуске браузера"
**Проблема:** Браузеры для Playwright не установлены.

**Решение:**
```
python -m playwright install
```

### Ошибки с путями к файлам
**Проблема:** Скрипты не могут найти файлы в других папках.

**Решение:**
1. Убедитесь, что вы запускаете скрипты из правильной директории (папка `examples` или `scripts`)
2. При необходимости измените пути к файлам в скриптах на абсолютные

### "ModuleNotFoundError: No module named 'some_module'"
**Проблема:** Отсутствует какой-то модуль, необходимый для работы.

**Решение:**
```
python -m pip install some_module
```

### Если браузер не открывается
**Проблема:** Браузер запускается в headless режиме (без графического интерфейса).

**Решение:**
Убедитесь, что в коде установлен параметр `headless=False`:
```python
browser = playwright.chromium.launch(headless=False)
```

## Дополнительная помощь

Если у вас возникли другие проблемы:
1. Посмотрите видео-инструкцию на [моем TikTok канале](https://www.tiktok.com/@aleksej_gir)
2. Задайте вопрос в комментариях к видео
3. Создайте Issue в репозитории на GitHub

## Что дальше?

После успешной установки и запуска примеров рекомендуем:
1. Изучить код примеров в папке `examples/`
2. Выполнить практические задания из файла `exercises.md`
3. Попробовать модифицировать примеры под свои задачи