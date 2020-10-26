from keras.models import Sequential, load_model
import librosa
import numpy as np

class manufacturing():
    def __init__(self, filenames):
        self.output(filenames)

    def extract_feature(file_name):
        X, sample_rate = librosa.load(file_name)

        stft = np.abs(
            librosa.stft(X))  # 단시간 푸리에 변환(Short-time Fourier Transform, STFT) https://darkpgmr.tistory.com/171
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T, axis=0)
        contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T, axis=0)
        tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T, axis=0)
        return mfccs, chroma, mel, contrast, tonnetz

    def parse_audio_files(filenames):
        rows = len(filenames)
        #print(rows)
        features, labels, groups = np.zeros((rows, 193)), np.zeros((rows, 10)), np.zeros((rows, 1))
        i = 0
        for fn in filenames:
            try:
                mfccs, chroma, mel, contrast, tonnetz = manufacturing.extract_feature(fn)
                ext_features = np.hstack(
                    [mfccs, chroma, mel, contrast, tonnetz])  # hstack 행의 수가 같은 두 개 이상의 배열을 옆으로 연결하여 열의 수가 더 많은 배열을 만든다

            except Exception  as e:
                print(fn + "     ERROR", e)
            else:
                features[i] = ext_features

                i += 1
        return features


    def output(filenames):
        X=manufacturing.parse_audio_files(filenames)
        X = X.reshape(X.shape[0], 1, X.shape[1])

        model = Sequential()

        model = load_model('keras206.hdf5')  # 모델을 새로 불러옴

        return (model.predict_classes(X))  # 불러온 모델로 테스트 실행
       # print(model.predict(X))


#filenamess=["7061-6-0-0.wav"]
#X=parse_audio_files(filenamess)
# 7061-6-0-0
#
# 맨 처음 숫자 7061 [soundid] by [username] 출처
#
# 두번째 숫자 6   소리에 대한 내용
#
# 0 = air_conditioner
# 1 = car_horn
# 2 = children_playing
# 3 = dog_bark
# 4 = drilling
# 5 = engine_idling
# 6 = gun_shot
# 7 = jackhammer
# 8 = siren
# 9 = street_music
#
# 그 뒤 번호는 시리즈 번호

#
# audio_files = []
# for i in range(1,11):
#     audio_files.extend(glob.glob('UrbanSound8K/UrbanSound8K/audio/fold%d/*.wav' % i))   # extend는 가장 바깥쪽 iterable의 모든 항목을 대입
#                     # glob 현재
#
# print(len(audio_files))
# for i in range(9):
#     files = audio_files[i*1000: (i+1)*1000]
#     X, y, groups = parse_audio_files(files)
#     for r in y:
#         if np.sum(r) > 1.5:
#             print('error occured')
#             break
#     np.savez('urban_sound_%d' % i, X=X, y=y, groups=groups)




# X=X.reshape(X.shape[0], 1, X.shape[1])
#
#
# model = Sequential()
#
# model = load_model('keras206.hdf5') # 모델을 새로 불러옴
#
# print(model.predict_classes(X))  # 불러온 모델로 테스트 실행
# print(model.predict(X))
#

# config={
#     "serviceAccount":"abc.json"
# }

# firebase=pyrebase.initialize_app(config)
# storage = firebase.storage()
#
# ab=str(1)
# all_files = storage.child("images").list_files() #Enter the name of the folder
# for file in all_files:
#
#     try:
#         print(file.name)
#         z=storage.child(file.name).get_url(None)
#         storage.child(file.name).download(""+path+"/"+ab+".mp3")
#         x=int(ab)
#         ab=str(x+1)
#     except:
#         print('Download Failed')
