# Create a file in /tmp with messege I love
file{ '/tmp/holberton':
    content => 'I love Puppet',
    mode    => '0744',
    owner   => www-data,
    group   => www-data;
    }
