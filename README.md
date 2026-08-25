# Approximate Multiplier for Image Processing

A final year B.Tech project (Electronics and Communication Engineering,
NIT Calicut) exploring approximate multiplier architectures for
power- and area-efficient image processing.

## About the Project

Conventional multipliers are accurate but power- and area-hungry, which
becomes a real bottleneck in image processing tasks like filtering,
convolution, and neural network operations, especially on embedded or
mobile hardware. This project looks at approximate multiplier designs
that trade a small, controlled amount of accuracy for meaningful gains in
speed, power, and area.

Three architectures were studied and compared:

- **Booth Multiplier** — the accurate baseline, using Booth encoding to
  reduce the number of partial products.
- **Logarithmic Multiplier** — based on Mitchell's Algorithm, which
  converts multiplication into addition in the logarithmic domain. Much
  cheaper in hardware, but the approximation error grows with input size
  and gets a lot worse once truncation is added.
- **LOBO Multiplier** — a Booth-based multiplier with approximation
  applied at the partial-product stage, which came out on top for power
  efficiency in our comparisons while still keeping the error within
  acceptable bounds.

The Booth multiplier was implemented and verified at the RTL level, and
the analysis of power, area, and approximation error (with and without
truncation) across all three architectures was done through Python
modeling, comparing execution time, RMS error, and accuracy as a function
of bit width.

The full literature survey, methodology, plots, and conclusions are in the
report PDF included in this repo.

## Tools Used

- Verilog / RTL simulation (Booth multiplier design and waveform
  verification)
- Python (multiplier modeling, error and performance analysis, plotting)

## Repo Contents

- Report PDF (full literature survey, methodology, results, and
  conclusions)
- Code files (Verilog + Python) — to be added
