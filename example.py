import boto3

# AWS 리전 및 Comprehend 클라이언트 생성
region_name = 'ap-northeast-2'
comprehend = boto3.client('comprehend', region_name=region_name)

# 감정분석 수행할 텍스트

text = '악뮤 노래중에서 givelove ❤️제가 제일 좋아하는데 리스트에 있어 너무 좋아요'
'원곡을 해치지않고 통통 밝은느낌의 연주.. 기원님 스타일이 들어가 몇 배로 좋아요'
'늘 감사히 듣고 있어요!! '
'아 너무 짜증난다 기분이 안좋아 왜이렇게 일이 진행되는지 모르겠어'

# 감정분석 수행
response = comprehend.detect_sentiment(Text=text, LanguageCode='ko')

# 결과 출력
sentiment = response['Sentiment']
print('감정: ' + sentiment)
