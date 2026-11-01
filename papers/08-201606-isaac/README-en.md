# ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars

## Original paper information

- Original title: ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars
- Authors: Ali Shafiee, Anirban Nag, Naveen Muralimanohar, et al.
- Year and venue: 2016, ISCA 2016

## Core method

- Compute-in-memory: ReRAM (resistive memory) crossbar arrays perform in-situ analog matrix-vector multiplication. Weights are stored as conductances at crosspoints, inputs are applied as voltages, and output currents are the multiply-accumulate results, so computation happens where the data is stored and weights do not need to be moved to a compute unit.
- Bit-slicing and pipelining: weights and inputs are expanded by bit slices, using multiple crossbar arrays plus shift-and-add to reconstruct multi-bit results; ISAAC organizes computation in a tile → IMA (in-situ multiply-accumulate unit) → crossbar hierarchy, and uses pipelining to hide ADC/DAC overhead.
- The key bottleneck is peripheral circuitry: ADC (analog-to-digital conversion) and DAC area and power often dominate the system, so the design must focus on "reducing ADC conversions and increasing reuse per conversion", not only on the array itself.
- Applicability boundary: analog computation is sensitive to device non-idealities (noise, drift, IR drop), so precision and robustness must be evaluated together with any comparison to digital designs.

## Core results

- The paper targets CNN inference and reports energy-efficiency and throughput advantages over digital baselines; however, because analog device parameters, ADC resolution, and process assumptions strongly affect results, this summary does not carry over a single second-hand speedup — see the original PDF's experimental tables and assumptions for exact numbers.
- The verifiable core conclusion is structural: in-situ computation removes weight movement, and the bottleneck moves from "memory access" to "peripheral circuitry and precision".
- A common reproduction pitfall: if ADC overhead and device non-idealities are not modeled, the benefits of compute-in-memory will be systematically overestimated.

## Reproduction points

- Reproduction goal: simulate crossbar MVM with a digital model (weight × input current summation), then add bit-slicing and ADC quantization, and observe how precision and ADC overhead change.
- Measure: the effect of bit-slice count on precision, the effect of ADC resolution on error, the number of ADC conversions per MVM, and precision degradation under device noise (simplified as random perturbation).
- What will not match the original chip: real ReRAM device characteristics, analog circuit power and area, and process parameters; the skeleton only verifies the MVM and quantization logic at the algorithm level.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
