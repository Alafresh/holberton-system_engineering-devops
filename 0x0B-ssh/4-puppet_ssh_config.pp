# This puppet file creates a holberton file with I love Puppet inside
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  }
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
  }
