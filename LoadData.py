def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
filename='./data1/cifar-10-batches-py/data_batch_1'
x=unpickle(filename)
print(x)
