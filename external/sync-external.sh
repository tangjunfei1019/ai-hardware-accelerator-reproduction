#!/usr/bin/env bash
# Sync the collected upstream projects in external/README.md.
# For each project: clone into external-checkouts/<name> if missing,
# otherwise git pull latest there. Prints the HEAD commit of each project.
# Usage: bash external/sync-external.sh
# The checkouts are NOT committed to this repo (see external/.gitignore-note.txt).
set -u
cd "$(dirname "$0")/.."
mkdir -p external-checkouts

declare -A REPOS=(
  [timeloop]="https://github.com/NVlabs/timeloop"
  [accelergy]="https://github.com/Accelergy-Project/accelergy"
  [scale-sim]="https://github.com/scalesim-project/SCALE-Sim"
  [gemmini]="https://github.com/ucb-bar/gemmini"
  [dnn-neurosim-v21]="https://github.com/neurosim/DNN_NeuroSim_V2.1"
  [cross-sim]="https://github.com/sandialabs/cross-sim"
  [pim-simulator]="https://github.com/SAITPublic/PIMSimulator"
  [xpu-perf]="https://github.com/bytedance/xpu-perf"
  [awesome-ai-accelerators]="https://github.com/LonghornSilicon/awesome-ai-accelerators"
  [awesome-ai-papers-reproduction]="https://github.com/Maxbay1017/awesome-ai-papers-reproduction"
  [code-reproductions]="https://github.com/EYE-666/code-reproductions"
)

for name in "${!REPOS[@]}"; do
  url="${REPOS[$name]}"
  dir="external-checkouts/$name"
  echo "=== $name ($url)"
  if [ -d "$dir/.git" ]; then
    echo "  pulling latest..."
    git -C "$dir" pull --ff-only || echo "  pull failed for $name (check network / local changes)"
  else
    echo "  cloning..."
    git clone "$url" "$dir" || { echo "  clone failed for $name"; continue; }
  fi
  echo -n "  HEAD: "
  git -C "$dir" rev-parse HEAD 2>/dev/null || echo "(unknown)"
done
echo "Done. Checkouts live in external-checkouts/ and are not committed to this repo."
