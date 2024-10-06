from crowdkit.datasets import load_dataset
from crowdkit.aggregation import ROVER
import pandas as pd
import re
import editdistance


files = ['atis.csv', 'chime4.csv', 'coraal.csv','cv.csv','lrs2.csv','ls_clean.csv','ls_other.csv','swbd.csv','td3.csv','wsj_score.csv']
for file in files:
    part_ensemble = []
    llama_df = pd.read_csv('llama_Gen_output/'+file)
    gemma_df = pd.read_csv('gemma_Gen_output/'+file)
    mistral_df = pd.read_csv('mistral_Gen_output/'+file)
    for index, row in llama_df.iterrows():
        for hyp in row['input'].split('\n'):
            part_ensemble.append({
                 'text': hyp,
                 'task': index
                 })
    for index, row in mistral_df.iterrows():
        for hyp in row['input'].split('\n'):
            part_ensemble.append({
                 'text': hyp,
                 'task': index
                 })
    for index, row in gemma_df.iterrows():
        for hyp in row['input'].split('\n'):
            part_ensemble.append({
                 'text': hyp,
                 'task': index
                 })
    df = pd.DataFrame(part_ensemble)
    df['text'] = df['text'].str.lower()
    tokenizer = lambda s: s.split(' ')
    detokenizer = lambda tokens: ' '.join(tokens)
    result = ROVER(tokenizer, detokenizer,silent=False).fit_predict(df)

    final_ens = llama_df.copy()
    final_ens['prediction'] = result
    final_ens.to_csv('Rover_ensemble/' + file,index=False)





punctuation_to_remove = ',.\"!?:;$'
punctuation_to_replace = '-'

def normalize_text(text):
    text = re.sub(f"[{re.escape(punctuation_to_remove)}]", '', text)
    text = re.sub(r'[-]', punctuation_to_replace, text)
    text = text.strip().lower()
    return text
    
def calculate_wer(pre, ref):
    wer_score = editdistance.eval(pre, ref) / len(ref)
    return wer_score


def calculate_wer_df(df):
    length  = len(df.index) 
    ignore = 0
    before = 0


    for index, row in df.iterrows():
        prediction = str(row['prediction'])
        ground_truth = row['output']
        prediction = normalize_text(prediction)
        ground_truth = normalize_text(ground_truth)


        try:
            wer = calculate_wer(prediction.split(), ground_truth.split())
        except Exception as e:
            print("CHECK HERE")
            print (ground_truth)
            print (prediction)
            ignore += 1
            continue

        before = before + wer
    error = before / (length - ignore) if (length - ignore) > 0 else 0
    return length, error


for file in files:
    df = pd.read_csv(f'Rover_ensemble/{file}')
    length, error = calculate_wer_df(df)
    print(f'{file}: ', error)