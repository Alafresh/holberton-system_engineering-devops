# Fix the wp setting file
exec { "fix the cconfiguration":
command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
path    => ['/bin', '/usr/bin']
}
