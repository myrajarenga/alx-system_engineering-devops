# install package

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => 'pip3 install flask',
  path    => ['/usr/local/bin', 'usr/bin', '/bin'],
  creates => '/usr/local/bin/flask',
  require => Package['python3-pip']
}
