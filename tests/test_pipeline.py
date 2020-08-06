from cdesf2.utils import read_csv
from cdesf2.core import CDESF


def test_pipeline():
    path = 'demo'
    filename = 'Detail_Supplier_IW-Frozen.csv'

    event_stream_test = read_csv(f'{path}/{filename}')
    cdesf = CDESF(name='Detail_Supplier_IW-Frozen',
                  time_horizon=259200,
                  lambda_=0.05,
                  beta=0.2,
                  epsilon=0.2,
                  mu=4,
                  stream_speed=100,
                  n_features=2,
                  gen_metrics=True,
                  gen_plot=False)
    cdesf.run(event_stream_test)
