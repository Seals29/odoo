DOCKER = docker
DOCKER_COMPOSE = ${DOCKER}-compose
CONTAINER_ODOO = odoo 
CONTAINER_DB = odoo-postgres
WEB_DB_NAME = odoo_dev
CONTAINER_DB_2 = odoo_postgres
help:
	@echo "Available Targets"
	@echo "  Start					Start the docker compose"
	@echo "  Stop					Stop all container"
	@echo "  Restart				Restart all container"
	@echo "  Console				Odoo Console"
	@echo "  psql					Postgresql Console"
	@echo "  logs odoo				Logs the odoo container"
	@echo "  logs db				Logs the postgresql container"
	@echo "  addons <addon_name>			Restart Instance and Upgrade addon"
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

define upgrade_addon
	$(DOCKER) exec -it $(CONTAINER_ODOO) odoo --db_host=$(CONTAINER_DB_2) -d $(WEB_DB_NAME) -r $(CONTAINER_ODOO) -w $(CONTAINER_ODOO) -u $(1)  --dev xml
endef
addon: restart
	$(call upgrade_addon,$(word 2, $(MAKECMDGOALS)))