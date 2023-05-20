#lx-software_engineering-devops

##  Webstack- debbuging

## 0. strace is your friend
Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

strace can attach to a current running process
You can use tmux to run strace in one window and curl in another one
## Requirements:

Your 0-strace_is_your_friend.pp file must contain Puppet code
You can use whatever Puppet resource type you want for you fix

Example
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#

## solution
I accessed the server with ssh
First i updated the system using the command sudo apt update
I checked to ensure that apache is installed and running
using the command service apache2

then I checked port 80nis listenning on tye server using the command ss -tuna | grep 80 
tcp LISTEN 0 128 *:80 *:*

root@969e98d6e5f0:/alx-system_engineering-devops/0x17-web_stack_debugging_3# ss -tuna | grep 80
tcp    LISTEN     0      128                    *:80
           *:*
tcp    LISTEN     0      128                   :::80
          :::*
root@969e98d6e5f0:/alx-system_engineering-devops/0x17-web_stack_debugging_3#
 Here's a breakdown of the command:

ss: The ss command is a utility used to display information about active network connections, sockets, and related statistics.

-tuna: These options specify the type of sockets to display:

-t indicates TCP sockets.
-u indicates UDP sockets.
-n disables hostname resolution and displays IP addresses and port numbers instead of domain names.
-a displays all sockets, including listening and non-listening sockets
| (pipe symbol): This symbol is used to redirect the output of the preceding command (ss -tuna) to the next command (grep 80).

grep 80: The grep command is used to search for a specified pattern in the input. In this case, it searches for the pattern "80" in the output of the ss -tuna command. It filters the output and displays only the lines that contain the number "80". This helps to identify the sockets that are listening on port 80.

With all these checked, I can see that apache is installed and running and port 80 was listening. Then I moved to do a curl request to confirm the issue.
