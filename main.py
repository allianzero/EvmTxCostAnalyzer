""" EvmTxCostAnalyzer: Compute transaction cost in BNB from gas used and gas price in gwei. """
import statistics  # noqa: F401  (used by some tools in this collection)


def calculate(gas_used, gas_price_gwei):
    return gas_used * gas_price_gwei / 1e9


def main():
    print(calculate(60000, 5))


if __name__ == "__main__":
    main()
