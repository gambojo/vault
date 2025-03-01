def test_service_is_running(host):
    service = host.service("vault")
    assert service.is_running
    assert service.is_enabled

def test_port_is_listning(host):
    socket = host.socket('tcp://0.0.0.0:8200')
    assert socket.is_listening
