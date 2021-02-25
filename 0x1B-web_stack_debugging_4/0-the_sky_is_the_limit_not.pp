exec { 'fix--for-nginx':
  command => 'sed -i "s/15/1024/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
