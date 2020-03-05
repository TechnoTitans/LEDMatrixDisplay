DIR=$(DESTDIR)/opt/countdownClock
#DIR= .
LIBDIR=$(DESTDIR)/usr/lib

COMPILELIBDIR=./lib

all: countdownClock

.PHONY: all install clean distclean

countdownClock: countdownClock.py
	export LIBRARY_PATH=$(COMPILELIBDIR):$(LIBRARY_PATH)
	chmod +x countdownClock.py

install: countdownClock
	mkdir -p $(LIBDIR)
	mkdir -p $(DIR)
	install countdownClock.py $(DIR)/countdownClock.py
	install samplebase.py $(DIR)/samplebase.py
	install countdownClock.init /etc/init.d/countdownClock
	update-rc.d countdownClock defaults

clean:
	rm -f countdownClock
