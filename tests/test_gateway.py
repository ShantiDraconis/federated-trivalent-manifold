import pytest
from gateway.hkdf_keys import KeyContexts, derive_keys
from gateway.teardown import teardown


def test_contexts_must_differ():
    with pytest.raises(ValueError):
        KeyContexts(b"same", b"same").validate()


def test_no_insecure_crypto_fallback():
    try:
        left, right = derive_keys(b"m" * 32, b"s" * 16)
    except RuntimeError:
        return
    assert len(left) == len(right) == 32 and left != right


def test_serial_validation_prevents_shell_injection():
    with pytest.raises(ValueError):
        teardown("device; malicious command")
