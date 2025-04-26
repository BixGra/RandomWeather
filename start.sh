echo "docker build . -t randomweather"

docker build . -t randomweather

echo "docker compose up -d --remove-orphans"

docker compose up -d --remove-orphans

echo "docker image prune -a"

docker system prune -a