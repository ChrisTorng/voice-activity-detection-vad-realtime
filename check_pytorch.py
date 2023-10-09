import torch

print(f"torch.cuda.is_available() = {torch.cuda.is_available()}") # should be True
print(f"torch.version.cuda = {torch.version.cuda}") # should be True
print(f"torch.backends.cudnn.enabled = {torch.backends.cudnn.enabled}") # should be True
print(f"torch.backends.cudnn.version() = {torch.backends.cudnn.version()}") # 8700
