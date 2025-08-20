# Development Plan
If you are a contributor, please follow this plan for development.

## Step 1: Create Model Architecture

Create the general Architecture for saving and loading.

## Step 2: Create Noising Systems

I want the AI to have two types of generation type.

First, the AI generates text by "filling in the blanks" as proposed in *[Diffusion-LM Improves Controllable Text Generation](https://arxiv.org/pdf/2205.14217)*

Second, I want a unique noising system that makes text from high quality, to decent, so that it can auto-improve its text.

## Step 3: Creating Training Code

Pretty simple- Just the code to train.

## Step 4: Creating a CLI

A simple CLI that can run and pull models

Something I want for this though is being able to create custom denoising layers for models that want to do things like denoise code specifically for example.

## Extra Helpful Things

### Giving Compute

My computer is pretty bad. If someone with a good computer is fine with training a model on it, I would be very grateful. I am thinking of having a few example models, like a 1b, 5b, 20b general use LM.