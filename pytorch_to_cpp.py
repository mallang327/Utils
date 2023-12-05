import torch

model = None # load your model (with load-state-dicted)

# For multi-modal input model
## torch tensor shape must be matched with model input shape
videoframe = torch.rand(1,16,3,224,224).cuda(0)
audioframe = torch.rand(1,8533,1).cuda(0);

# pyTorch model to cpp jit script
traced_script_module = torch.jit.trace(model, (videoframe, audioframe))
output = traced_script_module(videoframe, audioframe)

#print(output)

traced_script_module.save("model_cpp.pt")