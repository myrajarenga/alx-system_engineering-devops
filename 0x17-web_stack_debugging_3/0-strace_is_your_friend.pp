#puppet script that replaces the "phpp" with "php" in the /var/www/html/wp-settings.php file to prevent 500 server error
file_pth = '/var/www/html/wp-settings.php'
exec{{ 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
