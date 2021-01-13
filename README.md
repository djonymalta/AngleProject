

Sejam Bem Vindos ao Angle Project v1.0
==================
O que será necessário ter:

* IDE - Utilizado | [Pycharm][0]
* Python3 - Utilizado 3.8.5 | [Python3][1]
* Django - Utilizado 3.1.5 | [Django][2]
* Django Rest Framework | [Django-Rest-Framework][3]
* Postgresql | [Postgresql][4]
* Software Client SQL - Utilizado Dbeaver | [Dbeaver][5]



Neste artigo irei mostrar como instalar os requisitos básicos para rodar o projeto em um ambiente Linux. 
Para mais informações de instalação em ambientes Windows/Mac ou até mesmo outra distribuição Linux, segue o link 
de acesso: 

Documentação: Python
==================
| <img src="https://logodownload.org/wp-content/uploads/2016/03/Windows-10-logo-11.png" alt="Windows"  width="230" height="230" /> | <img src="https://archive.org/download/apple-mac-logo-icon-300x300/apple-mac-logo-icon-300x300.png" alt="Windows"  width="230" height="230" /> |
|------------------------------|------------------------------|
| [Windows][9]          	   | [Mac][10]                  |


Linux Mint(20.04)
==================

Os passos a seguir utilizaremos para deixar o seu ambiente pronto. Caso você já tenha as ferramentas a seguir instaladas e configurado corretamente, passe para o 
próximo passo.

	$ sudo apt install software-properties-common
	$ sudo add-apt-repository ppa:deadsnakes/ppa
 	$ sudo apt update
 	$ sudo apt install python3.8 
  
Após seguir esses passos, confira se o python3 já é o padrão do seu computador. Digite:

 	$ python --version
  
Se retornar algo parecido com: 

 	$ python - comando não encontrado
 
Digite:

 	$  sudo nano ~/.bashrc
  
  Adicione no final do arquivo
  
 	$ alias python=python3
  
  Salve o arquivo e em seguida digite:

 	$ source ~/.bashrc
  

Verifique novamente se o python3 já como default:

 	$ python --version

  
Com o Python3 instalado, instale o pip3 com o comando abaixo:.

 	$ sudo apt install python3-pip
  
  

Documentação: Postgresql
==================

Neste passo, você aprenderá instalar e configurar o postgresql para rodar o projeto. Lembrando que esta configuração é para Linux 20.04, para outras distrubuições,
segue o link da documentação aqui [Postgresql][7]
 
Mãos a obra!

Com o terminal aberto, digite:

 	$  /usr/lib/postgresql/(TAB)/bin/postgres -V
 
Se você não encontrar esse caminho, provavelmente você não tem postgresql instalado em seu computador. Utilize o comando abaixo para instalar: 

 	$  sudo apt install postgresql postgresql-contrib
  
O procedimento de instalação criou uma conta de usuário chamada postgres que está associada ao role padrão do Postgres. Existem algumas maneiras
de utilizar essa conta para acessar o Postgres. Uma maneira é trocar para a conta postgres em seu servidor digitando:

 	$ sudo -i -u postgres
 
Em seguida, você pode acessar o prompt do Postgres digitando:

 	$ psql 
  
Defina uma senha para o usuário postgresql:

 	$ postgres=# \password postgres
  
  **OBS**: Pode ser necessário dar permissão de acesso em seu arquivo pg_hba.conf. Edite-o usando o comando abaixo e deixando as permissões em trust como no 
  exemplo:
  
  	$ sudo nano /etc/postgresql/(versão)/main/pg_hba.conf 
	
Exemplo:
local   all             all                                     trust
local   all             postgres                                trust


  
Ultimos passos:
==================

Se você chegou até aqui, é porque ocorreu tudo bem até agora. As ferramentas necessárias já foram instaladas e seu ambiente já está pronto.
Você já clonou o repositório em seu computador e agora só falta instalar as dependências. Vamos lá!

Com o Pycharm ou a IDE de sua escolha aberto, abra na pasta do projeto e em seguida clica em terminal. Digite:

 	$ pip3 install -r requirements.txt
  

Pronto!

Agora é so subir a o projeto com o comando a seguir no terminal e o projeto estará funcionando:

 	$ python managy.py runserver 8080

Lembre-se de acessar o caminho correto da url em seu navegador.

Ex:
http://127.0.0.1/v1/rest/clock/9/0

 


[0]: https://www.jetbrains.com/pt-br/pycharm/download/
[1]: https://www.python.org/downloads/
[2]: https://www.djangoproject.com/download/
[3]: https://www.django-rest-framework.org/
[4]: https://www.postgresql.org/
[5]: https://dbeaver.io/
[6]: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
[7]: https://www.postgresql.org/download/
[9]: https://docs.python.org/pt-br/3/using/windows.html
[10]: https://docs.python.org/pt-br/3/using/mac.html
