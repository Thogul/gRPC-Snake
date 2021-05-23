# Portfolio 2
Student-ids: s344043, s344073, s344038, s344101.

**Technology Information:**
Program is written in python3.
GUI created in pyQt5.
Networking with gRPC.


## Notes:

We use docker yml syntax version 3.9, make sure to have the newest version of docker/docker-compose so the syntax is supported. If not, you can try to change the version in the Docker.yml and docker-compose.yml file til 3.3 and it will probably work.
We chose to have docker-compose because we need to build images for the server, database and Grafana

We are having trouble with stability over time. The server can handle all the bots, but after a while it freezes. We have not been able to find the reason for this freeze, but a quick docker compose down then up fixes it. Sorry for the inconvenience.

Our SSL certificate is self-signed for localhost. From our understanding and testing that means that the server can only run on localhost, and therefore other computers can’t connect unless the SSL certificate is signed with another domain name. We did not do that, however feel free to sign it again with other domain name etc…
How we generated ssl certificate:

    openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt -subj  "/CN=localhost"
    
    #change localhost to the correct %DOMAIN-NAME%
## Instructions: How to play
Make sure you are inside the correct folder:

    C:\Downloads\gRPC-Snake-main\gRPC-Snake-main> 


**Setup server only**
The server can run alone with only docker.

    docker build -t server .
    docker run -p 50051:50051 server -d

**Set up the** **complete docker environment****:**
Use the terminal, type: 

    docker-compose up -d  #turn off the server with docker-compose down

this will get the server going with both the database, Prometheus and Grafana.
Note: This may take some time.

        
![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621775886539_image.png)



    (.venv) PS C:\Users\margr\Documents\GitHub\gRPC-Snake> docker compose up -d
    [+] Running 5/5
     - Network grpc-snake_default         Created                                   0.1s 
     - Container grpc-snake_grafana_1     Start...                                  3.2s
     - Container grpc-snake_db_1          Started                                   3.2s 
     - Container grpc-snake_app_1         Started                                   4.2s
     - Container grpc-snake_prometheus_1  St...                                     5.3s
    (.venv) PS C:\Users\margr\Documents\GitHub\gRPC-Snake> 


For launching the game you need too make sure all in the requirements.txt is downloaded correctly on your computer


    $ python -m pip install -r requirements.txt
    or
    $ pip install -r requirements.txt

**Launch the game client**
Use the terminal, type:

    python game.py

A window will pop-up, where you need to enter a username and pick a color. When done, launch the game by pressing “Enter game”. Move with “WASD”-keys or arrow keys.

    
![](https://paper-attachments.dropbox.com/s_44DAA59FC1322A4E51B333F3B38D1035A8556B58548A6AD0BBFC69F65BDA9F3D_1621775574395_image.png)

    

**Add bots** **(Recommended)**

    python bot2.py 15  #number at the end is the amount of bots you want to add
![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621775190216_image.png)

- We recommend not having more then 20 bots if you don't want to much lag.

**Gaming instructions:** 

- When entering the game a new window will pop-up, your snake will spawn randomly.
- The game board itself will scroll around the snake to manage a lager grid.
![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621773340592_image.png)

- We chose to have collision walls to map the ending line and also a wall spawned in the middle to show that we can have obstacles in the game if we want.


- You will see the username and score of all the connected players in  the  game. The scoreboard is sorted from highest to lowest score.
![](https://paper-attachments.dropbox.com/s_44DAA59FC1322A4E51B333F3B38D1035A8556B58548A6AD0BBFC69F65BDA9F3D_1621774445566_image.png)

![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621773306130_image.png)



- Food will spawn near your body, red box gives you one length and yellow gives you three.
![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621773270961_image.png)



- There is a Music radio button on the left corner, which default is turned off, but if clicked you will hear the awesome music.
        
![](https://paper-attachments.dropbox.com/s_A716632741AC4176A425793AD10D8AC3E5480B1151AA54BEE3ED3B602FF80C8A_1621773146533_image.png)



- When you die, a new window within the main window will spawn and you will get three options
    - Quit (closes the app), Play again (restarts the game), Show high scores (opens a new window with everybody’s high score).
    
![](https://paper-attachments.dropbox.com/s_44DAA59FC1322A4E51B333F3B38D1035A8556B58548A6AD0BBFC69F65BDA9F3D_1621774716987_image.png)

    - Show Highscores: 
        
![](https://paper-attachments.dropbox.com/s_44DAA59FC1322A4E51B333F3B38D1035A8556B58548A6AD0BBFC69F65BDA9F3D_1621774490965_image.png)



## Instructions: Multiplayer

Lauch a new “python game.py” in another terminal, while the other is still in the game


## Instructions: Database

We use MongoDB as our database. It is exposing the standard port(27017). You can check it out with an explorer like MongoDBCompass by connection to mongodb://localhost:27017.

![](https://paper-attachments.dropbox.com/s_FDEC14D0A37AE22ACEA9B3DA9809C829ACE95CAB6EE30A57EB3ABEA803C0A50A_1621775019751_image.png)

## Instructions: Monitoring

We use Prometheus and Grafana to monitor resource usage. Prometheus is used to gather the data while Grafana is used to display it.

**Instructions: Promotheus**
You can enter the Prometheus website by going to 127.0.0.1:9090. Here you can query for data from the app and see it in graph form and tables. However, we don’t use Prometheus for displaying data, only for getting it.

**Instructions: Grafana**
Grafana can be accessed at 127.0.0.1:3000. We have set up Grafana to be completely fresh when you run the docker compose for the first time. The Prometheus data source is already set up and there exists a dashboard already made with a graph for displaying the data. 
Since the Grafana server is a fresh install, the default login credentials are to be used:

- Username: admin
- Password: admin

You will likely be prompted to change password, feel free to do so if you wish, or skip it.

To find the dashboard go to the side menu, to the 4 squares(Dashboard) and then to manage. There you will find a list of dashboards(only one is there). Click on it and you will be taken to the dashboard. The graph under shows performance use with 15 bots, and one player.

![](https://paper-attachments.dropbox.com/s_44DAA59FC1322A4E51B333F3B38D1035A8556B58548A6AD0BBFC69F65BDA9F3D_1621776015970_image.png)

## Highscore list hacking

We do all highscore computation on server side. Other than that the database is open for viewing and editing(for testing, in production one would turn that off), we believe it might not be so easy to hack our highscore list. One way is that bots are very easy to implement with our game, so one could always just write a bot and “hack” it that way.

