`t& V/#V/#fix limit
exec { 'limit':
    command => 'sed -ri "s/(ULIMIT=\"-n) [0-9]+/\1 10000/" /etc/default/nginx',
}
exec { 'restart':
    command => 'service nginx restart',
}
