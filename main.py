#!/usr/bin/env python3

import gi, os, pwd

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Choose an Option")

        self.connect("key-press-event", self.on_key_press_event)

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        shutdownIcon = Gtk.IconTheme.get_default().load_icon("system-shutdown-symbolic", 256, 0)
        shutdownImage = Gtk.Image()
        shutdownImage.set_from_pixbuf(shutdownIcon)
        self.bshutdown = Gtk.Button()
        self.bshutdown.set_image(shutdownImage)
        self.bshutdown.connect("clicked", self.shutdown)
        self.bshutdown.set_tooltip_text("Shutdown")
        self.box.pack_start(self.bshutdown, True, True, 0)

        restartIcon = Gtk.IconTheme.get_default().load_icon("system-reboot-symbolic", 256, 0)
        restartImage = Gtk.Image()
        restartImage.set_from_pixbuf(restartIcon)
        self.brestart = Gtk.Button()
        self.brestart.add(restartImage)
        self.brestart.connect("clicked", self.restart)
        self.brestart.set_tooltip_text("Restart")
        self.box.pack_start(self.brestart, True, True, 0)

        sleepIcon = Gtk.IconTheme.get_default().load_icon("preferences-desktop-screensaver-symbolic", 256, 0)
        # Could not find a "suspend icon" so had to make do with this
        sleepImage = Gtk.Image()
        sleepImage.set_from_pixbuf(sleepIcon)
        self.bsleep = Gtk.Button()
        self.bsleep.add(sleepImage)
        self.bsleep.connect("clicked", self.sleep)
        self.bsleep.set_tooltip_text("Sleep")
        self.box.pack_start(self.bsleep, True, True, 0)

        lockIcon = Gtk.IconTheme.get_default().load_icon("system-lock-screen-symbolic", 256, 0)
        lockImage = Gtk.Image()
        lockImage.set_from_pixbuf(lockIcon)
        self.block = Gtk.Button()
        self.block.add(lockImage)
        self.block.connect("clicked", self.lock)
        self.block.set_tooltip_text("Lock")
        self.box.pack_start(self.block, True, True, 0)

        logoutIcon = Gtk.IconTheme.get_default().load_icon("system-log-out-symbolic", 256, 0)
        logoutImage = Gtk.Image()
        logoutImage.set_from_pixbuf(logoutIcon)
        self.blogout = Gtk.Button()
        self.blogout.add(logoutImage)
        self.blogout.connect("clicked", self.logout)
        self.blogout.set_tooltip_text("Logout")
        self.box.pack_start(self.blogout, True, True, 0)

        cancelIcon = Gtk.IconTheme.get_default().load_icon("process-stop-symbolic", 256, 0)
        cancelImage = Gtk.Image()
        cancelImage.set_from_pixbuf(cancelIcon)
        self.bcancel = Gtk.Button()
        self.bcancel.add(cancelImage)
        self.bcancel.connect("clicked", self.cancel)
        self.bcancel.set_tooltip_text("Cancel")
        self.box.pack_start(self.bcancel, True, True, 0)

    def shutdown(self, widget):
        os.system("poweroff")
        Gtk.main_quit()

    def restart(self, widget):
        os.system("reboot")
        Gtk.main_quit()
    
    def sleep(self, widget):
        os.system("slock systemctl suspend -i")
        Gtk.main_quit()
    
    def lock(self, widget):
        os.system("slock")
        Gtk.main_quit()
    
    def logout(self, widget):
        currentUser = pwd.getpwuid(os.getuid())[0]
        cmd = "pkill -u {0}".format(currentUser)
        os.system(cmd)
        Gtk.main_quit()

    def cancel(self, widget):
        Gtk.main_quit()

    def on_key_press_event(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.set_position(Gtk.WindowPosition.CENTER)
win.show_all()
Gtk.main()
