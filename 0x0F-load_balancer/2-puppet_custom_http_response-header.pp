
exec { 'http config'
command => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "/http {/a add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf
 && sudo service nginx start'
}