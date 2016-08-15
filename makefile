
# default installation
.DEFAULT_GOAL := install

DEST=/usr/bin/

.PHONY: install
install:
	@echo "adding +x flag to scripts"
	chmod +x src/*
	@echo "copying scripts to $(DEST) (variable DEST=$(DEST))"
	cp src/* $(DEST)