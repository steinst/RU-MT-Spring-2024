#!/bin/bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=steinst@hi.is
#SBATCH --partition=Jotunn-GPU  # request node from a specific partition
#SBATCH --nodes=1                 # number of nodes
#SBATCH --ntasks-per-node=24      # 48 cores per node (96 in total)
#SBATCH --mem-per-cpu=3900        # MB RAM per cpu core
#SBATCH --time=0-04:00:00         # run for 4 hours maximum (DD-HH:MM:SS)
#SBATCH --hint=nomultithread      # Suppress multithread
#SBATCH --output=slurm_job_output.log
#SBATCH --error=slurm_job_errors.log   # Logs if job crashes

~/.conda/envs/alma-r/bin/python  /jotunn/home/steinst/ALMA/ALMA_translate_batch.py ../RU-MT-Spring-2024/Evaluation/source/newstest2021-is-en.src.is 7 isen

sentences_in = sys.argv[1]
alma_parameters_B = sys.argv[2]
lang_pair = sys.argv[3]