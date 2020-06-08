#!/bin/bash
#SBATCH --time=00:00:05
#SBATCH --output=simulation-m-%j.out
#SBATCH --error=simulation-m-%j.err
#SBATCH --ntasks=4

echo Starting Program
