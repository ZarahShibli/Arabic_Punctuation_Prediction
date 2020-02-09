# Arabic Punctuation Prediction
------
1. [Project Overview](#ProjectOverview)
2. [Installation](#installation)
3. [Data Exploration and Visualization](#data)
4. [Implementation](#model)
5. [Results](#results)
6. [Acknowledgements](#acknowledgements)

## 1. Project Overview <a name="ProjectOverview"></a> 
Punctuations are symbols used to organize written textual to make it clear and easy to read. Lack of punctuation could cause confusion and misunderstanding for the reader. This problem may occur when using an Automatic Speech Recognition (ASR), the ASR system doesn’t predict punctuation usually. The punctuation prediction is one of the Natural Language Processing (NLP) problems. The aim of this project is to build a Sequence to sequence model to predict punctuation in Arabic texts.

## 2. Installation <a name="installation"></a>

- Python versions 3.*.
- Python Libraries:
    - matplotlib.
    - tensorflow.
    - sklearn.
    - Pandas.
    - keras.
    - numpy.
    - string.
    - time.
    - re.

## 3. Data Exploration and Visualization <a name="data"></a> 

[Tashkeela](https://www.kaggle.com/linuxscout/tashkeela) dataset, the dataset contains over 75 Arabic words obtained from 97 books. Also, it contains different types of punctuation. So, we will use it in this project. We selected four files from the dataset for training our model, which contains around 4.6 Million words.
We focus on five punctuation marks: comma, dot, semicolon, question mark, two vertical points. Below are some texts from Al-Bahr Al-Muhit book.


وَقَالَ الْأُسْتَاذُ أَبُو مَنْصُورٍ : الْغَرَضُ مِنْ أُصُولِ الْفِقْهِ مَعْرِفَةُ أَدِلَّةِ أَحْكَامِ الْفِقْهِ ، وَمَعْرِفَةُ طُرُقِ الْأَدِلَّةِ ، لِأَنَّ مَنْ اسْتَقْرَأَ أَبْوَابَهُ وَجَدَهَا إمَّا دَلِيلًا عَلَى حُكْمٍ أَوْ طَرِيقًا يُتَوَصَّلُ بِهِ إلَى مَعْرِفَةِ الدَّلِيلِ ، وَذَلِكَ كَمَعْرِفَةِ النَّصِّ ، وَالْإِجْمَاعِ ، وَالْقِيَاسِ ، وَالْعِلَلِ ، وَالرُّجْحَانِ . وَهَذِهِ كُلُّهَا مَعْرِفَةٌ مُحِيطَةٌ بِالْأَدِلَّةِ الْمَنْصُوصَةِ عَلَى الْأَحْكَامِ . وَمَعْرِفَةُ الْأَخْبَارِ وَطُرُقِهَا مَعْرِفَةٌ بِالطُّرُقِ الْمُوَصِّلَةِ إلَى الدَّلَائِلِ الْمَنْصُوصَةِ عَلَى الْأَحْكَامِ .وَهَاهُنَا أُمُورٌ : أَحَدُهَا : أَنَّ الْأَسْمَاءَ الْمُسْتَعْمَلَةَ فِي هَذِهِ الْعُلُومِ . كَأُصُولِ الْفِقْهِ ، وَالْفِقْهِ ، وَالنَّحْوِ ، وَاللُّغَةِ ، وَالطِّبِّ . هَلْ هِيَ مَنْقُولَةٌ أَوْ لَا ؟


## 4. Implementation <a name="model"></a> 
In this project, we used the sequence to sequence (seq2seq) model the same technique used of [Neural Machine Translation (NMT)](https://www.tensorflow.org/tutorials/text/nmt_with_attention) provided by TensorFlow. The inputs pass through the encoder model to give s us the encoder output and encoder hidden state. [Bahdanau Attention](https://arxiv.org/pdf/1409.0473.pdf) has been used for the encoder.


## 5. Result <a name="results"></a> 
We trained our model using 10 epoch with 256 batch size. We use categorical cross-entropy loss function and Adam optimizer. In figure example of prediction with attention plot.

![result2](https://user-images.githubusercontent.com/42017072/74092065-5a7cc200-4ad0-11ea-81a3-39c55cc244e1.PNG)

## 6. Acknowledgements <a name="acknowledgements"></a> 
I wish to thank [Tashkeela](https://www.kaggle.com/linuxscout/tashkeela) for dataset. Also, thanks for [Udacity](https://www.udacity.com/) for advice. For more details about this project can read this [article](https://medium.com/@ZarahShibli/what-comes-after-the-word-61c5adc9b8a0).
