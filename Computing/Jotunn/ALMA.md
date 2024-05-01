## Setting up and running ALMA on Jotunn

You first log in to Jotunn using your username and ssh-key


### Setting up ALMA
```bash
conda create --name alma-r python=3.11
conda activate alma-r
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
git clone https://github.com/fe1ixxu/ALMA.git
cd ALMA
bash install_alma.sh
```

You can download the models simply by opening the Python IDLE Shell and type the following code:
```python
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Load base model and LoRA weights
model = AutoModelForCausalLM.from_pretrained("haoranxu/ALMA-13B-R", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("haoranxu/ALMA-13B-R", padding_side='left')
```
After this you can either proceed to translate, using for example the same approach as in the accompanying python files, or close the Python IDLE shell and run the scripts.

### Interactive mode
srun --job-name "InteractiveJob" --partition Jotunn-GPU --cpus-per-task 24 --mem-per-cpu 3900 --time 1-00:00:00 --pty bash
conda activate alma-r
cd ALMA
7BR_translate_interactive_isen.py
### Batch mode
python 7BR_translate_batch_isen.py