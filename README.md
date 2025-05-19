# TESTPYSOCKETRQ

A small simple socket converter library

Version -> **0.3.0**

## About Library and Questions

**What is the PYSOCKETRQ library and what is it for?**

> This library makes creating Server and Client very easy. It's just a little limited.

**Why should I use the module?**

> I can recommend it because it is simple and fast to use.

**What language is it written in and what library does it use?**

> It is written 100% in python and uses the Socket library.

![Static Badge](https://img.shields.io/badge/Python--3.13.3-yellow?logo=python&labelColor=black) ![Static Badge](https://img.shields.io/badge/xRangeroQ-gray?logo=github)



## Functions

First you need to create an object. We also need to specify the Address family and Transport protocol.

```python
from testpysocketrq import PySocketRQ # Import Library

exampleVariable=PySocketRQ(Debug=True, Address_Family="IPv4 or IPv6", Transport_Protocol="TCP or UDP", Host=Optional, Target=Optional) # Create PySocketRQ Object
```

- Debug indicates whether a debug message will be sent for each operation. You can use it completely without text by writing False.

- The Address_Family parameter here tells us which address family to use. For now, you can give the values ​​"IPv4" or "IPv6".

- Transport Protocol specifies which transport protocol to use. For now, you can give the values ​​"TCP" or "UDP".

- Host specifies which IP Address and Port the Server or Client will be associated with.

- If data is to be sent, Target specifies in advance which party it will be sent to.

---

### Server Side
```python
CreateServer() # Function used to create and start to the server

SendDataServer(data) # This is the function that the server should use to send data to the client. Here you can write whatever you want in the data parameter. However, it must be in BYTE type. Also, if you are going to use UDP Transport Protocol, you need to specify a specific Target.

RecvDataServer(BufferSize) # If you are using TCP Transport Protocol, you can use it directly. If you are using UDP Transport Protocol, 2 values ​​will be returned. The first value is the received data, the second value is from whom it was received. You can set BufferSize as an option.

CloseServer() # This function allows you to close the server connection.

```

---

### Client Side
```python
CreateClient() # Function used to create and start to the client

SendDataClient(data) # This is the function that the client should use to send data to the server. Here you can write whatever you want in the data parameter. However, it must be in BYTE type. Also, if you are going to use UDP Transport Protocol, you need to specify a specific Target.

RecvDataClient(BufferSize) # If you are using TCP Transport Protocol, you can use it directly. If you are using UDP Transport Protocol, 2 values ​​will be returned. The first value is the received data, the second value is from whom it was received. You can set BufferSize as an option.

CloseClient() # This function allows you to close the client connection.

```

---

  Server side and Client side are basically very close to each other in their usage.
