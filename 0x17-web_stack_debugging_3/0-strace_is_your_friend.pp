file { '/etc/apache2/sites-enabled/000-default.conf':
  ensure => file,
  source => '/etc/apache2/sites-available/000-default.conf',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  require => Package['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => File['/etc/apache2/sites-enabled/000-default.conf'],
}
