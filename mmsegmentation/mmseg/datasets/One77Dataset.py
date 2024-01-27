from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class One77Dataset(BaseSegDataset):
    # 类别和对应的 RGB配色
    METAINFO = {
        'classes': ['background', 'XianWo', 'HuiShengDai', 'GongJingXingTai', 'PangGuangXian', 'WeiZhi'],
        'palette': [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [128, 128, 128], [128, 0, 128]]
    }

    # 指定留像扩展名、注扩展名
    def __init__(self,
                 seg_map_suffix='.png',
                 reduce_zero_label=False,
                 **kwargs) -> None:
        super().__init__(
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
