import sys
import ipaddress
import ctypes
from bcc import BPF


interface = "eth0"

b = BPF(src_file="ip_blocking.c")
fn = b.load_func("block", BPF.XDP)
b.attach_xdp(dev=interface, fn=b.load_func("block", BPF.XDP))


def ip_to_bin(dotted_ip):
    ip = ipaddress.ip_address(dotted_ip)
    return ctypes.c_uint(int.from_bytes(ip.packed, "little"))


def _load_cache(dotted_ips):
    print("loading IPs...")
    cache = b.get_table("cache")
    for dotted_ip in dotted_ips:
        ip = ip_to_bin(dotted_ip)
        print(f"{dotted_ip}: {ip}")
        cache[ip] = ctypes.c_char(1)    


def run(ips):
    _load_cache(ips)

    try:
        print("running...")
        b.trace_print()
    except KeyboardInterrupt:
        print("going out !!")
    finally:
            b.remove_xdp(interface, 0)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No IPs have been provided")
        exit(1)
    run(sys.argv[1:])