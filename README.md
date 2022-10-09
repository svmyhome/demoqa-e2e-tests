# demoqa-e2e-tests

### Hot keys pyCharm
Alt + shift + E  в режиме дебага выполнить одну строку


### Tips and Tricks

setTimeout(function() {debugger}, 3000);   остановка JavaScripts
or 
перейти в настройки хром три точки->More tools->Rendering->Emulate a focuse page



### Python commands
python3 -m venv .venv - создает виртуальное окружение через коммандную строку
source .venv/bin/activate - активирует виртуальное окружение

### pyTest
pytest --fixtures -- список всех используемых фикстур
pytest tests/  --alluredir=./tests/allure-results

pytest . - запустит все тесты в каталоге

[pytest]
addopts = --alluredir=allure-results --durations=10 -vv --clean-alluredir

### Git commands 

ssh-keygen -t rsa  - создание ключевой пары для Ubuntu/MAc
ssh-keygen -t ed25519 -C "svmyhome@mail.ru" - windows

git init
git rm --cached nameFile 

git checkout Lesson_7_HomeWork_PageObjects_Part_1 ./models/controls/   - перетащить в текущую ветку все файлы из каталога с другой ветки
git checkout Lesson_7_HomeWork_PageObjects_Part_1 ./models/pages/webtables_fill.py - перетащить конкретный файл

вывести из под контроля файл
git rm --cached <file>
вывести из под контроля папку
git rm -r --cached path_to_your_folder/


### как назвать проекты в PyCharm
название проекта-test
например: demoqa-test 

## Selene
should - любая проверка  -- should(have.tite('name')) or be
element и all поиск по элементу/элементам
bowser.config.(разные настройки)
browser.config.timeout = 4   # к каждой команде применяется ожидание  4 секунды
    browser.with_(timeout=6).element('.main-header').should(have.text('Text Box'))  # например можно так таймаут установить эмулируя медленный браузер
    browser.all('#userForm input, #userForm textarea').with_(timeout=3).should(have.size(4)) # например можно так таймаут установить эмулируя долгую загрузку элементов
 

from demoqa_e2e_tests import models  # если в init прописать пути то можно собрать единую точку для вриложения
from demoqa_e2e_tests.models import pages as app # импорт страниц с синонимом app app.registration_form.add_hobbies()

## Allure
Windows
    В pyCharm: установить [scoop](https://github.com/ScoopInstaller/Scoop#readme)
    Перезагрузится: (Возможно просто закрыт консоли и pyCharm поможет)
    установить в pyCharm: scoop install allure
Linux
качаешь зип аллюра отсюда :  https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/    
 зип :allure-commandline-2.19.0.zip   

распаковываешь его в  /opt/
sudo tar -zxvf allure-2.6.0.tgz -C /opt/   
sudo ln -s /opt/allure-2.6.0/bin/allure /usr/bin/allure   (прописываешь символьную ссылку)
allure --version  

## Chat boot

берет данные для генерации из allure-report/widgets/summary.json
