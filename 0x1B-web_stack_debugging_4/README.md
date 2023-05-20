## web-stack debugging #4

## Objective
This project aims at impacting the skill of web stack debuging.

## Requirements
1. Ruby ==> `apt-get install -y ruby`
2. puppet-lint ==> `gem install puppet-lint -v 2.1.1` 
3. ApacheBench ==> `apt-get install -y apache2-utils`

## Featured Utility
**ApacheBench (ab)**  
This is a benchmarking tool that measures the performance of a web server by inundating it with HTTP requests and recording metrics for latency and success.

## Featured Commands
Tasks 
0. Sky is the limit, let's bring that limit higher  
* `ab -c 100 -n 2000 localhost/` ==> Makes 2000 requests to my server with 100 requests at a time using the **ApacheBench (ab)** utility.

## Featured Files
* **0-the_sky_is_the_limit_not.pp** ==> puppet script file containing solution

## Solution breakdown
When using the `ab -c 100 -n 2000 localhost/` command, I found that I had about 1336 failing requests. I then checked the error logs from my nginx web server in `/var/log/nginx/error.log`.  
The one error that repeat it self for all the failed request is **"/usr/share/nginx/html/index.html" failed (24: Too many open files), client: 127.0.0.1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"**.  
What this error basically means is that the open files have reached the allowed limit.  
To change the limit of open files at a time, I accessed `vi /etc/default/nginx` and changed the ULIMIT to 4096. `ULIMIT="-n 4096"
The run the command sudo service restartnginx before running the ab commandtobgest how your server handles requests

## In summary 
In instancess where the server complains of too many open files, we have to modify the limit of allowed open files ULIMIT in order to make the files accessible.`

Task 
2. User limit
Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

## Solution
Create the "holberton" user:

Run the command: sudo adduser holberton
Follow the prompts to set a password and provide additional user information.
Grant necessary permissions:

Add the "holberton" user to the appropriate groups to ensure access to required resources. For example, to grant sudo access, run: sudo usermod -aG sudo holberton

Adjust file permissions and ownership to allow the "holberton" user to access relevant files and directories. Use the chown and chmod commands to modify ownership and permissions as needed.
Modify the SSH configuration:

Open the SSH configuration file using a text editor: sudo nano /etc/ssh/sshd_config
Find the line that starts with "AllowUsers" (if it exists). If not, add a new line for "AllowUsers".
Append "holberton" to the line, separated by spaces. For example: AllowUsers holberton
Save the file and exit the text editor.
Restart the SSH service:

Restart the SSH service for the changes to take effect. Use the appropriate command for your operating system. For example for 
Ubuntu/Debian: sudo service ssh restart
