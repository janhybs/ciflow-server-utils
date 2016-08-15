
# default installation
.DEFAULT_GOAL := install-scripts

DEST=/usr/bin/
FLASK=/var/www/html/

.PHONY: install-scripts
install-scripts:
	@echo "adding +x flag to scripts"
	chmod +x docker-scripts/*
	chmod +x server-scripts/*
	@echo "copying scripts to $(DEST) (variable DEST=$(DEST))"
	cp docker-scripts/* $(DEST)
	cp server-scripts/* $(DEST)


.PHONY: install-flask
install-flask:
	@echo "mkdir for flask server"
	mkdir -p $(FLASK)
	@echo "copying flask server data to $(FLASK) (variable FLASK=$(FLASK))"
	cp -r flask-server/* $(FLASK)/