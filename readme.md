# Echo State Networks in Python

[Echo State Networks](http://www.scholarpedia.org/article/Echo_state_network) are easy-to-train recurrent neural networks, a variant of [Reservoir Computing](https://en.wikipedia.org/wiki/Reservoir_computing). In some sense, these networks show how far you can get with nothing but a good weight initialisation.

This ESN implementation is relatively simple and self-contained, though it offers tricks like noise injection and teacher forcing (feedback connections), plus a zoo of dubious little hyperparameters.

However! If your aims are practical and your gradients automatic, consider using a fully trained network.

# Modifications From the Original Implementation
1. Make the ESN readout layer able not to take the input vector.
1. Fix a bug on min-max rescaling.
1. Enable the `ESN.fit` output to return the train error.
1. Add freq2wav dataset generator as a file (location: `dataset/freq2wav.py`).

# Examples

- [learning to be a tunable frequency generator](http://nbviewer.ipython.org/github/cknd/pyESN/blob/master/freqgen.ipynb)
- [learning a Mackey-Glass system](http://nbviewer.ipython.org/github/cknd/pyESN/blob/master/mackey.ipynb)

# Experiments
- freq2wav problem
  1. Plot and explore the dataset.
  1. Hyperparameter exploration with ESNs of reservoir size 200.
  1. Hyperparameter exploration with ESNs of reservoir size 32.
