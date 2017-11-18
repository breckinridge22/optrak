#!/bin/bash
docker rm $(docker ps -aq) -f
docker-compose up
