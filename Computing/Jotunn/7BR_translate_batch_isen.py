import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Load base model and LoRA weights
model = AutoModelForCausalLM.from_pretrained("haoranxu/ALMA-13B-R", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("haoranxu/ALMA-13B-R", padding_side='left')


def translate_isen():
    # Add the source sentence into the prompt template
    prompt = "Translate this from Icelandic to English:\nIcelandic: Þetta er setning.\nEnglish:"
    input_ids = tokenizer(prompt, return_tensors="pt", padding=True, max_length=100, truncation=True).input_ids.cuda()
    # Translation
    with torch.no_grad():
        generated_ids = model.generate(input_ids=input_ids, num_beams=5, max_new_tokens=80, do_sample=True,
                                       temperature=0.6, top_p=0.9)
    outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    try:
        return outputs[0].split('\nEnglish:')[1].strip().lstrip()
    except:
        return outputs

with open('translations.txt', 'w') as fo:
    fo.write(translate_isen())
