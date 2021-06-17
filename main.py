#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import stat
import sys
import requests
import tarfile
import apt
import subprocess
import time

def Pkg_Install(pkg_name):
    cache = apt.cache.Cache()
    cache.update()
    cache.open()

    pkg = cache[pkg_name]

    if pkg.is_installed:
        print (f"{pkg_name} already installed")
    else:
        pkg.mark_install()
        print(f"Install {pkg_name}")
        try:
            cache.commit()
        except ErrorArg:
            print(f"Sorry, package installation failed {ErrorArg}")


def restart_service(service_name):
    new_start = subprocess.run(["systemctl" , "restart" , service_name])
    time.sleep(5)


def check_status(service_name):     
    new_status = subprocess.run(["systemctl", "status", service_name])  
    time.sleep(5)     


def check_content_file(spath):
    new_check = subprocess.run("ls /var/www/html/worpress/")
    time.sleep(5)   


# from urllib.parse import urlparse
# from urlparse import urlparse

# def checkUrl(url):
#     p = urlparse(url)
#     conn = httplib.HTTPConnection(p.netloc)
#     conn.request('HEAD', p.path)
#     resp = conn.getresponse()
#     return resp.status < 400

# command = 'pt install apache2 apache2-utils php libapache2-mod-php php-mysql php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip mariadb-server mariadb-client mysql-server php-mysql   -y'
# os.system('echo %s|sudo -S %s' % (sudo_password, command) )


listeName = ["apache2" , "apache2-utils" , "php" , "libapache2-mod-php" , "php-mysql" , "php-curl" , "php-gd" , "php-intl" , "php-mbstring" , "php-soap" , "php-xml" , "php-xmlrpc" , "php-zip" , "mariadb-server" , "mariadb-client" , "mysql-server", "php-mysql"]

for pkg_name_ in listeName:
    print(f"Next module : {pkg_name_}")
    Pkg_Install(pkg_name_)

print("avant ecriture\n")

fichier2 = open("/etc/apache2/mods-enabled/dir.conf","r")
print(fichier2.read())
fichier2.close()

print("ecriture\n")

fichier = open("/etc/apache2/mods-enabled/dir.conf","w")
fichier.write("<IfModule mod_dir.c>\n    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm\n</IfModule>\n# vim: syntax=apache ts=4 sw=4 sts=4 sr noet")
fichier.close()

print("apres ecriture\n")

fichier2 = open("/etc/apache2/mods-enabled/dir.conf","r")
print(fichier2.read())
fichier2.close()

print("Avant ecriture fichier hosts")

fichier3 = open("/etc/hosts","r")
print(fichier3.read())
fichier3.close()

print("ecriture dans fichier hosts")
fichier4 = open("/etc/hosts","w")
fichier4.write("127.0.0.1       localhost\n127.0.1.1       wordpress.lan\n\n# The following lines are desirable for IPv6 capable hosts\n::1     ip6-localhost ip6-loopback\nfe00::0 ip6-localnet\nff00::0 ip6-mcastprefix\nff02::1 ip6-allnodes\nff02::2 ip6-allrouters")
fichier4.close()

print("apres ecriture\n")
fichier3 = open("/etc/hosts","r")
print(fichier3.read())
fichier3.close()

process = subprocess.Popen(['ping', '-c 4', 'wordpress.lan'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break

restart_service('apache2')
restart_service('mysql')
# check_status('apache2')


url = 'https://fr.wordpress.org/latest-fr_FR.tar.gz'
# print(checkUrl(url))

# if checkUrl(url):
try:
    myfile = requests.get(url)

except ImportError:
    raise ImportError("probleme de recuperation avec l'url")

else:
    print("probleme avec l'url pour recuperer wordpress")
    exit()


print(os.stat(myfile).st_size)
if os.stat(myfile).st_size > 0:   
    try:
        open('/home/neoxyz/Desktop/Projets/gerald/wordpress.tar.gz','wb').write(myfile.content)
        tar = tarfile.open('wordpress.tar.gz')
        tar.extractall('/var/www/html/wordpress')
        tar.close()

    except ImportError:
        raise ImportError("probleme ouverture du fichier tar.gz")

else:
    print("le fichier n'a pas ete recupere correctement")


print("fin")