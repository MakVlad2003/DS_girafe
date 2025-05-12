import numpy as np

class LaplaceDistribution:    
    @staticmethod
    def mean_abs_deviation_from_median(x: np.ndarray):
        '''
        Args:
        - x: A numpy array of shape (n_objects, n_features) containing the data
          consisting of num_train samples each of dimension D.
        '''
        median = np.median(x, axis=0)
        mad = np.mean(np.abs(x - median), axis=0)
        return mad

    def __init__(self, features):
        '''
        Args:
            features: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        self.loc = np.median(features, axis=0)  # Median of each feature as location parameter
        self.scale = self.mean_abs_deviation_from_median(features)  # Mean absolute deviation from median as scale parameter

    def logpdf(self, values):
        '''
        Returns logarithm of probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        # The logarithm of the probability density function for the Laplace distribution
        log_density = -np.sum(np.abs(values - self.loc) / self.scale, axis=1) - np.sum(np.log(2 * self.scale))
        return log_density
        
    
    def pdf(self, values):
        '''
        Returns probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        return np.exp(self.logpdf(values))