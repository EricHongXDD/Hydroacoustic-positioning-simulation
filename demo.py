import re

from NetMain import *
from data.Dataloader import *
from torch.autograd import Variable
from model.xception import *
data_path = 'xxxx.sim'

dataset = SnSpectrumLoader(file_path=data_path, length_freq=151,
                           SNR_range=[15, 15], num_read_sources=32, Sr=np.array([10]),
                           Sd=np.array([10]), SNR=15, i_file=0, run_mode='test',
                           model='xception')
print(len(dataset))
val_loader = data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0, drop_last=True)

_, dataVali = list(enumerate(val_loader))[0]
inputs_v = dataVali['C'].float()
inputs_v = Variable(inputs_v)
default_device = 'cuda'
default_type = torch.float32
max_range = 20
max_depth = 100

model = make_model().cuda()
model.eval()
path_checkpoint = 'a.weight_parameter/xception_3_epoch_2.00.pth'
checkpoint = torch.load(path_checkpoint)  # Load breakpoints
model.load_state_dict(checkpoint['model'])
inputs_v = inputs_v.to(default_device).type(default_type)
r_v = dataVali['r'].float() / max_range
r_v = r_v.to(default_device).type(default_type)
z_v = dataVali['z'].float() / max_depth
z_v = z_v.to(default_device).type(default_type)

val_loss, log_vars_v, output_v = model(inputs_v, [r_v, z_v])

print(output_v)
print(val_loss)

# 使用正则表达式提取数字
values = re.findall(r'\[([\d.]+)\]', str(output_v))

# 根据描述赋值
range_value = float(values[0])
depth = float(values[1])

print("range:", range_value)
print("depth:", depth)