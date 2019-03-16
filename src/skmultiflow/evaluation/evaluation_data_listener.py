from abc import abstractmethod, ABCMeta

from skmultiflow.core.base_object import BaseObject


class EvaluationMetricsListener(BaseObject, metaclass=ABCMeta):

    @abstractmethod
    def listen(self, sample_id, metrics_data):
        raise NotImplementedError

    def get_class_type(self):
        return 'Evaluation Metrics Listener'

    def get_info(self):
        return 'Metrics listener base'
