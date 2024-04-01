#set up a New ubuntu server with nginx
#creating a custom HTTP header response with puppet

exec { 'update system':
        command => '/usr/bin/apt-get update',
}
#install nginx
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}
#Creating a index hmtl file
file {'/var/www/html/index.html':
	content => 'Hello World!'
}
#setting up /redirect_me to a youtube video
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

#custom HTTP header
exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
