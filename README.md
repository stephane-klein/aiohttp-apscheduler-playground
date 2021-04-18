# AIOHTTP and APScheduler playground

In this Python project playground, I launch [APScheduler](https://github.com/agronholm/apscheduler) with [AIOHTTP](https://docs.aiohttp.org/en/stable/) server.

```sh
python -m venv ./.pyenv/
source .pyenv/bin/activate
```

```sh
$ python main.py
Tick! The time is: 2021-04-19 00:07:13.720153
Tick! The time is: 2021-04-19 00:07:16.713943
Tick! The time is: 2021-04-19 00:07:19.721333
Tick! The time is: 2021-04-19 00:07:22.717949
```

In another terminal:

```sh
$ curl http://0.0.0.0:8080/foobar
Hello, foobar%
```
