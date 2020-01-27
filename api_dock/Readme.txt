docker build -t api-image ./api_dock
docker run -it --name api-cont -v pwd:/home/dev/app -p 8887:8887 api-image