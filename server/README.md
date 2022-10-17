# Server

Server is just a python web server running in a docker container.


## How to run it

```bash
$ ./run.sh
```

## Example

```bash
$ ./run.sh 
172.29.0.3 - - [17/Oct/2022 14:16:56] "GET / HTTP/1.1" 200 -
172.29.0.3 - - [17/Oct/2022 14:16:57] "GET / HTTP/1.1" 200 -
172.29.0.4 - - [17/Oct/2022 14:16:58] "GET / HTTP/1.1" 200 -
172.29.0.3 - - [17/Oct/2022 14:16:58] "GET / HTTP/1.1" 200 -
172.29.0.4 - - [17/Oct/2022 14:16:59] "GET / HTTP/1.1" 200 -
```

Server is also exposed in the por t 8000

```bash
$ curl localhost:8000
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Web Server</title>
</head>
<body cz-shortcut-listen="true">
<h1>Hello !!</h1>

</body></html>
```