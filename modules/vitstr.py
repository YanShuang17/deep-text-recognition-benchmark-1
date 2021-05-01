'''
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timm.models import create_model

def create_vitstr(num_tokens, model=None, checkpoint_path=''):
    model = create_model(
        model,
        pretrained=True,
        num_classes=num_tokens,
        drop_rate=0.,
        drop_connect_rate=None, 
        drop_path_rate=None,
        drop_block_rate=None,
        global_pool=None,
        bn_tf=False,
        bn_momentum=None,
        bn_eps=None,
        scriptable=False,
        checkpoint_path=checkpoint_path)

    # might need to run to get zero init head for transfer learning
    model.reset_classifier(num_classes=num_tokens)

    return model