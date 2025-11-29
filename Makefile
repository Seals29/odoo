DOCKER = docker
DOCKER_COMPOSE = ${DOCKER}-compose
CONTAINER_ODOO = odoo 
CONTAINER_DB = odoo-postgres
WEB_DB_NAME = odoo_dev

help:
	@echo "Available Targets"
	@echo "  Start"
	@echo "  Stop"
	@echo "  Restart"
	@echo "  Console"
	@echo "  psql"
	@echo "  logs odoo"
	@echo "  logs db"

start:
	${DOCKER_COMPOSE} up -d 
stop:
	${DOCKER_COMPOSE} down
restart:
	${DOCKER_COMPOSE} restart
console:
	${DOCKER} exec -it ${CONTAINER_ODOO} odoo shell
psql: 
	${DOCKER} exec -it odoo_postgres psql -U ${CONTAINER_ODOO} -d $(WEB_DB_NAME)

logs:
	${DOCKER} logs $(CONTAINER_ODOO)
logsdb:
	$(DOCKER) logs odoo_postgres
