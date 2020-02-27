# requests served within a certain .
exec {'adds max workers_connections':
  command  => "/bin/sed -i 's/worker_processes 4;/worker_processes 30;/g' /etc/nginx/nginx.conf | service nginx restart"
}
