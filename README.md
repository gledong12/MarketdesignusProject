# Moving System
<div align="center">
  <img src="https://images.velog.io/images/eagle5424/post/f697d2e4-fbed-4c9f-a814-c424f82de3b8/1.png"><br>
</div>



----------
## What is it?
**Moving System** is api that registers and inquires customers, companies, move applications, and feedback.

## Project Structure
```
├── moving
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── information
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── test.py
│   ├── urls.py
│   └── views.py
├── data
│   └── backup.sql
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── wait-for-it.sh
```
* `information`: Include API function code related to Moving
    * `MovingCompanyInformationView` : This function is that moving company register and inquire.
    * `CustomerInformationView` : This function is that customer register and inquire. 
    * `ApplicationofMovingView` : This api have register and inquire data related to application of moving
    * `CustomerFeedbackHistoryView` : The api have register feedback related to Moving service
* `Dockerfile` : Files that record packages, environment variables, etc. that need to be installed in a container
* `docker-compose.yml` : Files for operating multiple containers (api, db) at a time
* `requirements.txt` : Define libraries required for development and deployment
* `wait-for-it.sh` : Scripts for troubleshooting the sequence of operations that depend on django server and db server during deployment

## ERD
URL : https://aquerytool.com/aquerymain/index/?rurl=0db4012d-b512-45a4-bb80-bc4fa2684e3a

Password : 2m3p17

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/gledong12/MarketdesignusProject

## Requirements
Docker: https://www.docker.com/get-started

## Installation from the git repo
```sh
$ git clone https://github.com/gledong12/MarketdesignusProject
$ cd Email_Subscribe
$ docker-compose up
```
## How to use
url lists are as follows
```
 - /moving/company
 - /moving/customer
 - /moving/application
 - /moving/feedback
```
## API test results in Development Server
API test(integration test) used [POSTMAN](https://www.postman.com)<br>
The URL below is a document about integration test in develop server<br>
Please use chrome or safari<br><br>
[The Document about API TEST](https://documenter.getpostman.com/view/14893614/TzefC4wM)

## How to use the api in Web Browser
Try using a deployed web api !<br>
Please check a document below for how to use the API<br><br>
[The Document about How to use the API](https://www.notion.so/How-to-Use-API-Moving-system-e687861d01ac4db499be122c859e335e) <br>

## ISSUE
I met and solved various issues during the project<br>
The URL below is a document about the issue in progress of the project<br><br>
[The Document about ISSUE](https://www.notion.so/Blockers-ab2f998601bf42c69cb17ded0e2dfdff)
