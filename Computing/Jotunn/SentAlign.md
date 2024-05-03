## Setting up and running SentAlign on Jotunn

You first log in to Jotunn using your username and ssh-key


### Setting up SentAlign
```bash
conda create --name SentAlign python=3.9
conda activate SentAlign
pip3 install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Interactive mode
srun --job-name "InteractiveJob" --partition Jotunn-GPU --cpus-per-task 24 --mem-per-cpu 3900 --time 1-00:00:00 --pty bash
conda activate SentAlign
cd SentAlign
python3 files2align.py -dir eval_data/bleualign --source-language deu
python3 sentAlign.py -dir eval_data/bleualign -sl deu -tl fra
### Batch mode
You should be able to create your own sbatch-file for the slurm job, if you just look at the file for ALMA.