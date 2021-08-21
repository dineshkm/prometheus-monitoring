version=`cat VERSION.txt`
docker build -t http_monitor:${version} .