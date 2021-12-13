# NTHU-LINE-Flask

> The LINE server which handles users' messages from LINE client based on Python flask



# Get Stated

* Run it in the developing mode

  ~~~cmd
  python3 run.py
  ~~~

* Run it in the production mode

  ~~~cmd
  gunicorn app:app -c ./gunicorn.conf.py
  ~~~



# Feactures

All linebot's event handler is implemented in  `app/linebot`. There are four programs to handle the different events.

1. `callback.py`：Handle all post requests come from `/callback`.
2. `followEvent.py`：Handle the event that new user add NTHU LINE Chatbot.
3. `messageEvent.py`：The chatbot core program. Process the message sends by user and will reply proper message to the user.

4. `postbackEvent.py`：Handle the postback event.



# Docker & Kubernetes

Please refer to **Dockerfile** and **gke folder**



# License

Developed by **Jenson Su** & **Jonathan Wu**

