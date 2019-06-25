# -*- coding: utf-8 -*-

from typing import Union, Tuple, Optional
from copy import deepcopy

from sklearn.neural_network.multilayer_perceptron \
    import MLPRegressor as MLPRegressorClass

from sklearn_porter.estimator.EstimatorApiABC import EstimatorApiABC
from sklearn_porter.estimator.EstimatorBase import EstimatorBase
from sklearn_porter.enums import Method, Language, Template
from sklearn_porter.utils import get_logger


L = get_logger(__name__)


class MLPRegressor(EstimatorBase, EstimatorApiABC):
    """
    Extract model data and port a MLPRegressor regressor.

    See also
    --------
    http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html
    """
    estimator = None  # type: MLPRegressorClass

    def __init__(self, estimator: MLPRegressorClass):
        super().__init__(estimator)
        L.info('Create specific estimator `%s`.', self.estimator_name)
        est = self.estimator  # alias

        self.meta_info = dict()
        self.model_data = dict()

    def port(
            self,
            method: Optional[Method] = None,
            language: Optional[Language] = None,
            template: Optional[Template] = None,
            **kwargs
    ) -> Union[str, Tuple[str, str]]:
        """
        Port an estimator.

        Parameters
        ----------
        method : Method
            The required method.
        language : Language
            The required language.
        template : Template
            The required template.
        kwargs

        Returns
        -------
        The ported estimator.
        """
        method, language, template = self.check(
            method=method, language=language, template=template)

        kwargs.setdefault('method_name', method.value)

        converter = kwargs.get('converter')

        # Placeholders:
        plas = deepcopy(self.placeholders)  # alias
        plas.update(dict(
            class_name=kwargs.get('class_name'),
            method_name=kwargs.get('method_name'),
        ))
        plas.update(self.meta_info)

        # Load templates:
        temps = self._load_templates(language.value.KEY)

        return str(self.estimator)
