```python
import json
import socket
from typing import Dict, List, Optional

class CommunicationProtocol:
    """
    A class representing the communication protocol for agents to exchange messages and coordinate tasks.
    """

    def __init__(self, host: str = '127.0.0.1', port: int = 65432):
        """
        Initialize the communication protocol with a specific host and port.

        :param host: The hostname or IP address to connect to.
        :param port: The port number to connect to.
        """
        self.host = host
        self.port = port

    def send_message(self, message: Dict[str, any]) -> None:
        """
        Send a message to the connected agent.

        :param message: A dictionary representing the message to be sent.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(json.dumps(message).encode('utf-8'))
        except Exception as e:
            raise CommunicationError(f"Failed to send message: {e}")

    def receive_message(self) -> Dict[str, any]:
        """
        Receive a message from the connected agent.

        :return: A dictionary representing the received message.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(1024)
                    return json.loads(data.decode('utf-8'))
        except Exception as e:
            raise CommunicationError(f"Failed to receive message: {e}")

    def broadcast_message(self, message: Dict[str, any], addresses: List[str]) -> None:
        """
        Broadcast a message to multiple agents.

        :param message: A dictionary representing the message to be sent.
        :param addresses: A list of tuples containing the host and port for each agent.
        """
        try:
            for address in addresses:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(address)
                    s.sendall(json.dumps(message).encode('utf-8'))
        except Exception as e:
            raise CommunicationError(f"Failed to broadcast message: {e}")

class CommunicationError(Exception):
    """
    A custom exception class for communication protocol errors.
    """

    def __init__(self, message: str):
        super().__init__(message)
```

This Python code defines a `CommunicationProtocol` class that handles the communication between agents using a simple TCP socket connection. The class provides methods to send and receive messages, as well as broadcast messages to multiple agents. Error handling is included for each method to ensure robustness in case of network issues or invalid data.