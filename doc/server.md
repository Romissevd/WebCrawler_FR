Sindev

Run flask
PYTHONPATH=/var/www/webcrawler FLASK_APP=/var/www/webcrawler/client/index.py PYTHONIOENCODING=utf-8 flask run >& /dev/null &

Worker run
python3.6 console/workers/italy/wiki_task_recursive.py -t italy_recursive_2017-09-19-01-42-11 >& /dev/null &

python3.6 console/workers/italy/gmap_address.py >& /dev/null &

python3.6 console/workers/italy/wiki_task_request.py >& /dev/null &


digitalocean.com

Войти в учетную запись

sinoptik.dev@gmail.com

Раздел Droplets -> One-click apps

Вибераем образ:

Docker 17.06.0-ce или выше

Выбрать тариф, (текущий 5$)

 Датацентр Frankfurt (Там допступны расширение по диску)

 Выбрать Backups в доплонительных опциях

 Создать

Доступы

Droplet 
Name: g-w-parser-docker-512mb-fra1
IP Address: 138.68.76.60:22
Username: root

user
bpteam

user
ptax

user
dm

скачать актуальную версию из репозиторию в папку (на данный момент из https://github.com/bpteam/WebCrawler_FR.git) /project/gwparser
git clone https://github.com/bpteam/WebCrawler_FR /progect/gwparser


Запуск обновления проекта 

/project/gwparser/batch/update

запуск скриптов

docker exec -it gwparser_python /app/some_script.py