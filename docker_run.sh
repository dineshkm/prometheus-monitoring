version=`cat VERSION.txt`
docker run -p 8080:8080 http_monitor:${version}