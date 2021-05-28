#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import stat
import sys
import requests
import tarfile
import apt

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
        

# from urllib.parse import urlparse
# from urlparse import urlparse

# def checkUrl(url):
#     p = urlparse(url)
#     conn = httplib.HTTPConnection(p.netloc)
#     conn.request('HEAD', p.path)
#     resp = conn.getresponse()
#     return resp.status < 400


# url = 'https://fr.wordpress.org/latest-fr_FR.tar.gz'
# # print(checkUrl(url))

# # if checkUrl(url):
# try:
#     myfile = requests.get(url)

# except ImportError:
#     raise ImportError("probleme de recuperation avec l'url")

# # else:
# #     print("probleme avec l'url pour recuperer wordpress")
# #     exit()


# print(os.stat(myfile).st_size)
# if os.stat(myfile).st_size > 0:   
#     try:
#         open('/home/neoxyz/Desktop/Projets/gerald/wordpress.tar.gz','wb').write(myfile.content)
#         tar = tarfile.open('wordpress.tar.gz')
#         tar.extractall()
#         tar.close()

#     except ImportError:
#         raise ImportError("probleme ouverture du fichier tar.gz")

# else:
#     print("le fichier n'a pas ete recupere correctement")

# command = 'apt install apache2 apache2-utils php libapache2-mod-php php-mysql php-curl php-gd php-intl php-mbstring php-soap php-xml php-xmlrpc php-zip mariadb-server mariadb-client -y'
# os.system('echo %s|sudo -S %s' % (sudo_password, command) )


listeName = ["apache2" , "apache2-utils" , "php" , "libapache2-mod-php" , "php-mysql" , "php-curl" , "php-gd" , "php-intl" , "php-mbstring" , "php-soap" , "php-xml" , "php-xmlrpc" , "php-zip" , "mariadb-server" , "mariadb-client"]

for pkg_name_ in listeName:
    print(f"Next module : {pkg_name_}")
    Pkg_Install(pkg_name_)


# pkg_name = "apache2"

# cache = apt.cache.Cache()
# cache.update()
# cache.open()

# pkg = cache[pkg_name]

# if pkg.is_installed:
#     print (f"{pkg_name} already installed")
# else:
#     pkg.mark_install()
#     print(f"Install {pkg_name}")
#     try:
#         cache.commit()
#     except ErrorArg:
#         print(f"Sorry, package installation failed {ErrorArg}")


print("fin")