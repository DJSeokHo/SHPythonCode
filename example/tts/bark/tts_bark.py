from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# 下载模型时会遇到 url SSL 的问题，唯一正确的方法是
# Open the folder /Applications/Python 3.x (x is the version you are running).
# Double click the Install Certificates.command. It will open a terminal and install the certificate.

# download and load all models
preload_models()

list = []
# generate audio from text
# text_prompt_1 = "Long ago, in ancient Egypt, the Israelites were enslaved and oppressed. Their suffering moved the heart of God."
# text_prompt_2 = "God chose Moses and sent him to redeem the Israelites, leading them out of this land of bondage."
# text_prompt_3 = "Moses confronted the Pharaoh of Egypt, asking him to release the Israelites. But Pharaoh's heart was as hard as stone, unwilling to listen."
# text_prompt_4 = "So, God sent down ten plagues, shaking Pharaoh's resolve."
# text_prompt_5 = "Eventually, Pharaoh agreed to let the Israelites go, and they departed with God's blessing, leaving Egypt behind."
# text_prompt_6 = "However, Pharaoh regretted his decision and sent his army to pursue the Israelites."
# text_prompt_7 = "At the edge of the Red Sea, God parted the waters, allowing the Israelites to cross while escaping the pursuing army."
# text_prompt_8 = "As the Egyptian army chased after them, the sea closed in, engulfing them. The Israelites gained their freedom, a new beginning."
# text_prompt_9 = "This is the story of Exodus, a tale of faith, courage, and liberation."
text_prompt_1 = "옛날 옛적, 고대의 이집트에서, 이스라엘 사람들은 노예로 만들어져 압제를 받았습니다. 그들의 고통이 하나님의 자비를 불러일으켰습니다."
text_prompt_2 = "하나님께서는 모세를 택하셨고, 그를 통해 이스라엘 사람들을 구원하시고, 이 노예의 땅을 떠나게 하셨습니다."
text_prompt_3 = "모세가 이집트의 파로와 대립하여 그를 이스라엘 사람들을 석방하도록 청했지만, 파로의 마음은 돌처럼 단단하여 듣지 않았습니다."
text_prompt_4 = "그래서 하나님은 열 가지 재앙을 내려 파로의 결심을 떨게 하셨습니다."
text_prompt_5 = "결국 파로는 이스라엘 사람들을 놓아주기로 합의하고, 그들은 하나님의 축복을 받아 이집트를 떠났습니다."
text_prompt_6 = "그러나 파로는 자신의 결정을 후회하고, 그의 군대를 이스라엘 사람들을 추적하기 위해 보냈습니다."
text_prompt_7 = "붉은 바다 가장자리에서, 하나님은 바다를 갈라 이스라엘 사람들이 피할 수 있도록 했습니다."
text_prompt_8 = "이집트 군대가 그들을 쫓을 때, 바다가 닫혔고 그들을 뒤덮었습니다. 이스라엘 사람들은 자유를 얻고 새로운 생명을 얻었습니다."
text_prompt_9 = "이것이 출애굽기 이야기입니다, 믿음, 용기, 그리고 해방에 관한 이야기입니다."
list.append(text_prompt_1)
list.append(text_prompt_2)
list.append(text_prompt_3)
list.append(text_prompt_4)
list.append(text_prompt_5)
list.append(text_prompt_6)
list.append(text_prompt_7)
list.append(text_prompt_8)
list.append(text_prompt_9)

for index, item in enumerate(list):
    audio_array = generate_audio(item, history_prompt="v2/ko_speaker_4")
    # audio_array = generate_audio(item, history_prompt="v2/en_speaker_5")

    # save audio to disk
    write_wav(f"screen_{index + 1}.wav", SAMPLE_RATE, audio_array)

    # play text in notebook
    # Audio(audio_array, rate=SAMPLE_RATE)
