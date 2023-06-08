import testinfra


def test_os_release(host):
    """test host release for good measure"""

    assert host.file("/etc/os-release").contains("Ubuntu")


def test_wireguard_present(host):
    """test that the ssh service is running"""

    assert host.run("which wg").rc == 0


def test_wg_config_file(host):
    """test that the ssh service is running"""

    with host.sudo():
        assert host.file("/etc/wireguard/wg0.conf")
