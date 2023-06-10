import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_wireguard_present(host):
    """test that wireguard is present as command"""

    assert host.run("which wg").rc == 0


def test_wg_config_file(host):
    """test that the wireguard config file is present"""

    with host.sudo():
        assert host.file("/etc/wireguard/wg0.conf")


def test_peer_present(host):
    """test that the peer is present in the wireguard config file"""

    with host.sudo():
        assert host.file("/etc/wireguard/wg0.conf").contains("test-peer")
