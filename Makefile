REGISTRY = ghcr.io/jpmaligne/inter-process-communication:latest

build:
	docker build -t ${REGISTRY} \
	--cache-from ${REGISTRY} \
	-t ${REGISTRY} \
	-f Dockerfile . 

up:
	docker-compose up -d && docker-compose logs --tail 10 -f app
