REGISTRY           := registry.cn-hangzhou.aliyuncs.com
NAMESPACE          := taylor
TAG                := $$(git rev-parse --verify HEAD)#you can change the git HEAD to use the specific images
PODNAME            := jupyterhub
REGISTRYUSERNAME   := taylorhere
DATA_DIR           := ./
include .env

all: build run ps log

env:
	@echo "" > .env
	@echo "DATA_DIR=${DATA_DIR}" >> .env
	@echo "ENVFLAG=${ENVFLAG}" >> .env
	@echo "TAG=${TAG}" >> .env
	@echo "REGISTRY=${REGISTRY}" >> .env
	@echo "NAMESPACE=${NAMESPACE}" >> .env
	@echo "PODNAME=${PODNAME}" >> .env


build:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml build

ps:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml ps

run: build
	@docker-compose -f docker-compose-${ENVFLAG}.yaml up -d
	make ps
	make log

rerun: down run

exec:
	@docker exec -it $$(make ps | awk '{print $$1}' | sed -n '/${p}/p') ${cmd}

janusgraph-shell:
	@docker exec -it ai-mdt_janusgraph-server_1 ./bin/gremlin.sh

log:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml logs -f $(PODNAME)

status:
	@docker stats

push: build
	@docker-compose -f docker-compose-${ENVFLAG}.yaml push

pull:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml pull

down:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml down -v

clean:
	@docker-compose -f docker-compose-${ENVFLAG}.yaml down
	rm .env

config:
	cp ./hosts /etc/hosts

login:
	@echo "password for sudo"
	@echo "then password for registry user ${REGISTRYUSERNAME}"
	sudo docker login --username=${REGISTRYUSERNAME} ${REGISTRY}

deploy: login pull run-without-build ps log

quik-fix:
	git add .
	git commit -m "fix(quik): fix something and quik test it"
	git push

quik-deploy:
	git pull
	make pull
	make run-without-build
	make ps
	make log

quik-push: build quik-fix push