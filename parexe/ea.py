import torch

# Create a tensor with specific strides on GPU 3 using bfloat16
arg_1 = torch.rand_strided((1, 4101, 6144), (25196544, 6144, 1), device='cuda:3', dtype=torch.bfloat16)

# Perform some operations on arg_1
# Example: Apply a simple operation like addition
result = arg_1 + 1.0

# Move the result back to the CPU for inspection or further processing
result_cpu = result.cpu()

print(result_cpu)
