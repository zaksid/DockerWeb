## DockerWeb
Дозволяє користувачеві створювати і розгортати образи веб-серверів. Система побудована з використанням Docker контейнерів.
Спілкування між сервером і машинами, на яких запущені образи контейнерів, здійснюється за допомогою сокетів.

### Встановлення Docker:
`$ sudo apt-get install linux-image-generic-lts-trusty`

`$ wget -qO- https://get.docker.com/ | sh`

`$ sudo usermod -aG docker $USER`

`$ sudo service docker start`

### Встановлення компонентів python
`$ sudo apt-get install python3-pi`

`$ sudo apt-get install python3-setuptools`

`$ sudo easy_install3 pip`

`$ sudo pip3 install docker-py`

`$ sudo apt-get install gcc python3-dev`

`$ sudo pip3 install psutil`


#### Запуск контейнера nginx
`$ docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx`

### Структура програми
Додаток складається з наступних модулів:

**Container_manager**

Описує процес створення, запуску, зупинки контейнера, дозволяє отримати список контейнерів, інформацію про конкретний контейнер, а також кількість споживаної пам'яті.

**Hosts_manager**

Дозволяє читати зі вказаного файлу хости і отримувати список доступних для використання хостів.

**Server**

Основний модуль. Надає користувачу текстовий інтерфейс для управління контейнерами.

**Socket**

Здійснює основні дії з сокетами. Власне створює / зупиняє контейнер і підключає сокет.

**Host**

Здійснює прив'язку контейнера до сокета.

**Utility**

Містить деякі додаткові утиліти, необхідні для роботи програми.


### Робота програми
Управління контейнерами здійснюється за допомогою головного модуля serverpy:

`$ python3 server.py`

### Команди програми
`create`. Створити новий контейнер. Опції команди:
* _image name_ - ім'я образу контейнера;
* _host name_ - ім'я хоста контейнера;
* _memory_size_ - пам'ять, що виділяється під контейнер;
* _directory from_ - директорія, що містить статику сайту;
* _directory to_ - директорія, в яку цю статику буде скопійовано;
* _user name_ - ім'я користувача.

`stop`. 
Зупинити вказаний контейнер.

`hosts`. 
Список доступних для використання хостів.

`containers`. 
Список контейнерів, запущених на віддаленій машині.

`exit`. 
Вихід із програми.
