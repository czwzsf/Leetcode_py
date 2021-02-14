import numpy as np
import torch

np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)

print(
    '\nnumpy', np_data,  # numpy数组
    '\ntorch_data', torch_data,  # torch数组
)

data = [[-1, -2], [3, 4]]
tensor = torch.FloatTensor(data)  # 32bit

print('torch', torch.mm(tensor, tensor))
