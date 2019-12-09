# This puppet file creates a holberton file with I love Puppet inside
file { '/tmp/holberton':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
  }
