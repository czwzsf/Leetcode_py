import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2], [3, 4]])
Variable_data = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor * tensor)
v_out = torch.mean(Variable_data * Variable_data)
v_out.backward()
'''
v_out = 1/4*sum(var*var)
d(v_out)/d(var) = 1/4*2*Variable_data
'''
print(
    '\nt_out', t_out,
    '\nv_out', v_out,
)
print(Variable_data.grad)