#pragma once

#include <cstddef>
#include <string>
#include <vector>
#include <any>

class ModelConfig {
public:
    // Parameters for the model configuration
    size_t num_layers;
    size_t hidden_dim;
    size_t num_heads;
    size_t vocab_size;
    std::string model_name;

    void save(const std::string& filepath) const;
    void load(const std::string& filepath);
};

class Model {
public:
    Model(const ModelConfig& config);

    void save(const std::string& filepath) const;
    void load(const std::string& filepath);

    std::vector<float> generate(const std::vector<float>& input, size_t max_length);
    
    double train_step(const std::vector<std::vector<int>>& inputs, 
                      const std::vector<std::vector<int>>& targets);

private:
    ModelConfig config_;

    std::vector<std::any> parameters_;

    void save_weights(const std::string& path) const;
    void load_weights(const std::string& path);
};