import boto3

session = boto3.Session(profile_name='my_named_profile')
comprehend = boto3.client('comprehend', region_name='ap-northeast-2')
translate = boto3.client('translate', region_name='ap-northeast-2')

with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()

segments = text.split('\n\n')
for segment in segments:
    if not segment.strip():
        continue  # 빈 칸일 경우 건너뛰기

    # 번역 전 언어 감지
    source_lang_response = translate.translate_text(Text=segment.strip(), 
                                                    SourceLanguageCode='auto', 
                                                    TargetLanguageCode='ko')
    detected_source_lang = source_lang_response['SourceLanguageCode']

    # 번역
    translation_response = translate.translate_text(Text=segment.strip(),
                                                     SourceLanguageCode=detected_source_lang,
                                                     TargetLanguageCode='ko')
    translated_text = translation_response['TranslatedText']

    # 감정 분석
    sentiment_response = comprehend.detect_sentiment(Text=translated_text, LanguageCode='ko')
    sentiment = sentiment_response['Sentiment']
    positive = round(sentiment_response['SentimentScore']['Positive'] * 100, 2)
    negative = round(sentiment_response['SentimentScore']['Negative'] * 100, 2)
    neutral = round(sentiment_response['SentimentScore']['Neutral'] * 100, 2)
    mixed = round(sentiment_response['SentimentScore']['Mixed'] * 100, 2)

    print(f"Input Text: {segment.strip()}\n"
          f"Translated Text: {translated_text}\n"
          f"Detected Source Language: {detected_source_lang}\n"
          f"Sentiment: {sentiment}\n"
          f"Positive: {positive}%\n"
          f"Negative: {negative}%\n"
          f"Neutral: {neutral}%\n"
          f"Mixed: {mixed}%\n"
          f"------------------------------")
