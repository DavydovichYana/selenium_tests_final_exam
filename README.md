# selenium_tests_final_exam
The repo contains tests to final exam of the course dedicated to autotesting with Selenium on Python https://stepik.org/course/575

#Page Object Pattern

Набор тестов для сайта http://selenium1py.pythonanywhere.com/ru/.

Как установить:

Скачиваем файлы и переходим в папку. Устанавливаем chromedriver.

Затем используем pip для установки зависимостей:

pip install -r requirements.txt

Использование.

После настройки скрипта запускаем из корневой папки.

pytest -v --tb=line --language=en -m need_review
pytest -v --tb=line --language=en

Если возникает ошибка, запускаем:

python -m pytest -m need_review -s -v --tb=line .\test_product_page.py

Цель проекта: Итоговый проект для курса на https://stepik.org/