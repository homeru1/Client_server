Для работы:
1) Установить crypto pro на ubuntu'y и скомплировать библиотеку 
https://docs.cryptopro.ru/cades/pycades/pycades-build part 1
https://docs.cryptopro.ru/cades/pycades/pycades-install part 2
1.1 В этой команде : sudo apt install cmake build-essential libboost-all-dev python3-dev unzip
у меня не установилось только libboost-all-dev, но без него все стартануло
1.2 Делайти все шаги друг за другом и внимательно, чтобы каждый пункт у вас без ошибок прошел
1.3 6-ой пункт не пропустите 
1.4 Все приколы с arm64 пропускайте ubuntu работает под amd64
1.5 Все архивы и саму скомпилированную библеотеку я оставил, но не знаю насколько сильно она от окружения зависит 
1.6 Во второй части я использвал этот вариант "echo 'export PYTHONPATH=/path_to_pycades_so' >> ~/.bashrc"
2) Не забудтье установить временный сертификат при помощи этой команды:
/opt/cprocsp/bin/amd64/cryptcp -createcert -dn "CN=test" -provtype 80 -cont '\\.\HDIMAGE\test' -ca https://cryptopro.ru/certsrv
2.1 Если вдруг сертификат не будет работать нужно удалить все test.*** (Или что-то похожее от сюда /var/opt/cprocsp/keys/$name)
2.2 После всей установки протестировать на тестовых вариантах 
https://docs.cryptopro.ru/cades/pycades/pycades-samples/pycades-sign-verify
3) Установить GUI ( Я ставил при помощи этой команды apt-get install python-tk)
4) Если у вас WLS2 то проблем нет, если wls1, то надо еще настроить работу с gui (Так как в wls1 нельзя запускать окна в рабоет с терминалом) 
https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx
(Run Graphical Programs)
4.1 Поставить сервер на windwos
4.2 Установить x11-apps (sudo apt-get install x11-apps)
4.3 Настроить переменную DISPLAY (export DISPLAY=:0)
4.4 Протестиировать (xeyes )
5) Стартовать с gui.py
6) Enjoy
