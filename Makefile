.PHONY: env dev install test edit doc-storage-dev

LPYTHON=python3
V=$(PWD)/../$(LPYTHON)
PYTHON=$(V)/bin/$(LPYTHON)
ROOT=$(PWD)

test:	
	ip a | grep 2001
	ip a | grep 172.
	. $(V)/bin/activate
	cd src/icc && $(PYTHON) app.py

env:
	[ -d $(V) ] || virtualenv  $(V)

dev:	env doc-storage-dev
	$(PYTHON) setup.py develop

install: env
	$(PYTHON) setup.py install
	
edit:	
	cd src && emacs app.py

doc-storage-dev:
	make -C ../icc.contentstorage dev
