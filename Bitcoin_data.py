import requests
import pandas as pd
import time
import os
from datetime import datetime

### 심볼 불러오기
result = requests.get('https://api.binance.com/api/v3/ticker/price')
js = result.json()
symbols = [x['symbol'] for x in js]
symbols_usdt = [x for x in symbols if 'USDT' in x]  # 끝이 USDT로 끝나는 심볼들, ['BTCUSDT', 'ETHUSDT', ...]

### 데이터 불러오기

# 가져오는 데이터의 column
COLUMNS = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'quote_av', 'trades',
                   'tb_base_av', 'tb_quote_av', 'ignore']

# 조회하는 URL 주소
URL = 'https://api.binance.com/api/v3/klines'

# 함수
def get_data(start_date, end_date, symbol):
    data = []

    start = int(time.mktime(datetime.strptime(start_date + ' 00:00', '%Y-%m-%d %H:%M').timetuple())) * 1000
    end = int(time.mktime(datetime.strptime(end_date + ' 23:59', '%Y-%m-%d %H:%M').timetuple())) * 1000
    params = {
        'symbol': symbol,
        'interval': '1m', # 76번째 줄도 바꿔야 함 # 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
        'limit': 1000,
        'startTime': start,
        'endTime': end
    }

    while start < end:
        print(datetime.fromtimestamp(start // 1000))
        params['startTime'] = start
        result = requests.get(URL, params=params)
        js = result.json()
        if not js:
            break
        data.extend(js)  # result에 저장
        start = js[-1][0] + 60000  # 다음 step으로
    # 전처리
    if not data:  # 해당 기간에 데이터가 없는 경우
        print('해당 기간에 일치하는 데이터가 없습니다.')
        return -1
    df = pd.DataFrame(data)
    df.columns = COLUMNS
    df['Open_time'] = df.apply(lambda x: datetime.fromtimestamp(x['Open_time'] // 1000), axis=1)
    df = df.drop(columns=['Close_time', 'ignore'])
    df['Symbol'] = symbol
    df.loc[:, 'Open':'tb_quote_av'] = df.loc[:, 'Open':'tb_quote_av'].astype(float)  # string to float
    df['trades'] = df['trades'].astype(int)
    return df

# # 시작시간, 종료시간 입력
# start_date = '2021-12-15'
# end_date = '2022-02-01'
# symbol = symbols_usdt[0]
# data = get_data(start_date,end_date,symbol)

# # CSV 파일로 저장


### 모든 데이터 csv로 저장
# 티커 이름 - 타임프레임별 저장

# 1분 데이터부터 - 시간은 위의 interval 바꿔줘야 함

interval = '1m' # 33번째 줄 참고

# 1년 단위 데이터

years = list(range(2018,2023))  # 바이낸스에서는 2017년 8월 이후의 데이터부터 제공하므로, 이때부터 있는 모든 데이터 긁어오기

for symbol in symbols_usdt[:10]:
    try:
        os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data')
        for year in years: # 연도별 자료 백테스트
            start_date = f'{year}-01-01'
            end_date = f'{year}-12-31'
            try:
                try:
                    os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}')  # 티커명으로 폴더 만들기 ex. BTC/USDT
                    df = get_data(start_date, end_date, symbol)
                    df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_{year}.csv',index=False)  # 긁어온 데이터를 csv파일로 저장
                    time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
                except AttributeError:
                    pass

            except FileExistsError:  # 이미 디렉토리가 만들어져 있을 경우 실행
                try:
                    print(f"이미 {symbol[:-4]}-USDT_{interval} 디렉토리 만들어져 있습니다")
                    df = get_data(start_date, end_date, symbol)
                    df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_{year}.csv', index=False)  # 긁어온 데이터를 csv파일로 저장
                    time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
                except AttributeError:
                    pass

    except FileExistsError: # 이미 디렉토리가 만들어져 있을 경우 실행
        print (f"이미 {symbol[:-4]}-USDT 디렉토리가 만들어져 있습니다")
        for year in years: # 연도별 자료 백테스트
            start_date = f'{year}-01-01'
            end_date = f'{year}-12-31'
            try:
                try:
                    os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}')  # 티커명으로 폴더 만들기 ex. BTC/USDT
                    df = get_data(start_date, end_date, symbol)
                    df.to_csv(
                        f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_{year}.csv',
                        index=False)  # 긁어온 데이터를 ㄴcsv파일로 저장
                    time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
                except AttributeError:
                    pass

            except FileExistsError:  # 이미 디렉토리가 만들어져 있을 경우 실행
                try:
                    print(f"이미 {symbol[:-4]}-USDT_{interval} 디렉토리가 만들어져 있습니다")
                    df = get_data(start_date, end_date, symbol)
                    df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_{year}.csv', index=False)  # 긁어온 데이터를 ㄴcsv파일로 저장
                    time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
                except AttributeError:
                    pass

# 전체 연도 통합

years = list (range(2017,2024))
for symbol in symbols_usdt[:10]:
    try:
        os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data')
        start_date = f'{years[0]}-01-01'
        end_date = f'{years[-1]}-12-31'
        try:
            try:
                os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}')  # 티커명으로 폴더 만들기 ex. BTC/USDT
                df = get_data(start_date, end_date, symbol)
                df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_All.csv',index=False)  # 긁어온 데이터를 csv파일로 저장
                time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
            except AttributeError:
                pass

        except FileExistsError:  # 이미 디렉토리가 만들어져 있을 경우 실행
            try:
                print(f"이미 {symbol[:-4]}-USDT_{interval} 디렉토리 만들어져 있습니다")
                df = get_data(start_date, end_date, symbol)
                df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_All.csv', index=False)  # 긁어온 데이터를 csv파일로 저장
                time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
            except AttributeError:
                pass

    except FileExistsError: # 이미 디렉토리가 만들어져 있을 경우 실행
        print (f"이미 {symbol[:-4]}-USDT 디렉토리가 만들어져 있습니다")
        start_date = f'{years[0]}-01-01'
        end_date = f'{years[-1]}-12-31'
        try:
            try:
                os.makedirs(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}')  # 티커명으로 폴더 만들기 ex. BTC/USDT
                df = get_data(start_date, end_date, symbol)
                df.to_csv(
                    f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_All.csv',
                    index=False)  # 긁어온 데이터를 ㄴcsv파일로 저장
                time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
            except AttributeError:
                pass

        except FileExistsError:  # 이미 디렉토리가 만들어져 있을 경우 실행
            try:
                print(f"이미 {symbol[:-4]}-USDT_{interval} 디렉토리가 만들어져 있습니다")
                df = get_data(start_date, end_date, symbol)
                df.to_csv(f'C:.\\Data\\{symbol[:-4]}-USDT_Data\\{symbol[:-4]}-USDT_Data_{interval}\\{symbol[:-4].upper()}_USDT_{interval}_All.csv', index=False)  # 긁어온 데이터를 ㄴcsv파일로 저장
                time.sleep(1)  # 과다한 요청으로 API사용이 제한되는것을 막기 위해
            except AttributeError:
                pass
