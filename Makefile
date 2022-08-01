PREFIX ?= /usr/local

all:
	@echo Run \'make install\' to install this program.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p main.py $(DESTDIR)$(PREFIX)/bin/powermenu
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/powermenu
	@mkdir -p $(DESTDIR)$(PREFIX)/share/applications/
	@cp -p PowerMenu.desktop $(DESTDIR)$(PREFIX)/share/applications/PowerMenu.desktop

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/powermenu
