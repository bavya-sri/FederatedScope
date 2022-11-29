# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from federatedscope.core.auxiliaries.data_builder import get_data
from federatedscope.core.auxiliaries.utils import setup_seed
from federatedscope.core.auxiliaries.logging import update_logger
from federatedscope.core.configs.config import global_cfg
from federatedscope.autotune import get_scheduler, run_scheduler


class AutotuneTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))

    def test_toy_example_standalone_cmp_sim_impl(self):
        case_cfg = global_cfg.clone()
        case_cfg.merge_from_file(
            'federatedscope/autotune/baseline/fedhpo_vfl.yaml')
        setup_seed(case_cfg.seed)
        update_logger(case_cfg)

        scheduler = get_scheduler(case_cfg)
        # May cause timeout in UT
        # run_scheduler(scheduler, case_cfg)


if __name__ == '__main__':
    unittest.main()
