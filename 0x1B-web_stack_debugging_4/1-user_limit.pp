#create the "holberton" user
user { 'holberton':
  ensure => 'present',
}

# Grant necessary permissions
group { 'sudo':
  members => ['holberton'],
}

# Modify the SSH configuration
file { '/etc/ssh/sshd_config':
  ensure  => 'file',
  content => "AllowUsers holberton\n",
  mode    => '0644',
  notify  => Exec['restart-ssh'],
}

# Modify file limits for user holberton
exec { 'increase-file-limits-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/5/50000/; /^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Restart the SSH service
exec { 'restart-ssh':
  command     => '/usr/sbin/service ssh restart',
  refreshonly => true,
}
