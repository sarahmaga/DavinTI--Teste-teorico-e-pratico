# Packages usados

* Flask 
* Flask-SQLAlchemy (ORM for database)
* Flask-WTF (Generation of forms and validations)
* Faker (Generates fake data)

# Instalação necessária
```
pip install -r requirements.txt
```
## Observação: foi usado o Anaconda versão 22.9.0 no desenvolvimento desta aplicação WEB
## Python versão 3.9.13, disponibilizado pela Anaconda

# Instalação Anaconda Linux
https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```
bash Anaconda3-2022.10-Linux-x86_64.sh
```
## Instalação Anaconda Windows
https://repo.anaconda.com/archive/Anaconda3-2022.10-Windows-x86_64.exe
## Instalação Anaconda MacOS
https://repo.anaconda.com/archive/Anaconda3-2022.10-MacOSX-x86_64.pkg  Intel chip
https://repo.anaconda.com/archive/Anaconda3-2022.10-MacOSX-arm64.pkg   Apple chip
 
# Para rodar a aplicação
arquivo migrations.py é usado para criação do banco de dados com dados fakes.
```
python3 migrations.py 
python3 app.py
```

