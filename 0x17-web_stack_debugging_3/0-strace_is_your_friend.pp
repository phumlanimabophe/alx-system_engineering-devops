# Define an Exec resource to fix the WordPress file
exec { 'fix-wordpress':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  creates => '/var/www/html/wp-settings.php',
}

# Ensure that the Apache service is restarted when the file is modified
service { 'apache2':
  ensure  => running,
  require => Exec['fix-wordpress'],
}
