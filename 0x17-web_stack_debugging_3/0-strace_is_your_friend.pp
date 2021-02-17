#Using strace, find out why Apache is returning a 500 error.
#Once you find the issue, fix it and then automate it using Puppet
#(instead of using Bash as you were previously doing).

exec { 'Fin and replace the wrong syntax':
    path    => '/bin',
    command => 'sed -i -e "s/phpp/php/g" /var/www/html/wp-settings.php'
}
