if __name__ == '__main__':
    bot = Trading_Bot(symbol="EOSUSDT", contract_size=5)
    bot.start()
    input("Press any key to exit...\r")
    bot.stop()