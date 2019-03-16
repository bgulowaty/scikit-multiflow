"""
The :mod:`skmultiflow.evaluation` module includes evaluation methods for stream learning.
"""

from .evaluate_prequential import EvaluatePrequential
from .evaluate_holdout import EvaluateHoldout
from .evaluation_data_buffer import EvaluationDataBuffer
from .evaluation_data_listener import EvaluationMetricsListener

__all__ = ["EvaluatePrequential", "EvaluateHoldout", "EvaluationDataBuffer", "EvaluationMetricsListener"]
