#Puppet script that uses strace to troubleshoot Apache and fix a 500 error
class apache_troubleshooting {
  $pidfile = '/var/run/httpd.pid'
  $strace_logfile = '/tmp/apache-strace.log'

  # Install strace package
  package { 'strace':
    ensure => installed,
  }

  # Create strace log directory and file
  file { '/tmp':
    ensure => directory,
    mode   => '0755',
  }->
  file { $strace_logfile:
    ensure => absent,
  }->
  file { $strace_logfile:
    ensure => touch,
    mode   => '0644',
  }

  # Restart Apache with strace
  exec { 'restart_apache_with_strace':
    command => "strace -p `cat $pidfile` -o $strace_logfile -f -s 4096 -e trace=all",
    onlyif  => "test -f $pidfile && ps -p `cat $pidfile` > /dev/null",
    require => File[$strace_logfile],
  }

  # Notify if 500 error occurs
  notify { '500_error_detected':
    subscribe => File[$strace_logfile],
    refreshonly => true,
    unless => "grep -q 'HTTP/1.1\" 500' $strace_logfile",
  }

  # Fix the issue if 500 error occurs
  exec { 'fix_apache_500_error':
    command => 'sed -i "s/LogLevel warn/LogLevel debug/g" /etc/httpd/conf/httpd.conf && systemctl restart httpd',
    refreshonly => true,
    subscribe => Notify['500_error_detected'],
  }
}
