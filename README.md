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

```

---
wireguard_server_config_dir: /etc/wireguard
wireguard_client_config_dir: $HOME
wireguard_client_config_storage_host: localhost

wireguard_generate_server_keys: false
wireguard_generate_preshared_key: false
wireguard_show: false

wireguard_iffname: "wg0"
wireguard_endpoint: ""
wireguard_range_v4: ""
wireguard_range_v6: ""
wireguard_port: ""
wireguard_dns: ""
wireguard_routed_ips: ""
wireguard_allow_inet: true
wireguard_peers: []
#   - name: harry
#     routed_ips: 0.0.0.0/0, ::/0         # the IPv4/IPv6 addresses you would like to route (if this is not defined wg_routed_ips is used)
#     dns: 1.1.1.1, 2606:4700:4700::1111  # the DNS your peer uses when using the VPN (if this is not defined wg_dns is used)
#     force: false                        # can be skipped, whether to force recreate, overwriting keys

```

See the argument spec in meta/main.yaml for additional descriptions.

The ansible networking module:

ansible.utils.ipaddr

# Example playbook

```
hosts:
  - foo
roles:
  - ansible-wireguard

```

Please note that this role does not take care of allowing wireguard through the firewall and other iptables/nftables config, as this goes beyond the scope of this role. You have do that manually, or use other roles.

# TLDR - What will happen if I run this

- install wireguard
- generate server config/keys (on remote target)
- generate client config where requested
- save client configs where requested (can be set to any host)
- bring the wg interface up (using systemd)
- show wg config when requested
