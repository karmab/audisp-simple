audisp-simple
=============

auditd plugin to concatenate audit messages by serial and convert uid to usernames in messages prior to sending them to syslog
written in python, so quite simple to  tweak

Contents
--------

    README.md                          this file
    audisp-simple.py                   the plugin
    audisp-simple_test.py              same version, ready for testing
    simple.conf                        configuration file for audisp, to put in /etc/audisp/plugins.d

How to use it
-------------

put the plugin in the path you want, give it 750 permissions
put the simple.conf in /etc/audisp/plugins.d
restart auditd 
enjoy...

How does it look like
---------------------
Feb  3 17:07:28 k2 audisp-simple.py: serial=171972 node=k2.lab type=SYSCALL arch=x86_64 syscall=execve success=yes exit=0 a0=1e00220 a1=1e00200 a2=1e07120 a3=7fffd0624f10 items=2 ppid=18779 pid=18780 auid=root uid=root gid=root euid=root suid=root fsuid=root egid=root sgid=root fsgid=root tty=pts2 ses=7690 comm=hostname exe=/bin/hostname key=root node=k2.lab type=EXECVE argc=1 a0=/bin/hostname node=k2.lab type=CWD cwd=/root node=k2.lab type=PATH item=0 name=/bin/hostname inode=398503 dev=fd:01 mode=file,755 ouid=root ogid=root rdev=00:00 node=k2.lab type=PATH item=1 name=(null) inode=396040 dev=fd:01 mode=file,755 ouid=root ogid=root rdev=00:00 node=k2.lab type=EOE



Problems?
---------

Send a mail to karimboumedhel@gmail.com or find it yourself !
Ai seu te pego!

karmab

