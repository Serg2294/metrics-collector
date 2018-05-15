# metrics-collector

Metrics-collector is util, that uses python functions to get system metrics about ***CPU*** and ***RAM***
and shows it to user.

## Install

Clone this project via command:

```sh
git clone https://github.com/Serg2294/metrics-collector.git
```
Project has three files:
1. Dockerfile - instruction for docker build command.
2. metrics - script with parameters that creates docker image and starts container.
3. script.py - python script that collects metrics inside docker container.
Put all this files into one directory.

Make **metrics** file executable via command:

```sh
chmod +x metrics
```

## Run

To collect cpu metrics use command:

```sh
./metrics cpu
```

To collect memory metrics use command:

```sh
./metrics mem
```

To clear temporary images use command:

```sh
./metrics del
```
