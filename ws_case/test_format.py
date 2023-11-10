from airtest.core.api import *
from airtest.cli.parser import cli_setup
class TestFormat:
    auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8300",])

    def test_one(self):
        touch([195, 1921])

