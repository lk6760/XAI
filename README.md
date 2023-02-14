# XAI
<sup>This is the main repository for the QAML project on TUB. The repository was created for a project that was part of Quality Assurance for Machine Learning course at the Technical University of Berlin.</sub>

To use this repository as intended you should have a NVIDIA GPU with appropriate NVIDIA driver and CUDA versions that are compatible with PyTorch.
The majority of the work was done in the provided Collab notebook.

## Dataset
The dataset used in this project can be downloaded from [here](https://drive.google.com/file/d/1R5r5q_LExbb3f33Zycuq2-CEW8Ty_7Dw/view?usp=share_link)


## Task description
We were given a set of datasets containing images of dogs and cats, with each dataset having different watermark distribution.
Our task was to find the differences of the datasets and the models (binary classifiers) trained on each of them and try to explain the behaviour.
We used explainability methods such as Integrated Gradients, SHAP, LRP and others using the [Captum](https://captum.ai/) library for Model Interpretability in PyTorch.

We also proposed our own metric for quantifying watermark presence/activation of the model as ratio of mask energies.

## Examples

### Cat VS Cat w/ watermark
![image](https://user-images.githubusercontent.com/92629358/218581234-9c1cadbd-19ad-4907-8fcb-9391fd0721af.png)
![image](https://user-images.githubusercontent.com/92629358/218581484-cd9117cb-c5ee-4caa-af62-9f32120d95c2.png)

### Dog VS Dog w/ watermark
![image](https://user-images.githubusercontent.com/92629358/218581771-9c92b08b-4c4b-4068-a29e-bae7b94128a0.png)
![image](https://user-images.githubusercontent.com/92629358/218581803-a5768147-6d39-40f8-b979-fdbadcb12b73.png)

### Example of masking
![image](https://user-images.githubusercontent.com/92629358/218583697-427395f9-f1de-4c43-a0e0-d98cc8ce388c.png)
![image](https://user-images.githubusercontent.com/92629358/218583702-4213d7a0-1f38-4494-a893-7b4be91ce834.png)


