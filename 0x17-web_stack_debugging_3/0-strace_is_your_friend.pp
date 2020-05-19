#Correction of error 500 in server apache2
exec {'change line':
provider => shell,
command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
}
