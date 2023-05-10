#Bash script that replaces the "phpp" with "php" in the /var/www/html/wp-settings.php file to prevent 500 server error
file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => file('/var/www/html/wp-settings.php').content.gsub(/phpp/, 'php'),
}
