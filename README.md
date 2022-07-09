# Requirements

1. Ansible installed:

```
sudo apt install python3
python3 -m ensurepip --upgrade
pip3 install ansible
```

2. ansible.utils.ipaddr:

```
pip3 install netaddr 
```


## Required variables 

Set the variables as shown in defined.

The structure of the peer variable is as follows (very close to wireguard config):

```
peers:
  - name: harry
    routed_ips: 0.0.0.0/0, ::/0         # the IPv4/IPv6 addresses you would like to route (if this is not defined wg_routed_ips is used)
    dns: 1.1.1.1, 2606:4700:4700::1111  # the DNS your peer uses when using the VPN (if this is not defined wg_dns is used)
    force: false                        # can be skipped, whether to force recreate, overwriting keys
```

The ansible networking module:

ansible.utils.ipaddr

# Example playbook 

```
hosts:
  - foo
roles:
  - ansible-wireguard

```

Please not that this role does not take care of allowing wireguard through the firewall and other iptables/nftables config.

# TLDR - What will happen if I run this 

- install wireguard
- generate server config/keys (on remote target)
- generate client config where requested
- save client configs where requested (can be set see vars)
- bring the wg interface up (using systemd)
- show wg config when requested
