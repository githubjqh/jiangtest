import matplotlib.pyplot as plt
from torch import Tensor
# from varname import nameof
import inspect


# 这是从堆栈内存的第3层开始查找返回变量名称
def nameof(var):
    for fi in inspect.stack()[2:]:
        for item in fi.frame.f_locals.items():
            if var is item[1]:
                return item[0]
    return ""


def mplot(datas, vn_list=[], xt_names=[], figsize=(15, 8)):
    plt.figure(figsize=figsize)
    l_list = []
    for data in datas:
        l, = plt.plot(data)
        l_list.append(l)
    plt.legend(handles=l_list, labels=vn_list, loc='best')
    if len(xt_names) > 0:
        _ = plt.xticks(range(len(xt_names)), labels=xt_names, rotation=60)


def mpltshow(imgs, figsize=(40, 15)):
    fig = plt.figure(figsize=figsize)
    l = len(imgs)
    rows = l // 4 + 1
    for i, img in enumerate(imgs):
        ax = fig.add_subplot(rows, 4, i + 1, xticks=[], yticks=[])
        varname = nameof(img)
        ax.set_title(f'{i + 1}: {varname}', color=("green"), fontsize=30, ha='center')
        if isinstance(img, Tensor):
            img = img.cpu().detach().numpy().astype(float)
        plt.imshow(img)


def printshape(datas):
    [print(f'{nameof(x):<20}:{x.shape}') for x in datas]
