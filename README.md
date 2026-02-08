1. How did you develop this application?

I developed this application as a full-stack web application using React for the frontend and Django REST Framework for the backend, and then deployed it on AWS cloud services.

On the backend, I created a REST API using Django and Django REST Framework.
I designed a simple model to store facts, exposed CRUD APIs, and tested them using the Django REST Framework browsable API. I configured CORS settings so that the frontend could access the API securely from a different domain.

For deployment, I launched an EC2 instance, configured security groups to allow HTTP and API access, installed Python and required dependencies, and ran the backend server so that the APIs were accessible publicly via the EC2 public IP.

On the frontend, I built a React application that fetches data from the Django API using the fetch API and displays it in a structured table. I handled loading states and error handling to improve user experience.

After development, I created a production build of the React app and hosted it using Amazon S3 static website hosting. I configured the S3 bucket permissions and static hosting settings so the frontend could be accessed publicly through an S3 website endpoint.

Finally, I connected the React frontend hosted on S3 with the Django backend hosted on EC2, verified cross-origin access, and tested the full flow end-to-end across different browsers.



2. What did you learn from this exercise?

This exercise gave me strong hands-on experience across full-stack development and cloud deployment.

From the backend side, I learned how to design RESTful APIs using Django REST Framework, manage API responses, handle CORS issues, and expose APIs securely over the internet using EC2.

From the frontend side, I learned how to consume APIs in React, manage component state using hooks like useState and useEffect, handle asynchronous data loading, and build a production-ready React application.

From the cloud and deployment perspective, I learned:

 • How EC2 works and how backend services depend on running processes

 • The difference between development servers and production servers

 • How to host a static frontend using S3

 • How security groups, ports, and public IPs affect accessibility

Why backend services stop when terminals close and how production tools like Gunicorn are used

Most importantly, I learned how to debug real deployment issues, such as API connection failures, CORS errors, and differences between local, cloud, and mobile access.
