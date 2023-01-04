from main import argparse_default
from core.executer import Execute
import sys
import pytest


class TestRegressionAConEx:
    @pytest.mark.filterwarnings('ignore::UserWarning')
    def test_k_vs_all(self):
        args = argparse_default([])
        args.model = 'AConEx'
        args.scoring_technique = 'KvsAll'
        args.optim = 'Adam'
        args.path_dataset_folder = 'KGs/UMLS'
        args.num_epochs = 10
        args.batch_size = 1024
        args.lr = 0.1
        args.embedding_dim = 32
        args.num_of_output_channels = 32
        args.input_dropout_rate = 0.0
        args.hidden_dropout_rate = 0.0
        args.feature_map_dropout_rate = 0.0
        args.eval_model = 'train_val_test'
        args.read_only_few = None
        args.sample_triples_ratio = None
        args.num_folds_for_cv = None
        args.normalization = 'BatchNorm1d'
        args.init_param = 'xavier_normal'
        args.trainer = 'torchCPUTrainer'
        result = Execute(args).start()
        assert 0.70 >= result['Train']['MRR'] >= 0.69
        assert 0.56 >= result['Train']['H@1'] >= 0.55