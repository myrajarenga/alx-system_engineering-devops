# Install HAProxy package
package { 'haproxy':
  ensure => installed,
}

# Configure HAProxy
file { '/etc/haproxy/haproxy.cfg':
  content => "
frontend http-in
  bind *:80
  default_backend servers

backend servers
  balance roundrobin
  server web-01 34.224.94.210:80 check
  server web-02 54.87.252.193:80 check
",
  mode => '0644',
  notify => Service['haproxy'],
}

# Enable and start HAProxy service
service { 'haproxy':
  ensure => running,
  enable => true,
}
