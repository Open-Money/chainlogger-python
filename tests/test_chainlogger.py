import sys
sys.path.insert(0, '../chainlogger')
from chainlogger.logger import Logger


class TestCase:
    logger = None

    def set_up(self):
        abi = '[{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event",' \
              '"name":"LogRegistered","inputs":[{"type":"address","name":"_vendorAddress","internalType":"address",' \
              '"indexed":true},{"type":"uint256","name":"_projectId","internalType":"uint256","indexed":false},' \
              '{"type":"uint256","name":"_projectLogCounter","internalType":"uint256","indexed":false},' \
              '{"type":"bytes32","name":"_data","internalType":"bytes32","indexed":true}],"anonymous":false},' \
              '{"type":"event","name":"VendorRegistered","inputs":[{"type":"uint256","name":"_id",' \
              '"internalType":"uint256","indexed":true},{"type":"address","name":"_vendorAddress",' \
              '"internalType":"address","indexed":true}],"anonymous":false},{"type":"function",' \
              '"stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],' \
              '"name":"_changeOwner","inputs":[{"type":"address","name":"toOwner","internalType":"address"}]},' \
              '{"type":"function","stateMutability":"view","outputs":[{"type":"bytes32","name":"",' \
              '"internalType":"bytes32"}],"name":"getLog","inputs":[{"type":"address","name":"vendorAddress",' \
              '"internalType":"address"},{"type":"uint256","name":"projectId","internalType":"uint256"},' \
              '{"type":"uint256","name":"logId","internalType":"uint256"}]},{"type":"function",' \
              '"stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],' \
              '"name":"numVendors","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{' \
              '"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function",' \
              '"stateMutability":"nonpayable","outputs":[{"type":"address","name":"","internalType":"address"},' \
              '{"type":"uint256","name":"","internalType":"uint256"},{"type":"uint256","name":"",' \
              '"internalType":"uint256"},{"type":"bytes32","name":"","internalType":"bytes32"}],"name":"registerLog",' \
              '"inputs":[{"type":"uint256","name":"projectId","internalType":"uint256"},{"type":"bytes32",' \
              '"name":"data","internalType":"bytes32"}]},{"type":"function","stateMutability":"nonpayable",' \
              '"outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"registerProject",' \
              '"inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"uint256","name":"",' \
              '"internalType":"uint256"}],"name":"registerVendor","inputs":[]},{"type":"function",' \
              '"stateMutability":"view","outputs":[{"type":"address","name":"vendorAddress",' \
              '"internalType":"address"},{"type":"uint256","name":"projectCounter","internalType":"uint256"}],' \
              '"name":"vendorLogs","inputs":[{"type":"uint256","name":"","internalType":"uint256"}]},' \
              '{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"",' \
              '"internalType":"address"}],"name":"vendors","inputs":[{"type":"uint256","name":"",' \
              '"internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256",' \
              '"name":"","internalType":"uint256"}],"name":"vendorsReverse","inputs":[{"type":"address","name":"",' \
              '"internalType":"address"}]}]'

        provider = 'https://provider.omlira.com'
        eth_signer = 'http://127.0.0.1:8560'
        contract_address = "0x27977679d45bdB739E1cdd9A5c510B471CA0aB75"

        logger = Logger()
        logger.set_provider(provider)
        logger.set_abi(abi)
        logger.set_eth_signer(eth_signer)
        logger.set_web3()
        logger.set_salt("MY_SECRET_SALT")
        logger.set_contract(contract_address)
        logger.set_send_contract(contract_address)
        logger.set_account('0x00230c0b9eba13B028CeB359c6C4BbeA215463aA')
        self.logger = logger

    def test_register_log(self):
        raw_input = "MY_TEST_INPUT"
        tx_hash = self.logger.register_log(1, raw_input)
        print(tx_hash)

    def test_register_vendor(self):
        tx_hash = self.logger.register_vendor()
        tx_hash = self.logger.web3.toHex(tx_hash)
        print(tx_hash)

    def test_register_project(self):
        tx_hash = self.logger.register_project()
        tx_hash = self.logger.web3.toHex(tx_hash)
        print(tx_hash)


if "__main__":
    test = TestCase()
    test.set_up()
    test.test_register_project()
    test.test_register_vendor()
    test.test_register_log()
