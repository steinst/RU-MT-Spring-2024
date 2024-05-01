import sys
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

sentences_in = sys.argv[1]
alma_parameters_B = sys.argv[2]
lang_pair = sys.argv[3]

sourcelang = 'en'
targetlang = 'is'
SourceLanguage = 'English'
TargetLanguage = 'Icelandic'
if lang_pair == 'isen':
    sourcelang = 'is'
    SourceLanguage = 'Icelandic'
    targetlang = 'en'
    TargetLanguage = 'English'

# Load base model and LoRA weights
model = AutoModelForCausalLM.from_pretrained("haoranxu/ALMA-" + str(alma_parameters_B) + "B-R", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("haoranxu/ALMA-" + str(alma_parameters_B) + "B-R", padding_side='left')


def translate(sentence):
    # Add the source sentence into the prompt template
    prompt = "Translate this from " + SourceLanguage + " to " + TargetLanguage + ":\n" + SourceLanguage + ": " + sentence + "\n" + TargetLanguage + ":"
    input_ids = tokenizer(prompt, return_tensors="pt", padding=True, max_length=200, truncation=True).input_ids.cuda()
    # Translation
    with torch.no_grad():
        generated_ids = model.generate(input_ids=input_ids, num_beams=5, max_new_tokens=180, do_sample=True,
                                       temperature=0.6, top_p=0.9)
    outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    try:
        return outputs[0].split('\n' + TargetLanguage + ':')[1].strip().lstrip()
    except:
        return outputs

with open(sentences_in, 'r') as fi, open(sentences_in + '.alma' + str(alma_parameters_B), 'w') as fo:
    for sentence in fi:
        fo.write(sentence.strip() + '\t' + translate(sentence.strip()) + '\n')
