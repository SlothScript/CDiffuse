## About CDiffuse
CDiffuse is a lightweight diffusion model library designed to run on CPU-only machines. It allows you to train, fine-tune, and run transformer-based diffusion models entirely on your local system. Note: CPU-only inference/training may be slow for large models.

## Why?
The reason I created this is because I have a pretty weak Mac, one without a good GPU. I want to run diffusion language models on my computer, but I can't find any software that is able to run these models.

## How do I use it?
CDiffuse has two main ways of using it, the `CDiffuse.h` file for using it programatically, and the `CLI.cpp` for general use.

## Installation
1. Clone the repo
    ```sh
    git clone https://github.com/slothscript/CDiffuse.git
    ```

2. Build CDiffuse and the CLI
    ```sh
    cd CDiffuse
    mkdir build && cd build
    cmake ..
    cmake --build .
    ```

3. Add CLI to PATH (optional)
4. Install the manpage (optional)

## Quick Start
After installing and compiling, either download a model or train one.

**Running model:**

`CDI run --model <path to model>`

*Replace the `<path to model>` with the path to the model, like `~/Downloads/<model name>` on Mac, or `C:\Users\[YourUsername]\Downloads\<model name>` on Windows (**get a better OS.**)*


## CLI Documentation

### General Usage:
`CDI <command> [options]`

### Commands
#### CDI init
Creates a new model

**usage:**

`CDI init --model <model-name> [options]`

**options**
* `--model <name>`: Name for the model instance (required).
* `-p <parameters>`: Target number of parameters. CDI will attempt to estimate and set hyperparameters to reach this size. Supports shorthand suffixes:
    * K = Thousand (e.g. 3K = 3,000)
    * M = Million (e.g. 50M = 50,000,000)
    * B = Billion (e.g. 7B = 7,000,000,000)
    * T = Trillion (e.g. 2T = 2,000,000,000,000) *note: using trillions of parameters is not recommended.*
* `--layers <n>` (unusable with -p): Manually set number of layers.
* `--dim <n>` (unusable with -p): Hidden dimension size.
* `--heads <n>` (unusable with -p): Number of attention heads.

#### CDI train
Trains a diffusion model on a dataset.

**usage:**

`CDI train --model <model-name> --data <path> [options]`

**options:**
* `--model <name>`: Model name to train (required).
* `--data <path>`: Path to training dataset (required).
* `--batch <n>`: Batch size (default: 32).
* `--lr <n>`: Learning rate (default: 0.001).
* `--epochs <n>`: Number of training epochs (default: 10).

#### CDI finetune
Fine-tunes an existing model on conversational or task-specific data.

**usage:**

`CDI finetune --model <model-name> --data <path> [options]`

**options:**
* `--model <name>`: Model to fine-tune (required).
* `--data <path>`: Path to fine-tuning dataset (required).
* `--batch <n>`: Batch size (default: 16).
* `--lr <n>`: Learning rate (default: 0.0001).

***notes:***
Check out the (chat format)[chatFormat.md] documentation to learn the format that `CDI run` uses.

#### CDI run
Runs inference with a trained or fine-tuned model.

**usage:**

`CDI run --model <model-name> [options]`

**options:**
* `--model <name>`: Model name to run (required).
* `--complete`: Use autocompletion mode instead of chat.
* `--prompt "text"`: Provide an initial prompt.
* `--no-stream`: Disable streaming output (default: streaming enabled).
* `--stop <token>`: top generation when token/string is encountered (default, <|EOT|>).

#### CDI list
Lists all available models on your system.

**usage:**

`CDI list`

**options:**
* `--all`: Show all models, including models with improper format or just initialized.
* `--info`: Shows info about the listed models such as parameters, layers, heads, size, and last infrence time.

#### CDI delete
Deletes a model from disk. **Use with caution – this cannot be undone.**

**usage:**

`CDI delete --model <model-name>`

**options:**
* `--model <name>`: Name of the model to delete (required).
* `--force`: Skip confirmation prompt.

#### CDI clean
Clears cache and imcomplete models.

**usage:**

`CDI clean`

**options:**
* `--dry-run`: Echos models that will be deleted

#### CDI info
Provides detailed information about a model, including parameters, layers, heads, size, and last infrence time.

**usage:**

`CDI info --model <model-name>`

**options:**
* `--model <name>`: Name of the model to inspect (required).
* `--parameters`: Only shows parameter count and other selected to be shown.
* `--layers`: Only shows layer count and other selected to be shown.
* `--heads`: Only shows head count and other selected to be shown.
* `--size`: Only shows size and other selected to be shown.
* `--infrence`: Only shows last infrence time and other selected to be shown.

### Examples
**Initialize a model with 50M parameters (auto hyperparameter estimation):**
`CDI init --model myModel -p 50M`

**Train a model with dataset `train.txt`:**
`CDI train --model myModel --data train.txt --batch 64 --lr 0.0005 --epochs 5`

**Fine-tune for chat with `chat_data.json`:**
`CDI finetune --model myModel --data chat_data.json`

**Run a chat session:**
`CDI run --model myModel --prompt "Hello!"`

**Run in completion mode with a stopping prompt:**
`CDI run --model myModel --complete --prompt "The quick brown fox" --stop "."`

**Delete the model**
`CDI delete --model myModel`

## `CDiffuse.h` Documentation
... to be made when I make the code

