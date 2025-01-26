from enum import Enum

class TranslateExportType(Enum):
    # 交错导出类型
    INTERLACED = 1
    # 独立导出类型
    INDEPENDENT = 2
    # 合并导出类型
    MERGED = 3
