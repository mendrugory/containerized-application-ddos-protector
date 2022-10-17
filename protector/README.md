# Protector

Protector is a eBPF - XDP program which will drop TCP packages whose source are the provided IPs, in our case, the IPs of the attackers. We can pick these IPs from the log of the server.

Protector will work in the same network namespace where Server is running therefore, it will have access to the network interface.

## How to run it

```bash
$ ./run.sh <IPs of the attackers> # 172.29.0.3 172.29.0.4
```

## Example

```bash
$ ./run.sh 172.29.0.3 172.29.0.4
loading IPs...
172.29.0.3: c_uint(50339244)
172.29.0.4: c_uint(67116460)
running...
b'            wget-440265  [008] d.s1. 24377.243812: bpf_trace_printk: blocking 67116460...'
b''
b'            wget-440266  [000] d.s1. 24377.294718: bpf_trace_printk: blocking 50339244...'
```

> The int number represents the little endian binary integer of the IPv4 address. (172.29.0.3 -> 50339244).
