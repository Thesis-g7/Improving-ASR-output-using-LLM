# Error Analysis & Prompts

In this section, we will explore how our prompt changed overtime where we sought to optimize the WER. We also present a detailed analysis of ASR errors in general, and an analysis of errors that were found in the datasets.

## A history of all prompts 
This history is the change in the prompt used in Mistral LLM on Chime4 dataset from the test folder in hugging face. 

| Prompt used   | Edits done on it | Calc WER |
| ------------- | ---------------- | -------- |
| Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses. Focus on maximizing the repetition of phrases and words to create the most common hypothesis. If there is no commonality between the hypotheses, choose the hypothesis that is logical.  | no edits yet  | 14.58% |
| Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context. If there is no commonality between the hypotheses, choose the hypothesis that is logical.  | chosing the sequence that makes more sense among them  | 16.05% |
|Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context.If there is no commonality between the hypotheses, choose the hypothesis that is logical. SEPARATE THE CHARACTERS OF ANY ABBREVIATION WITH A SPACE.|separate the characters of any abbreviation with a space.|10.26%|
|Given 5 hypotheses, generate a single hypothesis by identifying and combining the  most repetitive sequences of sentences across all hypotheses considering the sequence making more sense with the rest of the sentence context. If there is no commonality between the hypotheses, choose the hypothesis that is logical.IF YOU NOTICED ANY ABBREVIATION, SEPARATE THE CHARACTERS OF THE ABBREVIATION WITH A SPACE. LIKE "U S" INSTEAD OF "US" OR "R L I COMPANY" INSTEAD OF "RLI COMPANY". DO NOT CONVERT NUMBERS WRITTEN IN CHARACTERS INTO ACTUAL NUMBERS. LIKE "FORTY TWO" INSTEAD OF "42" OR "five hundred and twenty five" INSTEAD OF "525". | more weight for the sentences at the begining of the hypotheses & grammatical correction of the sentences & Do not convert numbers written in characters into actual numbers.|9.63%|


This table only presents the significant changes to out prompt used, small changes to the prompts were not mentioned.

### Few shot Examples used in each prompt
    Speech recognition: list all us air flights from miami to cleveland leaving on sunday afternoon
    list all us air flights from miami to cleveland leaving on sunday afternoon
    list all us air flights from miami to cleveland leaving on sunday afternoon
    list all us airflights from miami to cleveland leaving on sunday afternoon
    list all us airflights from miami to cleveland leaving on sunday afternoon
    Truth: The true hypothesis is: list all u s air flights from miami to cleveland leaving on sunday afternoon

    Speech recognition: list the flights from dallas to baltimore arriving july onest
    list the flights from dallas to baltimore arriving july onest
    list the flights from dallas to baltimore arriving july one
    list the flights from dallas to baltimore arriving july one
    list the flights from dallas to baltimore arriving july onest
    Truth: The true hypothesis is: list the flights from dallas to baltimore arriving july first

    Speech recognition: realized capital gains increased forty-two percent to $nine hundred and nine million from $six hundred and forty point nine million
    realized capital gains increased forty-two percent to nine hundred and nine million dollars from six hundred and forty point nine million dollars
    realized capital gains increased forty-two percent to $nine hundred and nine million from $six hundred and forty point nine million
    realized capital gains increased forty-two percent to nine hundred and nine million dollars from six hundred and forty point nine million dollars
    realized capital gains increased forty-two percent from $six hundred and nine million to $six hundred and forty point nine million
    Truth: The true hypothesis is: realized capital gains increased forty two percent to nine hundred nine million dollars from six hundred forty point nine million dollars

    Speech recognition: i would like to fly from san diego to houston on june tenth
    i would like to fly from san diego to houston on june tenth
    i would like to fly from san diego to houston on june tenth
    i would like to fly from san diego to houston on june ten
    i would like to fly from san diego to houston on june ten
    Truth: The true hypothesis is: i would like to fly from san diego to houston on june tenth

<code style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;"> Theses examples were concatenated to the prompt
</code>

## Error Analysis


### ASR error Analysis 
A detailed analysis on what reasons might cause an ASR to make errors which was discussed in the paper and here is an overview for it 

<p align="center">
  <img src="../ASR error analysis.jpg" width="70%" />
</p>


<br>
Errors in ASR systems can be broadly categorized into three layers:
<br>

1. **Environmental Errors (Layer 1):** 
  - These are caused by external factors such as background noise, speaker accent, and speech rate, which the ASR system cannot control. <br> <br>
2. **Model and External Interaction Errors (Layer 2):**
  - These result from a combination of ASR model inefficiencies and external factors, such as slight mispronunciations or overlapping speech. <br> <br> 
3. **Internal Model Errors (Layer 3):**
  - These are intrinsic errors generated by the ASR system during transcription, such as misrecognition of words or phrases.

<br>
These error layers impact each other. For example, background noise (Layer 1) can lead to misheard words and context misunderstandings (Layer 2), which in turn can cause misspellings and other transcription errors (Layer 3). Figure2 depicts an illustration of various errors in each layer. The focus of our work in this paper addresses the errors in Layer 3, which are extensively discussed in literature.
<br> 
<br>

<code style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;"> <strong>Important:</strong> Based on this analysis, literal transcription seems to be the best way to transcribe, with no generaltion. This is due to the fact that some errors are beyond our control, as described above. Thus, the only evidence we have are the hypotheses given by the ASR.
</code>


### Dataset error analysis: 
Regarding the error analysis part and after reviewing most of the data instances we have concluded the following: <br>
- Below is a detailed analysis done in one of the datasets, chime4: 
	- higher rank but not majority voting: 
		- input: <br>
		"the company <code style="color : red">previously traded</code> over the counter", <br>
		"the company <code style="color : red">previously traded</code> over the counter", <br>
		"the company freely concentrated over the counter", <br>
		"the company freely concentrated over the counter", <br>
		"the company is really concentrated over the camera” 

		- expected output: <br>
		"the company <code style="color : red">previously traded</code> over the counter"

  	- No rank nor majority but logic:
 		- "interest rates rose on torture and treasury bills sold by the government yesterday at its regular weekly auction", <br>
		"interest rates rose on short term treasury bills sold by the government yesterday at its regular weekly auction", <br>
		"interest rates rose at a torture and treasury bill sold by the government yesterday at its regular weekly auction", <br>
		"interest rates rose on a torture and treasury bill sold by the government yesterday at its regular weekly auction", <br>
		"interest rates rose on torturing treasury bills sold by the government yesterday at its regular weekly auction”

		- "interest rates rose on <code style="color : red">short term</code> treasury bills sold by the government yesterday at its regular weekly auction",

  	- not matching any of the input:
  		- "the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous arson last year", <br>
		"the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous auction last year", <br>
		"the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous arson last year", <br>
		"the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous auction last year", <br>
		"the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous auction last year" 
		
		- "the average rate on new thirteen week treasury bills increased to six point one two percent from five point nine seven percent at the previous auction last <code style="color : red">week</code>",
  
	- another example on not matching any of the inputs: (there are tons of these examples where the output in not matching any of the inputs). 
		- "great spell on short term treasure", 	<br>
		"great spell on short term treasure rooms", 	<br>
		"great spell on short term treasure rooms", 	<br>
		"great spell on short term treasure", 		<br>
		"great spell on short term treasure rooms” 

		- "rates fell on short term treasury <code style="color : red">bills</code>",
  	- numbers are spelled differently:
  		- "although closed down funds have been around since at least the <code style="color : red">one thousand, nine hundred and twentys</code> they have boomed on popularity this year", <br>
		"although closed down funds have been around since at least the <code style="color : red">one thousand, nine hundred and twentys</code> they have boomed on popularity this year", <br>
		"although close down funds have been around since at least the <code style="color : red">one thousand, nine hundred and twentys</code> they have boomed on popularity this year", <br>
		"although close down funds have been around since at least the <code style="color : red">one thousand, nine hundred and twentys</code> they have boomed on popularity this year", <br>
		"although closed down funds have been around since at least the <code style="color : red">one thousand, nine hundred and twentys</code> they have boomed on popularity this year”

		- "although closed end funds have been around since at least the <code style="color : red">nineteen twenties</code> they have boomed in popularity this year",
## Our observations about the datasets
- no upper case characters found in any of the datasets. 
- abbreviations are always character separated in all datasets. 
- no punctuation marks in any of the datasets. 
- most of the datasets have grammatically correct output sentences, but others do have grammar mistakes. Like Coraal, swbd, and td3. 
- the number of instances in all datasets range from 170 to 3000 which is the reason why we get the average performance in WERR. 

<code style="border: 2px solid black; padding: 10px; margin: 10px 0; background-color: #f9f9f9;"> <strong>Important:</strong> Based on the previous analysis of errors and since the expected output sentence differs from the given hypotheses, it seems that we need to generate a new transciption, in order to have a logical output with no gramatical mistakes. This is how we prompted the LLMs and found the most optimized WER based on our trials.
</code>





