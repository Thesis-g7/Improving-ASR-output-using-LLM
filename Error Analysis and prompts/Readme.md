# Error Analysis & Prompts

In this section We will discuss how we managed to find out that the approach we are currently using the prompt we are following in all few-shot prompts in all LLMs is the best among other approaches. We will dig deeper in real examples from different datasets to explain and go through it step by step. 


## A history of all prompts 
This history is the change of prompt used in Mistral LLM on Chime4 dataset from test folder in hugging face. 

| Prompt used   | Edits done on it | Calc WER |
| ------------- | ---------------- | -------- |
| Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses. Focus on maximizing the repetition of phrases and words to create the most common hypothesis. If there is no commonality between the hypotheses, choose the hypothesis that is logical.  | no edits yet  | 14.58% |
| Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context. If there is no commonality between the hypotheses, choose the hypothesis that is logical.  | chosing the sequence that makes more sense among them  | 16.05% |
|Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context.If there is no commonality between the hypotheses, choose the hypothesis that is logical. SEPARATE THE CHARACTERS OF ANY ABBREVIATION WITH A SPACE.|separate the characters of any abbreviation with a space.|10.26%|
|Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context. If there is no commonality between the hypotheses, choose the hypothesis that is logical.IF YOU NOTICED ANY ABBREVIATION, SEPARATE THE CHARACTERS OF THE ABBREVIATION WITH A SPACE. LIKE "U S" INSTEAD OF "US" OR "R L I COMPANY" INSTEAD OF "RLI COMPANY". DO NOT CONVERT NUMBERS WRITTEN IN CHARACTERS INTO ACTUAL NUMBERS. LIKE "FORTY TWO" INSTEAD OF "42" OR "five hundred and twenty five" INSTEAD OF "525". | more weight for the sentences at the begging of the hypotheses & grammatical correction of the sentences &Do not convert numbers written in characters into actual numbers.|9.63%|


The rest of the done edits are really minor thus, no need to mention in the table. As you can view from the table a significant change is done between the second and the third prompt when only adjusting the abbreviation part, where characters of a single abbreviation word should be separated. Moreover, the more details you give to the prompt the higher performance you get from the LLM. 



## Error Analysis

Regarding the error analysis part and after reviewing most of the data instances we have concluded the following: <br>
- no upper case characters found in any of the datasets. 
- abbreviations are always character separated in all datasets. 
- no punctuation marks in any of the datasets. 
- most of the datasets have grammatically correct output sentences, but others do have grammar mistakes. Like Coraal, swbd, and td3. 
- the number of instances in all datasets range from 170 to 3000 which is the reason why we get the average performance in WERR. 
- Below all a detailed analysis done in one of the datasets, chime4: 
	- higher rank but not majority voting: 
		- "the company <code style="color : name_color">previously traded</code> over the counter",
		"the company <code style="color : name_color">previously traded</code> over the counter",
		"the company freely concentrated over the counter",
		"the company freely concentrated over the counter",
		"the company is really concentrated over the camera”

		- "the company <code style="color : name_color">previously traded</code> over the counter",



