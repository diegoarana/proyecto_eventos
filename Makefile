#### Start dev
.PHONY: start-dev
start-dev:
	docker-compose -f dev.yml up

#### Down dev
.PHONY: down-dev
down-dev:
	docker-compose -f dev.yml down

#### Down dev and remove volumes
.PHONY: down-dev-v
down-dev:
	docker-compose -f dev.yml down -v

#### Test
.PHONY: test
test:
	docker-compose -f dev.yml run -e DJANGO_TEST=TEST django_dev

#### Build
.PHONY: build
build:
	docker-compose -f dev.yml build
