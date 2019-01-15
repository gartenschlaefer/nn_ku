import numpy as np
from grammar import *

class ReberBatches():
  def __init__(self, n_train_samples, n_val_samples, n_test_samples, batch_size, sym_size=7):
    self.n_train_samples = n_train_samples
    self.n_val_samples = n_val_samples
    self.n_test_samples = n_test_samples
    self.batch_size = batch_size
    self.sym_size = sym_size

    # lists
    examples_train_list = []
    targets_train_list = []
    examples_val_list = []
    targets_val_list = []
    examples_test_list = []
    targets_test_list = []

    # max length of sequence
    self.train_max_seq_len = 0
    self.val_max_seq_len = 0
    self.test_max_seq_len = 0

    # create list of training examples
    for n in range(n_train_samples):
        example = make_embedded_reber()
        label = str_to_vec(example)
        target = str_to_next_embed(example)
        example_len = len(example)
        if self.train_max_seq_len < example_len:
            self.train_max_seq_len = example_len
        examples_train_list.append(label)
        targets_train_list.append(target)
        #print('\n\nReber String: ' + example + '\none hot: \n' + str(label) + '\nnext : \n' + str(target))

    # create 0-padded numpy matrix
    self.examples_train = np.zeros((n_train_samples, self.train_max_seq_len, sym_size))
    self.targets_train = np.zeros((n_train_samples, self.train_max_seq_len, sym_size))
    for sample_idx in range(n_train_samples):
        for str_idx in range(examples_train_list[sample_idx].shape[0]):
            self.examples_train[sample_idx][str_idx] = examples_train_list[sample_idx][str_idx]
            self.targets_train[sample_idx][str_idx] = targets_train_list[sample_idx][str_idx]

    # create list of validation examples
    for n in range(n_val_samples):
        example = make_embedded_reber()
        label = str_to_vec(example)
        target = str_to_next_embed(example)
        example_len = len(example)
        if self.val_max_seq_len < example_len:
            self.val_max_seq_len = example_len
        examples_val_list.append(label)
        targets_val_list.append(target)

    # create 0-padded numpy matrix
    self.examples_val = np.zeros((n_val_samples, self.val_max_seq_len, sym_size))
    self.targets_val = np.zeros((n_val_samples, self.val_max_seq_len, sym_size))
    for sample_idx in range(n_val_samples):
        for str_idx in range(examples_val_list[sample_idx].shape[0]):
            self.examples_val[sample_idx][str_idx] = examples_val_list[sample_idx][str_idx]
            self.targets_val[sample_idx][str_idx] = targets_val_list[sample_idx][str_idx]

    # create list of test examples
    for n in range(n_test_samples):
        example = make_embedded_reber()
        label = str_to_vec(example)
        target = str_to_next_embed(example)
        example_len = len(example)
        if self.test_max_seq_len < example_len:
            self.test_max_seq_len = example_len
        examples_test_list.append(label)
        targets_test_list.append(target)

    # create 0-padded numpy matrix
    self.examples_test = np.zeros((n_test_samples, self.test_max_seq_len, sym_size))
    self.targets_test = np.zeros((n_test_samples, self.test_max_seq_len, sym_size))
    for sample_idx in range(n_test_samples):
        for str_idx in range(examples_test_list[sample_idx].shape[0]):
            self.examples_test[sample_idx][str_idx] = examples_test_list[sample_idx][str_idx]
            self.targets_test[sample_idx][str_idx] = targets_test_list[sample_idx][str_idx]

    #print("\ntrain matrix: \n", self.examples_train)
    #print("\ntrain matrix: \n", self.targets_train)
    #print("\nval matrix: \n", self.examples_val)
    #print("\nval matrix: \n", self.targets_val)
    #print("\ntest matrix: \n", self.examples_test)
    #print("\ntest matrix: \n", self.targets_test)

    #print("max seq len: ", self.train_max_seq_len)
    #print("max seq len: ", self.val_max_seq_len)
    #print("max seq len: ", self.test_max_seq_len)

    # create training batches 
    # number of batches corresponding to batch_size
    self.batch_num = np.ceil(self.examples_train.shape[0] / batch_size)

    # split all examples and classes
    self.batch_examples_train = np.array_split(self.examples_train, self.batch_num) 
    self.batch_target_train = np.array_split(self.targets_train, self.batch_num)  
