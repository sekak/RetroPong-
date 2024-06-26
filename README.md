<h1>Retropong</h1>

![ss](https://github.com/sekak/RetroPong-/assets/53265264/1ec4bf74-4d66-4e04-9c4a-bfe191906dfe)

</br>
The Retropong project represents the culmination of the 1337 Common Core School curriculum, serving as the final collaborative endeavor for teams comprising a minimum of three to five members. This project is subdivided into three distinct components: the initial phase focuses on Auth/Authorization, followed by the integration of a chat system in the second phase, with the third phase dedicated to the development of the game itself.

# Technologies Used:

1. ***Vanilla JavaScript(VanillaJS)***: The core of RetroPong is built using `VanillaJs`, providing a lightweight and efficient foundations for dyanmic and interactive web expreinces.
  
2. ***Django***: RetroPon's backend is powered by `Django`, a high-level Pyhton web framwork that enables rapid development and clean, pragmatic design.

# Tools Utilized:

1. ***Figma***: Figma is our go-to tool for designing and prototyping the user interface of Retro Pong. With Figma, we can collaborate seamlessly, iterate quickly, and bring our design ideas to life.</br>
   - this link of design https://www.figma.com/design/MvE5V0LLjuV1mEe4CoIrmG/ft_transgender?node-id=0-1&t=nDR0OqZPiAThSbQr-0

3. ***Animista***: Animista helps us add delightful animations and transitions to Retro Pong, enhancing the overall user experience and bringing elements of the game to life with flair and style.

4. ***Bootstrap***: Bootstrap provides a robust and responsive CSS framework that ensures Retro Pong looks great and functions flawlessly across various devices and screen sizes.disturbed

# Project Structure:
  Retro Pong is divided into three main parts, each contributing to the game's functionality and user experience:

  1. Authentication and Authorization with JWT:

     We implement JWT (JSON Web Tokens) for handling authentication and authorization in Retro Pong. This ensures secure user authentication and access control to game features and resources.

  2. Real-Time Chat:

     Retro Pong features a real-time chat system that allows players to communicate with each other while enjoying the game. We leverage WebSockets to enable instant messaging

# Preview:

![338951003-41f0dff2-bdcb-4de7-abd8-ad70c8eac93d-ezgif com-video-to-gif-converter](https://github.com/sekak/RetroPong-/assets/53265264/d5a0b886-e708-46bf-a417-823d54b78558)

# **Environment Setup Guide for RetroPong**

## 1 - Django Virtual Environment:

Please run the following commands to initiate the virtual environment for the backend server:

```bash
cd Backend
python3 -m venv PyLibraries
```

Activate the environment using the following command

```bash
source ./PyLibraries/bin/activate
```

Run the following commands to install the necessary libraries on the virtual environment:

```bash
cd .. # goes back to the main folder
pip install -r requirements.txt
```

Once all is done go back to the RetroPong folder inside the backend and execute the following command to start the development server:

```bash
cd Backend/RetroPong
./manage.py runserver
```

## 2 - PostgreSQL Connection to the Database

Since iMacs in 1337 have a malfunctioning version of docker a vps had to be used to host the database

The credentials will be shared in the **Docs** section on notion

For ease of access and management i recommend you to install **pgAdmin** or if you like using VSC get this extension: [DB Manager](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-postgresql-client2)

## 3 - Microservices Configuration

Retropong Backend Interface will be implemented in accordance with microservices technology, which means that each service that handles an aspect in retropong will be isolated in it's own component.

Retropong Backend Interface will be comprised of several services:

* Authentication Service
* User/Player Information and Management Service.
* Game Stats and Events Service
* Chat Service
* Tournament Service

Each Service will have it's own **Docker Container.**

Here's how to setup the environment to start:

* Install Docker and Docker Compose, if you're working in School iMacs install a virtual machine and an OS of your choice (linux probably).
* After Installation Succeeds, Install python, django and any necessary services inside the container.
* Import your Service Project inside the container
* Run the service inside the container

After you finish working on the microservice assigned to you please make to commit and to push to the appropriate branch.

## 4 - Microservice Diagram, Explanations

Microservice Architecture is a backend design in which a set of services (servers) communicate with each other in order for them to relay content, validate client requests and to minimize downtime during deployment and development.

For example imagine there's 2 Microservices:

* Auth
* Profile

1. The **Client** will send a request to the **Profile** **Microservice** in order to get his profile information by sending his token (cookies or JWTs).
2. The **Profile** **Microservice** will send a request to **Auth Microservice**, Relaying the token acquired from the **Client** for it to be verified and serve the client the content he requested.
3. After the verification is done and is valid, The **Auth Microservice** will confirm it by regenerating a new token for the **Client** with a new expiry date, and sends it back to the **Profile Microservice**
4. The **Profile Microservice** will generate the requested data and sends it back to the **Client.**

Below you'll find some diagrams showing communication between The Microservices mentioned:

![img](https://i.imgur.com/tMXO45L.png)

![img](https://i.imgur.com/DgooOcK.png)

## 5 - Connecting to the Database between multiple microservices

RetroPong's Infrastructure is based on microservices which run django inside to provide compatibility and ease of use/debug, one of the many features provided by Django's ORM is the ability for two Microservices to connect to an existing table without the need to configure anything:

To start connecting your django instance (Microservice) to the database you need to do the following:

**(Assuming you already configured Database Connection inside settings.py)**

1. Run Django's inspectdb command to retrieve the database layout from postgres server:

   ```shell
   $ ./manage inspectdb > models.py
   ```

   1. What inspectdb does is to inspect the database for any existing tables and then make classes for them and their columns with appropriate types for each column.
2. After you get the models.py file from the command without errors, copy the newly created models.py file to the desired **APP** inside your **Microservice**.
3. You should have this class inside any of the tables in your **models.py** that class is the one responsible for providing metadata about the table:

   ```python
       class Meta:
           db_table = 'YOUR DESIRED TABLE'
   	managed = False
   ```

   1. `db_table` is an identifier that links your **Class** to your **Table** using the name of your table in the database to find it and link it.
   2. `managed` is a trigger that controls whether **Django's ORM** should preform any Creation/Deletion Operation on your existing table, `False` means **Django's ORM**  will not preform the previously mentioned operations on that db and will treat it as an existing table. I prefer not to mess with this option and do it the classic way.
   3. It's recommended to delete the `managed` option inside the `Meta` class.
4. Delete any Tables that are not related to your **Microservice**
5. Since Django thinks that the Tables generated inside models.py are new and with no migrations before, It will try to create it again and you will certainly get an error. To fix this issue just run the following command:

   ```shell
   $ ./manage.py makemigrations
   $ ./manage.py migrate --fake
   ```

   1. The above commands will make the migrations for the tables, so django identifies which tables to interact with and the second to commit those tables. `--fake` parameter insures that the migration to the db is faked and no data inside the db is affected and also to stop django from trying to create an already existing table.
6. Correct any missing information inside each of tables properties, `default` argument will be very useful when you use it to tweak the default value for each property (use `-1` for integer values and `""` for strings, Lastly use  `False` for booleans)
7. Once all is done, check if the connection is successful with the command:

   ```shell
   $ ./manage.py runserver
   ```
8. If no errors happen, you have successfully connected the **Microservice** to the existing **Table.**

