#!/usr/bin/env python3

import gi, os, pwd

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Choose an Option")

        self.connect("key-press-event", self.on_key_press_event)

        box = Gtk.Box(spacing=6)
        self.add(box)

        shutdownIcon = Gtk.IconTheme.get_default().load_icon("system-shutdown-symbolic", 256, 0)
        shutdownImage = Gtk.Image()
        shutdownImage.set_from_pixbuf(shutdownIcon)
        bshutdown = Gtk.Button()
        bshutdown.set_image(shutdownImage)
        bshutdown.connect("clicked", self.shutdown)
        bshutdown.set_tooltip_text("Shutdown")
        box.pack_start(bshutdown, True, True, 0)

        restartIcon = Gtk.IconTheme.get_default().load_icon("system-reboot-symbolic", 256, 0)
        restartImage = Gtk.Image()
        restartImage.set_from_pixbuf(restartIcon)
        brestart = Gtk.Button()
        brestart.add(restartImage)
        brestart.connect("clicked", self.restart)
        brestart.set_tooltip_text("Restart")
        box.pack_start(brestart, True, True, 0)

        sleepIcon = Gtk.IconTheme.get_default().load_icon("preferences-desktop-screensaver-symbolic", 256, 0)
        # Could not find a "suspend icon" so had to make do with this
        sleepImage = Gtk.Image()
        sleepImage.set_from_pixbuf(sleepIcon)
        bsleep = Gtk.Button()
        bsleep.add(sleepImage)
        bsleep.connect("clicked", self.sleep)
        bsleep.set_tooltip_text("Sleep")
        box.pack_start(bsleep, True, True, 0)

        lockIcon = Gtk.IconTheme.get_default().load_icon("system-lock-screen-symbolic", 256, 0)
        lockImage = Gtk.Image()
        lockImage.set_from_pixbuf(lockIcon)
        block = Gtk.Button()
        block.add(lockImage)
        block.connect("clicked", self.lock)
        block.set_tooltip_text("Lock")
        box.pack_start(block, True, True, 0)

        logoutIcon = Gtk.IconTheme.get_default().load_icon("system-log-out-symbolic", 256, 0)
        logoutImage = Gtk.Image()
        logoutImage.set_from_pixbuf(logoutIcon)
        blogout = Gtk.Button()
        blogout.add(logoutImage)
        blogout.connect("clicked", self.logout)
        blogout.set_tooltip_text("Logout")
        box.pack_start(blogout, True, True, 0)

        cancelIcon = Gtk.IconTheme.get_default().load_icon("process-stop-symbolic", 256, 0)
        cancelImage = Gtk.Image()
        cancelImage.set_from_pixbuf(cancelIcon)
        bcancel = Gtk.Button()
        bcancel.add(cancelImage)
        bcancel.connect("clicked", self.cancel)
        bcancel.set_tooltip_text("Cancel")
        box.pack_start(bcancel, True, True, 0)

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
