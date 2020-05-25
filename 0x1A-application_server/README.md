# Configurate Server Nginx whit web page

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Install and configurate Nginx

Nginx is one of the servers for web pages, both static and dynamic, that offer the best results, especially on web pages with a large number of visits. Although for users there are hardly any differences between using one server or another, for web administrators, one of the characteristics beyond performance and the way of working with processes is the configuration.

Nginx is characterized by being a web page server that is configured in a modular way, something that in some aspects can make the configuration of the web server difficult but, in turn, allows it to be much easier to interpret, being able to separate the configuration in several independent files and load them in the main configuration file so that they all work as one.

In this manual we are going to explain how this server works for static web pages. Later we will see how to configure it to process dynamic websites with PHP.

## How to install and control the Nginx daemon
The first thing we have to do to use Nginx is to install it on our system. To do this, the first thing we must do is type in our terminal:

If we use a Debian-based distribution:

apt-get install nginx
If we use a Red Hat based distribution:

yum install nginx
Once the installation of Nginx is finished, we will have the daemon working, ready to start loading our websites. We can easily control the web server daemon with the following commands:

service nginx start | stop | restart -> To start, stop or restart the service or daemon.
service nginx configtest | reload -> To test a configuration or reload it after making changes to the server.
service nginx status -> To know the status of the server at that moment.

## How to configure Nginx
Basic setup
One of the characteristics of this web server is that it allows you to configure the server and each of the web pages that we mount on it separately. On the one hand, the basic server configuration is found in the file:

/etc/nginx/nginx.conf
Within this file we will be able to configure the general functions of the web server, among others:

The user who will run the server.
Number of server processes (based on the number of CPU cores).
The server master process (pid)
The path where the log files will be saved.
Maximum users connected to the server.
HTTP configuration (file types, data transmission, Gzip compression, path of web servers, mail server configuration, etc.).

At the end of this file, inside the http block, we can see a default line called include / etc / nginx / sites-enabled / *. This line tells the server to load the specific settings from different files and directories in order to be able to function as "virtual servers" and to enable and disable settings easily without having to delete them.

In summary, the nginx.conf file is in charge of offering a global configuration of the server, which is complemented by what we are going to see next.

## How to set up your first website
As we have said, the virtual server configuration that creates us by default is found in the path "/ etc / nginx / sites-available / default".

If we edit this file we will be able to find, among other functions:

The listening ports (by default, 80).
The directory where the web is stored.
The default file when accessing the web, by default, index.html.
Behavior in case of 404 error.
Configuration of a virtual server based on it.
HTTPS configuration.

All the configuration of this file will be "overwritten" to the general configuration of the server.

As we have seen in the previous configuration file, the default website is located at the path / usr / share / nginx / html. If we scroll to it, we can see the following files.
By default, as indicated in the previous configuration file, when accessing the web through port 80, the index.html file will be opened by default. In case of having a php server associated with Nginx (which we will see later), the file that will be opened by default will be index.php.

We can open with "nano" the file "index.html", view its content and even modify or change it for another to display our own web page.

## Useful tips and practices for Nginx
With this we will be able to mount and simple http server ready to host static pages. In summary, some of the aspects that we must remember when configuring our server are:

We must separate the configurations as much as possible.
It is recommended to make a separate configuration for each server, even if they are the same.
We must use "include" to import each configuration to the Nginx server.
The names of each server must use a clear pattern and easy to identify names.

[more info](https://www.redeszone.net/2016/12/02/instalar-configurar-servidor-paginas-web-nginx/)
