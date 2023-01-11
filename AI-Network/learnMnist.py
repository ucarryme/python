import input_data   # 此时的导入只需要这么写就可以
mnist = input_data.read_data_sets("E:/study/learning python/AI-Network/mnist_data/", one_hot=True)
print('输入数据：',mnist.train.images)   # 输出图片数据
print('训练数据集shape：',mnist.train.images.shape)   # 输出训练数据集里图片个数
import pylab
im = mnist.train.images[1]    # 导出数据集中第一幅图片
im = im.reshape(-1,28)   # 将图片的shape变为计算机计算行数，自己定义列数为28列
pylab.imshow(im)
pylab.show()
print('测试数据集shape：',mnist.test.images.shape)   # 输出测试数据集里图片个数
print('验证数据集shape：',mnist.validation.images.shape)   # 输出验证数据集里图片个数