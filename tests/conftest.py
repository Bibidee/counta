from gltest.direct import sdk_loader
import sys

# Keep tests pinned to the contract's py-genlayer dependency.
sdk_loader.get_latest_version = lambda: "v0.2.12"


def pytest_configure(config):
    if sys.platform != "win32":
        return
    # Work around the pinned Windows loader's temporary-stdin unlink behavior.
    # Ubuntu/Linux CI always exercises the official unmodified Direct Mode path.
    import os
    import tempfile
    from gltest.direct import loader

    def inject(vm):
        from genlayer.py import calldata
        from genlayer.py.types import Address

        sender = vm.sender if isinstance(vm.sender, Address) else Address(vm.sender)
        contract = vm._contract_address if isinstance(vm._contract_address, Address) else Address(vm._contract_address)
        origin = vm.origin if isinstance(vm.origin, Address) else (Address(vm.origin) if vm.origin else None)
        encoded = calldata.encode({
            "contract_address": contract,
            "sender_address": sender,
            "origin_address": origin,
            "stack": [],
            "value": vm._value,
            "datetime": vm._datetime,
            "is_init": False,
            "chain_id": vm._chain_id,
            "entry_kind": 0,
            "entry_data": b"",
            "entry_stage_data": None,
        })
        fd, path = tempfile.mkstemp()
        os.write(fd, encoded)
        os.lseek(fd, 0, 0)
        vm._original_stdin_fd = os.dup(0)
        os.dup2(fd, 0)
        os.close(fd)
        vm._counta_test_stdin = path

    loader._inject_message_to_fd0 = inject
