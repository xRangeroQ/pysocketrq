# Libraries
import socket

# Variables
red="\033[31m"
green="\033[32m"
yellow="\033[33m"
clear="\033[0m"
sError, sInfo, sSuccessful=f"{red}[-]{clear}", f"{yellow}[?]{clear}", f"{green}[+]{clear}"


# PySocketRQ Class
class PySocketRQ:

    # İnitailize
    def __init__(self, Debug, Address_Family="IPv4" or "IPv6", Transport_Protocol="TCP" or "UDP", Host=("0.0.0.0", 8080), Target=("127.0.0.1", 8080)):
        self.debug=Debug
        self.Host=Host
        self.Target=Target
        self.Address_Family=Address_Family
        self.Transport_Protocol=Transport_Protocol

        # IPv Family Check
        if self.Address_Family.lower()=="ipv4":
            self.Address_Family=socket.AF_INET

        elif Address_Family.lower()=="ipv6":
            self.Address_Family=socket.AF_INET6


        # Communicate Protocol Check
        if self.Transport_Protocol.lower()=="udp":
            self.Transport_Protocol=socket.SOCK_DGRAM

        elif Transport_Protocol.lower()=="tcp":
            self.Transport_Protocol=socket.SOCK_STREAM


    # Debug Controller
    def _Debug(self, DebugMessage):
        if self.debug:
            print(DebugMessage)

        elif not self.debug:
            pass

        else:
            print(f"{sError} Error while configuring debugger!")


    # Create IPv4 || IPv6 && TCP || UDP Socket Server
    def CreateServer(self):
        # Variables
        global client, address, server
        

        # Create Socket && Bind
        try:
            server=socket.socket(self.Address_Family, self.Transport_Protocol)
            self._Debug(f"{sSuccessful} Successfully created socket!")

        except Exception as error:
            self._Debug(f"{sError} An error occurred while creating the socket! Error: {error}")

        try:
            server.bind(self.Host)

        except socket.error as error:
            self._Debug(f"{sError} An error occurred while associating the socket with the specified address! Error: {error}")

        
        # Config Socket
        # - TCP
        if self.Transport_Protocol==socket.SOCK_STREAM:
            server.listen()
            self._Debug(f"{sInfo} Server listening on {self.Host}...")

            client, address=server.accept()
            self._Debug(f"{sSuccessful} Connection to {address} established!")


        # - UDP
        elif self.Transport_Protocol==socket.SOCK_DGRAM:
            self._Debug(f"{sInfo} Socket started at specified address!")



    # Send Data to Client
    def SendDataServer(self, data):
        try:
            # -TCP
            if self.Transport_Protocol==socket.SOCK_STREAM:
                client.send(data)
                self._Debug(f"{sSuccessful} Data successfully delivered to {address}!")


            # - UDP
            elif self.Transport_Protocol==socket.SOCK_DGRAM:
                server.sendto(data, self.Target)
                self._Debug(f"{sSuccessful} Data was thrown to {self.Target}!")

        except Exception as error:
            self._Debug(f"{sError} An error was encountered while trying to send data! Error: {error}")


    # Receive Data opt(From Client)
    def RecvDataServer(self, BufferSize=4096):
        try:
            # - TCP
            if self.Transport_Protocol==socket.SOCK_STREAM:
                receivedData=client.recv(BufferSize)
                return receivedData
            

            # - UDP
            elif self.Transport_Protocol==socket.SOCK_DGRAM:
                receivedData, receivedAddress=server.recvfrom(BufferSize)
                return receivedData, receivedAddress
        
        except Exception as error:
            self._Debug(f"{sError} An error was encountered while trying to get data from the client! Error: {error}")


    # Close Server Connection
    def CloseServer(self):
        try:
            server.close()
            self._Debug(f"{sSuccessful} Successfully closed the Server connection!")

        except Exception as error:
            self._Debug(f"{sError} An error occurred while closing the Server connection! Error: {error}")


    # Close Client Connection
    def CloseClient(self):
        try:
            client.close()
            self._Debug(f"{sSuccessful} Successfully closed the Client connection!")

        except Exception as error:
            self._Debug(f"{sError} An error occurred while closing the Client connection! Error: {error}")



    # Create IPv4 || IPv6 && TCP || UDP Socket Client
    def CreateClient(self):
        # Variables
        global client, address

        # Create Socket && Bind
        try:
            client=socket.socket(self.Address_Family, self.Transport_Protocol)
            self._Debug(f"{sSuccessful} Successfully created socket!")

        except Exception as error:
            self._Debug(f"{sError} An error occurred while creating the socket! Error: {error}")

        
        # Config Socket

        # - TCP
        if self.Transport_Protocol==socket.SOCK_STREAM:
            try:
                client.connect(self.Target)
                self._Debug(f"{sSuccessful} The Client has successfully connected to the Server!")

            except Exception as error:
                self._Debug(f"{sError} An error occurred while the Client was connecting to the Server!")


        # - UDP
        elif self.Transport_Protocol==socket.SOCK_DGRAM:
            try:
                client.bind(self.Host)

            except socket.error as error:
                self._Debug(f"{sError} An error occurred while associating the socket with the specified address! Error: {error}")

            self._Debug(f"{sInfo} Socket started at specified address!")


    # Send Data to Server
    def SendDataClient(self, data):
        try:
            # -TCP
            if self.Transport_Protocol==socket.SOCK_STREAM:
                client.send(data)
                self._Debug(f"{sSuccessful} Data successfully delivered to {self.Target}!")


            # - UDP
            elif self.Transport_Protocol==socket.SOCK_DGRAM:
                client.sendto(data, self.Target)
                self._Debug(f"{sSuccessful} Data was thrown to {self.Target}!")

        except Exception as error:
            self._Debug(f"{sError} An error was encountered while trying to send data! Error: {error}")


    # Receive Data opt(From Client)
    def RecvDataClient(self, BufferSize=4096):
        try:
            # - TCP
            if self.Transport_Protocol==socket.SOCK_STREAM:
                receivedData=client.recv(BufferSize)
                return receivedData
            

            # - UDP
            elif self.Transport_Protocol==socket.SOCK_DGRAM:
                receivedData, receivedAddress=client.recvfrom(BufferSize)
                return receivedData, receivedAddress
        
        except Exception as error:
            self._Debug(f"{sError} An error was encountered while trying to get data from the client! Error: {error}")
