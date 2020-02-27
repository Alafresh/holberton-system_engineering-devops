# requests served within a certain .
exec {'adds max workers_connections':
  command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf && sudo service nginx restart"
}
