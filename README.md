# metrics-collector

## What is it?

Metrics-collector is util, that uses python functions to get system metrics about ***CPU*** and ***RAM***
and shows it to user.

## What do you need?

First of all you need to clone this project via command:

```sh
git clone https://github.com/Serg2294/metrics-collector.git
```
After that you will get three files:
1. Dockerfile - instruction for docker build command.
2. metrics - script with parameters that creates docker image and starts container.
3. script.py - python script that collects metrics inside docker container.

To start script make **metrics** file executable via command:

```sh
chmod +x metrics
```

## How to start?

To collect cpu metrics use command:

```sh
./metrics cpu
```

To collect memory metrics use command:

```sh
./metrics mem
```

When you finish to use metrics-collector, you can clear temporary images via command:

```sh
./metrics del
```
