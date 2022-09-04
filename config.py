
class Hyperparameter:
    # ################################################################
    #                             Data
    # ################################################################
    device = 'cpu'  # cuda
    data_dir = '/Users/yitingcao/cs/dl/02-08/data/'
    data_path = '/Users/yitingcao/cs/dl/02-08/data/data_banknote_authentication.txt'
    trainset_path = '/Users/yitingcao/cs/dl/02-08/data/train.txt'
    devset_path = '/Users/yitingcao/cs/dl/02-08/data/dev.txt'
    testset_path = '/Users/yitingcao/cs/dl/02-08/data/test.txt'

    in_features = 100  # input feature dim
    out_dim = 2  # output feature dim (classes number)
    seed = 1234  # random seed

    # ################################################################
    #                             Model Structure
    # ################################################################
    layer_list = [in_features, 128, 256, 128, 64, out_dim]
    # ################################################################
    #                             Experiment
    # ################################################################
    batch_size = 16
    init_lr = 1e-3
    epochs = 100
    verbose_step = 10
    save_step = 100


HP = Hyperparameter()
