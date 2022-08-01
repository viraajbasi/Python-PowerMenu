PREFIX ?= /usr/local

all:
	@echo Run \'make install\' to install this program.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p main.py $(DESTDIR)$(PREFIX)/bin/powermenu
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/powermenu

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/powermenu