#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/in.h>


BPF_HASH(cache, unsigned int, char, 128);

int block(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    struct ethhdr *eth = data;
    
    if ((void *)eth + sizeof(*eth) <= data_end) {
        struct iphdr *ip = data + sizeof(*eth);
        if ((void *)ip + sizeof(*ip) <= data_end) {
            if (ip->protocol != IPPROTO_TCP) {
                return XDP_PASS;
            }

            unsigned int address = ip->saddr;
            char *value = cache.lookup(&address);
            if (value != NULL) {
                bpf_trace_printk("blocking %d...\n", address);
                return XDP_DROP;
            }
        }
    }

    return XDP_PASS;
}

