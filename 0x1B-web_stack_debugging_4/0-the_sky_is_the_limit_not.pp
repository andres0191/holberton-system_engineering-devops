#Sky is the limit, let's bring that limit higher
exec { 'not limit':
  provider => shell,
  command  => 'sed -i "s/15/15000/g" /etc/default/nginx',
}
exec { 'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
