import torch
import torch.nn as nn
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
from autoencoders import LinearAutoencoder

img_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

train_dataset = datasets.ImageFolder(
    root='./../frames/UCF101/Archery/',
    transform=img_transforms
    )

data_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True,
    num_workers=4
    )

first_batch, _ = next(iter(data_loader))
fig = plt.figure(figsize=(12, 6))
for row in range(1, 4):  
    for col in range(1, 4):  
        index = 6 * (row - 1) + col
        image = first_batch[index - 1, 0, :]
        fig.add_subplot(3, 6, index)
        plt.imshow(image.numpy())

        plt.axis('off')
plt.show()

lae = LinearAutoencoder()
lr = 2e-3
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(lae.parameters(),lr=lr)
num_epochs = 50

for epoch in range(num_epochs):
    for data in data_loader:
        img, _ = data
        img = img.view(img.size(0),-1)
        output = lae(img)
        loss = criterion(output, img)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print('epoch [{}/{}], loss:{:.4f}'
          .format(epoch + 1, num_epochs, loss.data[0]))
    if epoch % 10 == 0:
        pic = to_img(output.cpu().data)
        save_image(pic, './mlp_img/image_{}.png'.format(epoch))

torch.save(model.state_dict(), './sim_autoencoder.pth')
