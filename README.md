# Assignment2

To build the image, I ran the command  
	
	docker build -t DockerCMS .

to run the container,

	docker run -d -p 80:5000 --name api DockerCMS

As the container didn't work, i ran app.py with python and worked with the following IP :

	http://35.195.89.128:8080


