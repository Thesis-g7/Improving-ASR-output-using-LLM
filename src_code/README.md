# Code Overview 
A single notebook source code file containing clean Python code for the whole research experiments. This enables the research paper to be fully reproducible. 
In the following lines, we will go step by step on each part of the code and discuss the main concepts and the general idea behind each of them. 

## Dataset

Our project utilizes a diverse set of datasets that are critical for training and evaluating our models. These datasets are downloaded from the Hyporadise repository on Hugging Face. Below is a detailed description of each dataset used in our work, including specific subsets and splits chosen for training and testing.

### Datasets Included

- **LibriSpeech:** 
  - LibriSpeech is a public corpus of read speech from audiobooks, including 1,000 hours of speech data with diverse speakers, genders, and accents. For generating our HP training data, we excluded simple cases from its train-960 split that resulted in a WER of 0, reducing the training set to 88,200 utterances. We use the entire test-clean and test-other splits for generating HP test data.
  
- **CHiME-4:**
  - CHiME-4 is a dataset for far-field speech recognition, featuring real and simulated noisy recordings in four noisy environments: bus, cafe, pedestrian area, and street junction. We utilize its train split (8,738 utterances) and test-real split (1,320 utterances) for generating HP training and test data. The four different noises in the test-real split are evaluated separately.

- **WSJ:**
  - The Wall Street Journal (WSJ) is a widely-used benchmark for speech recognition, with read speech focused on business news and financial data. We used its train-si284 split (37,514 utterances) to generate the HP training set, while the dev93 (503 utterances) and eval92 (333 utterances) splits were applied to build the test sets.

- **SwitchBoard:**
  - The SwitchBoard corpus is a telephone speech dataset collected from conversations between North American English speakers, consisting of over 2.4k conversations from approximately 200 speakers. We randomly selected 36,539 samples from its train split to generate the HP training set, as well as 2,000 utterances from the eval2000 split for the HP test set.

- **CommonVoice:**
  - CommonVoice 5.1 is a freely-available dataset for speech recognition, containing speech recordings from diverse speakers in over 60 languages. To generate the HP dataset, we randomly selected 51,758 samples from its train-en split with accent labels (African, Australian, Indian, and Singaporean). The training set contains 49,758 samples, while the test set contains 2,000 samples.

- **Tedlium-3:**
  - Tedlium-3 is a dataset of speech recorded from TED Talks, featuring a diverse range of background noise, speaker accents, and topics. We randomly selected 50,000 samples from its train split to generate the HP dataset, where the training set contains 47,500 samples, and the test set contains 2,500 samples.

- **LRS2:**
  - Lip Reading Sentences 2 (LRS2) is a large-scale publicly available labeled audio-visual dataset, consisting of 224 hours of video clips from BBC programs. We randomly selected 42,940 samples from its train split as the training set, and the remaining 2,259 samples were used for the test set.

- **ATIS:**
  - The Airline Travel Information System (ATIS) is a dataset comprising spoken queries for air travel information, such as flight times, prices, and availability. It contains around 5,000 to 5,400 utterances recorded from around 500 to 550 speakers.

- **CORAAL:**
  - The Corpus of Regional African American Language (CORAAL) is the first public corpus of African American Language (AAL) data, including audio recordings with time-aligned orthographic transcriptions from over 150 sociolinguistic interviews. To generate the HP dataset, we selected 1,728 samples as the training set and 100 samples as the test set.

### Preprocessing

In our preprocessing step, we handle punctuation in the following ways:

- Punctuation characters such as `, . " ! ? : ; $` are removed.
- Hyphens `-` are used as replacements for certain punctuation to preserve readability where necessary.

## Model Loading Process

- **Models Used:**
  - LLaMa 2 (`NousResearch/Llama-2-7b-chat-hf`)
  - Gemma (`google/gemma-7b-it`)
  - Mistral (`mistralai/Mistral-7B-Instruct-v0.1`)

- **Quantization:**
  - All models are loaded using 4-bit quantization with NF4 configuration.
  - Compute data types include `float16` and `bfloat16`.

- **Memory Management:**
  - Cache clearing (`torch.cuda.empty_cache()`) and garbage collection (`gc.collect()`) are performed before loading each model to optimize memory usage.

These configurations ensure that the models are loaded efficiently and are optimized for high-performance execution on the available hardware.
