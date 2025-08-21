import csv
import re
import random

noise_steps = 25

# Clean up/create data.csv
with open('data.csv', 'w', newline='') as csvfile:
   writer = csv.writer(csvfile)
   # Write header
   writer.writerow(['denoise' + str(i) for i in range(1, noise_steps + 1)])

# First pass - combine or split sentences to get ~100 words
sentences = []
with open('data.txt', 'r') as f:
   text = f.read()
   # Split into sentences (basic sentence splitting)
   sentences = re.split(r'[.!?]+', text)
   sentences = [s.strip() for s in sentences if s.strip()]

# Process sentences to create ~100 word chunks
processed_lines = []
current_chunk = ""
current_word_count = 0

for sentence in sentences:
   sentence_words = sentence.split()
   sentence_word_count = len(sentence_words)
   
   # If adding this sentence would go over 100 words significantly
   if current_word_count + sentence_word_count > 120 and current_chunk:
       # Save current chunk and start new one
       processed_lines.append(current_chunk.strip())
       current_chunk = sentence
       current_word_count = sentence_word_count
   else:
       # Add sentence to current chunk
       if current_chunk:
           current_chunk += " " + sentence
       else:
           current_chunk = sentence
       current_word_count += sentence_word_count
   
   # If current chunk is close to 100 words, save it
   if 80 <= current_word_count <= 120:
       processed_lines.append(current_chunk.strip())
       current_chunk = ""
       current_word_count = 0

# Don't forget the last chunk
if current_chunk.strip():
   processed_lines.append(current_chunk.strip())

# Write processed lines back to data.txt
with open('data.txt', 'w') as f:
   for line in processed_lines:
       f.write(line + '\n')

# Second pass - create progressive denoising for each line
with open('data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for line in processed_lines:
        words = line.split()
        row = []
        
        # Create random indices for revealing words
        word_indices = list(range(len(words)))
        random.shuffle(word_indices)
        
        # Create progressive denoising steps (random word revelation)
        for step in range(noise_steps):
            denoise_words = ['_'] * len(words)  # Start with all masked
            
            # Calculate how many words to reveal at this step
            words_to_reveal = int((step / (noise_steps - 1)) * len(words)) if noise_steps > 1 else len(words)
            
            # Reveal the first N words from our shuffled list
            for i in range(words_to_reveal):
                if i < len(word_indices):
                    word_idx = word_indices[i]
                    # Escape double quotes in the word
                    escaped_word = words[word_idx].replace('"', '""')
                    denoise_words[word_idx] = escaped_word
            
            row.append(' '.join(denoise_words))
        
        writer.writerow(row)