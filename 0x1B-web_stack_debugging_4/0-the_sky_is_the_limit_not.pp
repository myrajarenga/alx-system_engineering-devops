# acript increases the amount of traffic an Nginx server can handle
class nginx::config {
  file { '/etc/default/nginx':
    ensure  => present,
    content => "# Managed by Puppet\nULIMIT=\"-n 4096\"\n",
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
  }

  exec { 'fix_for_nginx':
    command     => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    path        => '/usr/local/bin/:/bin/',
    refreshonly => true,
    subscribe   => File['/etc/default/nginx'],
  }

  exec { 'nginx-restart':
    command     => '/bin/systemctl restart nginx',
    path        => '/usr/local/bin/:/bin/',
    refreshonly => true,
    subscribe   => Exec['fix_for_nginx'],
  }
}
