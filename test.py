import pyupbit

access = "sKqU7KkT1KBGsvvtqwF822eavPv83EtxxUzUyjOo"          # 본인 값으로 변경
secret = "V1xcE7Salxzb8AbWswlXwNzzjNX6xmfeUlWkoOxc"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회

print(upbit.get_balance("KRW"))         # 보유 현금 조회