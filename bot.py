import json
import time
import datetime
import bitmart
from typing import Union
from bitmart import initialize_client, Market, FuturesSide, OrderType, OrderOpenType, BtFuturesSocketKlineChannels, BtFuturesTPrivatePositionChannel, WebSocketKline, WebSocketPositionFutures
from my_module import initialize_client

import pandas as pd
from typing import Union
from bitmart import initialize_client, Market, FuturesSide, OrderType, OrderOpenType, BtFuturesSocketKlineChannels, BtFuturesTPrivatePositionChannel, WebSocketKline, WebSocketPositionFutures
from my_module import initialize_client


class TradingBot:
    """
    A trading bot that trades futures contracts on BitMart.

    Public Methods:
    - preload(): Preloads the candles data for the trading bot.
    - start(): Starts the trading bot.
    """

    class TradingBot:
        def __init__(self, symbol: str, contract_size: int):
            """
            Initializes a new instance of the TradingBot class.

            Args:
            symbol (str): The symbol to trade.
            contract_size (int): The contract size to use for trading.
            """
            self.symbol = symbol
            self.contract_size = contract_size
            self.position_side = None
            self.profit = 0
            self.candles = pd.DataFrame()
            self.client = initialize_client()  # initialize the client attribute

        def preload(self):
            """
            Preloads the candles data for the trading bot.
            """
            # Implement the preload logic here

        def start(self):
            """
            Starts the trading bot.
            """
            print("Starting bot...")
            self.preload()
            self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                          channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
            self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

            self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

        def open_position(self, side: FuturesSide):
            """
            Opens a new position.

            Args:
            side (FuturesSide): The position side to open.
            """
            print(f"Open position {side}")
            order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
            self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                      size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

            self.position_side = side

        def close_position(self):
            """
            Closes the current position.
            """
            print(f"Close position {self.position_side}")
            order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
            self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                      size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

            self.position_side = None

        def trade_decision(self):
            """
            Makes a trading decision based on the current market conditions.
            """
            row = self.candles.iloc[-1]
            # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
            # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
            # row contains the most recent candle data, which can be used to make a trading decision.

    def preload(self):
        """
        Preloads the candles data for the trading bot.
        """
        # Implement the preload logic here

    def start(self):
        """
        Starts the trading bot.
        """
        print("Starting bot...")
        self.preload()
        self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                      channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
        self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

        self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

    def open_position(self, side: FuturesSide):
        """
        Opens a new position.

        Args:
        side (FuturesSide): The position side to open.
        """
        print(f"Open position {side}")
        order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = side

    def close_position(self):
        """
        Closes the current position.
        """
        print(f"Close position {self.position_side}")
        order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = None

    def trade_decision(self):
        """
        Makes a trading decision based on the current market conditions.
        """
        row = self.candles.iloc[-1]
        # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
        # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
        # A trading bot that trades futures contracts on BitMart.

        Public Methods:
        - preload(): Preloads the candles data for the trading bot.
        - start(): Starts the trading bot.
        """

        def __init__(self, symbol: str, contract_size: int):
            """
            Initializes a new instance of the TradingBot class.

            Args:
            symbol (str): The symbol to trade.
            contract_size (int): The contract size to use for trading.
            """
            self.symbol = symbol
            self.contract_size = contract_size
            self.position_side = None
            self.profit = 0
            self.candles = pd.DataFrame()
            self.client = initialize_client()  # initialize the client attribute

        def preload(self):
            """
            Preloads the candles data for the trading bot.
            """
            # Implement the preload logic here

    def start(self):
        """
        Starts the trading bot.
        """
        print("Starting bot...")
        self.preload()
        self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                      channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
        self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

        self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

    def open_position(self, side: FuturesSide):
        """
        Opens a new position.

        Args:
        side (FuturesSide): The position side to open.
        """
        print(f"Open position {side}")
        order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = side

    def close_position(self):
        """
        Closes the current position.
        """
        print(f"Close position {self.position_side}")
        order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = None

    def trade_decision(self):
        """
        Makes a trading decision based on the current market conditions.
        """
        row = self.candles.iloc[-1]
        # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
        # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
    def __init__(self, symbol, contract_size):
        """
        Initializes the trading bot.

        Args:
        symbol (str): The symbol to trade.
        contract_size (int): The contract size to use for trading.
        """
        self.symbol = symbol
        self.contract_size = contract_size
        self.position_side = None
        self.profit = 0
        self.candles = pd.DataFrame()
        self.client = initialize_client()  # initialize the client attribute

    # rest of the code
import json
import time
import datetime
import bitmart
import pandas as pd
from typing import Union
from bitmart import initialize_client, Market, FuturesSide, OrderType, OrderOpenType, BtFuturesSocketKlineChannels, BtFuturesTPrivatePositionChannel, WebSocketKline, WebSocketPositionFutures
from my_module import initialize_client

class TradingBot:
    def __init__(self, symbol: str, contract_size: int):
        """
        import json
        import time
        import datetime
        import bitmart
        import pandas as pd
        from typing import Union
        from bitmart import initialize_client, Market, FuturesSide, OrderType, OrderOpenType, BtFuturesSocketKlineChannels, BtFuturesTPrivatePositionChannel, WebSocketKline, WebSocketPositionFutures
        from my_module import initialize_client

        class TradingBot:
            def __init__(self, symbol: str, contract_size: int):
                """
                Initializes a new instance of the TradingBot class.

                Args:
                symbol (str): The symbol to trade.
                contract_size (int): The contract size to use for trading.
                """
                self.symbol = symbol
                self.contract_size = contract_size
                self.position_side = None
                self.profit = 0
                self.candles = pd.DataFrame()
                self.client = initialize_client()  # initialize the client attribute

            def preload(self):
                """
                Preloads the candles data for the trading bot.
                """
                # Implement the preload logic here

            def start(self):
                """
                Starts the trading bot.
                """
                print("Starting bot...")
                self.preload()
                self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                              channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
                self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

                self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

            def open_position(self, side: FuturesSide):
                """
                Opens a new position.

                Args:
                side (FuturesSide): The position side to open.
                """
                print(f"Open position {side}")
                order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
                self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                          size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

                self.position_side = side

            def close_position(self):
                """
                Closes the current position.
                """
                print(f"Close position {self.position_side}")
                order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
                self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                          size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)
                import pandas as pd
                import datetime
                from typing import Union
                from bitmart.api_spot import Market
                from bitmart.api_futures import FuturesSide
                from bitmart.websocket import WebSocketKline, WebSocketPositionFutures
                from bitmart.client import initialize_client

                class TradingBot:
                    """
                    A class representing a trading bot.
                    """
                    def __init__(self, symbol: str, contract_size: int):
                        """
                        Initializes a new instance of the TradingBot class.

                        Args:
                        symbol (str): The symbol to trade.
                        contract_size (int): The contract size to use for trading.
                        """
                        self.symbol = symbol
                        self.contract_size = contract_size
                        self.position_side = None
                        self.profit = 0
                        self.candles = pd.DataFrame()
                        self.client = initialize_client()  # initialize the client attribute

                    def preload(self):
                        """
                        Preloads the candles data for the trading bot.
                        """
                        # Implement the preload logic here
                        pass

                    def start(self):
                        """
                        Starts the trading bot.
                        """
                        pass

                    def open_position(self, side: FuturesSide):
                        """
                        Opens a new position.

                        Args:
                        side (FuturesSide): The side of the position to open.
                        """
                        pass

                    def close_position(self):
                        """
                        Closes the current position.
                        """
                        pass

                    def trade_decision(self):
                        """
                        Makes a trading decision based on the current market conditions.
                        """
                        row = self.candles.iloc[-1]
                        # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
                        # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
                        # allows you to access the values of the last candle in the dataset for further analysis and
                        # decision making in the `trade_decision()` method.
                        print(f"rsi: {row.rsi} bb: {row.bb_upper} | {row.close} | {row.bb_lower}")

                        if self.should_buy(row) and self.position_side != FuturesSide.LONG:
                            if self.position_side is None:
                                self.open_position(FuturesSide.LONG)
                            else:
                                self.close_position()
                                self.open_position(FuturesSide.LONG)

                        elif self.should_sell(row) and self.position_side != FuturesSide.SHORT:
                            if self.position_side is None:
                                self.open_position(FuturesSide.SHORT)
                            else:
                                self.close_position()
                                self.open_position(FuturesSide.SHORT)

                    def should_buy(self, row):
                        """
                        Determines whether to buy based on the current market conditions.

                        Args:
                        row: The current row of the candles DataFrame.

                        Returns:
                        bool: True if a buy should be made, False otherwise.
                        """
                        # Implement the buy logic here
                        pass

                    def should_sell(self, row):
                        """
                        Determines whether to sell based on the current market conditions.

                        Args:
                        row: The current row of the candles DataFrame.

                        Returns:
                        bool: True if a sell should be made, False otherwise.
                        """
                        # Implement the sell logic here
                        pass

                    def _on_message(self, message: Union[WebSocketKline, WebSocketPositionFutures]):
                        """
                        Handles the incoming messages from the BitMart API.

                        Args:
                        message (Union[WebSocketKline, WebSocketPositionFutures]): The incoming message.
                        """
                        if isinstance(message, WebSocketKline):
                            self.candles = self.candles.append({
                                "open_time": datetime.datetime.fromtimestamp(message.timestamp / 1000),
                                "open": message.open,
                                "high": message.high,
                                "low": message.low,
                                "close": message.close,
                                "volume": message.volume
                            }, ignore_index=True)

                            self.trade_decision()

                        elif isinstance(message, WebSocketPositionFutures):
                            self.profit = message.profit
                            self.position_side = message.side
                print("Starting bot...")
                self.preload()
                self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol])

        Args:
        symbol (str): The symbol to trade.
        contract_size (int): The contract size to use for trading.
        """
        self.symbol = symbol
        self.contract_size = contract_size
        self.position_side = None
        self.profit = 0
        self.candles = pd.DataFrame()
        self.client = initialize_client()  # initialize the client attribute

    def preload(self):
        """
        Preloads the candles data for the trading bot.
        """
        # Implement the preload logic here

    def start(self):
        """
        Starts the trading bot.
        """
        print("Starting bot...")
        self.preload()
        self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                      channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
        self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

        self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

    def open(self, side: FuturesSide):
        """
        Opens a new position.

        Args:
        side (FuturesSide): The position side to open.
        """
        print(f"Open position {side}")
        order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = side

    def close(self):
        """
        Closes the current position.
        """
        print(f"Close position {self.position_side}")
        order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = None

    def trade_decision(self):
        """
        Makes a trading decision based on the current market conditions.
        """
        row = self.candles.iloc[-1]
        # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
        # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
        # allows you to access the values of the last candle in the dataset for further analysis and
        # decision making in the `trade_decision()` method.
        print(f"rsi: {row.rsi} bb: {row.bb_upper} | {row.close} | {row.bb_lower}")

        if should_buy(row) and self.position_side != FuturesSide.LONG:
            if self.position_side is None:
                self.open(FuturesSide.LONG)
            else:
                self.close()
        elif should_sell(row) and self.position_side != FuturesSide.SHORT:
            if self.position_side is None:
                self.open(FuturesSide.SHORT)
            else:
                self.close()

    def _on_message(self, msg: Union[WebSocketKline, WebSocketPositionFutures]):
        """
        Handles a new message received from the websocket.

        Args:
        msg (Union[WebSocketKline, WebSocketPositionFutures]): The message received from the websocket.
        """
        pass


    def stop(self):
        """
        Stops the trading bot.
        """
        print("Total profit is %.3f" % self.profit)
        self.client.stop_websockets(market=Market.FUTURES)

    def preload(self):
        """
        Preloads the candles data for the trading bot.
        """
        # Implement the preload logic here

    def start(self):
        """
        Starts the trading bot.
        """
        print("Starting bot...")
        self.preload()
        self.client.subscribe_public(market=Market.FUTURES, symbols=[self.symbol],
                                      channels=[BtFuturesSocketKlineChannels.K_LINE_CHANNEL_1HOUR])
        self.client.subscribe_private(market=Market.FUTURES, channels=[BtFuturesTPrivatePositionChannel])

        self.client.start_websockets(market=Market.FUTURES, on_message=self._on_message)

    def open(self, side: FuturesSide):
        """
        Opens a new position.

        Args:
        side (FuturesSide): The position side to open.
        """
        print(f"Open position {side}")
        order_side = FuturesSide.BUY_OPEN_LONG if side == FuturesSide.LONG else FuturesSide.SELL_OPEN_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = side

    def close(self):
        """
        Closes the current position.
        """
        print(f"Close position {self.position_side}")
        order_side = FuturesSide.SELL_CLOSE_LONG if self.position_side == FuturesSide.LONG else FuturesSide.BUY_CLOSE_SHORT
        self.client.submit_order(symbol=self.symbol, market=Market.FUTURES, order_type=OrderType.MARKET,
                                  size=self.contract_size, open_type=OrderOpenType.CROSS, side=order_side)

        self.position_side = None

    def trade_decision(self):
        """
        Makes a trading decision based on the current market conditions.
        """
        row = self.candles.iloc[-1]
        # The line `row = self.candles.iloc[-1]` is retrieving the last row of the `self.candles`
        # DataFrame. The `.iloc[-1]` indexing is used to access the last row of the DataFrame. This
        # allows you to access the values of the last candle in the dataset for further analysis and
        # decision making in the `trade_decision()` method.
        print(f"rsi: {row.rsi} bb: {row.bb_upper} | {row.close} | {row.bb_lower}")

        if should_buy(row) and self.position_side != FuturesSide.LONG:
            if self.position_side is None:
                self.open(FuturesSide.LONG)
            else:
                self.close()
        elif should_sell(row) and self.position_side != FuturesSide.SHORT:
            if self.position_side is None:
                self.open(FuturesSide.SHORT)
            else:
                self.close()

    def _on_message(self, msg: Union[WebSocketKline, WebSocketPositionFutures]):
        """
        Handles a new message received from the websocket.

        Args:
        msg (Union[WebSocketKline, WebSocketPositionFutures]): The message received from the websocket.
        """
        if isinstance(msg, WebSocketKline):
            self.trade_decision()
            if self.candles.index[-1] < msg.date_time:
                pass
                self.preload()
        else:
            print(f"Position {msg.open_avg_price} [{msg.volume}]")
            if msg.volume == 0:
                profit = get_profit(msg.position_type, msg.open_avg_price, msg.close_avg_price)
                # The line `profit = get_profit(msg.position_type, msg.open_avg_price,
                # msg.close_avg_price)` is calculating the profit made from a closed position.
                print("POSITION CLOSED: %.3f" % profit)
                self.profit += profit
        """

        if __name__ == '__main__':
            bot = TradingBot(symbol="EOSUSDT", contract_size=5)
            bot.start()
            input("Press any key to exit...\r")
            bot.stop()
